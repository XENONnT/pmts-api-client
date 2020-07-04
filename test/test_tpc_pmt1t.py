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
import datetime

import xepmts
from xepmts.models.tpc_pmt1t import TpcPmt1t  # noqa: E501
from xepmts.rest import ApiException

class TestTpcPmt1t(unittest.TestCase):
    """TpcPmt1t unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test TpcPmt1t
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = xepmts.models.tpc_pmt1t.TpcPmt1t()  # noqa: E501
        if include_optional :
            return TpcPmt1t(
                serial_number = '0', 
                manufacturer = '0', 
                location = '0', 
                datasheet = '0', 
                id = '0'
            )
        else :
            return TpcPmt1t(
                serial_number = '0',
        )

    def testTpcPmt1t(self):
        """Test TpcPmt1t"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()