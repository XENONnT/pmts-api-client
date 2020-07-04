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
from xepmts.models.muveto_dark_count_rate1t import MuvetoDarkCountRate1t  # noqa: E501
from xepmts.rest import ApiException

class TestMuvetoDarkCountRate1t(unittest.TestCase):
    """MuvetoDarkCountRate1t unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test MuvetoDarkCountRate1t
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = xepmts.models.muveto_dark_count_rate1t.MuvetoDarkCountRate1t()  # noqa: E501
        if include_optional :
            return MuvetoDarkCountRate1t(
                run_id = '0', 
                timestamp = 56, 
                detector = 'muveto', 
                experiment = 'xenon1t', 
                pmt_index = 56, 
                dcr_mean = 1.337, 
                dcr_std_dev = 1.337, 
                id = '0'
            )
        else :
            return MuvetoDarkCountRate1t(
                detector = 'muveto',
                experiment = 'xenon1t',
                pmt_index = 56,
                dcr_mean = 1.337,
        )

    def testMuvetoDarkCountRate1t(self):
        """Test MuvetoDarkCountRate1t"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
