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
from xepmts.api.nveto_dark_count_rate_api import NvetoDarkCountRateApi  # noqa: E501
from xepmts.rest import ApiException


class TestNvetoDarkCountRateApi(unittest.TestCase):
    """NvetoDarkCountRateApi unit test stubs"""

    def setUp(self):
        self.api = xepmts.api.nveto_dark_count_rate_api.NvetoDarkCountRateApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_delete_nveto_dark_count_rate_item(self):
        """Test case for delete_nveto_dark_count_rate_item

        Deletes a NvetoDarkCountRate document  # noqa: E501
        """
        pass

    def test_get_nveto_dark_count_rate_item(self):
        """Test case for get_nveto_dark_count_rate_item

        Retrieves a NvetoDarkCountRate document  # noqa: E501
        """
        pass

    def test_get_nveto_dark_count_rates(self):
        """Test case for get_nveto_dark_count_rates

        Retrieves one or more NvetoDarkCountRates  # noqa: E501
        """
        pass

    def test_patch_nveto_dark_count_rate_item(self):
        """Test case for patch_nveto_dark_count_rate_item

        Updates a NvetoDarkCountRate document  # noqa: E501
        """
        pass

    def test_post_nveto_dark_count_rates(self):
        """Test case for post_nveto_dark_count_rates

        Stores one or more NvetoDarkCountRates.  # noqa: E501
        """
        pass

    def test_put_nveto_dark_count_rate_item(self):
        """Test case for put_nveto_dark_count_rate_item

        Replaces a NvetoDarkCountRate document  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
