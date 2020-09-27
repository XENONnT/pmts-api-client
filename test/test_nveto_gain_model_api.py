# coding: utf-8

"""
    XENON PMT API

    API for the XENON PMT database  # noqa: E501

    The version of the OpenAPI document: 1.0
    Contact: joe.mosbacher@gmail.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import xepmts
from xepmts.api.nveto_gain_model_api import NvetoGainModelApi  # noqa: E501
from xepmts.rest import ApiException


class TestNvetoGainModelApi(unittest.TestCase):
    """NvetoGainModelApi unit test stubs"""

    def setUp(self):
        self.api = xepmts.api.nveto_gain_model_api.NvetoGainModelApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_delete_nveto_gain_model_item(self):
        """Test case for delete_nveto_gain_model_item

        Deletes a NvetoGainModel document  # noqa: E501
        """
        pass

    def test_delete_nveto_gain_models(self):
        """Test case for delete_nveto_gain_models

        Deletes all NvetoGainModels  # noqa: E501
        """
        pass

    def test_get_nveto_gain_model_item(self):
        """Test case for get_nveto_gain_model_item

        Retrieves a NvetoGainModel document  # noqa: E501
        """
        pass

    def test_get_nveto_gain_models(self):
        """Test case for get_nveto_gain_models

        Retrieves one or more NvetoGainModels  # noqa: E501
        """
        pass

    def test_patch_nveto_gain_model_item(self):
        """Test case for patch_nveto_gain_model_item

        Updates a NvetoGainModel document  # noqa: E501
        """
        pass

    def test_post_nveto_gain_models(self):
        """Test case for post_nveto_gain_models

        Stores one or more NvetoGainModels.  # noqa: E501
        """
        pass

    def test_put_nveto_gain_model_item(self):
        """Test case for put_nveto_gain_model_item

        Replaces a NvetoGainModel document  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
