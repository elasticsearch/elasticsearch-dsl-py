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

from typing import Any, Dict, Literal, Mapping, Sequence, Union

from elastic_transport.client_utils import DEFAULT, DefaultType

from elasticsearch_dsl import Query, function, types
from elasticsearch_dsl.document_base import InstrumentedField
from elasticsearch_dsl.utils import AttrDict

PipeSeparatedFlags = str


class QueryBase(AttrDict[Any]):
    """
    :arg boost: Floating point number used to decrease or increase the
        relevance scores of the query. Boost values are relative to the
        default value of 1.0. A boost value between 0 and 1.0 decreases
        the relevance score. A value greater than 1.0 increases the
        relevance score.
    :arg _name:
    """

    boost: Union[float, "DefaultType"]
    _name: Union[str, "DefaultType"]

    def __init__(
        self,
        *,
        boost: Union[float, "DefaultType"] = DEFAULT,
        _name: Union[str, "DefaultType"] = DEFAULT,
        **kwargs: Any,
    ):
        if boost is not DEFAULT:
            kwargs["boost"] = boost
        if _name is not DEFAULT:
            kwargs["_name"] = _name
        super().__init__(kwargs)


class CommonTermsQuery(QueryBase):
    """
    :arg query: (required)
    :arg analyzer:
    :arg cutoff_frequency:
    :arg high_freq_operator:
    :arg low_freq_operator:
    :arg minimum_should_match:
    :arg boost: Floating point number used to decrease or increase the
        relevance scores of the query. Boost values are relative to the
        default value of 1.0. A boost value between 0 and 1.0 decreases
        the relevance score. A value greater than 1.0 increases the
        relevance score.
    :arg _name:
    """

    query: Union[str, "DefaultType"]
    analyzer: Union[str, "DefaultType"]
    cutoff_frequency: Union[float, "DefaultType"]
    high_freq_operator: Union[Literal["and", "or"], "DefaultType"]
    low_freq_operator: Union[Literal["and", "or"], "DefaultType"]
    minimum_should_match: Union[int, str, "DefaultType"]
    boost: Union[float, "DefaultType"]
    _name: Union[str, "DefaultType"]

    def __init__(
        self,
        *,
        query: Union[str, "DefaultType"] = DEFAULT,
        analyzer: Union[str, "DefaultType"] = DEFAULT,
        cutoff_frequency: Union[float, "DefaultType"] = DEFAULT,
        high_freq_operator: Union[Literal["and", "or"], "DefaultType"] = DEFAULT,
        low_freq_operator: Union[Literal["and", "or"], "DefaultType"] = DEFAULT,
        minimum_should_match: Union[int, str, "DefaultType"] = DEFAULT,
        boost: Union[float, "DefaultType"] = DEFAULT,
        _name: Union[str, "DefaultType"] = DEFAULT,
        **kwargs: Any,
    ):
        if query is not DEFAULT:
            kwargs["query"] = query
        if analyzer is not DEFAULT:
            kwargs["analyzer"] = analyzer
        if cutoff_frequency is not DEFAULT:
            kwargs["cutoff_frequency"] = cutoff_frequency
        if high_freq_operator is not DEFAULT:
            kwargs["high_freq_operator"] = high_freq_operator
        if low_freq_operator is not DEFAULT:
            kwargs["low_freq_operator"] = low_freq_operator
        if minimum_should_match is not DEFAULT:
            kwargs["minimum_should_match"] = minimum_should_match
        if boost is not DEFAULT:
            kwargs["boost"] = boost
        if _name is not DEFAULT:
            kwargs["_name"] = _name
        super().__init__(**kwargs)


class CoordsGeoBounds(AttrDict[Any]):
    """
    :arg top: (required)
    :arg bottom: (required)
    :arg left: (required)
    :arg right: (required)
    """

    top: Union[float, "DefaultType"]
    bottom: Union[float, "DefaultType"]
    left: Union[float, "DefaultType"]
    right: Union[float, "DefaultType"]

    def __init__(
        self,
        *,
        top: Union[float, "DefaultType"] = DEFAULT,
        bottom: Union[float, "DefaultType"] = DEFAULT,
        left: Union[float, "DefaultType"] = DEFAULT,
        right: Union[float, "DefaultType"] = DEFAULT,
        **kwargs: Any,
    ):
        if top is not DEFAULT:
            kwargs["top"] = top
        if bottom is not DEFAULT:
            kwargs["bottom"] = bottom
        if left is not DEFAULT:
            kwargs["left"] = left
        if right is not DEFAULT:
            kwargs["right"] = right
        super().__init__(kwargs)


class FunctionScoreContainer(AttrDict[Any]):
    """
    :arg exp: Function that scores a document with a exponential decay,
        depending on the distance of a numeric field value of the document
        from an origin.
    :arg gauss: Function that scores a document with a normal decay,
        depending on the distance of a numeric field value of the document
        from an origin.
    :arg linear: Function that scores a document with a linear decay,
        depending on the distance of a numeric field value of the document
        from an origin.
    :arg field_value_factor: Function allows you to use a field from a
        document to influence the score. It’s similar to using the
        script_score function, however, it avoids the overhead of
        scripting.
    :arg random_score: Generates scores that are uniformly distributed
        from 0 up to but not including 1. In case you want scores to be
        reproducible, it is possible to provide a `seed` and `field`.
    :arg script_score: Enables you to wrap another query and customize the
        scoring of it optionally with a computation derived from other
        numeric field values in the doc using a script expression.
    :arg filter:
    :arg weight:
    """

    exp: Union["function.DecayFunction", "DefaultType"]
    gauss: Union["function.DecayFunction", "DefaultType"]
    linear: Union["function.DecayFunction", "DefaultType"]
    field_value_factor: Union["function.FieldValueFactorScore", "DefaultType"]
    random_score: Union["function.RandomScore", "DefaultType"]
    script_score: Union["function.ScriptScore", "DefaultType"]
    filter: Union[Query, "DefaultType"]
    weight: Union[float, "DefaultType"]

    def __init__(
        self,
        *,
        exp: Union["function.DecayFunction", "DefaultType"] = DEFAULT,
        gauss: Union["function.DecayFunction", "DefaultType"] = DEFAULT,
        linear: Union["function.DecayFunction", "DefaultType"] = DEFAULT,
        field_value_factor: Union[
            "function.FieldValueFactorScore", "DefaultType"
        ] = DEFAULT,
        random_score: Union["function.RandomScore", "DefaultType"] = DEFAULT,
        script_score: Union["function.ScriptScore", "DefaultType"] = DEFAULT,
        filter: Union[Query, "DefaultType"] = DEFAULT,
        weight: Union[float, "DefaultType"] = DEFAULT,
        **kwargs: Any,
    ):
        if exp is not DEFAULT:
            kwargs["exp"] = exp
        if gauss is not DEFAULT:
            kwargs["gauss"] = gauss
        if linear is not DEFAULT:
            kwargs["linear"] = linear
        if field_value_factor is not DEFAULT:
            kwargs["field_value_factor"] = field_value_factor
        if random_score is not DEFAULT:
            kwargs["random_score"] = random_score
        if script_score is not DEFAULT:
            kwargs["script_score"] = script_score
        if filter is not DEFAULT:
            kwargs["filter"] = filter
        if weight is not DEFAULT:
            kwargs["weight"] = weight
        super().__init__(kwargs)


class FuzzyQuery(QueryBase):
    """
    :arg value: (required) Term you wish to find in the provided field.
    :arg max_expansions: Maximum number of variations created.
    :arg prefix_length: Number of beginning characters left unchanged when
        creating expansions.
    :arg rewrite: Number of beginning characters left unchanged when
        creating expansions.
    :arg transpositions: Indicates whether edits include transpositions of
        two adjacent characters (for example `ab` to `ba`).
    :arg fuzziness: Maximum edit distance allowed for matching.
    :arg boost: Floating point number used to decrease or increase the
        relevance scores of the query. Boost values are relative to the
        default value of 1.0. A boost value between 0 and 1.0 decreases
        the relevance score. A value greater than 1.0 increases the
        relevance score.
    :arg _name:
    """

    value: Union[str, float, bool, "DefaultType"]
    max_expansions: Union[int, "DefaultType"]
    prefix_length: Union[int, "DefaultType"]
    rewrite: Union[str, "DefaultType"]
    transpositions: Union[bool, "DefaultType"]
    fuzziness: Union[str, int, "DefaultType"]
    boost: Union[float, "DefaultType"]
    _name: Union[str, "DefaultType"]

    def __init__(
        self,
        *,
        value: Union[str, float, bool, "DefaultType"] = DEFAULT,
        max_expansions: Union[int, "DefaultType"] = DEFAULT,
        prefix_length: Union[int, "DefaultType"] = DEFAULT,
        rewrite: Union[str, "DefaultType"] = DEFAULT,
        transpositions: Union[bool, "DefaultType"] = DEFAULT,
        fuzziness: Union[str, int, "DefaultType"] = DEFAULT,
        boost: Union[float, "DefaultType"] = DEFAULT,
        _name: Union[str, "DefaultType"] = DEFAULT,
        **kwargs: Any,
    ):
        if value is not DEFAULT:
            kwargs["value"] = value
        if max_expansions is not DEFAULT:
            kwargs["max_expansions"] = max_expansions
        if prefix_length is not DEFAULT:
            kwargs["prefix_length"] = prefix_length
        if rewrite is not DEFAULT:
            kwargs["rewrite"] = rewrite
        if transpositions is not DEFAULT:
            kwargs["transpositions"] = transpositions
        if fuzziness is not DEFAULT:
            kwargs["fuzziness"] = fuzziness
        if boost is not DEFAULT:
            kwargs["boost"] = boost
        if _name is not DEFAULT:
            kwargs["_name"] = _name
        super().__init__(**kwargs)


class GeoHashLocation(AttrDict[Any]):
    """
    :arg geohash: (required)
    """

    geohash: Union[str, "DefaultType"]

    def __init__(self, *, geohash: Union[str, "DefaultType"] = DEFAULT, **kwargs: Any):
        if geohash is not DEFAULT:
            kwargs["geohash"] = geohash
        super().__init__(kwargs)


class GeoPolygonPoints(AttrDict[Any]):
    """
    :arg points: (required)
    """

    points: Union[
        Sequence[
            Union[
                "types.LatLonGeoLocation", "types.GeoHashLocation", Sequence[float], str
            ]
        ],
        Dict[str, Any],
        "DefaultType",
    ]

    def __init__(
        self,
        *,
        points: Union[
            Sequence[
                Union[
                    "types.LatLonGeoLocation",
                    "types.GeoHashLocation",
                    Sequence[float],
                    str,
                ]
            ],
            Dict[str, Any],
            "DefaultType",
        ] = DEFAULT,
        **kwargs: Any,
    ):
        if points is not DEFAULT:
            kwargs["points"] = points
        super().__init__(kwargs)


class GeoShapeFieldQuery(AttrDict[Any]):
    """
    :arg shape:
    :arg indexed_shape: Query using an indexed shape retrieved from the
        the specified document and path.
    :arg relation: Spatial relation operator used to search a geo field.
    """

    shape: Any
    indexed_shape: Union["types.FieldLookup", Dict[str, Any], "DefaultType"]
    relation: Union[
        Literal["intersects", "disjoint", "within", "contains"], "DefaultType"
    ]

    def __init__(
        self,
        *,
        shape: Any = DEFAULT,
        indexed_shape: Union[
            "types.FieldLookup", Dict[str, Any], "DefaultType"
        ] = DEFAULT,
        relation: Union[
            Literal["intersects", "disjoint", "within", "contains"], "DefaultType"
        ] = DEFAULT,
        **kwargs: Any,
    ):
        if shape is not DEFAULT:
            kwargs["shape"] = shape
        if indexed_shape is not DEFAULT:
            kwargs["indexed_shape"] = indexed_shape
        if relation is not DEFAULT:
            kwargs["relation"] = relation
        super().__init__(kwargs)


class InnerHits(AttrDict[Any]):
    """
    :arg name: The name for the particular inner hit definition in the
        response. Useful when a search request contains multiple inner
        hits.
    :arg size: The maximum number of hits to return per `inner_hits`.
    :arg from: Inner hit starting document offset.
    :arg collapse:
    :arg docvalue_fields:
    :arg explain:
    :arg highlight:
    :arg ignore_unmapped:
    :arg script_fields:
    :arg seq_no_primary_term:
    :arg fields:
    :arg sort: How the inner hits should be sorted per `inner_hits`. By
        default, inner hits are sorted by score.
    :arg _source:
    :arg stored_fields:
    :arg track_scores:
    :arg version:
    """

    name: Union[str, "DefaultType"]
    size: Union[int, "DefaultType"]
    from_: Union[int, "DefaultType"]
    collapse: Union["types.FieldCollapse", Dict[str, Any], "DefaultType"]
    docvalue_fields: Union[
        Sequence["types.FieldAndFormat"], Dict[str, Any], "DefaultType"
    ]
    explain: Union[bool, "DefaultType"]
    highlight: Union["types.Highlight", Dict[str, Any], "DefaultType"]
    ignore_unmapped: Union[bool, "DefaultType"]
    script_fields: Union[
        Mapping[Union[str, "InstrumentedField"], "types.ScriptField"],
        Dict[str, Any],
        "DefaultType",
    ]
    seq_no_primary_term: Union[bool, "DefaultType"]
    fields: Union[
        Union[str, "InstrumentedField"],
        Sequence[Union[str, "InstrumentedField"]],
        "DefaultType",
    ]
    sort: Union[
        Union[Union[str, "InstrumentedField"], "types.SortOptions"],
        Sequence[Union[Union[str, "InstrumentedField"], "types.SortOptions"]],
        Dict[str, Any],
        "DefaultType",
    ]
    _source: Union[bool, "types.SourceFilter", Dict[str, Any], "DefaultType"]
    stored_fields: Union[
        Union[str, "InstrumentedField"],
        Sequence[Union[str, "InstrumentedField"]],
        "DefaultType",
    ]
    track_scores: Union[bool, "DefaultType"]
    version: Union[bool, "DefaultType"]

    def __init__(
        self,
        *,
        name: Union[str, "DefaultType"] = DEFAULT,
        size: Union[int, "DefaultType"] = DEFAULT,
        from_: Union[int, "DefaultType"] = DEFAULT,
        collapse: Union["types.FieldCollapse", Dict[str, Any], "DefaultType"] = DEFAULT,
        docvalue_fields: Union[
            Sequence["types.FieldAndFormat"], Dict[str, Any], "DefaultType"
        ] = DEFAULT,
        explain: Union[bool, "DefaultType"] = DEFAULT,
        highlight: Union["types.Highlight", Dict[str, Any], "DefaultType"] = DEFAULT,
        ignore_unmapped: Union[bool, "DefaultType"] = DEFAULT,
        script_fields: Union[
            Mapping[Union[str, "InstrumentedField"], "types.ScriptField"],
            Dict[str, Any],
            "DefaultType",
        ] = DEFAULT,
        seq_no_primary_term: Union[bool, "DefaultType"] = DEFAULT,
        fields: Union[
            Union[str, "InstrumentedField"],
            Sequence[Union[str, "InstrumentedField"]],
            "DefaultType",
        ] = DEFAULT,
        sort: Union[
            Union[Union[str, "InstrumentedField"], "types.SortOptions"],
            Sequence[Union[Union[str, "InstrumentedField"], "types.SortOptions"]],
            Dict[str, Any],
            "DefaultType",
        ] = DEFAULT,
        _source: Union[
            bool, "types.SourceFilter", Dict[str, Any], "DefaultType"
        ] = DEFAULT,
        stored_fields: Union[
            Union[str, "InstrumentedField"],
            Sequence[Union[str, "InstrumentedField"]],
            "DefaultType",
        ] = DEFAULT,
        track_scores: Union[bool, "DefaultType"] = DEFAULT,
        version: Union[bool, "DefaultType"] = DEFAULT,
        **kwargs: Any,
    ):
        if name is not DEFAULT:
            kwargs["name"] = name
        if size is not DEFAULT:
            kwargs["size"] = size
        if from_ is not DEFAULT:
            kwargs["from_"] = from_
        if collapse is not DEFAULT:
            kwargs["collapse"] = collapse
        if docvalue_fields is not DEFAULT:
            kwargs["docvalue_fields"] = docvalue_fields
        if explain is not DEFAULT:
            kwargs["explain"] = explain
        if highlight is not DEFAULT:
            kwargs["highlight"] = highlight
        if ignore_unmapped is not DEFAULT:
            kwargs["ignore_unmapped"] = ignore_unmapped
        if script_fields is not DEFAULT:
            kwargs["script_fields"] = str(script_fields)
        if seq_no_primary_term is not DEFAULT:
            kwargs["seq_no_primary_term"] = seq_no_primary_term
        if fields is not DEFAULT:
            kwargs["fields"] = str(fields)
        if sort is not DEFAULT:
            kwargs["sort"] = str(sort)
        if _source is not DEFAULT:
            kwargs["_source"] = _source
        if stored_fields is not DEFAULT:
            kwargs["stored_fields"] = str(stored_fields)
        if track_scores is not DEFAULT:
            kwargs["track_scores"] = track_scores
        if version is not DEFAULT:
            kwargs["version"] = version
        super().__init__(kwargs)


class IntervalsQuery(QueryBase):
    """
    :arg all_of: Returns matches that span a combination of other rules.
    :arg any_of: Returns intervals produced by any of its sub-rules.
    :arg fuzzy: Matches terms that are similar to the provided term,
        within an edit distance defined by `fuzziness`.
    :arg match: Matches analyzed text.
    :arg prefix: Matches terms that start with a specified set of
        characters.
    :arg wildcard: Matches terms using a wildcard pattern.
    :arg boost: Floating point number used to decrease or increase the
        relevance scores of the query. Boost values are relative to the
        default value of 1.0. A boost value between 0 and 1.0 decreases
        the relevance score. A value greater than 1.0 increases the
        relevance score.
    :arg _name:
    """

    all_of: Union["types.IntervalsAllOf", Dict[str, Any], "DefaultType"]
    any_of: Union["types.IntervalsAnyOf", Dict[str, Any], "DefaultType"]
    fuzzy: Union["types.IntervalsFuzzy", Dict[str, Any], "DefaultType"]
    match: Union["types.IntervalsMatch", Dict[str, Any], "DefaultType"]
    prefix: Union["types.IntervalsPrefix", Dict[str, Any], "DefaultType"]
    wildcard: Union["types.IntervalsWildcard", Dict[str, Any], "DefaultType"]
    boost: Union[float, "DefaultType"]
    _name: Union[str, "DefaultType"]

    def __init__(
        self,
        *,
        all_of: Union["types.IntervalsAllOf", Dict[str, Any], "DefaultType"] = DEFAULT,
        any_of: Union["types.IntervalsAnyOf", Dict[str, Any], "DefaultType"] = DEFAULT,
        fuzzy: Union["types.IntervalsFuzzy", Dict[str, Any], "DefaultType"] = DEFAULT,
        match: Union["types.IntervalsMatch", Dict[str, Any], "DefaultType"] = DEFAULT,
        prefix: Union["types.IntervalsPrefix", Dict[str, Any], "DefaultType"] = DEFAULT,
        wildcard: Union[
            "types.IntervalsWildcard", Dict[str, Any], "DefaultType"
        ] = DEFAULT,
        boost: Union[float, "DefaultType"] = DEFAULT,
        _name: Union[str, "DefaultType"] = DEFAULT,
        **kwargs: Any,
    ):
        if all_of is not DEFAULT:
            kwargs["all_of"] = all_of
        if any_of is not DEFAULT:
            kwargs["any_of"] = any_of
        if fuzzy is not DEFAULT:
            kwargs["fuzzy"] = fuzzy
        if match is not DEFAULT:
            kwargs["match"] = match
        if prefix is not DEFAULT:
            kwargs["prefix"] = prefix
        if wildcard is not DEFAULT:
            kwargs["wildcard"] = wildcard
        if boost is not DEFAULT:
            kwargs["boost"] = boost
        if _name is not DEFAULT:
            kwargs["_name"] = _name
        super().__init__(**kwargs)


class LatLonGeoLocation(AttrDict[Any]):
    """
    :arg lat: (required) Latitude
    :arg lon: (required) Longitude
    """

    lat: Union[float, "DefaultType"]
    lon: Union[float, "DefaultType"]

    def __init__(
        self,
        *,
        lat: Union[float, "DefaultType"] = DEFAULT,
        lon: Union[float, "DefaultType"] = DEFAULT,
        **kwargs: Any,
    ):
        if lat is not DEFAULT:
            kwargs["lat"] = lat
        if lon is not DEFAULT:
            kwargs["lon"] = lon
        super().__init__(kwargs)


class LikeDocument(AttrDict[Any]):
    """
    :arg doc: A document not present in the index.
    :arg fields:
    :arg _id: ID of a document.
    :arg _index: Index of a document.
    :arg per_field_analyzer: Overrides the default analyzer.
    :arg routing:
    :arg version:
    :arg version_type:
    """

    doc: Any
    fields: Union[Sequence[Union[str, "InstrumentedField"]], "DefaultType"]
    _id: Union[str, "DefaultType"]
    _index: Union[str, "DefaultType"]
    per_field_analyzer: Union[
        Mapping[Union[str, "InstrumentedField"], str], "DefaultType"
    ]
    routing: Union[str, "DefaultType"]
    version: Union[int, "DefaultType"]
    version_type: Union[
        Literal["internal", "external", "external_gte", "force"], "DefaultType"
    ]

    def __init__(
        self,
        *,
        doc: Any = DEFAULT,
        fields: Union[
            Sequence[Union[str, "InstrumentedField"]], "DefaultType"
        ] = DEFAULT,
        _id: Union[str, "DefaultType"] = DEFAULT,
        _index: Union[str, "DefaultType"] = DEFAULT,
        per_field_analyzer: Union[
            Mapping[Union[str, "InstrumentedField"], str], "DefaultType"
        ] = DEFAULT,
        routing: Union[str, "DefaultType"] = DEFAULT,
        version: Union[int, "DefaultType"] = DEFAULT,
        version_type: Union[
            Literal["internal", "external", "external_gte", "force"], "DefaultType"
        ] = DEFAULT,
        **kwargs: Any,
    ):
        if doc is not DEFAULT:
            kwargs["doc"] = doc
        if fields is not DEFAULT:
            kwargs["fields"] = str(fields)
        if _id is not DEFAULT:
            kwargs["_id"] = _id
        if _index is not DEFAULT:
            kwargs["_index"] = _index
        if per_field_analyzer is not DEFAULT:
            kwargs["per_field_analyzer"] = str(per_field_analyzer)
        if routing is not DEFAULT:
            kwargs["routing"] = routing
        if version is not DEFAULT:
            kwargs["version"] = version
        if version_type is not DEFAULT:
            kwargs["version_type"] = version_type
        super().__init__(kwargs)


class MatchBoolPrefixQuery(QueryBase):
    """
    :arg query: (required) Terms you wish to find in the provided field.
        The last term is used in a prefix query.
    :arg analyzer: Analyzer used to convert the text in the query value
        into tokens.
    :arg fuzziness: Maximum edit distance allowed for matching. Can be
        applied to the term subqueries constructed for all terms but the
        final term.
    :arg fuzzy_rewrite: Method used to rewrite the query. Can be applied
        to the term subqueries constructed for all terms but the final
        term.
    :arg fuzzy_transpositions: If `true`, edits for fuzzy matching include
        transpositions of two adjacent characters (for example, `ab` to
        `ba`). Can be applied to the term subqueries constructed for all
        terms but the final term.
    :arg max_expansions: Maximum number of terms to which the query will
        expand. Can be applied to the term subqueries constructed for all
        terms but the final term.
    :arg minimum_should_match: Minimum number of clauses that must match
        for a document to be returned. Applied to the constructed bool
        query.
    :arg operator: Boolean logic used to interpret text in the query
        value. Applied to the constructed bool query.
    :arg prefix_length: Number of beginning characters left unchanged for
        fuzzy matching. Can be applied to the term subqueries constructed
        for all terms but the final term.
    :arg boost: Floating point number used to decrease or increase the
        relevance scores of the query. Boost values are relative to the
        default value of 1.0. A boost value between 0 and 1.0 decreases
        the relevance score. A value greater than 1.0 increases the
        relevance score.
    :arg _name:
    """

    query: Union[str, "DefaultType"]
    analyzer: Union[str, "DefaultType"]
    fuzziness: Union[str, int, "DefaultType"]
    fuzzy_rewrite: Union[str, "DefaultType"]
    fuzzy_transpositions: Union[bool, "DefaultType"]
    max_expansions: Union[int, "DefaultType"]
    minimum_should_match: Union[int, str, "DefaultType"]
    operator: Union[Literal["and", "or"], "DefaultType"]
    prefix_length: Union[int, "DefaultType"]
    boost: Union[float, "DefaultType"]
    _name: Union[str, "DefaultType"]

    def __init__(
        self,
        *,
        query: Union[str, "DefaultType"] = DEFAULT,
        analyzer: Union[str, "DefaultType"] = DEFAULT,
        fuzziness: Union[str, int, "DefaultType"] = DEFAULT,
        fuzzy_rewrite: Union[str, "DefaultType"] = DEFAULT,
        fuzzy_transpositions: Union[bool, "DefaultType"] = DEFAULT,
        max_expansions: Union[int, "DefaultType"] = DEFAULT,
        minimum_should_match: Union[int, str, "DefaultType"] = DEFAULT,
        operator: Union[Literal["and", "or"], "DefaultType"] = DEFAULT,
        prefix_length: Union[int, "DefaultType"] = DEFAULT,
        boost: Union[float, "DefaultType"] = DEFAULT,
        _name: Union[str, "DefaultType"] = DEFAULT,
        **kwargs: Any,
    ):
        if query is not DEFAULT:
            kwargs["query"] = query
        if analyzer is not DEFAULT:
            kwargs["analyzer"] = analyzer
        if fuzziness is not DEFAULT:
            kwargs["fuzziness"] = fuzziness
        if fuzzy_rewrite is not DEFAULT:
            kwargs["fuzzy_rewrite"] = fuzzy_rewrite
        if fuzzy_transpositions is not DEFAULT:
            kwargs["fuzzy_transpositions"] = fuzzy_transpositions
        if max_expansions is not DEFAULT:
            kwargs["max_expansions"] = max_expansions
        if minimum_should_match is not DEFAULT:
            kwargs["minimum_should_match"] = minimum_should_match
        if operator is not DEFAULT:
            kwargs["operator"] = operator
        if prefix_length is not DEFAULT:
            kwargs["prefix_length"] = prefix_length
        if boost is not DEFAULT:
            kwargs["boost"] = boost
        if _name is not DEFAULT:
            kwargs["_name"] = _name
        super().__init__(**kwargs)


class MatchPhrasePrefixQuery(QueryBase):
    """
    :arg query: (required) Text you wish to find in the provided field.
    :arg analyzer: Analyzer used to convert text in the query value into
        tokens.
    :arg max_expansions: Maximum number of terms to which the last
        provided term of the query value will expand.
    :arg slop: Maximum number of positions allowed between matching
        tokens.
    :arg zero_terms_query: Indicates whether no documents are returned if
        the analyzer removes all tokens, such as when using a `stop`
        filter.
    :arg boost: Floating point number used to decrease or increase the
        relevance scores of the query. Boost values are relative to the
        default value of 1.0. A boost value between 0 and 1.0 decreases
        the relevance score. A value greater than 1.0 increases the
        relevance score.
    :arg _name:
    """

    query: Union[str, "DefaultType"]
    analyzer: Union[str, "DefaultType"]
    max_expansions: Union[int, "DefaultType"]
    slop: Union[int, "DefaultType"]
    zero_terms_query: Union[Literal["all", "none"], "DefaultType"]
    boost: Union[float, "DefaultType"]
    _name: Union[str, "DefaultType"]

    def __init__(
        self,
        *,
        query: Union[str, "DefaultType"] = DEFAULT,
        analyzer: Union[str, "DefaultType"] = DEFAULT,
        max_expansions: Union[int, "DefaultType"] = DEFAULT,
        slop: Union[int, "DefaultType"] = DEFAULT,
        zero_terms_query: Union[Literal["all", "none"], "DefaultType"] = DEFAULT,
        boost: Union[float, "DefaultType"] = DEFAULT,
        _name: Union[str, "DefaultType"] = DEFAULT,
        **kwargs: Any,
    ):
        if query is not DEFAULT:
            kwargs["query"] = query
        if analyzer is not DEFAULT:
            kwargs["analyzer"] = analyzer
        if max_expansions is not DEFAULT:
            kwargs["max_expansions"] = max_expansions
        if slop is not DEFAULT:
            kwargs["slop"] = slop
        if zero_terms_query is not DEFAULT:
            kwargs["zero_terms_query"] = zero_terms_query
        if boost is not DEFAULT:
            kwargs["boost"] = boost
        if _name is not DEFAULT:
            kwargs["_name"] = _name
        super().__init__(**kwargs)


class MatchPhraseQuery(QueryBase):
    """
    :arg query: (required) Query terms that are analyzed and turned into a
        phrase query.
    :arg analyzer: Analyzer used to convert the text in the query value
        into tokens.
    :arg slop: Maximum number of positions allowed between matching
        tokens.
    :arg zero_terms_query: Indicates whether no documents are returned if
        the `analyzer` removes all tokens, such as when using a `stop`
        filter.
    :arg boost: Floating point number used to decrease or increase the
        relevance scores of the query. Boost values are relative to the
        default value of 1.0. A boost value between 0 and 1.0 decreases
        the relevance score. A value greater than 1.0 increases the
        relevance score.
    :arg _name:
    """

    query: Union[str, "DefaultType"]
    analyzer: Union[str, "DefaultType"]
    slop: Union[int, "DefaultType"]
    zero_terms_query: Union[Literal["all", "none"], "DefaultType"]
    boost: Union[float, "DefaultType"]
    _name: Union[str, "DefaultType"]

    def __init__(
        self,
        *,
        query: Union[str, "DefaultType"] = DEFAULT,
        analyzer: Union[str, "DefaultType"] = DEFAULT,
        slop: Union[int, "DefaultType"] = DEFAULT,
        zero_terms_query: Union[Literal["all", "none"], "DefaultType"] = DEFAULT,
        boost: Union[float, "DefaultType"] = DEFAULT,
        _name: Union[str, "DefaultType"] = DEFAULT,
        **kwargs: Any,
    ):
        if query is not DEFAULT:
            kwargs["query"] = query
        if analyzer is not DEFAULT:
            kwargs["analyzer"] = analyzer
        if slop is not DEFAULT:
            kwargs["slop"] = slop
        if zero_terms_query is not DEFAULT:
            kwargs["zero_terms_query"] = zero_terms_query
        if boost is not DEFAULT:
            kwargs["boost"] = boost
        if _name is not DEFAULT:
            kwargs["_name"] = _name
        super().__init__(**kwargs)


class MatchQuery(QueryBase):
    """
    :arg query: (required) Text, number, boolean value or date you wish to
        find in the provided field.
    :arg analyzer: Analyzer used to convert the text in the query value
        into tokens.
    :arg auto_generate_synonyms_phrase_query: If `true`, match phrase
        queries are automatically created for multi-term synonyms.
    :arg cutoff_frequency:
    :arg fuzziness: Maximum edit distance allowed for matching.
    :arg fuzzy_rewrite: Method used to rewrite the query.
    :arg fuzzy_transpositions: If `true`, edits for fuzzy matching include
        transpositions of two adjacent characters (for example, `ab` to
        `ba`).
    :arg lenient: If `true`, format-based errors, such as providing a text
        query value for a numeric field, are ignored.
    :arg max_expansions: Maximum number of terms to which the query will
        expand.
    :arg minimum_should_match: Minimum number of clauses that must match
        for a document to be returned.
    :arg operator: Boolean logic used to interpret text in the query
        value.
    :arg prefix_length: Number of beginning characters left unchanged for
        fuzzy matching.
    :arg zero_terms_query: Indicates whether no documents are returned if
        the `analyzer` removes all tokens, such as when using a `stop`
        filter.
    :arg boost: Floating point number used to decrease or increase the
        relevance scores of the query. Boost values are relative to the
        default value of 1.0. A boost value between 0 and 1.0 decreases
        the relevance score. A value greater than 1.0 increases the
        relevance score.
    :arg _name:
    """

    query: Union[str, float, bool, "DefaultType"]
    analyzer: Union[str, "DefaultType"]
    auto_generate_synonyms_phrase_query: Union[bool, "DefaultType"]
    cutoff_frequency: Union[float, "DefaultType"]
    fuzziness: Union[str, int, "DefaultType"]
    fuzzy_rewrite: Union[str, "DefaultType"]
    fuzzy_transpositions: Union[bool, "DefaultType"]
    lenient: Union[bool, "DefaultType"]
    max_expansions: Union[int, "DefaultType"]
    minimum_should_match: Union[int, str, "DefaultType"]
    operator: Union[Literal["and", "or"], "DefaultType"]
    prefix_length: Union[int, "DefaultType"]
    zero_terms_query: Union[Literal["all", "none"], "DefaultType"]
    boost: Union[float, "DefaultType"]
    _name: Union[str, "DefaultType"]

    def __init__(
        self,
        *,
        query: Union[str, float, bool, "DefaultType"] = DEFAULT,
        analyzer: Union[str, "DefaultType"] = DEFAULT,
        auto_generate_synonyms_phrase_query: Union[bool, "DefaultType"] = DEFAULT,
        cutoff_frequency: Union[float, "DefaultType"] = DEFAULT,
        fuzziness: Union[str, int, "DefaultType"] = DEFAULT,
        fuzzy_rewrite: Union[str, "DefaultType"] = DEFAULT,
        fuzzy_transpositions: Union[bool, "DefaultType"] = DEFAULT,
        lenient: Union[bool, "DefaultType"] = DEFAULT,
        max_expansions: Union[int, "DefaultType"] = DEFAULT,
        minimum_should_match: Union[int, str, "DefaultType"] = DEFAULT,
        operator: Union[Literal["and", "or"], "DefaultType"] = DEFAULT,
        prefix_length: Union[int, "DefaultType"] = DEFAULT,
        zero_terms_query: Union[Literal["all", "none"], "DefaultType"] = DEFAULT,
        boost: Union[float, "DefaultType"] = DEFAULT,
        _name: Union[str, "DefaultType"] = DEFAULT,
        **kwargs: Any,
    ):
        if query is not DEFAULT:
            kwargs["query"] = query
        if analyzer is not DEFAULT:
            kwargs["analyzer"] = analyzer
        if auto_generate_synonyms_phrase_query is not DEFAULT:
            kwargs["auto_generate_synonyms_phrase_query"] = (
                auto_generate_synonyms_phrase_query
            )
        if cutoff_frequency is not DEFAULT:
            kwargs["cutoff_frequency"] = cutoff_frequency
        if fuzziness is not DEFAULT:
            kwargs["fuzziness"] = fuzziness
        if fuzzy_rewrite is not DEFAULT:
            kwargs["fuzzy_rewrite"] = fuzzy_rewrite
        if fuzzy_transpositions is not DEFAULT:
            kwargs["fuzzy_transpositions"] = fuzzy_transpositions
        if lenient is not DEFAULT:
            kwargs["lenient"] = lenient
        if max_expansions is not DEFAULT:
            kwargs["max_expansions"] = max_expansions
        if minimum_should_match is not DEFAULT:
            kwargs["minimum_should_match"] = minimum_should_match
        if operator is not DEFAULT:
            kwargs["operator"] = operator
        if prefix_length is not DEFAULT:
            kwargs["prefix_length"] = prefix_length
        if zero_terms_query is not DEFAULT:
            kwargs["zero_terms_query"] = zero_terms_query
        if boost is not DEFAULT:
            kwargs["boost"] = boost
        if _name is not DEFAULT:
            kwargs["_name"] = _name
        super().__init__(**kwargs)


class PinnedDoc(AttrDict[Any]):
    """
    :arg _id: (required) The unique document ID.
    :arg _index: (required) The index that contains the document.
    """

    _id: Union[str, "DefaultType"]
    _index: Union[str, "DefaultType"]

    def __init__(
        self,
        *,
        _id: Union[str, "DefaultType"] = DEFAULT,
        _index: Union[str, "DefaultType"] = DEFAULT,
        **kwargs: Any,
    ):
        if _id is not DEFAULT:
            kwargs["_id"] = _id
        if _index is not DEFAULT:
            kwargs["_index"] = _index
        super().__init__(kwargs)


class PrefixQuery(QueryBase):
    """
    :arg value: (required) Beginning characters of terms you wish to find
        in the provided field.
    :arg rewrite: Method used to rewrite the query.
    :arg case_insensitive: Allows ASCII case insensitive matching of the
        value with the indexed field values when set to `true`. Default is
        `false` which means the case sensitivity of matching depends on
        the underlying field’s mapping.
    :arg boost: Floating point number used to decrease or increase the
        relevance scores of the query. Boost values are relative to the
        default value of 1.0. A boost value between 0 and 1.0 decreases
        the relevance score. A value greater than 1.0 increases the
        relevance score.
    :arg _name:
    """

    value: Union[str, "DefaultType"]
    rewrite: Union[str, "DefaultType"]
    case_insensitive: Union[bool, "DefaultType"]
    boost: Union[float, "DefaultType"]
    _name: Union[str, "DefaultType"]

    def __init__(
        self,
        *,
        value: Union[str, "DefaultType"] = DEFAULT,
        rewrite: Union[str, "DefaultType"] = DEFAULT,
        case_insensitive: Union[bool, "DefaultType"] = DEFAULT,
        boost: Union[float, "DefaultType"] = DEFAULT,
        _name: Union[str, "DefaultType"] = DEFAULT,
        **kwargs: Any,
    ):
        if value is not DEFAULT:
            kwargs["value"] = value
        if rewrite is not DEFAULT:
            kwargs["rewrite"] = rewrite
        if case_insensitive is not DEFAULT:
            kwargs["case_insensitive"] = case_insensitive
        if boost is not DEFAULT:
            kwargs["boost"] = boost
        if _name is not DEFAULT:
            kwargs["_name"] = _name
        super().__init__(**kwargs)


class QueryVectorBuilder(AttrDict[Any]):
    """
    :arg text_embedding:
    """

    text_embedding: Union["types.TextEmbedding", Dict[str, Any], "DefaultType"]

    def __init__(
        self,
        *,
        text_embedding: Union[
            "types.TextEmbedding", Dict[str, Any], "DefaultType"
        ] = DEFAULT,
        **kwargs: Any,
    ):
        if text_embedding is not DEFAULT:
            kwargs["text_embedding"] = text_embedding
        super().__init__(kwargs)


class RankFeatureFunction(AttrDict[Any]):
    pass


class RankFeatureFunctionLinear(RankFeatureFunction):
    pass


class RankFeatureFunctionLogarithm(RankFeatureFunction):
    """
    :arg scaling_factor: (required) Configurable scaling factor.
    """

    scaling_factor: Union[float, "DefaultType"]

    def __init__(
        self, *, scaling_factor: Union[float, "DefaultType"] = DEFAULT, **kwargs: Any
    ):
        if scaling_factor is not DEFAULT:
            kwargs["scaling_factor"] = scaling_factor
        super().__init__(**kwargs)


class RankFeatureFunctionSaturation(RankFeatureFunction):
    """
    :arg pivot: Configurable pivot value so that the result will be less
        than 0.5.
    """

    pivot: Union[float, "DefaultType"]

    def __init__(self, *, pivot: Union[float, "DefaultType"] = DEFAULT, **kwargs: Any):
        if pivot is not DEFAULT:
            kwargs["pivot"] = pivot
        super().__init__(**kwargs)


class RankFeatureFunctionSigmoid(RankFeatureFunction):
    """
    :arg pivot: (required) Configurable pivot value so that the result
        will be less than 0.5.
    :arg exponent: (required) Configurable Exponent.
    """

    pivot: Union[float, "DefaultType"]
    exponent: Union[float, "DefaultType"]

    def __init__(
        self,
        *,
        pivot: Union[float, "DefaultType"] = DEFAULT,
        exponent: Union[float, "DefaultType"] = DEFAULT,
        **kwargs: Any,
    ):
        if pivot is not DEFAULT:
            kwargs["pivot"] = pivot
        if exponent is not DEFAULT:
            kwargs["exponent"] = exponent
        super().__init__(**kwargs)


class RegexpQuery(QueryBase):
    """
    :arg value: (required) Regular expression for terms you wish to find
        in the provided field.
    :arg case_insensitive: Allows case insensitive matching of the regular
        expression value with the indexed field values when set to `true`.
        When `false`, case sensitivity of matching depends on the
        underlying field’s mapping.
    :arg flags: Enables optional operators for the regular expression.
    :arg max_determinized_states: Maximum number of automaton states
        required for the query.
    :arg rewrite: Method used to rewrite the query.
    :arg boost: Floating point number used to decrease or increase the
        relevance scores of the query. Boost values are relative to the
        default value of 1.0. A boost value between 0 and 1.0 decreases
        the relevance score. A value greater than 1.0 increases the
        relevance score.
    :arg _name:
    """

    value: Union[str, "DefaultType"]
    case_insensitive: Union[bool, "DefaultType"]
    flags: Union[str, "DefaultType"]
    max_determinized_states: Union[int, "DefaultType"]
    rewrite: Union[str, "DefaultType"]
    boost: Union[float, "DefaultType"]
    _name: Union[str, "DefaultType"]

    def __init__(
        self,
        *,
        value: Union[str, "DefaultType"] = DEFAULT,
        case_insensitive: Union[bool, "DefaultType"] = DEFAULT,
        flags: Union[str, "DefaultType"] = DEFAULT,
        max_determinized_states: Union[int, "DefaultType"] = DEFAULT,
        rewrite: Union[str, "DefaultType"] = DEFAULT,
        boost: Union[float, "DefaultType"] = DEFAULT,
        _name: Union[str, "DefaultType"] = DEFAULT,
        **kwargs: Any,
    ):
        if value is not DEFAULT:
            kwargs["value"] = value
        if case_insensitive is not DEFAULT:
            kwargs["case_insensitive"] = case_insensitive
        if flags is not DEFAULT:
            kwargs["flags"] = flags
        if max_determinized_states is not DEFAULT:
            kwargs["max_determinized_states"] = max_determinized_states
        if rewrite is not DEFAULT:
            kwargs["rewrite"] = rewrite
        if boost is not DEFAULT:
            kwargs["boost"] = boost
        if _name is not DEFAULT:
            kwargs["_name"] = _name
        super().__init__(**kwargs)


class Script(AttrDict[Any]):
    """
    :arg source: The script source.
    :arg id: The `id` for a stored script.
    :arg params: Specifies any named parameters that are passed into the
        script as variables. Use parameters instead of hard-coded values
        to decrease compile time.
    :arg lang: Specifies the language the script is written in.
    :arg options:
    """

    source: Union[str, "DefaultType"]
    id: Union[str, "DefaultType"]
    params: Union[Mapping[str, Any], "DefaultType"]
    lang: Union[Literal["painless", "expression", "mustache", "java"], "DefaultType"]
    options: Union[Mapping[str, str], "DefaultType"]

    def __init__(
        self,
        *,
        source: Union[str, "DefaultType"] = DEFAULT,
        id: Union[str, "DefaultType"] = DEFAULT,
        params: Union[Mapping[str, Any], "DefaultType"] = DEFAULT,
        lang: Union[
            Literal["painless", "expression", "mustache", "java"], "DefaultType"
        ] = DEFAULT,
        options: Union[Mapping[str, str], "DefaultType"] = DEFAULT,
        **kwargs: Any,
    ):
        if source is not DEFAULT:
            kwargs["source"] = source
        if id is not DEFAULT:
            kwargs["id"] = id
        if params is not DEFAULT:
            kwargs["params"] = params
        if lang is not DEFAULT:
            kwargs["lang"] = lang
        if options is not DEFAULT:
            kwargs["options"] = options
        super().__init__(kwargs)


class ShapeFieldQuery(AttrDict[Any]):
    """
    :arg indexed_shape: Queries using a pre-indexed shape.
    :arg relation: Spatial relation between the query shape and the
        document shape.
    :arg shape: Queries using an inline shape definition in GeoJSON or
        Well Known Text (WKT) format.
    """

    indexed_shape: Union["types.FieldLookup", Dict[str, Any], "DefaultType"]
    relation: Union[
        Literal["intersects", "disjoint", "within", "contains"], "DefaultType"
    ]
    shape: Any

    def __init__(
        self,
        *,
        indexed_shape: Union[
            "types.FieldLookup", Dict[str, Any], "DefaultType"
        ] = DEFAULT,
        relation: Union[
            Literal["intersects", "disjoint", "within", "contains"], "DefaultType"
        ] = DEFAULT,
        shape: Any = DEFAULT,
        **kwargs: Any,
    ):
        if indexed_shape is not DEFAULT:
            kwargs["indexed_shape"] = indexed_shape
        if relation is not DEFAULT:
            kwargs["relation"] = relation
        if shape is not DEFAULT:
            kwargs["shape"] = shape
        super().__init__(kwargs)


class SpanQuery(AttrDict[Any]):
    """
    :arg span_containing: Accepts a list of span queries, but only returns
        those spans which also match a second span query.
    :arg span_field_masking: Allows queries like `span_near` or `span_or`
        across different fields.
    :arg span_first: Accepts another span query whose matches must appear
        within the first N positions of the field.
    :arg span_gap:
    :arg span_multi: Wraps a `term`, `range`, `prefix`, `wildcard`,
        `regexp`, or `fuzzy` query.
    :arg span_near: Accepts multiple span queries whose matches must be
        within the specified distance of each other, and possibly in the
        same order.
    :arg span_not: Wraps another span query, and excludes any documents
        which match that query.
    :arg span_or: Combines multiple span queries and returns documents
        which match any of the specified queries.
    :arg span_term: The equivalent of the `term` query but for use with
        other span queries.
    :arg span_within: The result from a single span query is returned as
        long is its span falls within the spans returned by a list of
        other span queries.
    """

    span_containing: Union["types.SpanContainingQuery", Dict[str, Any], "DefaultType"]
    span_field_masking: Union[
        "types.SpanFieldMaskingQuery", Dict[str, Any], "DefaultType"
    ]
    span_first: Union["types.SpanFirstQuery", Dict[str, Any], "DefaultType"]
    span_gap: Union[Mapping[Union[str, "InstrumentedField"], int], "DefaultType"]
    span_multi: Union["types.SpanMultiTermQuery", Dict[str, Any], "DefaultType"]
    span_near: Union["types.SpanNearQuery", Dict[str, Any], "DefaultType"]
    span_not: Union["types.SpanNotQuery", Dict[str, Any], "DefaultType"]
    span_or: Union["types.SpanOrQuery", Dict[str, Any], "DefaultType"]
    span_term: Union[
        Mapping[Union[str, "InstrumentedField"], "types.SpanTermQuery"],
        Dict[str, Any],
        "DefaultType",
    ]
    span_within: Union["types.SpanWithinQuery", Dict[str, Any], "DefaultType"]

    def __init__(
        self,
        *,
        span_containing: Union[
            "types.SpanContainingQuery", Dict[str, Any], "DefaultType"
        ] = DEFAULT,
        span_field_masking: Union[
            "types.SpanFieldMaskingQuery", Dict[str, Any], "DefaultType"
        ] = DEFAULT,
        span_first: Union[
            "types.SpanFirstQuery", Dict[str, Any], "DefaultType"
        ] = DEFAULT,
        span_gap: Union[
            Mapping[Union[str, "InstrumentedField"], int], "DefaultType"
        ] = DEFAULT,
        span_multi: Union[
            "types.SpanMultiTermQuery", Dict[str, Any], "DefaultType"
        ] = DEFAULT,
        span_near: Union[
            "types.SpanNearQuery", Dict[str, Any], "DefaultType"
        ] = DEFAULT,
        span_not: Union["types.SpanNotQuery", Dict[str, Any], "DefaultType"] = DEFAULT,
        span_or: Union["types.SpanOrQuery", Dict[str, Any], "DefaultType"] = DEFAULT,
        span_term: Union[
            Mapping[Union[str, "InstrumentedField"], "types.SpanTermQuery"],
            Dict[str, Any],
            "DefaultType",
        ] = DEFAULT,
        span_within: Union[
            "types.SpanWithinQuery", Dict[str, Any], "DefaultType"
        ] = DEFAULT,
        **kwargs: Any,
    ):
        if span_containing is not DEFAULT:
            kwargs["span_containing"] = span_containing
        if span_field_masking is not DEFAULT:
            kwargs["span_field_masking"] = span_field_masking
        if span_first is not DEFAULT:
            kwargs["span_first"] = span_first
        if span_gap is not DEFAULT:
            kwargs["span_gap"] = str(span_gap)
        if span_multi is not DEFAULT:
            kwargs["span_multi"] = span_multi
        if span_near is not DEFAULT:
            kwargs["span_near"] = span_near
        if span_not is not DEFAULT:
            kwargs["span_not"] = span_not
        if span_or is not DEFAULT:
            kwargs["span_or"] = span_or
        if span_term is not DEFAULT:
            kwargs["span_term"] = str(span_term)
        if span_within is not DEFAULT:
            kwargs["span_within"] = span_within
        super().__init__(kwargs)


class SpanTermQuery(QueryBase):
    """
    :arg value: (required)
    :arg boost: Floating point number used to decrease or increase the
        relevance scores of the query. Boost values are relative to the
        default value of 1.0. A boost value between 0 and 1.0 decreases
        the relevance score. A value greater than 1.0 increases the
        relevance score.
    :arg _name:
    """

    value: Union[str, "DefaultType"]
    boost: Union[float, "DefaultType"]
    _name: Union[str, "DefaultType"]

    def __init__(
        self,
        *,
        value: Union[str, "DefaultType"] = DEFAULT,
        boost: Union[float, "DefaultType"] = DEFAULT,
        _name: Union[str, "DefaultType"] = DEFAULT,
        **kwargs: Any,
    ):
        if value is not DEFAULT:
            kwargs["value"] = value
        if boost is not DEFAULT:
            kwargs["boost"] = boost
        if _name is not DEFAULT:
            kwargs["_name"] = _name
        super().__init__(**kwargs)


class TermQuery(QueryBase):
    """
    :arg value: (required) Term you wish to find in the provided field.
    :arg case_insensitive: Allows ASCII case insensitive matching of the
        value with the indexed field values when set to `true`. When
        `false`, the case sensitivity of matching depends on the
        underlying field’s mapping.
    :arg boost: Floating point number used to decrease or increase the
        relevance scores of the query. Boost values are relative to the
        default value of 1.0. A boost value between 0 and 1.0 decreases
        the relevance score. A value greater than 1.0 increases the
        relevance score.
    :arg _name:
    """

    value: Union[int, float, str, bool, None, Any, "DefaultType"]
    case_insensitive: Union[bool, "DefaultType"]
    boost: Union[float, "DefaultType"]
    _name: Union[str, "DefaultType"]

    def __init__(
        self,
        *,
        value: Union[int, float, str, bool, None, Any, "DefaultType"] = DEFAULT,
        case_insensitive: Union[bool, "DefaultType"] = DEFAULT,
        boost: Union[float, "DefaultType"] = DEFAULT,
        _name: Union[str, "DefaultType"] = DEFAULT,
        **kwargs: Any,
    ):
        if value is not DEFAULT:
            kwargs["value"] = value
        if case_insensitive is not DEFAULT:
            kwargs["case_insensitive"] = case_insensitive
        if boost is not DEFAULT:
            kwargs["boost"] = boost
        if _name is not DEFAULT:
            kwargs["_name"] = _name
        super().__init__(**kwargs)


class TermsLookup(AttrDict[Any]):
    """
    :arg index: (required)
    :arg id: (required)
    :arg path: (required)
    :arg routing:
    """

    index: Union[str, "DefaultType"]
    id: Union[str, "DefaultType"]
    path: Union[str, "InstrumentedField", "DefaultType"]
    routing: Union[str, "DefaultType"]

    def __init__(
        self,
        *,
        index: Union[str, "DefaultType"] = DEFAULT,
        id: Union[str, "DefaultType"] = DEFAULT,
        path: Union[str, "InstrumentedField", "DefaultType"] = DEFAULT,
        routing: Union[str, "DefaultType"] = DEFAULT,
        **kwargs: Any,
    ):
        if index is not DEFAULT:
            kwargs["index"] = index
        if id is not DEFAULT:
            kwargs["id"] = id
        if path is not DEFAULT:
            kwargs["path"] = str(path)
        if routing is not DEFAULT:
            kwargs["routing"] = routing
        super().__init__(kwargs)


class TermsSetQuery(QueryBase):
    """
    :arg terms: (required) Array of terms you wish to find in the provided
        field.
    :arg minimum_should_match_field: Numeric field containing the number
        of matching terms required to return a document.
    :arg minimum_should_match_script: Custom script containing the number
        of matching terms required to return a document.
    :arg boost: Floating point number used to decrease or increase the
        relevance scores of the query. Boost values are relative to the
        default value of 1.0. A boost value between 0 and 1.0 decreases
        the relevance score. A value greater than 1.0 increases the
        relevance score.
    :arg _name:
    """

    terms: Union[Sequence[str], "DefaultType"]
    minimum_should_match_field: Union[str, "InstrumentedField", "DefaultType"]
    minimum_should_match_script: Union["types.Script", Dict[str, Any], "DefaultType"]
    boost: Union[float, "DefaultType"]
    _name: Union[str, "DefaultType"]

    def __init__(
        self,
        *,
        terms: Union[Sequence[str], "DefaultType"] = DEFAULT,
        minimum_should_match_field: Union[
            str, "InstrumentedField", "DefaultType"
        ] = DEFAULT,
        minimum_should_match_script: Union[
            "types.Script", Dict[str, Any], "DefaultType"
        ] = DEFAULT,
        boost: Union[float, "DefaultType"] = DEFAULT,
        _name: Union[str, "DefaultType"] = DEFAULT,
        **kwargs: Any,
    ):
        if terms is not DEFAULT:
            kwargs["terms"] = terms
        if minimum_should_match_field is not DEFAULT:
            kwargs["minimum_should_match_field"] = str(minimum_should_match_field)
        if minimum_should_match_script is not DEFAULT:
            kwargs["minimum_should_match_script"] = minimum_should_match_script
        if boost is not DEFAULT:
            kwargs["boost"] = boost
        if _name is not DEFAULT:
            kwargs["_name"] = _name
        super().__init__(**kwargs)


class TextExpansionQuery(QueryBase):
    """
    :arg model_id: (required) The text expansion NLP model to use
    :arg model_text: (required) The query text
    :arg pruning_config: Token pruning configurations
    :arg boost: Floating point number used to decrease or increase the
        relevance scores of the query. Boost values are relative to the
        default value of 1.0. A boost value between 0 and 1.0 decreases
        the relevance score. A value greater than 1.0 increases the
        relevance score.
    :arg _name:
    """

    model_id: Union[str, "DefaultType"]
    model_text: Union[str, "DefaultType"]
    pruning_config: Union["types.TokenPruningConfig", Dict[str, Any], "DefaultType"]
    boost: Union[float, "DefaultType"]
    _name: Union[str, "DefaultType"]

    def __init__(
        self,
        *,
        model_id: Union[str, "DefaultType"] = DEFAULT,
        model_text: Union[str, "DefaultType"] = DEFAULT,
        pruning_config: Union[
            "types.TokenPruningConfig", Dict[str, Any], "DefaultType"
        ] = DEFAULT,
        boost: Union[float, "DefaultType"] = DEFAULT,
        _name: Union[str, "DefaultType"] = DEFAULT,
        **kwargs: Any,
    ):
        if model_id is not DEFAULT:
            kwargs["model_id"] = model_id
        if model_text is not DEFAULT:
            kwargs["model_text"] = model_text
        if pruning_config is not DEFAULT:
            kwargs["pruning_config"] = pruning_config
        if boost is not DEFAULT:
            kwargs["boost"] = boost
        if _name is not DEFAULT:
            kwargs["_name"] = _name
        super().__init__(**kwargs)


class TokenPruningConfig(AttrDict[Any]):
    """
    :arg tokens_freq_ratio_threshold: Tokens whose frequency is more than
        this threshold times the average frequency of all tokens in the
        specified field are considered outliers and pruned.
    :arg tokens_weight_threshold: Tokens whose weight is less than this
        threshold are considered nonsignificant and pruned.
    :arg only_score_pruned_tokens: Whether to only score pruned tokens, vs
        only scoring kept tokens.
    """

    tokens_freq_ratio_threshold: Union[int, "DefaultType"]
    tokens_weight_threshold: Union[float, "DefaultType"]
    only_score_pruned_tokens: Union[bool, "DefaultType"]

    def __init__(
        self,
        *,
        tokens_freq_ratio_threshold: Union[int, "DefaultType"] = DEFAULT,
        tokens_weight_threshold: Union[float, "DefaultType"] = DEFAULT,
        only_score_pruned_tokens: Union[bool, "DefaultType"] = DEFAULT,
        **kwargs: Any,
    ):
        if tokens_freq_ratio_threshold is not DEFAULT:
            kwargs["tokens_freq_ratio_threshold"] = tokens_freq_ratio_threshold
        if tokens_weight_threshold is not DEFAULT:
            kwargs["tokens_weight_threshold"] = tokens_weight_threshold
        if only_score_pruned_tokens is not DEFAULT:
            kwargs["only_score_pruned_tokens"] = only_score_pruned_tokens
        super().__init__(kwargs)


class TopLeftBottomRightGeoBounds(AttrDict[Any]):
    """
    :arg top_left: (required)
    :arg bottom_right: (required)
    """

    top_left: Union[
        "types.LatLonGeoLocation",
        "types.GeoHashLocation",
        Sequence[float],
        str,
        Dict[str, Any],
        "DefaultType",
    ]
    bottom_right: Union[
        "types.LatLonGeoLocation",
        "types.GeoHashLocation",
        Sequence[float],
        str,
        Dict[str, Any],
        "DefaultType",
    ]

    def __init__(
        self,
        *,
        top_left: Union[
            "types.LatLonGeoLocation",
            "types.GeoHashLocation",
            Sequence[float],
            str,
            Dict[str, Any],
            "DefaultType",
        ] = DEFAULT,
        bottom_right: Union[
            "types.LatLonGeoLocation",
            "types.GeoHashLocation",
            Sequence[float],
            str,
            Dict[str, Any],
            "DefaultType",
        ] = DEFAULT,
        **kwargs: Any,
    ):
        if top_left is not DEFAULT:
            kwargs["top_left"] = top_left
        if bottom_right is not DEFAULT:
            kwargs["bottom_right"] = bottom_right
        super().__init__(kwargs)


class TopRightBottomLeftGeoBounds(AttrDict[Any]):
    """
    :arg top_right: (required)
    :arg bottom_left: (required)
    """

    top_right: Union[
        "types.LatLonGeoLocation",
        "types.GeoHashLocation",
        Sequence[float],
        str,
        Dict[str, Any],
        "DefaultType",
    ]
    bottom_left: Union[
        "types.LatLonGeoLocation",
        "types.GeoHashLocation",
        Sequence[float],
        str,
        Dict[str, Any],
        "DefaultType",
    ]

    def __init__(
        self,
        *,
        top_right: Union[
            "types.LatLonGeoLocation",
            "types.GeoHashLocation",
            Sequence[float],
            str,
            Dict[str, Any],
            "DefaultType",
        ] = DEFAULT,
        bottom_left: Union[
            "types.LatLonGeoLocation",
            "types.GeoHashLocation",
            Sequence[float],
            str,
            Dict[str, Any],
            "DefaultType",
        ] = DEFAULT,
        **kwargs: Any,
    ):
        if top_right is not DEFAULT:
            kwargs["top_right"] = top_right
        if bottom_left is not DEFAULT:
            kwargs["bottom_left"] = bottom_left
        super().__init__(kwargs)


class WeightedTokensQuery(QueryBase):
    """
    :arg tokens: (required) The tokens representing this query
    :arg pruning_config: Token pruning configurations
    :arg boost: Floating point number used to decrease or increase the
        relevance scores of the query. Boost values are relative to the
        default value of 1.0. A boost value between 0 and 1.0 decreases
        the relevance score. A value greater than 1.0 increases the
        relevance score.
    :arg _name:
    """

    tokens: Union[Mapping[str, float], "DefaultType"]
    pruning_config: Union["types.TokenPruningConfig", Dict[str, Any], "DefaultType"]
    boost: Union[float, "DefaultType"]
    _name: Union[str, "DefaultType"]

    def __init__(
        self,
        *,
        tokens: Union[Mapping[str, float], "DefaultType"] = DEFAULT,
        pruning_config: Union[
            "types.TokenPruningConfig", Dict[str, Any], "DefaultType"
        ] = DEFAULT,
        boost: Union[float, "DefaultType"] = DEFAULT,
        _name: Union[str, "DefaultType"] = DEFAULT,
        **kwargs: Any,
    ):
        if tokens is not DEFAULT:
            kwargs["tokens"] = tokens
        if pruning_config is not DEFAULT:
            kwargs["pruning_config"] = pruning_config
        if boost is not DEFAULT:
            kwargs["boost"] = boost
        if _name is not DEFAULT:
            kwargs["_name"] = _name
        super().__init__(**kwargs)


class WildcardQuery(QueryBase):
    """
    :arg case_insensitive: Allows case insensitive matching of the pattern
        with the indexed field values when set to true. Default is false
        which means the case sensitivity of matching depends on the
        underlying field’s mapping.
    :arg rewrite: Method used to rewrite the query.
    :arg value: Wildcard pattern for terms you wish to find in the
        provided field. Required, when wildcard is not set.
    :arg wildcard: Wildcard pattern for terms you wish to find in the
        provided field. Required, when value is not set.
    :arg boost: Floating point number used to decrease or increase the
        relevance scores of the query. Boost values are relative to the
        default value of 1.0. A boost value between 0 and 1.0 decreases
        the relevance score. A value greater than 1.0 increases the
        relevance score.
    :arg _name:
    """

    case_insensitive: Union[bool, "DefaultType"]
    rewrite: Union[str, "DefaultType"]
    value: Union[str, "DefaultType"]
    wildcard: Union[str, "DefaultType"]
    boost: Union[float, "DefaultType"]
    _name: Union[str, "DefaultType"]

    def __init__(
        self,
        *,
        case_insensitive: Union[bool, "DefaultType"] = DEFAULT,
        rewrite: Union[str, "DefaultType"] = DEFAULT,
        value: Union[str, "DefaultType"] = DEFAULT,
        wildcard: Union[str, "DefaultType"] = DEFAULT,
        boost: Union[float, "DefaultType"] = DEFAULT,
        _name: Union[str, "DefaultType"] = DEFAULT,
        **kwargs: Any,
    ):
        if case_insensitive is not DEFAULT:
            kwargs["case_insensitive"] = case_insensitive
        if rewrite is not DEFAULT:
            kwargs["rewrite"] = rewrite
        if value is not DEFAULT:
            kwargs["value"] = value
        if wildcard is not DEFAULT:
            kwargs["wildcard"] = wildcard
        if boost is not DEFAULT:
            kwargs["boost"] = boost
        if _name is not DEFAULT:
            kwargs["_name"] = _name
        super().__init__(**kwargs)


class WktGeoBounds(AttrDict[Any]):
    """
    :arg wkt: (required)
    """

    wkt: Union[str, "DefaultType"]

    def __init__(self, *, wkt: Union[str, "DefaultType"] = DEFAULT, **kwargs: Any):
        if wkt is not DEFAULT:
            kwargs["wkt"] = wkt
        super().__init__(kwargs)


class FieldLookup(AttrDict[Any]):
    """
    :arg id: (required) `id` of the document.
    :arg index: Index from which to retrieve the document.
    :arg path: Name of the field.
    :arg routing: Custom routing value.
    """

    id: Union[str, "DefaultType"]
    index: Union[str, "DefaultType"]
    path: Union[str, "InstrumentedField", "DefaultType"]
    routing: Union[str, "DefaultType"]

    def __init__(
        self,
        *,
        id: Union[str, "DefaultType"] = DEFAULT,
        index: Union[str, "DefaultType"] = DEFAULT,
        path: Union[str, "InstrumentedField", "DefaultType"] = DEFAULT,
        routing: Union[str, "DefaultType"] = DEFAULT,
        **kwargs: Any,
    ):
        if id is not DEFAULT:
            kwargs["id"] = id
        if index is not DEFAULT:
            kwargs["index"] = index
        if path is not DEFAULT:
            kwargs["path"] = str(path)
        if routing is not DEFAULT:
            kwargs["routing"] = routing
        super().__init__(kwargs)


class FieldCollapse(AttrDict[Any]):
    """
    :arg field: (required) The field to collapse the result set on
    :arg inner_hits: The number of inner hits and their sort order
    :arg max_concurrent_group_searches: The number of concurrent requests
        allowed to retrieve the inner_hits per group
    :arg collapse:
    """

    field: Union[str, "InstrumentedField", "DefaultType"]
    inner_hits: Union[
        "types.InnerHits", Sequence["types.InnerHits"], Dict[str, Any], "DefaultType"
    ]
    max_concurrent_group_searches: Union[int, "DefaultType"]
    collapse: Union["types.FieldCollapse", Dict[str, Any], "DefaultType"]

    def __init__(
        self,
        *,
        field: Union[str, "InstrumentedField", "DefaultType"] = DEFAULT,
        inner_hits: Union[
            "types.InnerHits",
            Sequence["types.InnerHits"],
            Dict[str, Any],
            "DefaultType",
        ] = DEFAULT,
        max_concurrent_group_searches: Union[int, "DefaultType"] = DEFAULT,
        collapse: Union["types.FieldCollapse", Dict[str, Any], "DefaultType"] = DEFAULT,
        **kwargs: Any,
    ):
        if field is not DEFAULT:
            kwargs["field"] = str(field)
        if inner_hits is not DEFAULT:
            kwargs["inner_hits"] = inner_hits
        if max_concurrent_group_searches is not DEFAULT:
            kwargs["max_concurrent_group_searches"] = max_concurrent_group_searches
        if collapse is not DEFAULT:
            kwargs["collapse"] = collapse
        super().__init__(kwargs)


class FieldAndFormat(AttrDict[Any]):
    """
    :arg field: (required) Wildcard pattern. The request returns values
        for field names matching this pattern.
    :arg format: Format in which the values are returned.
    :arg include_unmapped:
    """

    field: Union[str, "InstrumentedField", "DefaultType"]
    format: Union[str, "DefaultType"]
    include_unmapped: Union[bool, "DefaultType"]

    def __init__(
        self,
        *,
        field: Union[str, "InstrumentedField", "DefaultType"] = DEFAULT,
        format: Union[str, "DefaultType"] = DEFAULT,
        include_unmapped: Union[bool, "DefaultType"] = DEFAULT,
        **kwargs: Any,
    ):
        if field is not DEFAULT:
            kwargs["field"] = str(field)
        if format is not DEFAULT:
            kwargs["format"] = format
        if include_unmapped is not DEFAULT:
            kwargs["include_unmapped"] = include_unmapped
        super().__init__(kwargs)


class HighlightBase(AttrDict[Any]):
    """
    :arg type:
    :arg boundary_chars: A string that contains each boundary character.
    :arg boundary_max_scan: How far to scan for boundary characters.
    :arg boundary_scanner: Specifies how to break the highlighted
        fragments: chars, sentence, or word. Only valid for the unified
        and fvh highlighters. Defaults to `sentence` for the `unified`
        highlighter. Defaults to `chars` for the `fvh` highlighter.
    :arg boundary_scanner_locale: Controls which locale is used to search
        for sentence and word boundaries. This parameter takes a form of a
        language tag, for example: `"en-US"`, `"fr-FR"`, `"ja-JP"`.
    :arg force_source:
    :arg fragmenter: Specifies how text should be broken up in highlight
        snippets: `simple` or `span`. Only valid for the `plain`
        highlighter.
    :arg fragment_size: The size of the highlighted fragment in
        characters.
    :arg highlight_filter:
    :arg highlight_query: Highlight matches for a query other than the
        search query. This is especially useful if you use a rescore query
        because those are not taken into account by highlighting by
        default.
    :arg max_fragment_length:
    :arg max_analyzed_offset: If set to a non-negative value, highlighting
        stops at this defined maximum limit. The rest of the text is not
        processed, thus not highlighted and no error is returned The
        `max_analyzed_offset` query setting does not override the
        `index.highlight.max_analyzed_offset` setting, which prevails when
        it’s set to lower value than the query setting.
    :arg no_match_size: The amount of text you want to return from the
        beginning of the field if there are no matching fragments to
        highlight.
    :arg number_of_fragments: The maximum number of fragments to return.
        If the number of fragments is set to `0`, no fragments are
        returned. Instead, the entire field contents are highlighted and
        returned. This can be handy when you need to highlight short texts
        such as a title or address, but fragmentation is not required. If
        `number_of_fragments` is `0`, `fragment_size` is ignored.
    :arg options:
    :arg order: Sorts highlighted fragments by score when set to `score`.
        By default, fragments will be output in the order they appear in
        the field (order: `none`). Setting this option to `score` will
        output the most relevant fragments first. Each highlighter applies
        its own logic to compute relevancy scores.
    :arg phrase_limit: Controls the number of matching phrases in a
        document that are considered. Prevents the `fvh` highlighter from
        analyzing too many phrases and consuming too much memory. When
        using `matched_fields`, `phrase_limit` phrases per matched field
        are considered. Raising the limit increases query time and
        consumes more memory. Only supported by the `fvh` highlighter.
    :arg post_tags: Use in conjunction with `pre_tags` to define the HTML
        tags to use for the highlighted text. By default, highlighted text
        is wrapped in `<em>` and `</em>` tags.
    :arg pre_tags: Use in conjunction with `post_tags` to define the HTML
        tags to use for the highlighted text. By default, highlighted text
        is wrapped in `<em>` and `</em>` tags.
    :arg require_field_match: By default, only fields that contains a
        query match are highlighted. Set to `false` to highlight all
        fields.
    :arg tags_schema: Set to `styled` to use the built-in tag schema.
    """

    type: Union[Literal["plain", "fvh", "unified"], "DefaultType"]
    boundary_chars: Union[str, "DefaultType"]
    boundary_max_scan: Union[int, "DefaultType"]
    boundary_scanner: Union[Literal["chars", "sentence", "word"], "DefaultType"]
    boundary_scanner_locale: Union[str, "DefaultType"]
    force_source: Union[bool, "DefaultType"]
    fragmenter: Union[Literal["simple", "span"], "DefaultType"]
    fragment_size: Union[int, "DefaultType"]
    highlight_filter: Union[bool, "DefaultType"]
    highlight_query: Union[Query, "DefaultType"]
    max_fragment_length: Union[int, "DefaultType"]
    max_analyzed_offset: Union[int, "DefaultType"]
    no_match_size: Union[int, "DefaultType"]
    number_of_fragments: Union[int, "DefaultType"]
    options: Union[Mapping[str, Any], "DefaultType"]
    order: Union[Literal["score"], "DefaultType"]
    phrase_limit: Union[int, "DefaultType"]
    post_tags: Union[Sequence[str], "DefaultType"]
    pre_tags: Union[Sequence[str], "DefaultType"]
    require_field_match: Union[bool, "DefaultType"]
    tags_schema: Union[Literal["styled"], "DefaultType"]

    def __init__(
        self,
        *,
        type: Union[Literal["plain", "fvh", "unified"], "DefaultType"] = DEFAULT,
        boundary_chars: Union[str, "DefaultType"] = DEFAULT,
        boundary_max_scan: Union[int, "DefaultType"] = DEFAULT,
        boundary_scanner: Union[
            Literal["chars", "sentence", "word"], "DefaultType"
        ] = DEFAULT,
        boundary_scanner_locale: Union[str, "DefaultType"] = DEFAULT,
        force_source: Union[bool, "DefaultType"] = DEFAULT,
        fragmenter: Union[Literal["simple", "span"], "DefaultType"] = DEFAULT,
        fragment_size: Union[int, "DefaultType"] = DEFAULT,
        highlight_filter: Union[bool, "DefaultType"] = DEFAULT,
        highlight_query: Union[Query, "DefaultType"] = DEFAULT,
        max_fragment_length: Union[int, "DefaultType"] = DEFAULT,
        max_analyzed_offset: Union[int, "DefaultType"] = DEFAULT,
        no_match_size: Union[int, "DefaultType"] = DEFAULT,
        number_of_fragments: Union[int, "DefaultType"] = DEFAULT,
        options: Union[Mapping[str, Any], "DefaultType"] = DEFAULT,
        order: Union[Literal["score"], "DefaultType"] = DEFAULT,
        phrase_limit: Union[int, "DefaultType"] = DEFAULT,
        post_tags: Union[Sequence[str], "DefaultType"] = DEFAULT,
        pre_tags: Union[Sequence[str], "DefaultType"] = DEFAULT,
        require_field_match: Union[bool, "DefaultType"] = DEFAULT,
        tags_schema: Union[Literal["styled"], "DefaultType"] = DEFAULT,
        **kwargs: Any,
    ):
        if type is not DEFAULT:
            kwargs["type"] = type
        if boundary_chars is not DEFAULT:
            kwargs["boundary_chars"] = boundary_chars
        if boundary_max_scan is not DEFAULT:
            kwargs["boundary_max_scan"] = boundary_max_scan
        if boundary_scanner is not DEFAULT:
            kwargs["boundary_scanner"] = boundary_scanner
        if boundary_scanner_locale is not DEFAULT:
            kwargs["boundary_scanner_locale"] = boundary_scanner_locale
        if force_source is not DEFAULT:
            kwargs["force_source"] = force_source
        if fragmenter is not DEFAULT:
            kwargs["fragmenter"] = fragmenter
        if fragment_size is not DEFAULT:
            kwargs["fragment_size"] = fragment_size
        if highlight_filter is not DEFAULT:
            kwargs["highlight_filter"] = highlight_filter
        if highlight_query is not DEFAULT:
            kwargs["highlight_query"] = highlight_query
        if max_fragment_length is not DEFAULT:
            kwargs["max_fragment_length"] = max_fragment_length
        if max_analyzed_offset is not DEFAULT:
            kwargs["max_analyzed_offset"] = max_analyzed_offset
        if no_match_size is not DEFAULT:
            kwargs["no_match_size"] = no_match_size
        if number_of_fragments is not DEFAULT:
            kwargs["number_of_fragments"] = number_of_fragments
        if options is not DEFAULT:
            kwargs["options"] = options
        if order is not DEFAULT:
            kwargs["order"] = order
        if phrase_limit is not DEFAULT:
            kwargs["phrase_limit"] = phrase_limit
        if post_tags is not DEFAULT:
            kwargs["post_tags"] = post_tags
        if pre_tags is not DEFAULT:
            kwargs["pre_tags"] = pre_tags
        if require_field_match is not DEFAULT:
            kwargs["require_field_match"] = require_field_match
        if tags_schema is not DEFAULT:
            kwargs["tags_schema"] = tags_schema
        super().__init__(kwargs)


class Highlight(HighlightBase):
    """
    :arg fields: (required)
    :arg encoder:
    :arg type:
    :arg boundary_chars: A string that contains each boundary character.
    :arg boundary_max_scan: How far to scan for boundary characters.
    :arg boundary_scanner: Specifies how to break the highlighted
        fragments: chars, sentence, or word. Only valid for the unified
        and fvh highlighters. Defaults to `sentence` for the `unified`
        highlighter. Defaults to `chars` for the `fvh` highlighter.
    :arg boundary_scanner_locale: Controls which locale is used to search
        for sentence and word boundaries. This parameter takes a form of a
        language tag, for example: `"en-US"`, `"fr-FR"`, `"ja-JP"`.
    :arg force_source:
    :arg fragmenter: Specifies how text should be broken up in highlight
        snippets: `simple` or `span`. Only valid for the `plain`
        highlighter.
    :arg fragment_size: The size of the highlighted fragment in
        characters.
    :arg highlight_filter:
    :arg highlight_query: Highlight matches for a query other than the
        search query. This is especially useful if you use a rescore query
        because those are not taken into account by highlighting by
        default.
    :arg max_fragment_length:
    :arg max_analyzed_offset: If set to a non-negative value, highlighting
        stops at this defined maximum limit. The rest of the text is not
        processed, thus not highlighted and no error is returned The
        `max_analyzed_offset` query setting does not override the
        `index.highlight.max_analyzed_offset` setting, which prevails when
        it’s set to lower value than the query setting.
    :arg no_match_size: The amount of text you want to return from the
        beginning of the field if there are no matching fragments to
        highlight.
    :arg number_of_fragments: The maximum number of fragments to return.
        If the number of fragments is set to `0`, no fragments are
        returned. Instead, the entire field contents are highlighted and
        returned. This can be handy when you need to highlight short texts
        such as a title or address, but fragmentation is not required. If
        `number_of_fragments` is `0`, `fragment_size` is ignored.
    :arg options:
    :arg order: Sorts highlighted fragments by score when set to `score`.
        By default, fragments will be output in the order they appear in
        the field (order: `none`). Setting this option to `score` will
        output the most relevant fragments first. Each highlighter applies
        its own logic to compute relevancy scores.
    :arg phrase_limit: Controls the number of matching phrases in a
        document that are considered. Prevents the `fvh` highlighter from
        analyzing too many phrases and consuming too much memory. When
        using `matched_fields`, `phrase_limit` phrases per matched field
        are considered. Raising the limit increases query time and
        consumes more memory. Only supported by the `fvh` highlighter.
    :arg post_tags: Use in conjunction with `pre_tags` to define the HTML
        tags to use for the highlighted text. By default, highlighted text
        is wrapped in `<em>` and `</em>` tags.
    :arg pre_tags: Use in conjunction with `post_tags` to define the HTML
        tags to use for the highlighted text. By default, highlighted text
        is wrapped in `<em>` and `</em>` tags.
    :arg require_field_match: By default, only fields that contains a
        query match are highlighted. Set to `false` to highlight all
        fields.
    :arg tags_schema: Set to `styled` to use the built-in tag schema.
    """

    fields: Union[
        Mapping[Union[str, "InstrumentedField"], "types.HighlightField"],
        Dict[str, Any],
        "DefaultType",
    ]
    encoder: Union[Literal["default", "html"], "DefaultType"]
    type: Union[Literal["plain", "fvh", "unified"], "DefaultType"]
    boundary_chars: Union[str, "DefaultType"]
    boundary_max_scan: Union[int, "DefaultType"]
    boundary_scanner: Union[Literal["chars", "sentence", "word"], "DefaultType"]
    boundary_scanner_locale: Union[str, "DefaultType"]
    force_source: Union[bool, "DefaultType"]
    fragmenter: Union[Literal["simple", "span"], "DefaultType"]
    fragment_size: Union[int, "DefaultType"]
    highlight_filter: Union[bool, "DefaultType"]
    highlight_query: Union[Query, "DefaultType"]
    max_fragment_length: Union[int, "DefaultType"]
    max_analyzed_offset: Union[int, "DefaultType"]
    no_match_size: Union[int, "DefaultType"]
    number_of_fragments: Union[int, "DefaultType"]
    options: Union[Mapping[str, Any], "DefaultType"]
    order: Union[Literal["score"], "DefaultType"]
    phrase_limit: Union[int, "DefaultType"]
    post_tags: Union[Sequence[str], "DefaultType"]
    pre_tags: Union[Sequence[str], "DefaultType"]
    require_field_match: Union[bool, "DefaultType"]
    tags_schema: Union[Literal["styled"], "DefaultType"]

    def __init__(
        self,
        *,
        fields: Union[
            Mapping[Union[str, "InstrumentedField"], "types.HighlightField"],
            Dict[str, Any],
            "DefaultType",
        ] = DEFAULT,
        encoder: Union[Literal["default", "html"], "DefaultType"] = DEFAULT,
        type: Union[Literal["plain", "fvh", "unified"], "DefaultType"] = DEFAULT,
        boundary_chars: Union[str, "DefaultType"] = DEFAULT,
        boundary_max_scan: Union[int, "DefaultType"] = DEFAULT,
        boundary_scanner: Union[
            Literal["chars", "sentence", "word"], "DefaultType"
        ] = DEFAULT,
        boundary_scanner_locale: Union[str, "DefaultType"] = DEFAULT,
        force_source: Union[bool, "DefaultType"] = DEFAULT,
        fragmenter: Union[Literal["simple", "span"], "DefaultType"] = DEFAULT,
        fragment_size: Union[int, "DefaultType"] = DEFAULT,
        highlight_filter: Union[bool, "DefaultType"] = DEFAULT,
        highlight_query: Union[Query, "DefaultType"] = DEFAULT,
        max_fragment_length: Union[int, "DefaultType"] = DEFAULT,
        max_analyzed_offset: Union[int, "DefaultType"] = DEFAULT,
        no_match_size: Union[int, "DefaultType"] = DEFAULT,
        number_of_fragments: Union[int, "DefaultType"] = DEFAULT,
        options: Union[Mapping[str, Any], "DefaultType"] = DEFAULT,
        order: Union[Literal["score"], "DefaultType"] = DEFAULT,
        phrase_limit: Union[int, "DefaultType"] = DEFAULT,
        post_tags: Union[Sequence[str], "DefaultType"] = DEFAULT,
        pre_tags: Union[Sequence[str], "DefaultType"] = DEFAULT,
        require_field_match: Union[bool, "DefaultType"] = DEFAULT,
        tags_schema: Union[Literal["styled"], "DefaultType"] = DEFAULT,
        **kwargs: Any,
    ):
        if fields is not DEFAULT:
            kwargs["fields"] = str(fields)
        if encoder is not DEFAULT:
            kwargs["encoder"] = encoder
        if type is not DEFAULT:
            kwargs["type"] = type
        if boundary_chars is not DEFAULT:
            kwargs["boundary_chars"] = boundary_chars
        if boundary_max_scan is not DEFAULT:
            kwargs["boundary_max_scan"] = boundary_max_scan
        if boundary_scanner is not DEFAULT:
            kwargs["boundary_scanner"] = boundary_scanner
        if boundary_scanner_locale is not DEFAULT:
            kwargs["boundary_scanner_locale"] = boundary_scanner_locale
        if force_source is not DEFAULT:
            kwargs["force_source"] = force_source
        if fragmenter is not DEFAULT:
            kwargs["fragmenter"] = fragmenter
        if fragment_size is not DEFAULT:
            kwargs["fragment_size"] = fragment_size
        if highlight_filter is not DEFAULT:
            kwargs["highlight_filter"] = highlight_filter
        if highlight_query is not DEFAULT:
            kwargs["highlight_query"] = highlight_query
        if max_fragment_length is not DEFAULT:
            kwargs["max_fragment_length"] = max_fragment_length
        if max_analyzed_offset is not DEFAULT:
            kwargs["max_analyzed_offset"] = max_analyzed_offset
        if no_match_size is not DEFAULT:
            kwargs["no_match_size"] = no_match_size
        if number_of_fragments is not DEFAULT:
            kwargs["number_of_fragments"] = number_of_fragments
        if options is not DEFAULT:
            kwargs["options"] = options
        if order is not DEFAULT:
            kwargs["order"] = order
        if phrase_limit is not DEFAULT:
            kwargs["phrase_limit"] = phrase_limit
        if post_tags is not DEFAULT:
            kwargs["post_tags"] = post_tags
        if pre_tags is not DEFAULT:
            kwargs["pre_tags"] = pre_tags
        if require_field_match is not DEFAULT:
            kwargs["require_field_match"] = require_field_match
        if tags_schema is not DEFAULT:
            kwargs["tags_schema"] = tags_schema
        super().__init__(**kwargs)


class ScriptField(AttrDict[Any]):
    """
    :arg script: (required)
    :arg ignore_failure:
    """

    script: Union["types.Script", Dict[str, Any], "DefaultType"]
    ignore_failure: Union[bool, "DefaultType"]

    def __init__(
        self,
        *,
        script: Union["types.Script", Dict[str, Any], "DefaultType"] = DEFAULT,
        ignore_failure: Union[bool, "DefaultType"] = DEFAULT,
        **kwargs: Any,
    ):
        if script is not DEFAULT:
            kwargs["script"] = script
        if ignore_failure is not DEFAULT:
            kwargs["ignore_failure"] = ignore_failure
        super().__init__(kwargs)


class SortOptions(AttrDict[Any]):
    """
    :arg _score:
    :arg _doc:
    :arg _geo_distance:
    :arg _script:
    """

    _score: Union["types.ScoreSort", Dict[str, Any], "DefaultType"]
    _doc: Union["types.ScoreSort", Dict[str, Any], "DefaultType"]
    _geo_distance: Union["types.GeoDistanceSort", Dict[str, Any], "DefaultType"]
    _script: Union["types.ScriptSort", Dict[str, Any], "DefaultType"]

    def __init__(
        self,
        *,
        _score: Union["types.ScoreSort", Dict[str, Any], "DefaultType"] = DEFAULT,
        _doc: Union["types.ScoreSort", Dict[str, Any], "DefaultType"] = DEFAULT,
        _geo_distance: Union[
            "types.GeoDistanceSort", Dict[str, Any], "DefaultType"
        ] = DEFAULT,
        _script: Union["types.ScriptSort", Dict[str, Any], "DefaultType"] = DEFAULT,
        **kwargs: Any,
    ):
        if _score is not DEFAULT:
            kwargs["_score"] = _score
        if _doc is not DEFAULT:
            kwargs["_doc"] = _doc
        if _geo_distance is not DEFAULT:
            kwargs["_geo_distance"] = _geo_distance
        if _script is not DEFAULT:
            kwargs["_script"] = _script
        super().__init__(kwargs)


class SourceFilter(AttrDict[Any]):
    """
    :arg excludes:
    :arg includes:
    """

    excludes: Union[
        Union[str, "InstrumentedField"],
        Sequence[Union[str, "InstrumentedField"]],
        "DefaultType",
    ]
    includes: Union[
        Union[str, "InstrumentedField"],
        Sequence[Union[str, "InstrumentedField"]],
        "DefaultType",
    ]

    def __init__(
        self,
        *,
        excludes: Union[
            Union[str, "InstrumentedField"],
            Sequence[Union[str, "InstrumentedField"]],
            "DefaultType",
        ] = DEFAULT,
        includes: Union[
            Union[str, "InstrumentedField"],
            Sequence[Union[str, "InstrumentedField"]],
            "DefaultType",
        ] = DEFAULT,
        **kwargs: Any,
    ):
        if excludes is not DEFAULT:
            kwargs["excludes"] = str(excludes)
        if includes is not DEFAULT:
            kwargs["includes"] = str(includes)
        super().__init__(kwargs)


class IntervalsAllOf(AttrDict[Any]):
    """
    :arg intervals: (required) An array of rules to combine. All rules
        must produce a match in a document for the overall source to
        match.
    :arg max_gaps: Maximum number of positions between the matching terms.
        Intervals produced by the rules further apart than this are not
        considered matches.
    :arg ordered: If `true`, intervals produced by the rules should appear
        in the order in which they are specified.
    :arg filter: Rule used to filter returned intervals.
    """

    intervals: Union[
        Sequence["types.IntervalsContainer"], Dict[str, Any], "DefaultType"
    ]
    max_gaps: Union[int, "DefaultType"]
    ordered: Union[bool, "DefaultType"]
    filter: Union["types.IntervalsFilter", Dict[str, Any], "DefaultType"]

    def __init__(
        self,
        *,
        intervals: Union[
            Sequence["types.IntervalsContainer"], Dict[str, Any], "DefaultType"
        ] = DEFAULT,
        max_gaps: Union[int, "DefaultType"] = DEFAULT,
        ordered: Union[bool, "DefaultType"] = DEFAULT,
        filter: Union["types.IntervalsFilter", Dict[str, Any], "DefaultType"] = DEFAULT,
        **kwargs: Any,
    ):
        if intervals is not DEFAULT:
            kwargs["intervals"] = intervals
        if max_gaps is not DEFAULT:
            kwargs["max_gaps"] = max_gaps
        if ordered is not DEFAULT:
            kwargs["ordered"] = ordered
        if filter is not DEFAULT:
            kwargs["filter"] = filter
        super().__init__(kwargs)


class IntervalsAnyOf(AttrDict[Any]):
    """
    :arg intervals: (required) An array of rules to match.
    :arg filter: Rule used to filter returned intervals.
    """

    intervals: Union[
        Sequence["types.IntervalsContainer"], Dict[str, Any], "DefaultType"
    ]
    filter: Union["types.IntervalsFilter", Dict[str, Any], "DefaultType"]

    def __init__(
        self,
        *,
        intervals: Union[
            Sequence["types.IntervalsContainer"], Dict[str, Any], "DefaultType"
        ] = DEFAULT,
        filter: Union["types.IntervalsFilter", Dict[str, Any], "DefaultType"] = DEFAULT,
        **kwargs: Any,
    ):
        if intervals is not DEFAULT:
            kwargs["intervals"] = intervals
        if filter is not DEFAULT:
            kwargs["filter"] = filter
        super().__init__(kwargs)


class IntervalsFuzzy(AttrDict[Any]):
    """
    :arg term: (required) The term to match.
    :arg analyzer: Analyzer used to normalize the term.
    :arg fuzziness: Maximum edit distance allowed for matching.
    :arg prefix_length: Number of beginning characters left unchanged when
        creating expansions.
    :arg transpositions: Indicates whether edits include transpositions of
        two adjacent characters (for example, `ab` to `ba`).
    :arg use_field: If specified, match intervals from this field rather
        than the top-level field. The `term` is normalized using the
        search analyzer from this field, unless `analyzer` is specified
        separately.
    """

    term: Union[str, "DefaultType"]
    analyzer: Union[str, "DefaultType"]
    fuzziness: Union[str, int, "DefaultType"]
    prefix_length: Union[int, "DefaultType"]
    transpositions: Union[bool, "DefaultType"]
    use_field: Union[str, "InstrumentedField", "DefaultType"]

    def __init__(
        self,
        *,
        term: Union[str, "DefaultType"] = DEFAULT,
        analyzer: Union[str, "DefaultType"] = DEFAULT,
        fuzziness: Union[str, int, "DefaultType"] = DEFAULT,
        prefix_length: Union[int, "DefaultType"] = DEFAULT,
        transpositions: Union[bool, "DefaultType"] = DEFAULT,
        use_field: Union[str, "InstrumentedField", "DefaultType"] = DEFAULT,
        **kwargs: Any,
    ):
        if term is not DEFAULT:
            kwargs["term"] = term
        if analyzer is not DEFAULT:
            kwargs["analyzer"] = analyzer
        if fuzziness is not DEFAULT:
            kwargs["fuzziness"] = fuzziness
        if prefix_length is not DEFAULT:
            kwargs["prefix_length"] = prefix_length
        if transpositions is not DEFAULT:
            kwargs["transpositions"] = transpositions
        if use_field is not DEFAULT:
            kwargs["use_field"] = str(use_field)
        super().__init__(kwargs)


class IntervalsMatch(AttrDict[Any]):
    """
    :arg query: (required) Text you wish to find in the provided field.
    :arg analyzer: Analyzer used to analyze terms in the query.
    :arg max_gaps: Maximum number of positions between the matching terms.
        Terms further apart than this are not considered matches.
    :arg ordered: If `true`, matching terms must appear in their specified
        order.
    :arg use_field: If specified, match intervals from this field rather
        than the top-level field. The `term` is normalized using the
        search analyzer from this field, unless `analyzer` is specified
        separately.
    :arg filter: An optional interval filter.
    """

    query: Union[str, "DefaultType"]
    analyzer: Union[str, "DefaultType"]
    max_gaps: Union[int, "DefaultType"]
    ordered: Union[bool, "DefaultType"]
    use_field: Union[str, "InstrumentedField", "DefaultType"]
    filter: Union["types.IntervalsFilter", Dict[str, Any], "DefaultType"]

    def __init__(
        self,
        *,
        query: Union[str, "DefaultType"] = DEFAULT,
        analyzer: Union[str, "DefaultType"] = DEFAULT,
        max_gaps: Union[int, "DefaultType"] = DEFAULT,
        ordered: Union[bool, "DefaultType"] = DEFAULT,
        use_field: Union[str, "InstrumentedField", "DefaultType"] = DEFAULT,
        filter: Union["types.IntervalsFilter", Dict[str, Any], "DefaultType"] = DEFAULT,
        **kwargs: Any,
    ):
        if query is not DEFAULT:
            kwargs["query"] = query
        if analyzer is not DEFAULT:
            kwargs["analyzer"] = analyzer
        if max_gaps is not DEFAULT:
            kwargs["max_gaps"] = max_gaps
        if ordered is not DEFAULT:
            kwargs["ordered"] = ordered
        if use_field is not DEFAULT:
            kwargs["use_field"] = str(use_field)
        if filter is not DEFAULT:
            kwargs["filter"] = filter
        super().__init__(kwargs)


class IntervalsPrefix(AttrDict[Any]):
    """
    :arg prefix: (required) Beginning characters of terms you wish to find
        in the top-level field.
    :arg analyzer: Analyzer used to analyze the `prefix`.
    :arg use_field: If specified, match intervals from this field rather
        than the top-level field. The `prefix` is normalized using the
        search analyzer from this field, unless `analyzer` is specified
        separately.
    """

    prefix: Union[str, "DefaultType"]
    analyzer: Union[str, "DefaultType"]
    use_field: Union[str, "InstrumentedField", "DefaultType"]

    def __init__(
        self,
        *,
        prefix: Union[str, "DefaultType"] = DEFAULT,
        analyzer: Union[str, "DefaultType"] = DEFAULT,
        use_field: Union[str, "InstrumentedField", "DefaultType"] = DEFAULT,
        **kwargs: Any,
    ):
        if prefix is not DEFAULT:
            kwargs["prefix"] = prefix
        if analyzer is not DEFAULT:
            kwargs["analyzer"] = analyzer
        if use_field is not DEFAULT:
            kwargs["use_field"] = str(use_field)
        super().__init__(kwargs)


class IntervalsWildcard(AttrDict[Any]):
    """
    :arg pattern: (required) Wildcard pattern used to find matching terms.
    :arg analyzer: Analyzer used to analyze the `pattern`. Defaults to the
        top-level field's analyzer.
    :arg use_field: If specified, match intervals from this field rather
        than the top-level field. The `pattern` is normalized using the
        search analyzer from this field, unless `analyzer` is specified
        separately.
    """

    pattern: Union[str, "DefaultType"]
    analyzer: Union[str, "DefaultType"]
    use_field: Union[str, "InstrumentedField", "DefaultType"]

    def __init__(
        self,
        *,
        pattern: Union[str, "DefaultType"] = DEFAULT,
        analyzer: Union[str, "DefaultType"] = DEFAULT,
        use_field: Union[str, "InstrumentedField", "DefaultType"] = DEFAULT,
        **kwargs: Any,
    ):
        if pattern is not DEFAULT:
            kwargs["pattern"] = pattern
        if analyzer is not DEFAULT:
            kwargs["analyzer"] = analyzer
        if use_field is not DEFAULT:
            kwargs["use_field"] = str(use_field)
        super().__init__(kwargs)


class TextEmbedding(AttrDict[Any]):
    """
    :arg model_id: (required)
    :arg model_text: (required)
    """

    model_id: Union[str, "DefaultType"]
    model_text: Union[str, "DefaultType"]

    def __init__(
        self,
        *,
        model_id: Union[str, "DefaultType"] = DEFAULT,
        model_text: Union[str, "DefaultType"] = DEFAULT,
        **kwargs: Any,
    ):
        if model_id is not DEFAULT:
            kwargs["model_id"] = model_id
        if model_text is not DEFAULT:
            kwargs["model_text"] = model_text
        super().__init__(kwargs)


class SpanContainingQuery(QueryBase):
    """
    :arg big: (required) Can be any span query. Matching spans from `big`
        that contain matches from `little` are returned.
    :arg little: (required) Can be any span query. Matching spans from
        `big` that contain matches from `little` are returned.
    :arg boost: Floating point number used to decrease or increase the
        relevance scores of the query. Boost values are relative to the
        default value of 1.0. A boost value between 0 and 1.0 decreases
        the relevance score. A value greater than 1.0 increases the
        relevance score.
    :arg _name:
    """

    big: Union["types.SpanQuery", Dict[str, Any], "DefaultType"]
    little: Union["types.SpanQuery", Dict[str, Any], "DefaultType"]
    boost: Union[float, "DefaultType"]
    _name: Union[str, "DefaultType"]

    def __init__(
        self,
        *,
        big: Union["types.SpanQuery", Dict[str, Any], "DefaultType"] = DEFAULT,
        little: Union["types.SpanQuery", Dict[str, Any], "DefaultType"] = DEFAULT,
        boost: Union[float, "DefaultType"] = DEFAULT,
        _name: Union[str, "DefaultType"] = DEFAULT,
        **kwargs: Any,
    ):
        if big is not DEFAULT:
            kwargs["big"] = big
        if little is not DEFAULT:
            kwargs["little"] = little
        if boost is not DEFAULT:
            kwargs["boost"] = boost
        if _name is not DEFAULT:
            kwargs["_name"] = _name
        super().__init__(**kwargs)


class SpanFieldMaskingQuery(QueryBase):
    """
    :arg field: (required)
    :arg query: (required)
    :arg boost: Floating point number used to decrease or increase the
        relevance scores of the query. Boost values are relative to the
        default value of 1.0. A boost value between 0 and 1.0 decreases
        the relevance score. A value greater than 1.0 increases the
        relevance score.
    :arg _name:
    """

    field: Union[str, "InstrumentedField", "DefaultType"]
    query: Union["types.SpanQuery", Dict[str, Any], "DefaultType"]
    boost: Union[float, "DefaultType"]
    _name: Union[str, "DefaultType"]

    def __init__(
        self,
        *,
        field: Union[str, "InstrumentedField", "DefaultType"] = DEFAULT,
        query: Union["types.SpanQuery", Dict[str, Any], "DefaultType"] = DEFAULT,
        boost: Union[float, "DefaultType"] = DEFAULT,
        _name: Union[str, "DefaultType"] = DEFAULT,
        **kwargs: Any,
    ):
        if field is not DEFAULT:
            kwargs["field"] = str(field)
        if query is not DEFAULT:
            kwargs["query"] = query
        if boost is not DEFAULT:
            kwargs["boost"] = boost
        if _name is not DEFAULT:
            kwargs["_name"] = _name
        super().__init__(**kwargs)


class SpanFirstQuery(QueryBase):
    """
    :arg end: (required) Controls the maximum end position permitted in a
        match.
    :arg match: (required) Can be any other span type query.
    :arg boost: Floating point number used to decrease or increase the
        relevance scores of the query. Boost values are relative to the
        default value of 1.0. A boost value between 0 and 1.0 decreases
        the relevance score. A value greater than 1.0 increases the
        relevance score.
    :arg _name:
    """

    end: Union[int, "DefaultType"]
    match: Union["types.SpanQuery", Dict[str, Any], "DefaultType"]
    boost: Union[float, "DefaultType"]
    _name: Union[str, "DefaultType"]

    def __init__(
        self,
        *,
        end: Union[int, "DefaultType"] = DEFAULT,
        match: Union["types.SpanQuery", Dict[str, Any], "DefaultType"] = DEFAULT,
        boost: Union[float, "DefaultType"] = DEFAULT,
        _name: Union[str, "DefaultType"] = DEFAULT,
        **kwargs: Any,
    ):
        if end is not DEFAULT:
            kwargs["end"] = end
        if match is not DEFAULT:
            kwargs["match"] = match
        if boost is not DEFAULT:
            kwargs["boost"] = boost
        if _name is not DEFAULT:
            kwargs["_name"] = _name
        super().__init__(**kwargs)


class SpanMultiTermQuery(QueryBase):
    """
    :arg match: (required) Should be a multi term query (one of
        `wildcard`, `fuzzy`, `prefix`, `range`, or `regexp` query).
    :arg boost: Floating point number used to decrease or increase the
        relevance scores of the query. Boost values are relative to the
        default value of 1.0. A boost value between 0 and 1.0 decreases
        the relevance score. A value greater than 1.0 increases the
        relevance score.
    :arg _name:
    """

    match: Union[Query, "DefaultType"]
    boost: Union[float, "DefaultType"]
    _name: Union[str, "DefaultType"]

    def __init__(
        self,
        *,
        match: Union[Query, "DefaultType"] = DEFAULT,
        boost: Union[float, "DefaultType"] = DEFAULT,
        _name: Union[str, "DefaultType"] = DEFAULT,
        **kwargs: Any,
    ):
        if match is not DEFAULT:
            kwargs["match"] = match
        if boost is not DEFAULT:
            kwargs["boost"] = boost
        if _name is not DEFAULT:
            kwargs["_name"] = _name
        super().__init__(**kwargs)


class SpanNearQuery(QueryBase):
    """
    :arg clauses: (required) Array of one or more other span type queries.
    :arg in_order: Controls whether matches are required to be in-order.
    :arg slop: Controls the maximum number of intervening unmatched
        positions permitted.
    :arg boost: Floating point number used to decrease or increase the
        relevance scores of the query. Boost values are relative to the
        default value of 1.0. A boost value between 0 and 1.0 decreases
        the relevance score. A value greater than 1.0 increases the
        relevance score.
    :arg _name:
    """

    clauses: Union[Sequence["types.SpanQuery"], Dict[str, Any], "DefaultType"]
    in_order: Union[bool, "DefaultType"]
    slop: Union[int, "DefaultType"]
    boost: Union[float, "DefaultType"]
    _name: Union[str, "DefaultType"]

    def __init__(
        self,
        *,
        clauses: Union[
            Sequence["types.SpanQuery"], Dict[str, Any], "DefaultType"
        ] = DEFAULT,
        in_order: Union[bool, "DefaultType"] = DEFAULT,
        slop: Union[int, "DefaultType"] = DEFAULT,
        boost: Union[float, "DefaultType"] = DEFAULT,
        _name: Union[str, "DefaultType"] = DEFAULT,
        **kwargs: Any,
    ):
        if clauses is not DEFAULT:
            kwargs["clauses"] = clauses
        if in_order is not DEFAULT:
            kwargs["in_order"] = in_order
        if slop is not DEFAULT:
            kwargs["slop"] = slop
        if boost is not DEFAULT:
            kwargs["boost"] = boost
        if _name is not DEFAULT:
            kwargs["_name"] = _name
        super().__init__(**kwargs)


class SpanNotQuery(QueryBase):
    """
    :arg exclude: (required) Span query whose matches must not overlap
        those returned.
    :arg include: (required) Span query whose matches are filtered.
    :arg dist: The number of tokens from within the include span that
        can’t have overlap with the exclude span. Equivalent to setting
        both `pre` and `post`.
    :arg post: The number of tokens after the include span that can’t have
        overlap with the exclude span.
    :arg pre: The number of tokens before the include span that can’t have
        overlap with the exclude span.
    :arg boost: Floating point number used to decrease or increase the
        relevance scores of the query. Boost values are relative to the
        default value of 1.0. A boost value between 0 and 1.0 decreases
        the relevance score. A value greater than 1.0 increases the
        relevance score.
    :arg _name:
    """

    exclude: Union["types.SpanQuery", Dict[str, Any], "DefaultType"]
    include: Union["types.SpanQuery", Dict[str, Any], "DefaultType"]
    dist: Union[int, "DefaultType"]
    post: Union[int, "DefaultType"]
    pre: Union[int, "DefaultType"]
    boost: Union[float, "DefaultType"]
    _name: Union[str, "DefaultType"]

    def __init__(
        self,
        *,
        exclude: Union["types.SpanQuery", Dict[str, Any], "DefaultType"] = DEFAULT,
        include: Union["types.SpanQuery", Dict[str, Any], "DefaultType"] = DEFAULT,
        dist: Union[int, "DefaultType"] = DEFAULT,
        post: Union[int, "DefaultType"] = DEFAULT,
        pre: Union[int, "DefaultType"] = DEFAULT,
        boost: Union[float, "DefaultType"] = DEFAULT,
        _name: Union[str, "DefaultType"] = DEFAULT,
        **kwargs: Any,
    ):
        if exclude is not DEFAULT:
            kwargs["exclude"] = exclude
        if include is not DEFAULT:
            kwargs["include"] = include
        if dist is not DEFAULT:
            kwargs["dist"] = dist
        if post is not DEFAULT:
            kwargs["post"] = post
        if pre is not DEFAULT:
            kwargs["pre"] = pre
        if boost is not DEFAULT:
            kwargs["boost"] = boost
        if _name is not DEFAULT:
            kwargs["_name"] = _name
        super().__init__(**kwargs)


class SpanOrQuery(QueryBase):
    """
    :arg clauses: (required) Array of one or more other span type queries.
    :arg boost: Floating point number used to decrease or increase the
        relevance scores of the query. Boost values are relative to the
        default value of 1.0. A boost value between 0 and 1.0 decreases
        the relevance score. A value greater than 1.0 increases the
        relevance score.
    :arg _name:
    """

    clauses: Union[Sequence["types.SpanQuery"], Dict[str, Any], "DefaultType"]
    boost: Union[float, "DefaultType"]
    _name: Union[str, "DefaultType"]

    def __init__(
        self,
        *,
        clauses: Union[
            Sequence["types.SpanQuery"], Dict[str, Any], "DefaultType"
        ] = DEFAULT,
        boost: Union[float, "DefaultType"] = DEFAULT,
        _name: Union[str, "DefaultType"] = DEFAULT,
        **kwargs: Any,
    ):
        if clauses is not DEFAULT:
            kwargs["clauses"] = clauses
        if boost is not DEFAULT:
            kwargs["boost"] = boost
        if _name is not DEFAULT:
            kwargs["_name"] = _name
        super().__init__(**kwargs)


class SpanWithinQuery(QueryBase):
    """
    :arg big: (required) Can be any span query. Matching spans from
        `little` that are enclosed within `big` are returned.
    :arg little: (required) Can be any span query. Matching spans from
        `little` that are enclosed within `big` are returned.
    :arg boost: Floating point number used to decrease or increase the
        relevance scores of the query. Boost values are relative to the
        default value of 1.0. A boost value between 0 and 1.0 decreases
        the relevance score. A value greater than 1.0 increases the
        relevance score.
    :arg _name:
    """

    big: Union["types.SpanQuery", Dict[str, Any], "DefaultType"]
    little: Union["types.SpanQuery", Dict[str, Any], "DefaultType"]
    boost: Union[float, "DefaultType"]
    _name: Union[str, "DefaultType"]

    def __init__(
        self,
        *,
        big: Union["types.SpanQuery", Dict[str, Any], "DefaultType"] = DEFAULT,
        little: Union["types.SpanQuery", Dict[str, Any], "DefaultType"] = DEFAULT,
        boost: Union[float, "DefaultType"] = DEFAULT,
        _name: Union[str, "DefaultType"] = DEFAULT,
        **kwargs: Any,
    ):
        if big is not DEFAULT:
            kwargs["big"] = big
        if little is not DEFAULT:
            kwargs["little"] = little
        if boost is not DEFAULT:
            kwargs["boost"] = boost
        if _name is not DEFAULT:
            kwargs["_name"] = _name
        super().__init__(**kwargs)


class HighlightField(HighlightBase):
    """
    :arg fragment_offset:
    :arg matched_fields:
    :arg analyzer:
    :arg type:
    :arg boundary_chars: A string that contains each boundary character.
    :arg boundary_max_scan: How far to scan for boundary characters.
    :arg boundary_scanner: Specifies how to break the highlighted
        fragments: chars, sentence, or word. Only valid for the unified
        and fvh highlighters. Defaults to `sentence` for the `unified`
        highlighter. Defaults to `chars` for the `fvh` highlighter.
    :arg boundary_scanner_locale: Controls which locale is used to search
        for sentence and word boundaries. This parameter takes a form of a
        language tag, for example: `"en-US"`, `"fr-FR"`, `"ja-JP"`.
    :arg force_source:
    :arg fragmenter: Specifies how text should be broken up in highlight
        snippets: `simple` or `span`. Only valid for the `plain`
        highlighter.
    :arg fragment_size: The size of the highlighted fragment in
        characters.
    :arg highlight_filter:
    :arg highlight_query: Highlight matches for a query other than the
        search query. This is especially useful if you use a rescore query
        because those are not taken into account by highlighting by
        default.
    :arg max_fragment_length:
    :arg max_analyzed_offset: If set to a non-negative value, highlighting
        stops at this defined maximum limit. The rest of the text is not
        processed, thus not highlighted and no error is returned The
        `max_analyzed_offset` query setting does not override the
        `index.highlight.max_analyzed_offset` setting, which prevails when
        it’s set to lower value than the query setting.
    :arg no_match_size: The amount of text you want to return from the
        beginning of the field if there are no matching fragments to
        highlight.
    :arg number_of_fragments: The maximum number of fragments to return.
        If the number of fragments is set to `0`, no fragments are
        returned. Instead, the entire field contents are highlighted and
        returned. This can be handy when you need to highlight short texts
        such as a title or address, but fragmentation is not required. If
        `number_of_fragments` is `0`, `fragment_size` is ignored.
    :arg options:
    :arg order: Sorts highlighted fragments by score when set to `score`.
        By default, fragments will be output in the order they appear in
        the field (order: `none`). Setting this option to `score` will
        output the most relevant fragments first. Each highlighter applies
        its own logic to compute relevancy scores.
    :arg phrase_limit: Controls the number of matching phrases in a
        document that are considered. Prevents the `fvh` highlighter from
        analyzing too many phrases and consuming too much memory. When
        using `matched_fields`, `phrase_limit` phrases per matched field
        are considered. Raising the limit increases query time and
        consumes more memory. Only supported by the `fvh` highlighter.
    :arg post_tags: Use in conjunction with `pre_tags` to define the HTML
        tags to use for the highlighted text. By default, highlighted text
        is wrapped in `<em>` and `</em>` tags.
    :arg pre_tags: Use in conjunction with `post_tags` to define the HTML
        tags to use for the highlighted text. By default, highlighted text
        is wrapped in `<em>` and `</em>` tags.
    :arg require_field_match: By default, only fields that contains a
        query match are highlighted. Set to `false` to highlight all
        fields.
    :arg tags_schema: Set to `styled` to use the built-in tag schema.
    """

    fragment_offset: Union[int, "DefaultType"]
    matched_fields: Union[
        Union[str, "InstrumentedField"],
        Sequence[Union[str, "InstrumentedField"]],
        "DefaultType",
    ]
    analyzer: Union[str, Dict[str, Any], "DefaultType"]
    type: Union[Literal["plain", "fvh", "unified"], "DefaultType"]
    boundary_chars: Union[str, "DefaultType"]
    boundary_max_scan: Union[int, "DefaultType"]
    boundary_scanner: Union[Literal["chars", "sentence", "word"], "DefaultType"]
    boundary_scanner_locale: Union[str, "DefaultType"]
    force_source: Union[bool, "DefaultType"]
    fragmenter: Union[Literal["simple", "span"], "DefaultType"]
    fragment_size: Union[int, "DefaultType"]
    highlight_filter: Union[bool, "DefaultType"]
    highlight_query: Union[Query, "DefaultType"]
    max_fragment_length: Union[int, "DefaultType"]
    max_analyzed_offset: Union[int, "DefaultType"]
    no_match_size: Union[int, "DefaultType"]
    number_of_fragments: Union[int, "DefaultType"]
    options: Union[Mapping[str, Any], "DefaultType"]
    order: Union[Literal["score"], "DefaultType"]
    phrase_limit: Union[int, "DefaultType"]
    post_tags: Union[Sequence[str], "DefaultType"]
    pre_tags: Union[Sequence[str], "DefaultType"]
    require_field_match: Union[bool, "DefaultType"]
    tags_schema: Union[Literal["styled"], "DefaultType"]

    def __init__(
        self,
        *,
        fragment_offset: Union[int, "DefaultType"] = DEFAULT,
        matched_fields: Union[
            Union[str, "InstrumentedField"],
            Sequence[Union[str, "InstrumentedField"]],
            "DefaultType",
        ] = DEFAULT,
        analyzer: Union[str, Dict[str, Any], "DefaultType"] = DEFAULT,
        type: Union[Literal["plain", "fvh", "unified"], "DefaultType"] = DEFAULT,
        boundary_chars: Union[str, "DefaultType"] = DEFAULT,
        boundary_max_scan: Union[int, "DefaultType"] = DEFAULT,
        boundary_scanner: Union[
            Literal["chars", "sentence", "word"], "DefaultType"
        ] = DEFAULT,
        boundary_scanner_locale: Union[str, "DefaultType"] = DEFAULT,
        force_source: Union[bool, "DefaultType"] = DEFAULT,
        fragmenter: Union[Literal["simple", "span"], "DefaultType"] = DEFAULT,
        fragment_size: Union[int, "DefaultType"] = DEFAULT,
        highlight_filter: Union[bool, "DefaultType"] = DEFAULT,
        highlight_query: Union[Query, "DefaultType"] = DEFAULT,
        max_fragment_length: Union[int, "DefaultType"] = DEFAULT,
        max_analyzed_offset: Union[int, "DefaultType"] = DEFAULT,
        no_match_size: Union[int, "DefaultType"] = DEFAULT,
        number_of_fragments: Union[int, "DefaultType"] = DEFAULT,
        options: Union[Mapping[str, Any], "DefaultType"] = DEFAULT,
        order: Union[Literal["score"], "DefaultType"] = DEFAULT,
        phrase_limit: Union[int, "DefaultType"] = DEFAULT,
        post_tags: Union[Sequence[str], "DefaultType"] = DEFAULT,
        pre_tags: Union[Sequence[str], "DefaultType"] = DEFAULT,
        require_field_match: Union[bool, "DefaultType"] = DEFAULT,
        tags_schema: Union[Literal["styled"], "DefaultType"] = DEFAULT,
        **kwargs: Any,
    ):
        if fragment_offset is not DEFAULT:
            kwargs["fragment_offset"] = fragment_offset
        if matched_fields is not DEFAULT:
            kwargs["matched_fields"] = str(matched_fields)
        if analyzer is not DEFAULT:
            kwargs["analyzer"] = analyzer
        if type is not DEFAULT:
            kwargs["type"] = type
        if boundary_chars is not DEFAULT:
            kwargs["boundary_chars"] = boundary_chars
        if boundary_max_scan is not DEFAULT:
            kwargs["boundary_max_scan"] = boundary_max_scan
        if boundary_scanner is not DEFAULT:
            kwargs["boundary_scanner"] = boundary_scanner
        if boundary_scanner_locale is not DEFAULT:
            kwargs["boundary_scanner_locale"] = boundary_scanner_locale
        if force_source is not DEFAULT:
            kwargs["force_source"] = force_source
        if fragmenter is not DEFAULT:
            kwargs["fragmenter"] = fragmenter
        if fragment_size is not DEFAULT:
            kwargs["fragment_size"] = fragment_size
        if highlight_filter is not DEFAULT:
            kwargs["highlight_filter"] = highlight_filter
        if highlight_query is not DEFAULT:
            kwargs["highlight_query"] = highlight_query
        if max_fragment_length is not DEFAULT:
            kwargs["max_fragment_length"] = max_fragment_length
        if max_analyzed_offset is not DEFAULT:
            kwargs["max_analyzed_offset"] = max_analyzed_offset
        if no_match_size is not DEFAULT:
            kwargs["no_match_size"] = no_match_size
        if number_of_fragments is not DEFAULT:
            kwargs["number_of_fragments"] = number_of_fragments
        if options is not DEFAULT:
            kwargs["options"] = options
        if order is not DEFAULT:
            kwargs["order"] = order
        if phrase_limit is not DEFAULT:
            kwargs["phrase_limit"] = phrase_limit
        if post_tags is not DEFAULT:
            kwargs["post_tags"] = post_tags
        if pre_tags is not DEFAULT:
            kwargs["pre_tags"] = pre_tags
        if require_field_match is not DEFAULT:
            kwargs["require_field_match"] = require_field_match
        if tags_schema is not DEFAULT:
            kwargs["tags_schema"] = tags_schema
        super().__init__(**kwargs)


class ScoreSort(AttrDict[Any]):
    """
    :arg order:
    """

    order: Union[Literal["asc", "desc"], "DefaultType"]

    def __init__(
        self,
        *,
        order: Union[Literal["asc", "desc"], "DefaultType"] = DEFAULT,
        **kwargs: Any,
    ):
        if order is not DEFAULT:
            kwargs["order"] = order
        super().__init__(kwargs)


class GeoDistanceSort(AttrDict[Any]):
    """
    :arg mode:
    :arg distance_type:
    :arg ignore_unmapped:
    :arg order:
    :arg unit:
    :arg nested:
    """

    mode: Union[Literal["min", "max", "sum", "avg", "median"], "DefaultType"]
    distance_type: Union[Literal["arc", "plane"], "DefaultType"]
    ignore_unmapped: Union[bool, "DefaultType"]
    order: Union[Literal["asc", "desc"], "DefaultType"]
    unit: Union[
        Literal["in", "ft", "yd", "mi", "nmi", "km", "m", "cm", "mm"], "DefaultType"
    ]
    nested: Union["types.NestedSortValue", Dict[str, Any], "DefaultType"]

    def __init__(
        self,
        *,
        mode: Union[
            Literal["min", "max", "sum", "avg", "median"], "DefaultType"
        ] = DEFAULT,
        distance_type: Union[Literal["arc", "plane"], "DefaultType"] = DEFAULT,
        ignore_unmapped: Union[bool, "DefaultType"] = DEFAULT,
        order: Union[Literal["asc", "desc"], "DefaultType"] = DEFAULT,
        unit: Union[
            Literal["in", "ft", "yd", "mi", "nmi", "km", "m", "cm", "mm"], "DefaultType"
        ] = DEFAULT,
        nested: Union["types.NestedSortValue", Dict[str, Any], "DefaultType"] = DEFAULT,
        **kwargs: Any,
    ):
        if mode is not DEFAULT:
            kwargs["mode"] = mode
        if distance_type is not DEFAULT:
            kwargs["distance_type"] = distance_type
        if ignore_unmapped is not DEFAULT:
            kwargs["ignore_unmapped"] = ignore_unmapped
        if order is not DEFAULT:
            kwargs["order"] = order
        if unit is not DEFAULT:
            kwargs["unit"] = unit
        if nested is not DEFAULT:
            kwargs["nested"] = nested
        super().__init__(kwargs)


class ScriptSort(AttrDict[Any]):
    """
    :arg script: (required)
    :arg order:
    :arg type:
    :arg mode:
    :arg nested:
    """

    script: Union["types.Script", Dict[str, Any], "DefaultType"]
    order: Union[Literal["asc", "desc"], "DefaultType"]
    type: Union[Literal["string", "number", "version"], "DefaultType"]
    mode: Union[Literal["min", "max", "sum", "avg", "median"], "DefaultType"]
    nested: Union["types.NestedSortValue", Dict[str, Any], "DefaultType"]

    def __init__(
        self,
        *,
        script: Union["types.Script", Dict[str, Any], "DefaultType"] = DEFAULT,
        order: Union[Literal["asc", "desc"], "DefaultType"] = DEFAULT,
        type: Union[Literal["string", "number", "version"], "DefaultType"] = DEFAULT,
        mode: Union[
            Literal["min", "max", "sum", "avg", "median"], "DefaultType"
        ] = DEFAULT,
        nested: Union["types.NestedSortValue", Dict[str, Any], "DefaultType"] = DEFAULT,
        **kwargs: Any,
    ):
        if script is not DEFAULT:
            kwargs["script"] = script
        if order is not DEFAULT:
            kwargs["order"] = order
        if type is not DEFAULT:
            kwargs["type"] = type
        if mode is not DEFAULT:
            kwargs["mode"] = mode
        if nested is not DEFAULT:
            kwargs["nested"] = nested
        super().__init__(kwargs)


class IntervalsContainer(AttrDict[Any]):
    """
    :arg all_of: Returns matches that span a combination of other rules.
    :arg any_of: Returns intervals produced by any of its sub-rules.
    :arg fuzzy: Matches analyzed text.
    :arg match: Matches analyzed text.
    :arg prefix: Matches terms that start with a specified set of
        characters.
    :arg wildcard: Matches terms using a wildcard pattern.
    """

    all_of: Union["types.IntervalsAllOf", Dict[str, Any], "DefaultType"]
    any_of: Union["types.IntervalsAnyOf", Dict[str, Any], "DefaultType"]
    fuzzy: Union["types.IntervalsFuzzy", Dict[str, Any], "DefaultType"]
    match: Union["types.IntervalsMatch", Dict[str, Any], "DefaultType"]
    prefix: Union["types.IntervalsPrefix", Dict[str, Any], "DefaultType"]
    wildcard: Union["types.IntervalsWildcard", Dict[str, Any], "DefaultType"]

    def __init__(
        self,
        *,
        all_of: Union["types.IntervalsAllOf", Dict[str, Any], "DefaultType"] = DEFAULT,
        any_of: Union["types.IntervalsAnyOf", Dict[str, Any], "DefaultType"] = DEFAULT,
        fuzzy: Union["types.IntervalsFuzzy", Dict[str, Any], "DefaultType"] = DEFAULT,
        match: Union["types.IntervalsMatch", Dict[str, Any], "DefaultType"] = DEFAULT,
        prefix: Union["types.IntervalsPrefix", Dict[str, Any], "DefaultType"] = DEFAULT,
        wildcard: Union[
            "types.IntervalsWildcard", Dict[str, Any], "DefaultType"
        ] = DEFAULT,
        **kwargs: Any,
    ):
        if all_of is not DEFAULT:
            kwargs["all_of"] = all_of
        if any_of is not DEFAULT:
            kwargs["any_of"] = any_of
        if fuzzy is not DEFAULT:
            kwargs["fuzzy"] = fuzzy
        if match is not DEFAULT:
            kwargs["match"] = match
        if prefix is not DEFAULT:
            kwargs["prefix"] = prefix
        if wildcard is not DEFAULT:
            kwargs["wildcard"] = wildcard
        super().__init__(kwargs)


class IntervalsFilter(AttrDict[Any]):
    """
    :arg after: Query used to return intervals that follow an interval
        from the `filter` rule.
    :arg before: Query used to return intervals that occur before an
        interval from the `filter` rule.
    :arg contained_by: Query used to return intervals contained by an
        interval from the `filter` rule.
    :arg containing: Query used to return intervals that contain an
        interval from the `filter` rule.
    :arg not_contained_by: Query used to return intervals that are **not**
        contained by an interval from the `filter` rule.
    :arg not_containing: Query used to return intervals that do **not**
        contain an interval from the `filter` rule.
    :arg not_overlapping: Query used to return intervals that do **not**
        overlap with an interval from the `filter` rule.
    :arg overlapping: Query used to return intervals that overlap with an
        interval from the `filter` rule.
    :arg script: Script used to return matching documents. This script
        must return a boolean value: `true` or `false`.
    """

    after: Union["types.IntervalsContainer", Dict[str, Any], "DefaultType"]
    before: Union["types.IntervalsContainer", Dict[str, Any], "DefaultType"]
    contained_by: Union["types.IntervalsContainer", Dict[str, Any], "DefaultType"]
    containing: Union["types.IntervalsContainer", Dict[str, Any], "DefaultType"]
    not_contained_by: Union["types.IntervalsContainer", Dict[str, Any], "DefaultType"]
    not_containing: Union["types.IntervalsContainer", Dict[str, Any], "DefaultType"]
    not_overlapping: Union["types.IntervalsContainer", Dict[str, Any], "DefaultType"]
    overlapping: Union["types.IntervalsContainer", Dict[str, Any], "DefaultType"]
    script: Union["types.Script", Dict[str, Any], "DefaultType"]

    def __init__(
        self,
        *,
        after: Union[
            "types.IntervalsContainer", Dict[str, Any], "DefaultType"
        ] = DEFAULT,
        before: Union[
            "types.IntervalsContainer", Dict[str, Any], "DefaultType"
        ] = DEFAULT,
        contained_by: Union[
            "types.IntervalsContainer", Dict[str, Any], "DefaultType"
        ] = DEFAULT,
        containing: Union[
            "types.IntervalsContainer", Dict[str, Any], "DefaultType"
        ] = DEFAULT,
        not_contained_by: Union[
            "types.IntervalsContainer", Dict[str, Any], "DefaultType"
        ] = DEFAULT,
        not_containing: Union[
            "types.IntervalsContainer", Dict[str, Any], "DefaultType"
        ] = DEFAULT,
        not_overlapping: Union[
            "types.IntervalsContainer", Dict[str, Any], "DefaultType"
        ] = DEFAULT,
        overlapping: Union[
            "types.IntervalsContainer", Dict[str, Any], "DefaultType"
        ] = DEFAULT,
        script: Union["types.Script", Dict[str, Any], "DefaultType"] = DEFAULT,
        **kwargs: Any,
    ):
        if after is not DEFAULT:
            kwargs["after"] = after
        if before is not DEFAULT:
            kwargs["before"] = before
        if contained_by is not DEFAULT:
            kwargs["contained_by"] = contained_by
        if containing is not DEFAULT:
            kwargs["containing"] = containing
        if not_contained_by is not DEFAULT:
            kwargs["not_contained_by"] = not_contained_by
        if not_containing is not DEFAULT:
            kwargs["not_containing"] = not_containing
        if not_overlapping is not DEFAULT:
            kwargs["not_overlapping"] = not_overlapping
        if overlapping is not DEFAULT:
            kwargs["overlapping"] = overlapping
        if script is not DEFAULT:
            kwargs["script"] = script
        super().__init__(kwargs)


class NestedSortValue(AttrDict[Any]):
    """
    :arg path: (required)
    :arg filter:
    :arg max_children:
    :arg nested:
    """

    path: Union[str, "InstrumentedField", "DefaultType"]
    filter: Union[Query, "DefaultType"]
    max_children: Union[int, "DefaultType"]
    nested: Union["types.NestedSortValue", Dict[str, Any], "DefaultType"]

    def __init__(
        self,
        *,
        path: Union[str, "InstrumentedField", "DefaultType"] = DEFAULT,
        filter: Union[Query, "DefaultType"] = DEFAULT,
        max_children: Union[int, "DefaultType"] = DEFAULT,
        nested: Union["types.NestedSortValue", Dict[str, Any], "DefaultType"] = DEFAULT,
        **kwargs: Any,
    ):
        if path is not DEFAULT:
            kwargs["path"] = str(path)
        if filter is not DEFAULT:
            kwargs["filter"] = filter
        if max_children is not DEFAULT:
            kwargs["max_children"] = max_children
        if nested is not DEFAULT:
            kwargs["nested"] = nested
        super().__init__(kwargs)
