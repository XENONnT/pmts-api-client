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
from xepmts.api.tpc_voltage_change_api import TpcVoltageChangeApi  # noqa: E501
from xepmts.rest import ApiException


class TestTpcVoltageChangeApi(unittest.TestCase):
    """TpcVoltageChangeApi unit test stubs"""

    def setUp(self):
        self.api = xepmts.api.tpc_voltage_change_api.TpcVoltageChangeApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_delete_tpc_voltage_change_item(self):
        """Test case for delete_tpc_voltage_change_item

        Deletes a TpcVoltageChange document  # noqa: E501
        """
        pass

    def test_get_tpc_voltage_change_item(self):
        """Test case for get_tpc_voltage_change_item

        Retrieves a TpcVoltageChange document  # noqa: E501
        """
        pass

    def test_get_tpc_voltage_changes(self):
        """Test case for get_tpc_voltage_changes

        Retrieves one or more TpcVoltageChanges  # noqa: E501
        """
        pass

    def test_patch_tpc_voltage_change_item(self):
        """Test case for patch_tpc_voltage_change_item

        Updates a TpcVoltageChange document  # noqa: E501
        """
        pass

    def test_post_tpc_voltage_changes(self):
        """Test case for post_tpc_voltage_changes

        Stores one or more TpcVoltageChanges.  # noqa: E501
        """
        pass

    def test_put_tpc_voltage_change_item(self):
        """Test case for put_tpc_voltage_change_item

        Replaces a TpcVoltageChange document  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
