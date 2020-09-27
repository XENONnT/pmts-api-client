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
from xepmts.api.tpc_install_api import TpcInstallApi  # noqa: E501
from xepmts.rest import ApiException


class TestTpcInstallApi(unittest.TestCase):
    """TpcInstallApi unit test stubs"""

    def setUp(self):
        self.api = xepmts.api.tpc_install_api.TpcInstallApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_delete_tpc_install_item(self):
        """Test case for delete_tpc_install_item

        Deletes a TpcInstall document  # noqa: E501
        """
        pass

    def test_get_tpc_install_item(self):
        """Test case for get_tpc_install_item

        Retrieves a TpcInstall document  # noqa: E501
        """
        pass

    def test_get_tpc_install_item_by_uid(self):
        """Test case for get_tpc_install_item_by_uid

        Retrieves a TpcInstall document by uid  # noqa: E501
        """
        pass

    def test_get_tpc_installs(self):
        """Test case for get_tpc_installs

        Retrieves one or more TpcInstalls  # noqa: E501
        """
        pass

    def test_patch_tpc_install_item(self):
        """Test case for patch_tpc_install_item

        Updates a TpcInstall document  # noqa: E501
        """
        pass

    def test_post_tpc_installs(self):
        """Test case for post_tpc_installs

        Stores one or more TpcInstalls.  # noqa: E501
        """
        pass

    def test_put_tpc_install_item(self):
        """Test case for put_tpc_install_item

        Replaces a TpcInstall document  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
