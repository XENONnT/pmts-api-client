# coding: utf-8

"""
    XENON PMT API

    API for the XENON PMT database  # noqa: E501

    The version of the OpenAPI document: 0.2
    Contact: joe.mosbacher@gmail.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from xepmts.configuration import Configuration


class ResponeMetadata(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'page': 'str',
        'total': 'int',
        'max_results': 'int'
    }

    attribute_map = {
        'page': 'page',
        'total': 'total',
        'max_results': 'max_results'
    }

    def __init__(self, page=None, total=None, max_results=None, local_vars_configuration=None):  # noqa: E501
        """ResponeMetadata - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._page = None
        self._total = None
        self._max_results = None
        self.discriminator = None

        if page is not None:
            self.page = page
        if total is not None:
            self.total = total
        if max_results is not None:
            self.max_results = max_results

    @property
    def page(self):
        """Gets the page of this ResponeMetadata.  # noqa: E501


        :return: The page of this ResponeMetadata.  # noqa: E501
        :rtype: str
        """
        return self._page

    @page.setter
    def page(self, page):
        """Sets the page of this ResponeMetadata.


        :param page: The page of this ResponeMetadata.  # noqa: E501
        :type: str
        """

        self._page = page

    @property
    def total(self):
        """Gets the total of this ResponeMetadata.  # noqa: E501


        :return: The total of this ResponeMetadata.  # noqa: E501
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this ResponeMetadata.


        :param total: The total of this ResponeMetadata.  # noqa: E501
        :type: int
        """

        self._total = total

    @property
    def max_results(self):
        """Gets the max_results of this ResponeMetadata.  # noqa: E501


        :return: The max_results of this ResponeMetadata.  # noqa: E501
        :rtype: int
        """
        return self._max_results

    @max_results.setter
    def max_results(self, max_results):
        """Sets the max_results of this ResponeMetadata.


        :param max_results: The max_results of this ResponeMetadata.  # noqa: E501
        :type: int
        """

        self._max_results = max_results

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ResponeMetadata):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ResponeMetadata):
            return True

        return self.to_dict() != other.to_dict()
