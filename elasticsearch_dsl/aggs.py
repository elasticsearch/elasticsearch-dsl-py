#  Licensed to Elasticsearch B.V. under one or more contributor
#  license agreements. See the NOTICE file distributed with
#  this work for additional information regarding copyright
#  ownership. Elasticsearch B.V. licenses this file to you under
#  the Apache License, Version 2.0 (the "License"); you may
#  not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
# 	http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing,
#  software distributed under the License is distributed on an
#  "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
#  KIND, either express or implied.  See the License for the
#  specific language governing permissions and limitations
#  under the License.

import collections.abc
from copy import deepcopy
from typing import (
    TYPE_CHECKING,
    Any,
    ClassVar,
    Dict,
    Iterable,
    MutableMapping,
    Optional,
    Union,
    cast,
)

from .response.aggs import AggResponse, BucketData, FieldBucketData, TopHitsData
from .utils import AttrDict, DslBase, JSONType

if TYPE_CHECKING:
    from .query import Query
    from .search_base import SearchBase


def A(
    name_or_agg: Union[MutableMapping[str, Any], "Agg", str],
    filter: Optional[Union[str, "Query"]] = None,
    **params: Any,
) -> "Agg":
    if filter is not None:
        if name_or_agg != "filter":
            raise ValueError(
                "Aggregation %r doesn't accept positional argument 'filter'."
                % name_or_agg
            )
        params["filter"] = filter

    # {"terms": {"field": "tags"}, "aggs": {...}}
    if isinstance(name_or_agg, collections.abc.MutableMapping):
        if params:
            raise ValueError("A() cannot accept parameters when passing in a dict.")
        # copy to avoid modifying in-place
        agg = deepcopy(name_or_agg)
        # pop out nested aggs
        aggs = agg.pop("aggs", None)
        # pop out meta data
        meta = agg.pop("meta", None)
        # should be {"terms": {"field": "tags"}}
        if len(agg) != 1:
            raise ValueError(
                'A() can only accept dict with an aggregation ({"terms": {...}}). '
                "Instead it got (%r)" % name_or_agg
            )
        agg_type, params = agg.popitem()
        if aggs:
            params = params.copy()
            params["aggs"] = aggs
        if meta:
            params = params.copy()
            params["meta"] = meta
        return Agg.get_dsl_class(agg_type)(_expand__to_dot=False, **params)

    # Terms(...) just return the nested agg
    elif isinstance(name_or_agg, Agg):
        if params:
            raise ValueError(
                "A() cannot accept parameters when passing in an Agg object."
            )
        return name_or_agg

    # "terms", field="tags"
    return Agg.get_dsl_class(name_or_agg)(**params)


class Agg(DslBase):
    _type_name = "agg"
    _type_shortcut = staticmethod(A)
    name = ""

    def __contains__(self, key: str) -> bool:
        return False

    def to_dict(self) -> Dict[str, JSONType]:
        d = super().to_dict()
        if isinstance(d[self.name], dict):
            n = cast(Dict[str, JSONType], d[self.name])
            if "meta" in n:
                d["meta"] = n.pop("meta")
        return d

    def result(self, search: "SearchBase", data: Any) -> AttrDict[str, Any]:
        return AggResponse(self, search, data)


class AggBase:
    if TYPE_CHECKING:
        aggs: Dict[str, Agg]
        _base: Agg
    _params: Dict[str, Any]
    _param_defs: ClassVar[Dict[str, Any]] = {
        "aggs": {"type": "agg", "hash": True},
    }

    def __contains__(self, key: str) -> bool:
        return key in self._params.get("aggs", {})

    def __getitem__(self, agg_name: str) -> Agg:
        agg = cast(
            Agg, self._params.setdefault("aggs", {})[agg_name]
        )  # propagate KeyError

        # make sure we're not mutating a shared state - whenever accessing a
        # bucket, return a shallow copy of it to be safe
        if isinstance(agg, Bucket):
            agg = A(agg.name, filter=None, **agg._params)
            # be sure to store the copy so any modifications to it will affect us
            self._params["aggs"][agg_name] = agg

        return agg

    def __setitem__(self, agg_name: str, agg: Agg) -> None:
        self.aggs[agg_name] = A(agg)

    def __iter__(self) -> Iterable[str]:
        return iter(self.aggs)

    def _agg(
        self, bucket: bool, name: str, agg_type: str, *args: Any, **params: Any
    ) -> Agg:
        agg = self[name] = A(agg_type, *args, **params)

        # For chaining - when creating new buckets return them...
        if bucket:
            return agg
        # otherwise return self._base so we can keep chaining
        else:
            return self._base

    def metric(self, name: str, agg_type: str, *args: Any, **params: Any) -> Agg:
        return self._agg(False, name, agg_type, *args, **params)

    def bucket(self, name: str, agg_type: str, *args: Any, **params: Any) -> Agg:
        return self._agg(True, name, agg_type, *args, **params)

    def pipeline(self, name: str, agg_type: str, *args: Any, **params: Any) -> Agg:
        return self._agg(False, name, agg_type, *args, **params)

    def result(self, search: "SearchBase", data: Any) -> AttrDict[str, Any]:
        return BucketData(self, search, data)


class Bucket(AggBase, Agg):
    def __init__(self, **params: Any):
        super().__init__(**params)
        # remember self for chaining
        self._base = self

    def to_dict(self) -> Dict[str, JSONType]:
        d = super(AggBase, self).to_dict()
        if isinstance(d[self.name], dict):
            n = cast(AttrDict[str, Any], d[self.name])
            if "aggs" in n:
                d["aggs"] = n.pop("aggs")
        return d


class Filter(Bucket):
    name = "filter"
    _param_defs = {
        "filter": {"type": "query"},
        "aggs": {"type": "agg", "hash": True},
    }

    def __init__(self, filter: Optional[Union[str, "Query"]] = None, **params: Any):
        if filter is not None:
            params["filter"] = filter
        super().__init__(**params)

    def to_dict(self) -> Dict[str, JSONType]:
        d = super().to_dict()
        if isinstance(d[self.name], dict):
            n = cast(AttrDict[str, Any], d[self.name])
            n.update(n.pop("filter", {}))
        return d


class Pipeline(Agg):
    pass


# bucket aggregations
class Filters(Bucket):
    name = "filters"
    _param_defs = {
        "filters": {"type": "query", "hash": True},
        "aggs": {"type": "agg", "hash": True},
    }


class Children(Bucket):
    name = "children"


class Parent(Bucket):
    name = "parent"


class DateHistogram(Bucket):
    name = "date_histogram"

    def result(self, search: "SearchBase", data: Any) -> AttrDict[str, Any]:
        return FieldBucketData(self, search, data)


class AutoDateHistogram(DateHistogram):
    name = "auto_date_histogram"


class AdjacencyMatrix(Bucket):
    name = "adjacency_matrix"


class DateRange(Bucket):
    name = "date_range"


class GeoDistance(Bucket):
    name = "geo_distance"


class GeohashGrid(Bucket):
    name = "geohash_grid"


class GeohexGrid(Bucket):
    name = "geohex_grid"


class GeotileGrid(Bucket):
    name = "geotile_grid"


class GeoCentroid(Bucket):
    name = "geo_centroid"


class Global(Bucket):
    name = "global"


class Histogram(Bucket):
    name = "histogram"

    def result(self, search: "SearchBase", data: Any) -> AttrDict[str, Any]:
        return FieldBucketData(self, search, data)


class IPRange(Bucket):
    name = "ip_range"


class IPPrefix(Bucket):
    name = "ip_prefix"


class Missing(Bucket):
    name = "missing"


class Nested(Bucket):
    name = "nested"


class Range(Bucket):
    name = "range"


class RareTerms(Bucket):
    name = "rare_terms"

    def result(self, search: "SearchBase", data: Any) -> AttrDict[str, Any]:
        return FieldBucketData(self, search, data)


class ReverseNested(Bucket):
    name = "reverse_nested"


class SignificantTerms(Bucket):
    name = "significant_terms"


class SignificantText(Bucket):
    name = "significant_text"


class Terms(Bucket):
    name = "terms"

    def result(self, search: "SearchBase", data: Any) -> AttrDict[str, Any]:
        return FieldBucketData(self, search, data)


class Sampler(Bucket):
    name = "sampler"


class DiversifiedSampler(Bucket):
    name = "diversified_sampler"


class RandomSampler(Bucket):
    name = "random_sampler"


class Composite(Bucket):
    name = "composite"
    _param_defs = {
        "sources": {"type": "agg", "hash": True, "multi": True},
        "aggs": {"type": "agg", "hash": True},
    }


class VariableWidthHistogram(Bucket):
    name = "variable_width_histogram"

    def result(self, search: "SearchBase", data: Any) -> AttrDict[str, Any]:
        return FieldBucketData(self, search, data)


class MultiTerms(Bucket):
    name = "multi_terms"


class CategorizeText(Bucket):
    name = "categorize_text"


# metric aggregations
class TopHits(Agg):
    name = "top_hits"

    def result(self, search: "SearchBase", data: Any) -> AttrDict[str, Any]:
        return TopHitsData(self, search, data)


class Avg(Agg):
    name = "avg"


class WeightedAvg(Agg):
    name = "weighted_avg"


class Cardinality(Agg):
    name = "cardinality"


class ExtendedStats(Agg):
    name = "extended_stats"


class Boxplot(Agg):
    name = "boxplot"


class GeoBounds(Agg):
    name = "geo_bounds"


class GeoLine(Agg):
    name = "geo_line"


class Max(Agg):
    name = "max"


class MatrixStats(Agg):
    name = "matrix_stats"


class MedianAbsoluteDeviation(Agg):
    name = "median_absolute_deviation"


class Min(Agg):
    name = "min"


class Percentiles(Agg):
    name = "percentiles"


class PercentileRanks(Agg):
    name = "percentile_ranks"


class ScriptedMetric(Agg):
    name = "scripted_metric"


class Stats(Agg):
    name = "stats"


class Sum(Agg):
    name = "sum"


class TopMetrics(Agg):
    name = "top_metrics"


class TTest(Agg):
    name = "t_test"


class ValueCount(Agg):
    name = "value_count"


# pipeline aggregations
class AvgBucket(Pipeline):
    name = "avg_bucket"


class BucketScript(Pipeline):
    name = "bucket_script"


class BucketSelector(Pipeline):
    name = "bucket_selector"


class CumulativeSum(Pipeline):
    name = "cumulative_sum"


class CumulativeCardinality(Pipeline):
    name = "cumulative_cardinality"


class Derivative(Pipeline):
    name = "derivative"


class ExtendedStatsBucket(Pipeline):
    name = "extended_stats_bucket"


class Inference(Pipeline):
    name = "inference"


class MaxBucket(Pipeline):
    name = "max_bucket"


class MinBucket(Pipeline):
    name = "min_bucket"


class MovingFn(Pipeline):
    name = "moving_fn"


class MovingAvg(Pipeline):
    name = "moving_avg"


class MovingPercentiles(Pipeline):
    name = "moving_percentiles"


class Normalize(Pipeline):
    name = "normalize"


class PercentilesBucket(Pipeline):
    name = "percentiles_bucket"


class SerialDiff(Pipeline):
    name = "serial_diff"


class StatsBucket(Pipeline):
    name = "stats_bucket"


class SumBucket(Pipeline):
    name = "sum_bucket"


class BucketSort(Pipeline):
    name = "bucket_sort"
