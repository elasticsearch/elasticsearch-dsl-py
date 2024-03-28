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

import os
import subprocess
import sys
from pathlib import Path

import unasync


def main(check=False):
    source_dirs = [
        "elasticsearch_dsl",
        "tests",
        "tests/test_integration",
        "tests/test_integration/test_examples",
    ]
    output_dir = "_sync" if not check else "_sync_check"

    # Unasync all the generated async code
    additional_replacements = {
        "_async": "_sync",
        "AsyncElasticsearch": "Elasticsearch",
        "AsyncSearch": "Search",
        "AsyncMultiSearch": "MultiSearch",
        "AsyncDocument": "Document",
        "AsyncIndexMeta": "IndexMeta",
        "AsyncIndexTemplate": "IndexTemplate",
        "AsyncIndex": "Index",
        "AsyncUpdateByQuery": "UpdateByQuery",
        "AsyncMapping": "Mapping",
        "AsyncFacetedSearch": "FacetedSearch",
        "async_connections": "connections",
        "async_scan": "scan",
        "async_simulate": "simulate",
        "async_mock_client": "mock_client",
        "async_client": "client",
        "async_data_client": "data_client",
        "async_write_client": "write_client",
        "async_pull_request": "pull_request",
        "async_examples": "examples",
        "assert_awaited_once_with": "assert_called_once_with",
    }
    rules = [
        unasync.Rule(
            fromdir=f"{source_dir}/_async/",
            todir=f"{source_dir}/{output_dir}/",
            additional_replacements=additional_replacements,
        )
        for source_dir in source_dirs
    ]

    filepaths = []
    for root, _, filenames in os.walk(Path(__file__).absolute().parent.parent):
        for filename in filenames:
            if filename.rpartition(".")[-1] in (
                "py",
                "pyi",
            ) and not filename.startswith("utils.py"):
                filepaths.append(os.path.join(root, filename))

    unasync.unasync_files(filepaths, rules)

    if check:
        # make sure there are no differences between _sync and _sync_check
        for source_dir in source_dirs:
            subprocess.check_call(
                ["black", "--target-version=py38", f"{source_dir}/_sync_check/"]
            )
            subprocess.check_call(["isort", f"{source_dir}/_sync_check/"])
            subprocess.check_call(
                [
                    "diff",
                    "-x",
                    "__pycache__",
                    f"{source_dir}/_sync",
                    f"{source_dir}/_sync_check",
                ]
            )
            subprocess.check_call(["rm", "-rf", f"{source_dir}/_sync_check"])


if __name__ == "__main__":
    main(check="--check" in sys.argv)