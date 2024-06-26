# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

import unittest
from unittest.mock import patch

import urllib3

import gridly
from gridly.paths.v1_template_grids import get  # noqa: E501
from gridly import configuration, schemas, api_client

from .. import ApiTestMixin


class TestV1TemplateGrids(ApiTestMixin, unittest.TestCase):
    """
    V1TemplateGrids unit test stubs
        listTemplateGrids  # noqa: E501
    """
    _configuration = configuration.Configuration()

    def setUp(self):
        used_api_client = api_client.ApiClient(configuration=self._configuration)
        self.api = get.ApiForget(api_client=used_api_client)  # noqa: E501

    def tearDown(self):
        pass

    response_status = 200




if __name__ == '__main__':
    unittest.main()
