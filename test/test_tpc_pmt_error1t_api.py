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

import xepmts
from xepmts.api.tpc_pmt_error1t_api import TpcPmtError1tApi  # noqa: E501
from xepmts.rest import ApiException


class TestTpcPmtError1tApi(unittest.TestCase):
    """TpcPmtError1tApi unit test stubs"""

    def setUp(self):
        self.api = xepmts.api.tpc_pmt_error1t_api.TpcPmtError1tApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_delete_tpc_pmt_error1t_item(self):
        """Test case for delete_tpc_pmt_error1t_item

        Deletes a TpcPmtError1t document  # noqa: E501
        """
        pass

    def test_get_tpc_pmt_error1t_item(self):
        """Test case for get_tpc_pmt_error1t_item

        Retrieves a TpcPmtError1t document  # noqa: E501
        """
        pass

    def test_get_tpc_pmt_error1ts(self):
        """Test case for get_tpc_pmt_error1ts

        Retrieves one or more TpcPmtError1ts  # noqa: E501
        """
        pass

    def test_patch_tpc_pmt_error1t_item(self):
        """Test case for patch_tpc_pmt_error1t_item

        Updates a TpcPmtError1t document  # noqa: E501
        """
        pass

    def test_post_tpc_pmt_error1ts(self):
        """Test case for post_tpc_pmt_error1ts

        Stores one or more TpcPmtError1ts.  # noqa: E501
        """
        pass

    def test_put_tpc_pmt_error1t_item(self):
        """Test case for put_tpc_pmt_error1t_item

        Replaces a TpcPmtError1t document  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
