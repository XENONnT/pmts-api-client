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
from xepmts.models.inline_response20037 import InlineResponse20037  # noqa: E501
from xepmts.rest import ApiException

class TestInlineResponse20037(unittest.TestCase):
    """InlineResponse20037 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test InlineResponse20037
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = xepmts.models.inline_response20037.InlineResponse20037()  # noqa: E501
        if include_optional :
            return InlineResponse20037(
                items = [
                    xepmts.models.muveto_voltage_map_name.MuvetoVoltageMapName(
                        name = '0', 
                        experiment = 'xenonnt', 
                        detector = 'muveto', 
                        _id = '0', )
                    ], 
                meta = xepmts.models.respone_metadata.respone_metadata(
                    page = '0', 
                    total = 56, 
                    max_results = 56, )
            )
        else :
            return InlineResponse20037(
        )

    def testInlineResponse20037(self):
        """Test InlineResponse20037"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
