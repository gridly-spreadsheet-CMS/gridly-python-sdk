# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

import unittest
from unittest.mock import patch

import urllib3

import gridly
from gridly.paths.v1_views_view_id_columns_column_id import delete  # noqa: E501
from gridly import configuration, schemas, api_client

from .. import ApiTestMixin


class TestV1ViewsViewIdColumnsColumnId(ApiTestMixin, unittest.TestCase):
    """
    V1ViewsViewIdColumnsColumnId unit test stubs
        delete  # noqa: E501
    """
    _configuration = configuration.Configuration()

    def setUp(self):
        used_api_client = api_client.ApiClient(configuration=self._configuration)
        self.api = delete.ApiFordelete(api_client=used_api_client)  # noqa: E501

    def tearDown(self):
        pass

    response_status = 204
    response_body = ''


if __name__ == '__main__':
    unittest.main()