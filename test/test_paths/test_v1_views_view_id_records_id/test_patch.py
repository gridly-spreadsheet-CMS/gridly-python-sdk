# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

import unittest
from unittest.mock import patch

import urllib3

import gridly
from gridly.paths.v1_views_view_id_records_id import patch  # noqa: E501
from gridly import configuration, schemas, api_client

from .. import ApiTestMixin


class TestV1ViewsViewIdRecordsId(ApiTestMixin, unittest.TestCase):
    """
    V1ViewsViewIdRecordsId unit test stubs
        updateRecord  # noqa: E501
    """
    _configuration = configuration.Configuration()

    def setUp(self):
        used_api_client = api_client.ApiClient(configuration=self._configuration)
        self.api = patch.ApiForpatch(api_client=used_api_client)  # noqa: E501

    def tearDown(self):
        pass

    response_status = 200






if __name__ == '__main__':
    unittest.main()
