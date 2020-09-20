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


class NvetoGainModel(object):
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
        'gain_model': 'float',
        'gain_model_stat_err': 'float',
        'gain_model_err': 'float',
        'adctoe_gain_model': 'float',
        'adctoe_gain_model_err': 'float',
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
        'gain_model': 'gain_model',
        'gain_model_stat_err': 'gain_model_stat_err',
        'gain_model_err': 'gain_model_err',
        'adctoe_gain_model': 'adctoe_gain_model',
        'adctoe_gain_model_err': 'adctoe_gain_model_err',
        'id': '_id'
    }

    def __init__(self, detector='nveto', experiment='xenonnt', run_id=None, timestamp=None, pmt_index=None, gain=None, gain_err=None, gain_stat_err=None, gain_sys_err=None, voltage=None, gain_model=None, gain_model_stat_err=None, gain_model_err=None, adctoe_gain_model=None, adctoe_gain_model_err=None, id=None, local_vars_configuration=None):  # noqa: E501
        """NvetoGainModel - a model defined in OpenAPI"""  # noqa: E501
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
        self._gain_model = None
        self._gain_model_stat_err = None
        self._gain_model_err = None
        self._adctoe_gain_model = None
        self._adctoe_gain_model_err = None
        self._id = None
        self.discriminator = None

        self.detector = detector
        self.experiment = experiment
        self.run_id = run_id
        if timestamp is not None:
            self.timestamp = timestamp
        self.pmt_index = pmt_index
        self.gain = gain
        self.gain_err = gain_err
        if gain_stat_err is not None:
            self.gain_stat_err = gain_stat_err
        if gain_sys_err is not None:
            self.gain_sys_err = gain_sys_err
        if voltage is not None:
            self.voltage = voltage
        if gain_model is not None:
            self.gain_model = gain_model
        if gain_model_stat_err is not None:
            self.gain_model_stat_err = gain_model_stat_err
        if gain_model_err is not None:
            self.gain_model_err = gain_model_err
        if adctoe_gain_model is not None:
            self.adctoe_gain_model = adctoe_gain_model
        if adctoe_gain_model_err is not None:
            self.adctoe_gain_model_err = adctoe_gain_model_err
        if id is not None:
            self.id = id

    @property
    def detector(self):
        """Gets the detector of this NvetoGainModel.  # noqa: E501


        :return: The detector of this NvetoGainModel.  # noqa: E501
        :rtype: str
        """
        return self._detector

    @detector.setter
    def detector(self, detector):
        """Sets the detector of this NvetoGainModel.


        :param detector: The detector of this NvetoGainModel.  # noqa: E501
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
        """Gets the experiment of this NvetoGainModel.  # noqa: E501


        :return: The experiment of this NvetoGainModel.  # noqa: E501
        :rtype: str
        """
        return self._experiment

    @experiment.setter
    def experiment(self, experiment):
        """Sets the experiment of this NvetoGainModel.


        :param experiment: The experiment of this NvetoGainModel.  # noqa: E501
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
        """Gets the run_id of this NvetoGainModel.  # noqa: E501


        :return: The run_id of this NvetoGainModel.  # noqa: E501
        :rtype: str
        """
        return self._run_id

    @run_id.setter
    def run_id(self, run_id):
        """Sets the run_id of this NvetoGainModel.


        :param run_id: The run_id of this NvetoGainModel.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and run_id is None:  # noqa: E501
            raise ValueError("Invalid value for `run_id`, must not be `None`")  # noqa: E501

        self._run_id = run_id

    @property
    def timestamp(self):
        """Gets the timestamp of this NvetoGainModel.  # noqa: E501


        :return: The timestamp of this NvetoGainModel.  # noqa: E501
        :rtype: int
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this NvetoGainModel.


        :param timestamp: The timestamp of this NvetoGainModel.  # noqa: E501
        :type: int
        """

        self._timestamp = timestamp

    @property
    def pmt_index(self):
        """Gets the pmt_index of this NvetoGainModel.  # noqa: E501


        :return: The pmt_index of this NvetoGainModel.  # noqa: E501
        :rtype: int
        """
        return self._pmt_index

    @pmt_index.setter
    def pmt_index(self, pmt_index):
        """Sets the pmt_index of this NvetoGainModel.


        :param pmt_index: The pmt_index of this NvetoGainModel.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and pmt_index is None:  # noqa: E501
            raise ValueError("Invalid value for `pmt_index`, must not be `None`")  # noqa: E501

        self._pmt_index = pmt_index

    @property
    def gain(self):
        """Gets the gain of this NvetoGainModel.  # noqa: E501


        :return: The gain of this NvetoGainModel.  # noqa: E501
        :rtype: float
        """
        return self._gain

    @gain.setter
    def gain(self, gain):
        """Sets the gain of this NvetoGainModel.


        :param gain: The gain of this NvetoGainModel.  # noqa: E501
        :type: float
        """
        if self.local_vars_configuration.client_side_validation and gain is None:  # noqa: E501
            raise ValueError("Invalid value for `gain`, must not be `None`")  # noqa: E501

        self._gain = gain

    @property
    def gain_err(self):
        """Gets the gain_err of this NvetoGainModel.  # noqa: E501


        :return: The gain_err of this NvetoGainModel.  # noqa: E501
        :rtype: float
        """
        return self._gain_err

    @gain_err.setter
    def gain_err(self, gain_err):
        """Sets the gain_err of this NvetoGainModel.


        :param gain_err: The gain_err of this NvetoGainModel.  # noqa: E501
        :type: float
        """
        if self.local_vars_configuration.client_side_validation and gain_err is None:  # noqa: E501
            raise ValueError("Invalid value for `gain_err`, must not be `None`")  # noqa: E501

        self._gain_err = gain_err

    @property
    def gain_stat_err(self):
        """Gets the gain_stat_err of this NvetoGainModel.  # noqa: E501


        :return: The gain_stat_err of this NvetoGainModel.  # noqa: E501
        :rtype: float
        """
        return self._gain_stat_err

    @gain_stat_err.setter
    def gain_stat_err(self, gain_stat_err):
        """Sets the gain_stat_err of this NvetoGainModel.


        :param gain_stat_err: The gain_stat_err of this NvetoGainModel.  # noqa: E501
        :type: float
        """

        self._gain_stat_err = gain_stat_err

    @property
    def gain_sys_err(self):
        """Gets the gain_sys_err of this NvetoGainModel.  # noqa: E501


        :return: The gain_sys_err of this NvetoGainModel.  # noqa: E501
        :rtype: float
        """
        return self._gain_sys_err

    @gain_sys_err.setter
    def gain_sys_err(self, gain_sys_err):
        """Sets the gain_sys_err of this NvetoGainModel.


        :param gain_sys_err: The gain_sys_err of this NvetoGainModel.  # noqa: E501
        :type: float
        """

        self._gain_sys_err = gain_sys_err

    @property
    def voltage(self):
        """Gets the voltage of this NvetoGainModel.  # noqa: E501


        :return: The voltage of this NvetoGainModel.  # noqa: E501
        :rtype: float
        """
        return self._voltage

    @voltage.setter
    def voltage(self, voltage):
        """Sets the voltage of this NvetoGainModel.


        :param voltage: The voltage of this NvetoGainModel.  # noqa: E501
        :type: float
        """

        self._voltage = voltage

    @property
    def gain_model(self):
        """Gets the gain_model of this NvetoGainModel.  # noqa: E501


        :return: The gain_model of this NvetoGainModel.  # noqa: E501
        :rtype: float
        """
        return self._gain_model

    @gain_model.setter
    def gain_model(self, gain_model):
        """Sets the gain_model of this NvetoGainModel.


        :param gain_model: The gain_model of this NvetoGainModel.  # noqa: E501
        :type: float
        """

        self._gain_model = gain_model

    @property
    def gain_model_stat_err(self):
        """Gets the gain_model_stat_err of this NvetoGainModel.  # noqa: E501


        :return: The gain_model_stat_err of this NvetoGainModel.  # noqa: E501
        :rtype: float
        """
        return self._gain_model_stat_err

    @gain_model_stat_err.setter
    def gain_model_stat_err(self, gain_model_stat_err):
        """Sets the gain_model_stat_err of this NvetoGainModel.


        :param gain_model_stat_err: The gain_model_stat_err of this NvetoGainModel.  # noqa: E501
        :type: float
        """

        self._gain_model_stat_err = gain_model_stat_err

    @property
    def gain_model_err(self):
        """Gets the gain_model_err of this NvetoGainModel.  # noqa: E501


        :return: The gain_model_err of this NvetoGainModel.  # noqa: E501
        :rtype: float
        """
        return self._gain_model_err

    @gain_model_err.setter
    def gain_model_err(self, gain_model_err):
        """Sets the gain_model_err of this NvetoGainModel.


        :param gain_model_err: The gain_model_err of this NvetoGainModel.  # noqa: E501
        :type: float
        """

        self._gain_model_err = gain_model_err

    @property
    def adctoe_gain_model(self):
        """Gets the adctoe_gain_model of this NvetoGainModel.  # noqa: E501


        :return: The adctoe_gain_model of this NvetoGainModel.  # noqa: E501
        :rtype: float
        """
        return self._adctoe_gain_model

    @adctoe_gain_model.setter
    def adctoe_gain_model(self, adctoe_gain_model):
        """Sets the adctoe_gain_model of this NvetoGainModel.


        :param adctoe_gain_model: The adctoe_gain_model of this NvetoGainModel.  # noqa: E501
        :type: float
        """

        self._adctoe_gain_model = adctoe_gain_model

    @property
    def adctoe_gain_model_err(self):
        """Gets the adctoe_gain_model_err of this NvetoGainModel.  # noqa: E501


        :return: The adctoe_gain_model_err of this NvetoGainModel.  # noqa: E501
        :rtype: float
        """
        return self._adctoe_gain_model_err

    @adctoe_gain_model_err.setter
    def adctoe_gain_model_err(self, adctoe_gain_model_err):
        """Sets the adctoe_gain_model_err of this NvetoGainModel.


        :param adctoe_gain_model_err: The adctoe_gain_model_err of this NvetoGainModel.  # noqa: E501
        :type: float
        """

        self._adctoe_gain_model_err = adctoe_gain_model_err

    @property
    def id(self):
        """Gets the id of this NvetoGainModel.  # noqa: E501


        :return: The id of this NvetoGainModel.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this NvetoGainModel.


        :param id: The id of this NvetoGainModel.  # noqa: E501
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
        if not isinstance(other, NvetoGainModel):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, NvetoGainModel):
            return True

        return self.to_dict() != other.to_dict()
