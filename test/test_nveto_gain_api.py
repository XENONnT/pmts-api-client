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
from xepmts.api.nveto_gain_api import NvetoGainApi  # noqa: E501
from xepmts.rest import ApiException


class TestNvetoGainApi(unittest.TestCase):
    """NvetoGainApi unit test stubs"""

    def setUp(self):
        self.api = xepmts.api.nveto_gain_api.NvetoGainApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_delete_nveto_gain_item(self):
        """Test case for delete_nveto_gain_item

        Deletes a NvetoGain document  # noqa: E501
        """
        pass

    def test_get_nveto_gain_item(self):
        """Test case for get_nveto_gain_item

        Retrieves a NvetoGain document  # noqa: E501
        """
        pass

    def test_get_nveto_gains(self):
        """Test case for get_nveto_gains

        Retrieves one or more NvetoGains  # noqa: E501
        """
        pass

    def test_patch_nveto_gain_item(self):
        """Test case for patch_nveto_gain_item

        Updates a NvetoGain document  # noqa: E501
        """
        pass

    def test_post_nveto_gains(self):
        """Test case for post_nveto_gains

        Stores one or more NvetoGains.  # noqa: E501
        """
        pass

    def test_put_nveto_gain_item(self):
        """Test case for put_nveto_gain_item

        Replaces a NvetoGain document  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
