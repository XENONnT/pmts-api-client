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
from xepmts.models.muveto_dark_count_rate import MuvetoDarkCountRate  # noqa: E501
from xepmts.rest import ApiException

class TestMuvetoDarkCountRate(unittest.TestCase):
    """MuvetoDarkCountRate unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test MuvetoDarkCountRate
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = xepmts.models.muveto_dark_count_rate.MuvetoDarkCountRate()  # noqa: E501
        if include_optional :
            return MuvetoDarkCountRate(
                run_id = '0', 
                timestamp = 56, 
                detector = 'muveto', 
                experiment = 'xenonnt', 
                pmt_index = 56, 
                dcr_mean = 1.337, 
                dcr_std_dev = 1.337, 
                id = '0'
            )
        else :
            return MuvetoDarkCountRate(
                detector = 'muveto',
                experiment = 'xenonnt',
                pmt_index = 56,
                dcr_mean = 1.337,
        )

    def testMuvetoDarkCountRate(self):
        """Test MuvetoDarkCountRate"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
