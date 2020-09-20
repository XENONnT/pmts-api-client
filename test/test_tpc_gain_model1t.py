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
from xepmts.models.tpc_gain_model1t import TpcGainModel1t  # noqa: E501
from xepmts.rest import ApiException

class TestTpcGainModel1t(unittest.TestCase):
    """TpcGainModel1t unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test TpcGainModel1t
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = xepmts.models.tpc_gain_model1t.TpcGainModel1t()  # noqa: E501
        if include_optional :
            return TpcGainModel1t(
                detector = 'tpc', 
                experiment = 'xenon1t', 
                run_id = '0', 
                timestamp = 56, 
                pmt_index = 56, 
                gain = 1.337, 
                gain_err = 1.337, 
                gain_stat_err = 1.337, 
                gain_sys_err = 1.337, 
                voltage = 1.337, 
                gain_model = 1.337, 
                gain_model_stat_err = 1.337, 
                gain_model_err = 1.337, 
                adctoe_gain_model = 1.337, 
                adctoe_gain_model_err = 1.337, 
                id = '0'
            )
        else :
            return TpcGainModel1t(
                detector = 'tpc',
                experiment = 'xenon1t',
                run_id = '0',
                pmt_index = 56,
                gain = 1.337,
                gain_err = 1.337,
        )

    def testTpcGainModel1t(self):
        """Test TpcGainModel1t"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
