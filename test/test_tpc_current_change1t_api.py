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
from xepmts.api.tpc_current_change1t_api import TpcCurrentChange1tApi  # noqa: E501
from xepmts.rest import ApiException


class TestTpcCurrentChange1tApi(unittest.TestCase):
    """TpcCurrentChange1tApi unit test stubs"""

    def setUp(self):
        self.api = xepmts.api.tpc_current_change1t_api.TpcCurrentChange1tApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_delete_tpc_current_change1t_item(self):
        """Test case for delete_tpc_current_change1t_item

        Deletes a TpcCurrentChange1t document  # noqa: E501
        """
        pass

    def test_get_tpc_current_change1t_item(self):
        """Test case for get_tpc_current_change1t_item

        Retrieves a TpcCurrentChange1t document  # noqa: E501
        """
        pass

    def test_get_tpc_current_change1ts(self):
        """Test case for get_tpc_current_change1ts

        Retrieves one or more TpcCurrentChange1ts  # noqa: E501
        """
        pass

    def test_patch_tpc_current_change1t_item(self):
        """Test case for patch_tpc_current_change1t_item

        Updates a TpcCurrentChange1t document  # noqa: E501
        """
        pass

    def test_post_tpc_current_change1ts(self):
        """Test case for post_tpc_current_change1ts

        Stores one or more TpcCurrentChange1ts.  # noqa: E501
        """
        pass

    def test_put_tpc_current_change1t_item(self):
        """Test case for put_tpc_current_change1t_item

        Replaces a TpcCurrentChange1t document  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
