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
from xepmts.models.tpc_current_change1_t import TpcCurrentChange1T  # noqa: E501
from xepmts.rest import ApiException

class TestTpcCurrentChange1T(unittest.TestCase):
    """TpcCurrentChange1T unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test TpcCurrentChange1T
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = xepmts.models.tpc_current_change1_t.TpcCurrentChange1T()  # noqa: E501
        if include_optional :
            return TpcCurrentChange1T(
                timestamp = '0', 
                detector = 'tpc', 
                experiment = 'xenon1t', 
                pmt_index = 56, 
                old_current = 1.337, 
                new_current = 1.337, 
                operator = '0', 
                comments = '0', 
                id = '0'
            )
        else :
            return TpcCurrentChange1T(
                timestamp = '0',
                detector = 'tpc',
                experiment = 'xenon1t',
                pmt_index = 56,
                new_current = 1.337,
        )

    def testTpcCurrentChange1T(self):
        """Test TpcCurrentChange1T"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
