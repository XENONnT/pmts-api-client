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
from xepmts.api.tpc_voltage_map1_t_api import TpcVoltageMap1TApi  # noqa: E501
from xepmts.rest import ApiException


class TestTpcVoltageMap1TApi(unittest.TestCase):
    """TpcVoltageMap1TApi unit test stubs"""

    def setUp(self):
        self.api = xepmts.api.tpc_voltage_map1_t_api.TpcVoltageMap1TApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_delete_tpc_voltage_map1_t_item(self):
        """Test case for delete_tpc_voltage_map1_t_item

        Deletes a TpcVoltageMap1T document  # noqa: E501
        """
        pass

    def test_delete_tpc_voltage_maps1_t(self):
        """Test case for delete_tpc_voltage_maps1_t

        Deletes all TpcVoltageMaps1T  # noqa: E501
        """
        pass

    def test_get_tpc_voltage_map1_t_item(self):
        """Test case for get_tpc_voltage_map1_t_item

        Retrieves a TpcVoltageMap1T document  # noqa: E501
        """
        pass

    def test_get_tpc_voltage_map1_t_item_by_name(self):
        """Test case for get_tpc_voltage_map1_t_item_by_name

        Retrieves a TpcVoltageMap1T document by name  # noqa: E501
        """
        pass

    def test_get_tpc_voltage_maps1_t(self):
        """Test case for get_tpc_voltage_maps1_t

        Retrieves one or more TpcVoltageMaps1T  # noqa: E501
        """
        pass

    def test_post_tpc_voltage_maps1_t(self):
        """Test case for post_tpc_voltage_maps1_t

        Stores one or more TpcVoltageMaps1T.  # noqa: E501
        """
        pass

    def test_put_tpc_voltage_map1_t_item(self):
        """Test case for put_tpc_voltage_map1_t_item

        Replaces a TpcVoltageMap1T document  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
