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
import datetime

import xepmts
from xepmts.models.tpc_voltage_map import TpcVoltageMap  # noqa: E501
from xepmts.rest import ApiException

class TestTpcVoltageMap(unittest.TestCase):
    """TpcVoltageMap unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test TpcVoltageMap
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = xepmts.models.tpc_voltage_map.TpcVoltageMap()  # noqa: E501
        if include_optional :
            return TpcVoltageMap(
                name = 'a', 
                experiment = 'xenonnt', 
                detector = 'tpc', 
                active = True, 
                voltages = [
                    xepmts.models.tpc_voltage_map_voltages.TpcVoltageMap_voltages(
                        voltage = 1.337, 
                        pmt_index = 56, )
                    ], 
                created_by = '0', 
                comments = '0', 
                date = '0', 
                id = '0'
            )
        else :
            return TpcVoltageMap(
                name = 'a',
                experiment = 'xenonnt',
                detector = 'tpc',
        )

    def testTpcVoltageMap(self):
        """Test TpcVoltageMap"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
