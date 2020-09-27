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
from xepmts.models.inline_response2007 import InlineResponse2007  # noqa: E501
from xepmts.rest import ApiException

class TestInlineResponse2007(unittest.TestCase):
    """InlineResponse2007 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test InlineResponse2007
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = xepmts.models.inline_response2007.InlineResponse2007()  # noqa: E501
        if include_optional :
            return InlineResponse2007(
                items = [
                    xepmts.models.high_voltage_change.HighVoltageChange(
                        timestamp = '0', 
                        detector = 'tpc', 
                        experiment = 'xenonnt', 
                        kind = 'voltage', 
                        pmt_index = 56, 
                        old_value = 1.337, 
                        new_value = 1.337, 
                        operator = '0', 
                        comments = '0', 
                        _id = '0', )
                    ], 
                meta = xepmts.models.respone_metadata.respone_metadata(
                    page = '0', 
                    total = 56, 
                    max_results = 56, ), 
                links = xepmts.models.respone_links.respone_links(
                    parent = xepmts.models.respone_links_parent.respone_links_parent(
                        title = '0', 
                        href = '0', ), 
                    self = xepmts.models.respone_links_parent.respone_links_parent(
                        title = '0', 
                        href = '0', ), )
            )
        else :
            return InlineResponse2007(
        )

    def testInlineResponse2007(self):
        """Test InlineResponse2007"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
