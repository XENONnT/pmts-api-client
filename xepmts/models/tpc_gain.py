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


class TpcGain(object):
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
        'gain': 'float',
        'gain_err': 'float',
        'gain_stat_err': 'float',
        'gain_sys_err': 'float',
        'voltage': 'float',
        'occupancy': 'float',
        'occupancy_err': 'float',
        'id': 'str'
    }

    attribute_map = {
        'detector': 'detector',
        'experiment': 'experiment',
        'run_id': 'run_id',
        'timestamp': 'timestamp',
        'pmt_index': 'pmt_index',
        'gain': 'gain',
        'gain_err': 'gain_err',
        'gain_stat_err': 'gain_stat_err',
        'gain_sys_err': 'gain_sys_err',
        'voltage': 'voltage',
        'occupancy': 'occupancy',
        'occupancy_err': 'occupancy_err',
        'id': '_id'
    }

    def __init__(self, detector='tpc', experiment='xenonnt', run_id=None, timestamp=None, pmt_index=None, gain=None, gain_err=None, gain_stat_err=None, gain_sys_err=None, voltage=None, occupancy=None, occupancy_err=None, id=None, local_vars_configuration=None):  # noqa: E501
        """TpcGain - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._detector = None
        self._experiment = None
        self._run_id = None
        self._timestamp = None
        self._pmt_index = None
        self._gain = None
        self._gain_err = None
        self._gain_stat_err = None
        self._gain_sys_err = None
        self._voltage = None
        self._occupancy = None
        self._occupancy_err = None
        self._id = None
        self.discriminator = None

        self.detector = detector
        self.experiment = experiment
        if run_id is not None:
            self.run_id = run_id
        if timestamp is not None:
            self.timestamp = timestamp
        self.pmt_index = pmt_index
        self.gain = gain
        if gain_err is not None:
            self.gain_err = gain_err
        if gain_stat_err is not None:
            self.gain_stat_err = gain_stat_err
        if gain_sys_err is not None:
            self.gain_sys_err = gain_sys_err
        if voltage is not None:
            self.voltage = voltage
        if occupancy is not None:
            self.occupancy = occupancy
        if occupancy_err is not None:
            self.occupancy_err = occupancy_err
        if id is not None:
            self.id = id

    @property
    def detector(self):
        """Gets the detector of this TpcGain.  # noqa: E501


        :return: The detector of this TpcGain.  # noqa: E501
        :rtype: str
        """
        return self._detector

    @detector.setter
    def detector(self, detector):
        """Sets the detector of this TpcGain.


        :param detector: The detector of this TpcGain.  # noqa: E501
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
        """Gets the experiment of this TpcGain.  # noqa: E501


        :return: The experiment of this TpcGain.  # noqa: E501
        :rtype: str
        """
        return self._experiment

    @experiment.setter
    def experiment(self, experiment):
        """Sets the experiment of this TpcGain.


        :param experiment: The experiment of this TpcGain.  # noqa: E501
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
        """Gets the run_id of this TpcGain.  # noqa: E501


        :return: The run_id of this TpcGain.  # noqa: E501
        :rtype: str
        """
        return self._run_id

    @run_id.setter
    def run_id(self, run_id):
        """Sets the run_id of this TpcGain.


        :param run_id: The run_id of this TpcGain.  # noqa: E501
        :type: str
        """

        self._run_id = run_id

    @property
    def timestamp(self):
        """Gets the timestamp of this TpcGain.  # noqa: E501


        :return: The timestamp of this TpcGain.  # noqa: E501
        :rtype: int
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this TpcGain.


        :param timestamp: The timestamp of this TpcGain.  # noqa: E501
        :type: int
        """

        self._timestamp = timestamp

    @property
    def pmt_index(self):
        """Gets the pmt_index of this TpcGain.  # noqa: E501


        :return: The pmt_index of this TpcGain.  # noqa: E501
        :rtype: int
        """
        return self._pmt_index

    @pmt_index.setter
    def pmt_index(self, pmt_index):
        """Sets the pmt_index of this TpcGain.


        :param pmt_index: The pmt_index of this TpcGain.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and pmt_index is None:  # noqa: E501
            raise ValueError("Invalid value for `pmt_index`, must not be `None`")  # noqa: E501

        self._pmt_index = pmt_index

    @property
    def gain(self):
        """Gets the gain of this TpcGain.  # noqa: E501


        :return: The gain of this TpcGain.  # noqa: E501
        :rtype: float
        """
        return self._gain

    @gain.setter
    def gain(self, gain):
        """Sets the gain of this TpcGain.


        :param gain: The gain of this TpcGain.  # noqa: E501
        :type: float
        """
        if self.local_vars_configuration.client_side_validation and gain is None:  # noqa: E501
            raise ValueError("Invalid value for `gain`, must not be `None`")  # noqa: E501

        self._gain = gain

    @property
    def gain_err(self):
        """Gets the gain_err of this TpcGain.  # noqa: E501


        :return: The gain_err of this TpcGain.  # noqa: E501
        :rtype: float
        """
        return self._gain_err

    @gain_err.setter
    def gain_err(self, gain_err):
        """Sets the gain_err of this TpcGain.


        :param gain_err: The gain_err of this TpcGain.  # noqa: E501
        :type: float
        """

        self._gain_err = gain_err

    @property
    def gain_stat_err(self):
        """Gets the gain_stat_err of this TpcGain.  # noqa: E501


        :return: The gain_stat_err of this TpcGain.  # noqa: E501
        :rtype: float
        """
        return self._gain_stat_err

    @gain_stat_err.setter
    def gain_stat_err(self, gain_stat_err):
        """Sets the gain_stat_err of this TpcGain.


        :param gain_stat_err: The gain_stat_err of this TpcGain.  # noqa: E501
        :type: float
        """

        self._gain_stat_err = gain_stat_err

    @property
    def gain_sys_err(self):
        """Gets the gain_sys_err of this TpcGain.  # noqa: E501


        :return: The gain_sys_err of this TpcGain.  # noqa: E501
        :rtype: float
        """
        return self._gain_sys_err

    @gain_sys_err.setter
    def gain_sys_err(self, gain_sys_err):
        """Sets the gain_sys_err of this TpcGain.


        :param gain_sys_err: The gain_sys_err of this TpcGain.  # noqa: E501
        :type: float
        """

        self._gain_sys_err = gain_sys_err

    @property
    def voltage(self):
        """Gets the voltage of this TpcGain.  # noqa: E501


        :return: The voltage of this TpcGain.  # noqa: E501
        :rtype: float
        """
        return self._voltage

    @voltage.setter
    def voltage(self, voltage):
        """Sets the voltage of this TpcGain.


        :param voltage: The voltage of this TpcGain.  # noqa: E501
        :type: float
        """

        self._voltage = voltage

    @property
    def occupancy(self):
        """Gets the occupancy of this TpcGain.  # noqa: E501


        :return: The occupancy of this TpcGain.  # noqa: E501
        :rtype: float
        """
        return self._occupancy

    @occupancy.setter
    def occupancy(self, occupancy):
        """Sets the occupancy of this TpcGain.


        :param occupancy: The occupancy of this TpcGain.  # noqa: E501
        :type: float
        """

        self._occupancy = occupancy

    @property
    def occupancy_err(self):
        """Gets the occupancy_err of this TpcGain.  # noqa: E501


        :return: The occupancy_err of this TpcGain.  # noqa: E501
        :rtype: float
        """
        return self._occupancy_err

    @occupancy_err.setter
    def occupancy_err(self, occupancy_err):
        """Sets the occupancy_err of this TpcGain.


        :param occupancy_err: The occupancy_err of this TpcGain.  # noqa: E501
        :type: float
        """

        self._occupancy_err = occupancy_err

    @property
    def id(self):
        """Gets the id of this TpcGain.  # noqa: E501


        :return: The id of this TpcGain.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TpcGain.


        :param id: The id of this TpcGain.  # noqa: E501
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
        if not isinstance(other, TpcGain):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TpcGain):
            return True

        return self.to_dict() != other.to_dict()
