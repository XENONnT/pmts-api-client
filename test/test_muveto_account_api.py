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

import xepmts
from xepmts.api.muveto_account_api import MuvetoAccountApi  # noqa: E501
from xepmts.rest import ApiException


class TestMuvetoAccountApi(unittest.TestCase):
    """MuvetoAccountApi unit test stubs"""

    def setUp(self):
        self.api = xepmts.api.muveto_account_api.MuvetoAccountApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_delete_muveto_account_item(self):
        """Test case for delete_muveto_account_item

        Deletes a MuvetoAccount document  # noqa: E501
        """
        pass

    def test_get_muveto_account_item(self):
        """Test case for get_muveto_account_item

        Retrieves a MuvetoAccount document  # noqa: E501
        """
        pass

    def test_get_muveto_account_item_by_username(self):
        """Test case for get_muveto_account_item_by_username

        Retrieves a MuvetoAccount document by username  # noqa: E501
        """
        pass

    def test_get_muveto_accounts(self):
        """Test case for get_muveto_accounts

        Retrieves one or more MuvetoAccounts  # noqa: E501
        """
        pass

    def test_post_muveto_accounts(self):
        """Test case for post_muveto_accounts

        Stores one or more MuvetoAccounts.  # noqa: E501
        """
        pass

    def test_put_muveto_account_item(self):
        """Test case for put_muveto_account_item

        Replaces a MuvetoAccount document  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
