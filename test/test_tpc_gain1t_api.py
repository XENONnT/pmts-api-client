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
from xepmts.api.tpc_gain1t_api import TpcGain1tApi  # noqa: E501
from xepmts.rest import ApiException


class TestTpcGain1tApi(unittest.TestCase):
    """TpcGain1tApi unit test stubs"""

    def setUp(self):
        self.api = xepmts.api.tpc_gain1t_api.TpcGain1tApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_delete_tpc_gain1t_item(self):
        """Test case for delete_tpc_gain1t_item

        Deletes a TpcGain1t document  # noqa: E501
        """
        pass

    def test_get_tpc_gain1t_item(self):
        """Test case for get_tpc_gain1t_item

        Retrieves a TpcGain1t document  # noqa: E501
        """
        pass

    def test_get_tpc_gain1ts(self):
        """Test case for get_tpc_gain1ts

        Retrieves one or more TpcGain1ts  # noqa: E501
        """
        pass

    def test_post_tpc_gain1ts(self):
        """Test case for post_tpc_gain1ts

        Stores one or more TpcGain1ts.  # noqa: E501
        """
        pass

    def test_put_tpc_gain1t_item(self):
        """Test case for put_tpc_gain1t_item

        Replaces a TpcGain1t document  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
