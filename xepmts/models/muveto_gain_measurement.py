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


class MuvetoGainMeasurement(object):
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
        'detector': 'str',
        'experiment': 'str',
        'run_id': 'str',
        'timestamp': 'int',
        'pmt_index': 'int',
        'led_data': 'list[int]',
        'noise_data': 'list[int]',
        'id': 'str'
    }

    attribute_map = {
        'detector': 'detector',
        'experiment': 'experiment',
        'run_id': 'run_id',
        'timestamp': 'timestamp',
        'pmt_index': 'pmt_index',
        'led_data': 'led_data',
        'noise_data': 'noise_data',
        'id': '_id'
    }

    def __init__(self, detector='muveto', experiment='xenonnt', run_id=None, timestamp=None, pmt_index=None, led_data=None, noise_data=None, id=None, local_vars_configuration=None):  # noqa: E501
        """MuvetoGainMeasurement - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._detector = None
        self._experiment = None
        self._run_id = None
        self._timestamp = None
        self._pmt_index = None
        self._led_data = None
        self._noise_data = None
        self._id = None
        self.discriminator = None

        self.detector = detector
        self.experiment = experiment
        if run_id is not None:
            self.run_id = run_id
        if timestamp is not None:
            self.timestamp = timestamp
        self.pmt_index = pmt_index
        if led_data is not None:
            self.led_data = led_data
        if noise_data is not None:
            self.noise_data = noise_data
        if id is not None:
            self.id = id

    @property
    def detector(self):
        """Gets the detector of this MuvetoGainMeasurement.  # noqa: E501


        :return: The detector of this MuvetoGainMeasurement.  # noqa: E501
        :rtype: str
        """
        return self._detector

    @detector.setter
    def detector(self, detector):
        """Sets the detector of this MuvetoGainMeasurement.


        :param detector: The detector of this MuvetoGainMeasurement.  # noqa: E501
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
    def experiment(self):
        """Gets the experiment of this MuvetoGainMeasurement.  # noqa: E501


        :return: The experiment of this MuvetoGainMeasurement.  # noqa: E501
        :rtype: str
        """
        return self._experiment

    @experiment.setter
    def experiment(self, experiment):
        """Sets the experiment of this MuvetoGainMeasurement.


        :param experiment: The experiment of this MuvetoGainMeasurement.  # noqa: E501
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
    def run_id(self):
        """Gets the run_id of this MuvetoGainMeasurement.  # noqa: E501


        :return: The run_id of this MuvetoGainMeasurement.  # noqa: E501
        :rtype: str
        """
        return self._run_id

    @run_id.setter
    def run_id(self, run_id):
        """Sets the run_id of this MuvetoGainMeasurement.


        :param run_id: The run_id of this MuvetoGainMeasurement.  # noqa: E501
        :type: str
        """

        self._run_id = run_id

    @property
    def timestamp(self):
        """Gets the timestamp of this MuvetoGainMeasurement.  # noqa: E501


        :return: The timestamp of this MuvetoGainMeasurement.  # noqa: E501
        :rtype: int
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this MuvetoGainMeasurement.


        :param timestamp: The timestamp of this MuvetoGainMeasurement.  # noqa: E501
        :type: int
        """

        self._timestamp = timestamp

    @property
    def pmt_index(self):
        """Gets the pmt_index of this MuvetoGainMeasurement.  # noqa: E501


        :return: The pmt_index of this MuvetoGainMeasurement.  # noqa: E501
        :rtype: int
        """
        return self._pmt_index

    @pmt_index.setter
    def pmt_index(self, pmt_index):
        """Sets the pmt_index of this MuvetoGainMeasurement.


        :param pmt_index: The pmt_index of this MuvetoGainMeasurement.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and pmt_index is None:  # noqa: E501
            raise ValueError("Invalid value for `pmt_index`, must not be `None`")  # noqa: E501

        self._pmt_index = pmt_index

    @property
    def led_data(self):
        """Gets the led_data of this MuvetoGainMeasurement.  # noqa: E501


        :return: The led_data of this MuvetoGainMeasurement.  # noqa: E501
        :rtype: list[int]
        """
        return self._led_data

    @led_data.setter
    def led_data(self, led_data):
        """Sets the led_data of this MuvetoGainMeasurement.


        :param led_data: The led_data of this MuvetoGainMeasurement.  # noqa: E501
        :type: list[int]
        """

        self._led_data = led_data

    @property
    def noise_data(self):
        """Gets the noise_data of this MuvetoGainMeasurement.  # noqa: E501


        :return: The noise_data of this MuvetoGainMeasurement.  # noqa: E501
        :rtype: list[int]
        """
        return self._noise_data

    @noise_data.setter
    def noise_data(self, noise_data):
        """Sets the noise_data of this MuvetoGainMeasurement.


        :param noise_data: The noise_data of this MuvetoGainMeasurement.  # noqa: E501
        :type: list[int]
        """

        self._noise_data = noise_data

    @property
    def id(self):
        """Gets the id of this MuvetoGainMeasurement.  # noqa: E501


        :return: The id of this MuvetoGainMeasurement.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this MuvetoGainMeasurement.


        :param id: The id of this MuvetoGainMeasurement.  # noqa: E501
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
        if not isinstance(other, MuvetoGainMeasurement):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MuvetoGainMeasurement):
            return True

        return self.to_dict() != other.to_dict()
