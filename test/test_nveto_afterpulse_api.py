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
from xepmts.api.nveto_afterpulse_api import NvetoAfterpulseApi  # noqa: E501
from xepmts.rest import ApiException


class TestNvetoAfterpulseApi(unittest.TestCase):
    """NvetoAfterpulseApi unit test stubs"""

    def setUp(self):
        self.api = xepmts.api.nveto_afterpulse_api.NvetoAfterpulseApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_delete_nveto_afterpulse_item(self):
        """Test case for delete_nveto_afterpulse_item

        Deletes a NvetoAfterpulse document  # noqa: E501
        """
        pass

    def test_get_nveto_afterpulse_item(self):
        """Test case for get_nveto_afterpulse_item

        Retrieves a NvetoAfterpulse document  # noqa: E501
        """
        pass

    def test_get_nveto_afterpulses(self):
        """Test case for get_nveto_afterpulses

        Retrieves one or more NvetoAfterpulses  # noqa: E501
        """
        pass

    def test_post_nveto_afterpulses(self):
        """Test case for post_nveto_afterpulses

        Stores one or more NvetoAfterpulses.  # noqa: E501
        """
        pass

    def test_put_nveto_afterpulse_item(self):
        """Test case for put_nveto_afterpulse_item

        Replaces a NvetoAfterpulse document  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
