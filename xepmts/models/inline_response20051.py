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


class InlineResponse20051(object):
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
        'items': 'list[MuvetoPmt1T]',
        'meta': 'ResponeMetadata',
        'links': 'ResponeLinks'
    }

    attribute_map = {
        'items': '_items',
        'meta': '_meta',
        'links': '_links'
    }

    def __init__(self, items=None, meta=None, links=None, local_vars_configuration=None):  # noqa: E501
        """InlineResponse20051 - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._items = None
        self._meta = None
        self._links = None
        self.discriminator = None

        if items is not None:
            self.items = items
        if meta is not None:
            self.meta = meta
        if links is not None:
            self.links = links

    @property
    def items(self):
        """Gets the items of this InlineResponse20051.  # noqa: E501


        :return: The items of this InlineResponse20051.  # noqa: E501
        :rtype: list[MuvetoPmt1T]
        """
        return self._items

    @items.setter
    def items(self, items):
        """Sets the items of this InlineResponse20051.


        :param items: The items of this InlineResponse20051.  # noqa: E501
        :type: list[MuvetoPmt1T]
        """

        self._items = items

    @property
    def meta(self):
        """Gets the meta of this InlineResponse20051.  # noqa: E501


        :return: The meta of this InlineResponse20051.  # noqa: E501
        :rtype: ResponeMetadata
        """
        return self._meta

    @meta.setter
    def meta(self, meta):
        """Sets the meta of this InlineResponse20051.


        :param meta: The meta of this InlineResponse20051.  # noqa: E501
        :type: ResponeMetadata
        """

        self._meta = meta

    @property
    def links(self):
        """Gets the links of this InlineResponse20051.  # noqa: E501


        :return: The links of this InlineResponse20051.  # noqa: E501
        :rtype: ResponeLinks
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this InlineResponse20051.


        :param links: The links of this InlineResponse20051.  # noqa: E501
        :type: ResponeLinks
        """

        self._links = links

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
        if not isinstance(other, InlineResponse20051):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InlineResponse20051):
            return True

        return self.to_dict() != other.to_dict()
