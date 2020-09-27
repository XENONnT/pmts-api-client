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
from xepmts.api.nveto_voltage_change_api import NvetoVoltageChangeApi  # noqa: E501
from xepmts.rest import ApiException


class TestNvetoVoltageChangeApi(unittest.TestCase):
    """NvetoVoltageChangeApi unit test stubs"""

    def setUp(self):
        self.api = xepmts.api.nveto_voltage_change_api.NvetoVoltageChangeApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_delete_nveto_voltage_change_item(self):
        """Test case for delete_nveto_voltage_change_item

        Deletes a NvetoVoltageChange document  # noqa: E501
        """
        pass

    def test_get_nveto_voltage_change_item(self):
        """Test case for get_nveto_voltage_change_item

        Retrieves a NvetoVoltageChange document  # noqa: E501
        """
        pass

    def test_get_nveto_voltage_changes(self):
        """Test case for get_nveto_voltage_changes

        Retrieves one or more NvetoVoltageChanges  # noqa: E501
        """
        pass

    def test_patch_nveto_voltage_change_item(self):
        """Test case for patch_nveto_voltage_change_item

        Updates a NvetoVoltageChange document  # noqa: E501
        """
        pass

    def test_post_nveto_voltage_changes(self):
        """Test case for post_nveto_voltage_changes

        Stores one or more NvetoVoltageChanges.  # noqa: E501
        """
        pass

    def test_put_nveto_voltage_change_item(self):
        """Test case for put_nveto_voltage_change_item

        Replaces a NvetoVoltageChange document  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
