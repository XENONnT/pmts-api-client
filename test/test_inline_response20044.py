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
from xepmts.models.inline_response20044 import InlineResponse20044  # noqa: E501
from xepmts.rest import ApiException

class TestInlineResponse20044(unittest.TestCase):
    """InlineResponse20044 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test InlineResponse20044
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = xepmts.models.inline_response20044.InlineResponse20044()  # noqa: E501
        if include_optional :
            return InlineResponse20044(
                items = [
                    xepmts.models.tpc_install1t.TpcInstall1t(
                        uid = '0', 
                        array = '0', 
                        detector = 'tpc', 
                        experiment = 'xenon1t', 
                        pmt_index = 56, 
                        sector = 56, 
                        position_x = 1.337, 
                        position_y = 1.337, 
                        position_z = 1.337, 
                        position_r = 1.337, 
                        amplifier_crate = 56, 
                        amplifier_fan = 56, 
                        amplifier_plug = 56, 
                        amplifier_serial = 56, 
                        amplifier_slot = 56, 
                        amplifier_channel = 56, 
                        digitizer_channel = 56, 
                        digitizer_crate = 56, 
                        digitizer_module = 56, 
                        digitizer_slot = 56, 
                        high_voltage_crate = 56, 
                        high_voltage_board = 56, 
                        high_voltage_channel = 56, 
                        high_voltage_connector = 56, 
                        high_voltage_feedthrough = '0', 
                        high_voltage_return = 56, 
                        serial_number = '0', 
                        signal_channel = 56, 
                        signal_connector = 56, 
                        signal_feedthrough = '0', 
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
            return InlineResponse20044(
        )

    def testInlineResponse20044(self):
        """Test InlineResponse20044"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
