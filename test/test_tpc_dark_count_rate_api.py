# coding: utf-8

"""
    XENON PMT API

    API for the XENON PMT database  # noqa: E501

    The version of the OpenAPI document: 0.2
    Contact: joe.mosbacher@gmail.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import xepmts
from xepmts.api.tpc_dark_count_rate_api import TpcDarkCountRateApi  # noqa: E501
from xepmts.rest import ApiException


class TestTpcDarkCountRateApi(unittest.TestCase):
    """TpcDarkCountRateApi unit test stubs"""

    def setUp(self):
        self.api = xepmts.api.tpc_dark_count_rate_api.TpcDarkCountRateApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_delete_tpc_dark_count_rate_item(self):
        """Test case for delete_tpc_dark_count_rate_item

        Deletes a TpcDarkCountRate document  # noqa: E501
        """
        pass

    def test_get_tpc_dark_count_rate_item(self):
        """Test case for get_tpc_dark_count_rate_item

        Retrieves a TpcDarkCountRate document  # noqa: E501
        """
        pass

    def test_get_tpc_dark_count_rates(self):
        """Test case for get_tpc_dark_count_rates

        Retrieves one or more TpcDarkCountRates  # noqa: E501
        """
        pass

    def test_post_tpc_dark_count_rates(self):
        """Test case for post_tpc_dark_count_rates

        Stores one or more TpcDarkCountRates.  # noqa: E501
        """
        pass

    def test_put_tpc_dark_count_rate_item(self):
        """Test case for put_tpc_dark_count_rate_item

        Replaces a TpcDarkCountRate document  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
