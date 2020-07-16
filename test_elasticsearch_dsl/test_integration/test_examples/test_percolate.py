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

from .percolate import setup, BlogPost


def test_post_gets_tagged_automatically(write_client):
    setup()

    bp = BlogPost(_id=47, content="nothing about snakes here!")
    bp_py = BlogPost(_id=42, content="something about Python here!")

    bp.save()
    bp_py.save()

    assert [] == bp.tags
    assert {"programming", "development", "python"} == set(bp_py.tags)
