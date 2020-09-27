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


class TpcAfterpulse1t(object):
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
        'experiment': 'str',
        'detector': 'str',
        'pmt_index': 'int',
        'run_id': 'str',
        'timestamp': 'int',
        'start_time': 'int',
        'end_time': 'int',
        'trigger_sigma': 'float',
        'total_ap': 'float',
        'pe': 'float',
        'pe_error': 'float',
        'ar_pos': 'float',
        'hv': 'float',
        'ne_ap': 'float',
        'ne_pos': 'float',
        'xe_pos': 'float',
        'n2_pos': 'float',
        'ch4ap': 'float',
        'he_ap': 'float',
        'ar_ap': 'float',
        'doublexe_pos': 'float',
        'doublexe_ap': 'float',
        'trigger_mean': 'float',
        'gain': 'float',
        'ch4_pos': 'float',
        'n2_ap': 'float',
        'xe_ap': 'float',
        'pe_pulses': 'float',
        'trigger_number': 'float',
        'id': 'str'
    }

    attribute_map = {
        'experiment': 'experiment',
        'detector': 'detector',
        'pmt_index': 'pmt_index',
        'run_id': 'run_id',
        'timestamp': 'timestamp',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'trigger_sigma': 'trigger_sigma',
        'total_ap': 'total_ap',
        'pe': 'pe',
        'pe_error': 'pe_error',
        'ar_pos': 'ar_pos',
        'hv': 'hv',
        'ne_ap': 'ne_ap',
        'ne_pos': 'ne_pos',
        'xe_pos': 'xe_pos',
        'n2_pos': 'n2_pos',
        'ch4ap': 'ch4ap',
        'he_ap': 'he_ap',
        'ar_ap': 'ar_ap',
        'doublexe_pos': 'doublexe_pos',
        'doublexe_ap': 'doublexe_ap',
        'trigger_mean': 'trigger_mean',
        'gain': 'gain',
        'ch4_pos': 'ch4_pos',
        'n2_ap': 'n2_ap',
        'xe_ap': 'xe_ap',
        'pe_pulses': 'pe_pulses',
        'trigger_number': 'trigger_number',
        'id': '_id'
    }

    def __init__(self, experiment='xenon1t', detector='tpc', pmt_index=None, run_id=None, timestamp=None, start_time=None, end_time=None, trigger_sigma=None, total_ap=None, pe=None, pe_error=None, ar_pos=None, hv=None, ne_ap=None, ne_pos=None, xe_pos=None, n2_pos=None, ch4ap=None, he_ap=None, ar_ap=None, doublexe_pos=None, doublexe_ap=None, trigger_mean=None, gain=None, ch4_pos=None, n2_ap=None, xe_ap=None, pe_pulses=None, trigger_number=None, id=None, local_vars_configuration=None):  # noqa: E501
        """TpcAfterpulse1t - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._experiment = None
        self._detector = None
        self._pmt_index = None
        self._run_id = None
        self._timestamp = None
        self._start_time = None
        self._end_time = None
        self._trigger_sigma = None
        self._total_ap = None
        self._pe = None
        self._pe_error = None
        self._ar_pos = None
        self._hv = None
        self._ne_ap = None
        self._ne_pos = None
        self._xe_pos = None
        self._n2_pos = None
        self._ch4ap = None
        self._he_ap = None
        self._ar_ap = None
        self._doublexe_pos = None
        self._doublexe_ap = None
        self._trigger_mean = None
        self._gain = None
        self._ch4_pos = None
        self._n2_ap = None
        self._xe_ap = None
        self._pe_pulses = None
        self._trigger_number = None
        self._id = None
        self.discriminator = None

        self.experiment = experiment
        self.detector = detector
        self.pmt_index = pmt_index
        if run_id is not None:
            self.run_id = run_id
        if timestamp is not None:
            self.timestamp = timestamp
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if trigger_sigma is not None:
            self.trigger_sigma = trigger_sigma
        if total_ap is not None:
            self.total_ap = total_ap
        if pe is not None:
            self.pe = pe
        if pe_error is not None:
            self.pe_error = pe_error
        if ar_pos is not None:
            self.ar_pos = ar_pos
        if hv is not None:
            self.hv = hv
        if ne_ap is not None:
            self.ne_ap = ne_ap
        if ne_pos is not None:
            self.ne_pos = ne_pos
        if xe_pos is not None:
            self.xe_pos = xe_pos
        if n2_pos is not None:
            self.n2_pos = n2_pos
        if ch4ap is not None:
            self.ch4ap = ch4ap
        if he_ap is not None:
            self.he_ap = he_ap
        if ar_ap is not None:
            self.ar_ap = ar_ap
        if doublexe_pos is not None:
            self.doublexe_pos = doublexe_pos
        if doublexe_ap is not None:
            self.doublexe_ap = doublexe_ap
        if trigger_mean is not None:
            self.trigger_mean = trigger_mean
        if gain is not None:
            self.gain = gain
        if ch4_pos is not None:
            self.ch4_pos = ch4_pos
        if n2_ap is not None:
            self.n2_ap = n2_ap
        if xe_ap is not None:
            self.xe_ap = xe_ap
        if pe_pulses is not None:
            self.pe_pulses = pe_pulses
        if trigger_number is not None:
            self.trigger_number = trigger_number
        if id is not None:
            self.id = id

    @property
    def experiment(self):
        """Gets the experiment of this TpcAfterpulse1t.  # noqa: E501


        :return: The experiment of this TpcAfterpulse1t.  # noqa: E501
        :rtype: str
        """
        return self._experiment

    @experiment.setter
    def experiment(self, experiment):
        """Sets the experiment of this TpcAfterpulse1t.


        :param experiment: The experiment of this TpcAfterpulse1t.  # noqa: E501
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
        """Gets the detector of this TpcAfterpulse1t.  # noqa: E501


        :return: The detector of this TpcAfterpulse1t.  # noqa: E501
        :rtype: str
        """
        return self._detector

    @detector.setter
    def detector(self, detector):
        """Sets the detector of this TpcAfterpulse1t.


        :param detector: The detector of this TpcAfterpulse1t.  # noqa: E501
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
    def pmt_index(self):
        """Gets the pmt_index of this TpcAfterpulse1t.  # noqa: E501


        :return: The pmt_index of this TpcAfterpulse1t.  # noqa: E501
        :rtype: int
        """
        return self._pmt_index

    @pmt_index.setter
    def pmt_index(self, pmt_index):
        """Sets the pmt_index of this TpcAfterpulse1t.


        :param pmt_index: The pmt_index of this TpcAfterpulse1t.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and pmt_index is None:  # noqa: E501
            raise ValueError("Invalid value for `pmt_index`, must not be `None`")  # noqa: E501

        self._pmt_index = pmt_index

    @property
    def run_id(self):
        """Gets the run_id of this TpcAfterpulse1t.  # noqa: E501


        :return: The run_id of this TpcAfterpulse1t.  # noqa: E501
        :rtype: str
        """
        return self._run_id

    @run_id.setter
    def run_id(self, run_id):
        """Sets the run_id of this TpcAfterpulse1t.


        :param run_id: The run_id of this TpcAfterpulse1t.  # noqa: E501
        :type: str
        """

        self._run_id = run_id

    @property
    def timestamp(self):
        """Gets the timestamp of this TpcAfterpulse1t.  # noqa: E501


        :return: The timestamp of this TpcAfterpulse1t.  # noqa: E501
        :rtype: int
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this TpcAfterpulse1t.


        :param timestamp: The timestamp of this TpcAfterpulse1t.  # noqa: E501
        :type: int
        """

        self._timestamp = timestamp

    @property
    def start_time(self):
        """Gets the start_time of this TpcAfterpulse1t.  # noqa: E501


        :return: The start_time of this TpcAfterpulse1t.  # noqa: E501
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this TpcAfterpulse1t.


        :param start_time: The start_time of this TpcAfterpulse1t.  # noqa: E501
        :type: int
        """

        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this TpcAfterpulse1t.  # noqa: E501


        :return: The end_time of this TpcAfterpulse1t.  # noqa: E501
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this TpcAfterpulse1t.


        :param end_time: The end_time of this TpcAfterpulse1t.  # noqa: E501
        :type: int
        """

        self._end_time = end_time

    @property
    def trigger_sigma(self):
        """Gets the trigger_sigma of this TpcAfterpulse1t.  # noqa: E501


        :return: The trigger_sigma of this TpcAfterpulse1t.  # noqa: E501
        :rtype: float
        """
        return self._trigger_sigma

    @trigger_sigma.setter
    def trigger_sigma(self, trigger_sigma):
        """Sets the trigger_sigma of this TpcAfterpulse1t.


        :param trigger_sigma: The trigger_sigma of this TpcAfterpulse1t.  # noqa: E501
        :type: float
        """

        self._trigger_sigma = trigger_sigma

    @property
    def total_ap(self):
        """Gets the total_ap of this TpcAfterpulse1t.  # noqa: E501


        :return: The total_ap of this TpcAfterpulse1t.  # noqa: E501
        :rtype: float
        """
        return self._total_ap

    @total_ap.setter
    def total_ap(self, total_ap):
        """Sets the total_ap of this TpcAfterpulse1t.


        :param total_ap: The total_ap of this TpcAfterpulse1t.  # noqa: E501
        :type: float
        """

        self._total_ap = total_ap

    @property
    def pe(self):
        """Gets the pe of this TpcAfterpulse1t.  # noqa: E501


        :return: The pe of this TpcAfterpulse1t.  # noqa: E501
        :rtype: float
        """
        return self._pe

    @pe.setter
    def pe(self, pe):
        """Sets the pe of this TpcAfterpulse1t.


        :param pe: The pe of this TpcAfterpulse1t.  # noqa: E501
        :type: float
        """

        self._pe = pe

    @property
    def pe_error(self):
        """Gets the pe_error of this TpcAfterpulse1t.  # noqa: E501


        :return: The pe_error of this TpcAfterpulse1t.  # noqa: E501
        :rtype: float
        """
        return self._pe_error

    @pe_error.setter
    def pe_error(self, pe_error):
        """Sets the pe_error of this TpcAfterpulse1t.


        :param pe_error: The pe_error of this TpcAfterpulse1t.  # noqa: E501
        :type: float
        """

        self._pe_error = pe_error

    @property
    def ar_pos(self):
        """Gets the ar_pos of this TpcAfterpulse1t.  # noqa: E501


        :return: The ar_pos of this TpcAfterpulse1t.  # noqa: E501
        :rtype: float
        """
        return self._ar_pos

    @ar_pos.setter
    def ar_pos(self, ar_pos):
        """Sets the ar_pos of this TpcAfterpulse1t.


        :param ar_pos: The ar_pos of this TpcAfterpulse1t.  # noqa: E501
        :type: float
        """

        self._ar_pos = ar_pos

    @property
    def hv(self):
        """Gets the hv of this TpcAfterpulse1t.  # noqa: E501


        :return: The hv of this TpcAfterpulse1t.  # noqa: E501
        :rtype: float
        """
        return self._hv

    @hv.setter
    def hv(self, hv):
        """Sets the hv of this TpcAfterpulse1t.


        :param hv: The hv of this TpcAfterpulse1t.  # noqa: E501
        :type: float
        """

        self._hv = hv

    @property
    def ne_ap(self):
        """Gets the ne_ap of this TpcAfterpulse1t.  # noqa: E501


        :return: The ne_ap of this TpcAfterpulse1t.  # noqa: E501
        :rtype: float
        """
        return self._ne_ap

    @ne_ap.setter
    def ne_ap(self, ne_ap):
        """Sets the ne_ap of this TpcAfterpulse1t.


        :param ne_ap: The ne_ap of this TpcAfterpulse1t.  # noqa: E501
        :type: float
        """

        self._ne_ap = ne_ap

    @property
    def ne_pos(self):
        """Gets the ne_pos of this TpcAfterpulse1t.  # noqa: E501


        :return: The ne_pos of this TpcAfterpulse1t.  # noqa: E501
        :rtype: float
        """
        return self._ne_pos

    @ne_pos.setter
    def ne_pos(self, ne_pos):
        """Sets the ne_pos of this TpcAfterpulse1t.


        :param ne_pos: The ne_pos of this TpcAfterpulse1t.  # noqa: E501
        :type: float
        """

        self._ne_pos = ne_pos

    @property
    def xe_pos(self):
        """Gets the xe_pos of this TpcAfterpulse1t.  # noqa: E501


        :return: The xe_pos of this TpcAfterpulse1t.  # noqa: E501
        :rtype: float
        """
        return self._xe_pos

    @xe_pos.setter
    def xe_pos(self, xe_pos):
        """Sets the xe_pos of this TpcAfterpulse1t.


        :param xe_pos: The xe_pos of this TpcAfterpulse1t.  # noqa: E501
        :type: float
        """

        self._xe_pos = xe_pos

    @property
    def n2_pos(self):
        """Gets the n2_pos of this TpcAfterpulse1t.  # noqa: E501


        :return: The n2_pos of this TpcAfterpulse1t.  # noqa: E501
        :rtype: float
        """
        return self._n2_pos

    @n2_pos.setter
    def n2_pos(self, n2_pos):
        """Sets the n2_pos of this TpcAfterpulse1t.


        :param n2_pos: The n2_pos of this TpcAfterpulse1t.  # noqa: E501
        :type: float
        """

        self._n2_pos = n2_pos

    @property
    def ch4ap(self):
        """Gets the ch4ap of this TpcAfterpulse1t.  # noqa: E501


        :return: The ch4ap of this TpcAfterpulse1t.  # noqa: E501
        :rtype: float
        """
        return self._ch4ap

    @ch4ap.setter
    def ch4ap(self, ch4ap):
        """Sets the ch4ap of this TpcAfterpulse1t.


        :param ch4ap: The ch4ap of this TpcAfterpulse1t.  # noqa: E501
        :type: float
        """

        self._ch4ap = ch4ap

    @property
    def he_ap(self):
        """Gets the he_ap of this TpcAfterpulse1t.  # noqa: E501


        :return: The he_ap of this TpcAfterpulse1t.  # noqa: E501
        :rtype: float
        """
        return self._he_ap

    @he_ap.setter
    def he_ap(self, he_ap):
        """Sets the he_ap of this TpcAfterpulse1t.


        :param he_ap: The he_ap of this TpcAfterpulse1t.  # noqa: E501
        :type: float
        """

        self._he_ap = he_ap

    @property
    def ar_ap(self):
        """Gets the ar_ap of this TpcAfterpulse1t.  # noqa: E501


        :return: The ar_ap of this TpcAfterpulse1t.  # noqa: E501
        :rtype: float
        """
        return self._ar_ap

    @ar_ap.setter
    def ar_ap(self, ar_ap):
        """Sets the ar_ap of this TpcAfterpulse1t.


        :param ar_ap: The ar_ap of this TpcAfterpulse1t.  # noqa: E501
        :type: float
        """

        self._ar_ap = ar_ap

    @property
    def doublexe_pos(self):
        """Gets the doublexe_pos of this TpcAfterpulse1t.  # noqa: E501


        :return: The doublexe_pos of this TpcAfterpulse1t.  # noqa: E501
        :rtype: float
        """
        return self._doublexe_pos

    @doublexe_pos.setter
    def doublexe_pos(self, doublexe_pos):
        """Sets the doublexe_pos of this TpcAfterpulse1t.


        :param doublexe_pos: The doublexe_pos of this TpcAfterpulse1t.  # noqa: E501
        :type: float
        """

        self._doublexe_pos = doublexe_pos

    @property
    def doublexe_ap(self):
        """Gets the doublexe_ap of this TpcAfterpulse1t.  # noqa: E501


        :return: The doublexe_ap of this TpcAfterpulse1t.  # noqa: E501
        :rtype: float
        """
        return self._doublexe_ap

    @doublexe_ap.setter
    def doublexe_ap(self, doublexe_ap):
        """Sets the doublexe_ap of this TpcAfterpulse1t.


        :param doublexe_ap: The doublexe_ap of this TpcAfterpulse1t.  # noqa: E501
        :type: float
        """

        self._doublexe_ap = doublexe_ap

    @property
    def trigger_mean(self):
        """Gets the trigger_mean of this TpcAfterpulse1t.  # noqa: E501


        :return: The trigger_mean of this TpcAfterpulse1t.  # noqa: E501
        :rtype: float
        """
        return self._trigger_mean

    @trigger_mean.setter
    def trigger_mean(self, trigger_mean):
        """Sets the trigger_mean of this TpcAfterpulse1t.


        :param trigger_mean: The trigger_mean of this TpcAfterpulse1t.  # noqa: E501
        :type: float
        """

        self._trigger_mean = trigger_mean

    @property
    def gain(self):
        """Gets the gain of this TpcAfterpulse1t.  # noqa: E501


        :return: The gain of this TpcAfterpulse1t.  # noqa: E501
        :rtype: float
        """
        return self._gain

    @gain.setter
    def gain(self, gain):
        """Sets the gain of this TpcAfterpulse1t.


        :param gain: The gain of this TpcAfterpulse1t.  # noqa: E501
        :type: float
        """

        self._gain = gain

    @property
    def ch4_pos(self):
        """Gets the ch4_pos of this TpcAfterpulse1t.  # noqa: E501


        :return: The ch4_pos of this TpcAfterpulse1t.  # noqa: E501
        :rtype: float
        """
        return self._ch4_pos

    @ch4_pos.setter
    def ch4_pos(self, ch4_pos):
        """Sets the ch4_pos of this TpcAfterpulse1t.


        :param ch4_pos: The ch4_pos of this TpcAfterpulse1t.  # noqa: E501
        :type: float
        """

        self._ch4_pos = ch4_pos

    @property
    def n2_ap(self):
        """Gets the n2_ap of this TpcAfterpulse1t.  # noqa: E501


        :return: The n2_ap of this TpcAfterpulse1t.  # noqa: E501
        :rtype: float
        """
        return self._n2_ap

    @n2_ap.setter
    def n2_ap(self, n2_ap):
        """Sets the n2_ap of this TpcAfterpulse1t.


        :param n2_ap: The n2_ap of this TpcAfterpulse1t.  # noqa: E501
        :type: float
        """

        self._n2_ap = n2_ap

    @property
    def xe_ap(self):
        """Gets the xe_ap of this TpcAfterpulse1t.  # noqa: E501


        :return: The xe_ap of this TpcAfterpulse1t.  # noqa: E501
        :rtype: float
        """
        return self._xe_ap

    @xe_ap.setter
    def xe_ap(self, xe_ap):
        """Sets the xe_ap of this TpcAfterpulse1t.


        :param xe_ap: The xe_ap of this TpcAfterpulse1t.  # noqa: E501
        :type: float
        """

        self._xe_ap = xe_ap

    @property
    def pe_pulses(self):
        """Gets the pe_pulses of this TpcAfterpulse1t.  # noqa: E501


        :return: The pe_pulses of this TpcAfterpulse1t.  # noqa: E501
        :rtype: float
        """
        return self._pe_pulses

    @pe_pulses.setter
    def pe_pulses(self, pe_pulses):
        """Sets the pe_pulses of this TpcAfterpulse1t.


        :param pe_pulses: The pe_pulses of this TpcAfterpulse1t.  # noqa: E501
        :type: float
        """

        self._pe_pulses = pe_pulses

    @property
    def trigger_number(self):
        """Gets the trigger_number of this TpcAfterpulse1t.  # noqa: E501


        :return: The trigger_number of this TpcAfterpulse1t.  # noqa: E501
        :rtype: float
        """
        return self._trigger_number

    @trigger_number.setter
    def trigger_number(self, trigger_number):
        """Sets the trigger_number of this TpcAfterpulse1t.


        :param trigger_number: The trigger_number of this TpcAfterpulse1t.  # noqa: E501
        :type: float
        """

        self._trigger_number = trigger_number

    @property
    def id(self):
        """Gets the id of this TpcAfterpulse1t.  # noqa: E501


        :return: The id of this TpcAfterpulse1t.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TpcAfterpulse1t.


        :param id: The id of this TpcAfterpulse1t.  # noqa: E501
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
        if not isinstance(other, TpcAfterpulse1t):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TpcAfterpulse1t):
            return True

        return self.to_dict() != other.to_dict()
