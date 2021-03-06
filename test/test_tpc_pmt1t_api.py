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
from xepmts.api.tpc_pmt1t_api import TpcPmt1tApi  # noqa: E501
from xepmts.rest import ApiException


class TestTpcPmt1tApi(unittest.TestCase):
    """TpcPmt1tApi unit test stubs"""

    def setUp(self):
        self.api = xepmts.api.tpc_pmt1t_api.TpcPmt1tApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_delete_tpc_pmt1t_item(self):
        """Test case for delete_tpc_pmt1t_item

        Deletes a TpcPmt1t document  # noqa: E501
        """
        pass

    def test_get_tpc_pmt1t_item(self):
        """Test case for get_tpc_pmt1t_item

        Retrieves a TpcPmt1t document  # noqa: E501
        """
        pass

    def test_get_tpc_pmt1t_item_by_serial_number(self):
        """Test case for get_tpc_pmt1t_item_by_serial_number

        Retrieves a TpcPmt1t document by serial_number  # noqa: E501
        """
        pass

    def test_get_tpc_pmt1ts(self):
        """Test case for get_tpc_pmt1ts

        Retrieves one or more TpcPmt1ts  # noqa: E501
        """
        pass

    def test_patch_tpc_pmt1t_item(self):
        """Test case for patch_tpc_pmt1t_item

        Updates a TpcPmt1t document  # noqa: E501
        """
        pass

    def test_post_tpc_pmt1ts(self):
        """Test case for post_tpc_pmt1ts

        Stores one or more TpcPmt1ts.  # noqa: E501
        """
        pass

    def test_put_tpc_pmt1t_item(self):
        """Test case for put_tpc_pmt1t_item

        Replaces a TpcPmt1t document  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
