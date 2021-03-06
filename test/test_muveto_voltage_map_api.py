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
from xepmts.api.muveto_voltage_map_api import MuvetoVoltageMapApi  # noqa: E501
from xepmts.rest import ApiException


class TestMuvetoVoltageMapApi(unittest.TestCase):
    """MuvetoVoltageMapApi unit test stubs"""

    def setUp(self):
        self.api = xepmts.api.muveto_voltage_map_api.MuvetoVoltageMapApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_delete_muveto_voltage_map_item(self):
        """Test case for delete_muveto_voltage_map_item

        Deletes a MuvetoVoltageMap document  # noqa: E501
        """
        pass

    def test_delete_muveto_voltage_maps(self):
        """Test case for delete_muveto_voltage_maps

        Deletes all MuvetoVoltageMaps  # noqa: E501
        """
        pass

    def test_get_muveto_voltage_map_item(self):
        """Test case for get_muveto_voltage_map_item

        Retrieves a MuvetoVoltageMap document  # noqa: E501
        """
        pass

    def test_get_muveto_voltage_map_item_by_name(self):
        """Test case for get_muveto_voltage_map_item_by_name

        Retrieves a MuvetoVoltageMap document by name  # noqa: E501
        """
        pass

    def test_get_muveto_voltage_maps(self):
        """Test case for get_muveto_voltage_maps

        Retrieves one or more MuvetoVoltageMaps  # noqa: E501
        """
        pass

    def test_patch_muveto_voltage_map_item(self):
        """Test case for patch_muveto_voltage_map_item

        Updates a MuvetoVoltageMap document  # noqa: E501
        """
        pass

    def test_post_muveto_voltage_maps(self):
        """Test case for post_muveto_voltage_maps

        Stores one or more MuvetoVoltageMaps.  # noqa: E501
        """
        pass

    def test_put_muveto_voltage_map_item(self):
        """Test case for put_muveto_voltage_map_item

        Replaces a MuvetoVoltageMap document  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
