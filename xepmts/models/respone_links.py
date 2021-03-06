# coding: utf-8

"""
    XENON PMT API

    API for the XENON PMT database  # noqa: E501

    The version of the OpenAPI document: 1.0
    Contact: joe.mosbacher@gmail.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from xepmts.configuration import Configuration


class ResponeLinks(object):
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
        'parent': 'ResponeLinksParent',
        '_self': 'ResponeLinksParent'
    }

    attribute_map = {
        'parent': 'parent',
        '_self': 'self'
    }

    def __init__(self, parent=None, _self=None, local_vars_configuration=None):  # noqa: E501
        """ResponeLinks - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._parent = None
        self.__self = None
        self.discriminator = None

        if parent is not None:
            self.parent = parent
        if _self is not None:
            self._self = _self

    @property
    def parent(self):
        """Gets the parent of this ResponeLinks.  # noqa: E501


        :return: The parent of this ResponeLinks.  # noqa: E501
        :rtype: ResponeLinksParent
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """Sets the parent of this ResponeLinks.


        :param parent: The parent of this ResponeLinks.  # noqa: E501
        :type: ResponeLinksParent
        """

        self._parent = parent

    @property
    def _self(self):
        """Gets the _self of this ResponeLinks.  # noqa: E501


        :return: The _self of this ResponeLinks.  # noqa: E501
        :rtype: ResponeLinksParent
        """
        return self.__self

    @_self.setter
    def _self(self, _self):
        """Sets the _self of this ResponeLinks.


        :param _self: The _self of this ResponeLinks.  # noqa: E501
        :type: ResponeLinksParent
        """

        self.__self = _self

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
        if not isinstance(other, ResponeLinks):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ResponeLinks):
            return True

        return self.to_dict() != other.to_dict()
