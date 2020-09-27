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


class MuvetoVoltageMap1t(object):
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
        'name': 'str',
        'experiment': 'str',
        'detector': 'str',
        'active': 'bool',
        'voltages': 'list[TpcVoltageMapVoltages]',
        'created_by': 'str',
        'comments': 'str',
        'date': 'str',
        'id': 'str'
    }

    attribute_map = {
        'name': 'name',
        'experiment': 'experiment',
        'detector': 'detector',
        'active': 'active',
        'voltages': 'voltages',
        'created_by': 'created_by',
        'comments': 'comments',
        'date': 'date',
        'id': '_id'
    }

    def __init__(self, name=None, experiment='xenon1t', detector='muveto', active=True, voltages=None, created_by=None, comments=None, date=None, id=None, local_vars_configuration=None):  # noqa: E501
        """MuvetoVoltageMap1t - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._experiment = None
        self._detector = None
        self._active = None
        self._voltages = None
        self._created_by = None
        self._comments = None
        self._date = None
        self._id = None
        self.discriminator = None

        self.name = name
        self.experiment = experiment
        self.detector = detector
        if active is not None:
            self.active = active
        if voltages is not None:
            self.voltages = voltages
        if created_by is not None:
            self.created_by = created_by
        if comments is not None:
            self.comments = comments
        if date is not None:
            self.date = date
        if id is not None:
            self.id = id

    @property
    def name(self):
        """Gets the name of this MuvetoVoltageMap1t.  # noqa: E501


        :return: The name of this MuvetoVoltageMap1t.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this MuvetoVoltageMap1t.


        :param name: The name of this MuvetoVoltageMap1t.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and not re.search(r'^\S+$', name)):  # noqa: E501
            raise ValueError(r"Invalid value for `name`, must be a follow pattern or equal to `/^\S+$/`")  # noqa: E501

        self._name = name

    @property
    def experiment(self):
        """Gets the experiment of this MuvetoVoltageMap1t.  # noqa: E501


        :return: The experiment of this MuvetoVoltageMap1t.  # noqa: E501
        :rtype: str
        """
        return self._experiment

    @experiment.setter
    def experiment(self, experiment):
        """Sets the experiment of this MuvetoVoltageMap1t.


        :param experiment: The experiment of this MuvetoVoltageMap1t.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and experiment is None:  # noqa: E501
            raise ValueError("Invalid value for `experiment`, must not be `None`")  # noqa: E501
        allowed_values = ["xenon1t", "xenonnt", "unknown"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and experiment not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `experiment` ({0}), must be one of {1}"  # noqa: E501
                .format(experiment, allowed_values)
            )

        self._experiment = experiment

    @property
    def detector(self):
        """Gets the detector of this MuvetoVoltageMap1t.  # noqa: E501


        :return: The detector of this MuvetoVoltageMap1t.  # noqa: E501
        :rtype: str
        """
        return self._detector

    @detector.setter
    def detector(self, detector):
        """Sets the detector of this MuvetoVoltageMap1t.


        :param detector: The detector of this MuvetoVoltageMap1t.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and detector is None:  # noqa: E501
            raise ValueError("Invalid value for `detector`, must not be `None`")  # noqa: E501
        allowed_values = ["tpc", "nveto", "muveto", "unknown"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and detector not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `detector` ({0}), must be one of {1}"  # noqa: E501
                .format(detector, allowed_values)
            )

        self._detector = detector

    @property
    def active(self):
        """Gets the active of this MuvetoVoltageMap1t.  # noqa: E501


        :return: The active of this MuvetoVoltageMap1t.  # noqa: E501
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """Sets the active of this MuvetoVoltageMap1t.


        :param active: The active of this MuvetoVoltageMap1t.  # noqa: E501
        :type: bool
        """

        self._active = active

    @property
    def voltages(self):
        """Gets the voltages of this MuvetoVoltageMap1t.  # noqa: E501


        :return: The voltages of this MuvetoVoltageMap1t.  # noqa: E501
        :rtype: list[TpcVoltageMapVoltages]
        """
        return self._voltages

    @voltages.setter
    def voltages(self, voltages):
        """Sets the voltages of this MuvetoVoltageMap1t.


        :param voltages: The voltages of this MuvetoVoltageMap1t.  # noqa: E501
        :type: list[TpcVoltageMapVoltages]
        """

        self._voltages = voltages

    @property
    def created_by(self):
        """Gets the created_by of this MuvetoVoltageMap1t.  # noqa: E501


        :return: The created_by of this MuvetoVoltageMap1t.  # noqa: E501
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this MuvetoVoltageMap1t.


        :param created_by: The created_by of this MuvetoVoltageMap1t.  # noqa: E501
        :type: str
        """

        self._created_by = created_by

    @property
    def comments(self):
        """Gets the comments of this MuvetoVoltageMap1t.  # noqa: E501


        :return: The comments of this MuvetoVoltageMap1t.  # noqa: E501
        :rtype: str
        """
        return self._comments

    @comments.setter
    def comments(self, comments):
        """Sets the comments of this MuvetoVoltageMap1t.


        :param comments: The comments of this MuvetoVoltageMap1t.  # noqa: E501
        :type: str
        """

        self._comments = comments

    @property
    def date(self):
        """Gets the date of this MuvetoVoltageMap1t.  # noqa: E501


        :return: The date of this MuvetoVoltageMap1t.  # noqa: E501
        :rtype: str
        """
        return self._date

    @date.setter
    def date(self, date):
        """Sets the date of this MuvetoVoltageMap1t.


        :param date: The date of this MuvetoVoltageMap1t.  # noqa: E501
        :type: str
        """

        self._date = date

    @property
    def id(self):
        """Gets the id of this MuvetoVoltageMap1t.  # noqa: E501


        :return: The id of this MuvetoVoltageMap1t.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this MuvetoVoltageMap1t.


        :param id: The id of this MuvetoVoltageMap1t.  # noqa: E501
        :type: str
        """

        self._id = id

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
        if not isinstance(other, MuvetoVoltageMap1t):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MuvetoVoltageMap1t):
            return True

        return self.to_dict() != other.to_dict()
