# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

import unittest
from unittest.mock import patch

import urllib3

import gridly
from gridly.paths.v1_transmems_upload import post  # noqa: E501
from gridly import configuration, schemas, api_client

from .. import ApiTestMixin


class TestV1TransmemsUpload(ApiTestMixin, unittest.TestCase):
    """
    V1TransmemsUpload unit test stubs
        Create a new translation memory by uploading tmx file  # noqa: E501
    """
    _configuration = configuration.Configuration()

    def setUp(self):
        used_api_client = api_client.ApiClient(configuration=self._configuration)
        self.api = post.ApiForpost(api_client=used_api_client)  # noqa: E501

    def tearDown(self):
        pass

    response_status = 201




if __name__ == '__main__':
    unittest.main()
