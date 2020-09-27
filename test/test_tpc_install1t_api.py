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
from xepmts.api.tpc_install1t_api import TpcInstall1tApi  # noqa: E501
from xepmts.rest import ApiException


class TestTpcInstall1tApi(unittest.TestCase):
    """TpcInstall1tApi unit test stubs"""

    def setUp(self):
        self.api = xepmts.api.tpc_install1t_api.TpcInstall1tApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_delete_tpc_install1t_item(self):
        """Test case for delete_tpc_install1t_item

        Deletes a TpcInstall1t document  # noqa: E501
        """
        pass

    def test_get_tpc_install1t_item(self):
        """Test case for get_tpc_install1t_item

        Retrieves a TpcInstall1t document  # noqa: E501
        """
        pass

    def test_get_tpc_install1t_item_by_uid(self):
        """Test case for get_tpc_install1t_item_by_uid

        Retrieves a TpcInstall1t document by uid  # noqa: E501
        """
        pass

    def test_get_tpc_install1ts(self):
        """Test case for get_tpc_install1ts

        Retrieves one or more TpcInstall1ts  # noqa: E501
        """
        pass

    def test_patch_tpc_install1t_item(self):
        """Test case for patch_tpc_install1t_item

        Updates a TpcInstall1t document  # noqa: E501
        """
        pass

    def test_post_tpc_install1ts(self):
        """Test case for post_tpc_install1ts

        Stores one or more TpcInstall1ts.  # noqa: E501
        """
        pass

    def test_put_tpc_install1t_item(self):
        """Test case for put_tpc_install1t_item

        Replaces a TpcInstall1t document  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
