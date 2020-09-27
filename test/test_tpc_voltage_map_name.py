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
from xepmts.models.tpc_voltage_map_name import TpcVoltageMapName  # noqa: E501
from xepmts.rest import ApiException

class TestTpcVoltageMapName(unittest.TestCase):
    """TpcVoltageMapName unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test TpcVoltageMapName
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = xepmts.models.tpc_voltage_map_name.TpcVoltageMapName()  # noqa: E501
        if include_optional :
            return TpcVoltageMapName(
                name = '0', 
                experiment = 'xenonnt', 
                detector = 'tpc', 
                id = '0'
            )
        else :
            return TpcVoltageMapName(
                experiment = 'xenonnt',
                detector = 'tpc',
        )

    def testTpcVoltageMapName(self):
        """Test TpcVoltageMapName"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
