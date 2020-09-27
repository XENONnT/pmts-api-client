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
from xepmts.models.nveto_afterpulse import NvetoAfterpulse  # noqa: E501
from xepmts.rest import ApiException

class TestNvetoAfterpulse(unittest.TestCase):
    """NvetoAfterpulse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test NvetoAfterpulse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = xepmts.models.nveto_afterpulse.NvetoAfterpulse()  # noqa: E501
        if include_optional :
            return NvetoAfterpulse(
                experiment = 'xenonnt', 
                detector = 'nveto', 
                pmt_index = 56, 
                run_id = '0', 
                timestamp = 56, 
                start_time = 56, 
                end_time = 56, 
                trigger_sigma = 1.337, 
                total_ap = 1.337, 
                pe = 1.337, 
                pe_error = 1.337, 
                ar_pos = 1.337, 
                hv = 1.337, 
                ne_ap = 1.337, 
                ne_pos = 1.337, 
                xe_pos = 1.337, 
                n2_pos = 1.337, 
                ch4ap = 1.337, 
                he_ap = 1.337, 
                ar_ap = 1.337, 
                doublexe_pos = 1.337, 
                doublexe_ap = 1.337, 
                trigger_mean = 1.337, 
                gain = 1.337, 
                ch4_pos = 1.337, 
                n2_ap = 1.337, 
                xe_ap = 1.337, 
                pe_pulses = 1.337, 
                trigger_number = 1.337, 
                id = '0'
            )
        else :
            return NvetoAfterpulse(
                experiment = 'xenonnt',
                detector = 'nveto',
                pmt_index = 56,
        )

    def testNvetoAfterpulse(self):
        """Test NvetoAfterpulse"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
