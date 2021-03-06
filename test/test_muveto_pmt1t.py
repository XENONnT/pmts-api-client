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
from xepmts.models.muveto_pmt1t import MuvetoPmt1t  # noqa: E501
from xepmts.rest import ApiException

class TestMuvetoPmt1t(unittest.TestCase):
    """MuvetoPmt1t unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test MuvetoPmt1t
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = xepmts.models.muveto_pmt1t.MuvetoPmt1t()  # noqa: E501
        if include_optional :
            return MuvetoPmt1t(
                serial_number = '0', 
                manufacturer = '0', 
                location = '0', 
                datasheet = '0', 
                id = '0'
            )
        else :
            return MuvetoPmt1t(
                serial_number = '0',
        )

    def testMuvetoPmt1t(self):
        """Test MuvetoPmt1t"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
