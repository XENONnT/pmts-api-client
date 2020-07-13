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


class TpcInstall1t(object):
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
        'uid': 'str',
        'array': 'str',
        'detector': 'str',
        'experiment': 'str',
        'pmt_index': 'int',
        'sector': 'int',
        'position_x': 'float',
        'position_y': 'float',
        'position_z': 'float',
        'position_r': 'float',
        'amplifier_crate': 'int',
        'amplifier_fan': 'int',
        'amplifier_plug': 'int',
        'amplifier_serial': 'int',
        'amplifier_slot': 'int',
        'amplifier_channel': 'int',
        'digitizer_channel': 'int',
        'digitizer_crate': 'int',
        'digitizer_module': 'int',
        'digitizer_slot': 'int',
        'high_voltage_crate': 'int',
        'high_voltage_board': 'int',
        'high_voltage_channel': 'int',
        'high_voltage_connector': 'int',
        'high_voltage_feedthrough': 'str',
        'high_voltage_return': 'int',
        'serial_number': 'str',
        'signal_channel': 'int',
        'signal_connector': 'int',
        'signal_feedthrough': 'str',
        'id': 'str'
    }

    attribute_map = {
        'uid': 'uid',
        'array': 'array',
        'detector': 'detector',
        'experiment': 'experiment',
        'pmt_index': 'pmt_index',
        'sector': 'sector',
        'position_x': 'position_x',
        'position_y': 'position_y',
        'position_z': 'position_z',
        'position_r': 'position_r',
        'amplifier_crate': 'amplifier_crate',
        'amplifier_fan': 'amplifier_fan',
        'amplifier_plug': 'amplifier_plug',
        'amplifier_serial': 'amplifier_serial',
        'amplifier_slot': 'amplifier_slot',
        'amplifier_channel': 'amplifier_channel',
        'digitizer_channel': 'digitizer_channel',
        'digitizer_crate': 'digitizer_crate',
        'digitizer_module': 'digitizer_module',
        'digitizer_slot': 'digitizer_slot',
        'high_voltage_crate': 'high_voltage_crate',
        'high_voltage_board': 'high_voltage_board',
        'high_voltage_channel': 'high_voltage_channel',
        'high_voltage_connector': 'high_voltage_connector',
        'high_voltage_feedthrough': 'high_voltage_feedthrough',
        'high_voltage_return': 'high_voltage_return',
        'serial_number': 'serial_number',
        'signal_channel': 'signal_channel',
        'signal_connector': 'signal_connector',
        'signal_feedthrough': 'signal_feedthrough',
        'id': '_id'
    }

    def __init__(self, uid=None, array=None, detector='tpc', experiment='xenon1t', pmt_index=None, sector=None, position_x=None, position_y=None, position_z=None, position_r=None, amplifier_crate=None, amplifier_fan=None, amplifier_plug=None, amplifier_serial=None, amplifier_slot=None, amplifier_channel=None, digitizer_channel=None, digitizer_crate=None, digitizer_module=None, digitizer_slot=None, high_voltage_crate=None, high_voltage_board=None, high_voltage_channel=None, high_voltage_connector=None, high_voltage_feedthrough=None, high_voltage_return=None, serial_number=None, signal_channel=None, signal_connector=None, signal_feedthrough=None, id=None, local_vars_configuration=None):  # noqa: E501
        """TpcInstall1t - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._uid = None
        self._array = None
        self._detector = None
        self._experiment = None
        self._pmt_index = None
        self._sector = None
        self._position_x = None
        self._position_y = None
        self._position_z = None
        self._position_r = None
        self._amplifier_crate = None
        self._amplifier_fan = None
        self._amplifier_plug = None
        self._amplifier_serial = None
        self._amplifier_slot = None
        self._amplifier_channel = None
        self._digitizer_channel = None
        self._digitizer_crate = None
        self._digitizer_module = None
        self._digitizer_slot = None
        self._high_voltage_crate = None
        self._high_voltage_board = None
        self._high_voltage_channel = None
        self._high_voltage_connector = None
        self._high_voltage_feedthrough = None
        self._high_voltage_return = None
        self._serial_number = None
        self._signal_channel = None
        self._signal_connector = None
        self._signal_feedthrough = None
        self._id = None
        self.discriminator = None

        self.uid = uid
        if array is not None:
            self.array = array
        self.detector = detector
        self.experiment = experiment
        self.pmt_index = pmt_index
        if sector is not None:
            self.sector = sector
        if position_x is not None:
            self.position_x = position_x
        if position_y is not None:
            self.position_y = position_y
        if position_z is not None:
            self.position_z = position_z
        if position_r is not None:
            self.position_r = position_r
        if amplifier_crate is not None:
            self.amplifier_crate = amplifier_crate
        if amplifier_fan is not None:
            self.amplifier_fan = amplifier_fan
        if amplifier_plug is not None:
            self.amplifier_plug = amplifier_plug
        if amplifier_serial is not None:
            self.amplifier_serial = amplifier_serial
        if amplifier_slot is not None:
            self.amplifier_slot = amplifier_slot
        if amplifier_channel is not None:
            self.amplifier_channel = amplifier_channel
        if digitizer_channel is not None:
            self.digitizer_channel = digitizer_channel
        if digitizer_crate is not None:
            self.digitizer_crate = digitizer_crate
        if digitizer_module is not None:
            self.digitizer_module = digitizer_module
        if digitizer_slot is not None:
            self.digitizer_slot = digitizer_slot
        if high_voltage_crate is not None:
            self.high_voltage_crate = high_voltage_crate
        if high_voltage_board is not None:
            self.high_voltage_board = high_voltage_board
        if high_voltage_channel is not None:
            self.high_voltage_channel = high_voltage_channel
        if high_voltage_connector is not None:
            self.high_voltage_connector = high_voltage_connector
        if high_voltage_feedthrough is not None:
            self.high_voltage_feedthrough = high_voltage_feedthrough
        if high_voltage_return is not None:
            self.high_voltage_return = high_voltage_return
        if serial_number is not None:
            self.serial_number = serial_number
        if signal_channel is not None:
            self.signal_channel = signal_channel
        if signal_connector is not None:
            self.signal_connector = signal_connector
        if signal_feedthrough is not None:
            self.signal_feedthrough = signal_feedthrough
        if id is not None:
            self.id = id

    @property
    def uid(self):
        """Gets the uid of this TpcInstall1t.  # noqa: E501


        :return: The uid of this TpcInstall1t.  # noqa: E501
        :rtype: str
        """
        return self._uid

    @uid.setter
    def uid(self, uid):
        """Sets the uid of this TpcInstall1t.


        :param uid: The uid of this TpcInstall1t.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and uid is None:  # noqa: E501
            raise ValueError("Invalid value for `uid`, must not be `None`")  # noqa: E501

        self._uid = uid

    @property
    def array(self):
        """Gets the array of this TpcInstall1t.  # noqa: E501


        :return: The array of this TpcInstall1t.  # noqa: E501
        :rtype: str
        """
        return self._array

    @array.setter
    def array(self, array):
        """Sets the array of this TpcInstall1t.


        :param array: The array of this TpcInstall1t.  # noqa: E501
        :type: str
        """

        self._array = array

    @property
    def detector(self):
        """Gets the detector of this TpcInstall1t.  # noqa: E501


        :return: The detector of this TpcInstall1t.  # noqa: E501
        :rtype: str
        """
        return self._detector

    @detector.setter
    def detector(self, detector):
        """Sets the detector of this TpcInstall1t.


        :param detector: The detector of this TpcInstall1t.  # noqa: E501
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
        """Gets the experiment of this TpcInstall1t.  # noqa: E501


        :return: The experiment of this TpcInstall1t.  # noqa: E501
        :rtype: str
        """
        return self._experiment

    @experiment.setter
    def experiment(self, experiment):
        """Sets the experiment of this TpcInstall1t.


        :param experiment: The experiment of this TpcInstall1t.  # noqa: E501
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
    def pmt_index(self):
        """Gets the pmt_index of this TpcInstall1t.  # noqa: E501


        :return: The pmt_index of this TpcInstall1t.  # noqa: E501
        :rtype: int
        """
        return self._pmt_index

    @pmt_index.setter
    def pmt_index(self, pmt_index):
        """Sets the pmt_index of this TpcInstall1t.


        :param pmt_index: The pmt_index of this TpcInstall1t.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and pmt_index is None:  # noqa: E501
            raise ValueError("Invalid value for `pmt_index`, must not be `None`")  # noqa: E501

        self._pmt_index = pmt_index

    @property
    def sector(self):
        """Gets the sector of this TpcInstall1t.  # noqa: E501


        :return: The sector of this TpcInstall1t.  # noqa: E501
        :rtype: int
        """
        return self._sector

    @sector.setter
    def sector(self, sector):
        """Sets the sector of this TpcInstall1t.


        :param sector: The sector of this TpcInstall1t.  # noqa: E501
        :type: int
        """

        self._sector = sector

    @property
    def position_x(self):
        """Gets the position_x of this TpcInstall1t.  # noqa: E501


        :return: The position_x of this TpcInstall1t.  # noqa: E501
        :rtype: float
        """
        return self._position_x

    @position_x.setter
    def position_x(self, position_x):
        """Sets the position_x of this TpcInstall1t.


        :param position_x: The position_x of this TpcInstall1t.  # noqa: E501
        :type: float
        """

        self._position_x = position_x

    @property
    def position_y(self):
        """Gets the position_y of this TpcInstall1t.  # noqa: E501


        :return: The position_y of this TpcInstall1t.  # noqa: E501
        :rtype: float
        """
        return self._position_y

    @position_y.setter
    def position_y(self, position_y):
        """Sets the position_y of this TpcInstall1t.


        :param position_y: The position_y of this TpcInstall1t.  # noqa: E501
        :type: float
        """

        self._position_y = position_y

    @property
    def position_z(self):
        """Gets the position_z of this TpcInstall1t.  # noqa: E501


        :return: The position_z of this TpcInstall1t.  # noqa: E501
        :rtype: float
        """
        return self._position_z

    @position_z.setter
    def position_z(self, position_z):
        """Sets the position_z of this TpcInstall1t.


        :param position_z: The position_z of this TpcInstall1t.  # noqa: E501
        :type: float
        """

        self._position_z = position_z

    @property
    def position_r(self):
        """Gets the position_r of this TpcInstall1t.  # noqa: E501


        :return: The position_r of this TpcInstall1t.  # noqa: E501
        :rtype: float
        """
        return self._position_r

    @position_r.setter
    def position_r(self, position_r):
        """Sets the position_r of this TpcInstall1t.


        :param position_r: The position_r of this TpcInstall1t.  # noqa: E501
        :type: float
        """

        self._position_r = position_r

    @property
    def amplifier_crate(self):
        """Gets the amplifier_crate of this TpcInstall1t.  # noqa: E501


        :return: The amplifier_crate of this TpcInstall1t.  # noqa: E501
        :rtype: int
        """
        return self._amplifier_crate

    @amplifier_crate.setter
    def amplifier_crate(self, amplifier_crate):
        """Sets the amplifier_crate of this TpcInstall1t.


        :param amplifier_crate: The amplifier_crate of this TpcInstall1t.  # noqa: E501
        :type: int
        """

        self._amplifier_crate = amplifier_crate

    @property
    def amplifier_fan(self):
        """Gets the amplifier_fan of this TpcInstall1t.  # noqa: E501


        :return: The amplifier_fan of this TpcInstall1t.  # noqa: E501
        :rtype: int
        """
        return self._amplifier_fan

    @amplifier_fan.setter
    def amplifier_fan(self, amplifier_fan):
        """Sets the amplifier_fan of this TpcInstall1t.


        :param amplifier_fan: The amplifier_fan of this TpcInstall1t.  # noqa: E501
        :type: int
        """

        self._amplifier_fan = amplifier_fan

    @property
    def amplifier_plug(self):
        """Gets the amplifier_plug of this TpcInstall1t.  # noqa: E501


        :return: The amplifier_plug of this TpcInstall1t.  # noqa: E501
        :rtype: int
        """
        return self._amplifier_plug

    @amplifier_plug.setter
    def amplifier_plug(self, amplifier_plug):
        """Sets the amplifier_plug of this TpcInstall1t.


        :param amplifier_plug: The amplifier_plug of this TpcInstall1t.  # noqa: E501
        :type: int
        """

        self._amplifier_plug = amplifier_plug

    @property
    def amplifier_serial(self):
        """Gets the amplifier_serial of this TpcInstall1t.  # noqa: E501


        :return: The amplifier_serial of this TpcInstall1t.  # noqa: E501
        :rtype: int
        """
        return self._amplifier_serial

    @amplifier_serial.setter
    def amplifier_serial(self, amplifier_serial):
        """Sets the amplifier_serial of this TpcInstall1t.


        :param amplifier_serial: The amplifier_serial of this TpcInstall1t.  # noqa: E501
        :type: int
        """

        self._amplifier_serial = amplifier_serial

    @property
    def amplifier_slot(self):
        """Gets the amplifier_slot of this TpcInstall1t.  # noqa: E501


        :return: The amplifier_slot of this TpcInstall1t.  # noqa: E501
        :rtype: int
        """
        return self._amplifier_slot

    @amplifier_slot.setter
    def amplifier_slot(self, amplifier_slot):
        """Sets the amplifier_slot of this TpcInstall1t.


        :param amplifier_slot: The amplifier_slot of this TpcInstall1t.  # noqa: E501
        :type: int
        """

        self._amplifier_slot = amplifier_slot

    @property
    def amplifier_channel(self):
        """Gets the amplifier_channel of this TpcInstall1t.  # noqa: E501


        :return: The amplifier_channel of this TpcInstall1t.  # noqa: E501
        :rtype: int
        """
        return self._amplifier_channel

    @amplifier_channel.setter
    def amplifier_channel(self, amplifier_channel):
        """Sets the amplifier_channel of this TpcInstall1t.


        :param amplifier_channel: The amplifier_channel of this TpcInstall1t.  # noqa: E501
        :type: int
        """

        self._amplifier_channel = amplifier_channel

    @property
    def digitizer_channel(self):
        """Gets the digitizer_channel of this TpcInstall1t.  # noqa: E501


        :return: The digitizer_channel of this TpcInstall1t.  # noqa: E501
        :rtype: int
        """
        return self._digitizer_channel

    @digitizer_channel.setter
    def digitizer_channel(self, digitizer_channel):
        """Sets the digitizer_channel of this TpcInstall1t.


        :param digitizer_channel: The digitizer_channel of this TpcInstall1t.  # noqa: E501
        :type: int
        """

        self._digitizer_channel = digitizer_channel

    @property
    def digitizer_crate(self):
        """Gets the digitizer_crate of this TpcInstall1t.  # noqa: E501


        :return: The digitizer_crate of this TpcInstall1t.  # noqa: E501
        :rtype: int
        """
        return self._digitizer_crate

    @digitizer_crate.setter
    def digitizer_crate(self, digitizer_crate):
        """Sets the digitizer_crate of this TpcInstall1t.


        :param digitizer_crate: The digitizer_crate of this TpcInstall1t.  # noqa: E501
        :type: int
        """

        self._digitizer_crate = digitizer_crate

    @property
    def digitizer_module(self):
        """Gets the digitizer_module of this TpcInstall1t.  # noqa: E501


        :return: The digitizer_module of this TpcInstall1t.  # noqa: E501
        :rtype: int
        """
        return self._digitizer_module

    @digitizer_module.setter
    def digitizer_module(self, digitizer_module):
        """Sets the digitizer_module of this TpcInstall1t.


        :param digitizer_module: The digitizer_module of this TpcInstall1t.  # noqa: E501
        :type: int
        """

        self._digitizer_module = digitizer_module

    @property
    def digitizer_slot(self):
        """Gets the digitizer_slot of this TpcInstall1t.  # noqa: E501


        :return: The digitizer_slot of this TpcInstall1t.  # noqa: E501
        :rtype: int
        """
        return self._digitizer_slot

    @digitizer_slot.setter
    def digitizer_slot(self, digitizer_slot):
        """Sets the digitizer_slot of this TpcInstall1t.


        :param digitizer_slot: The digitizer_slot of this TpcInstall1t.  # noqa: E501
        :type: int
        """

        self._digitizer_slot = digitizer_slot

    @property
    def high_voltage_crate(self):
        """Gets the high_voltage_crate of this TpcInstall1t.  # noqa: E501


        :return: The high_voltage_crate of this TpcInstall1t.  # noqa: E501
        :rtype: int
        """
        return self._high_voltage_crate

    @high_voltage_crate.setter
    def high_voltage_crate(self, high_voltage_crate):
        """Sets the high_voltage_crate of this TpcInstall1t.


        :param high_voltage_crate: The high_voltage_crate of this TpcInstall1t.  # noqa: E501
        :type: int
        """

        self._high_voltage_crate = high_voltage_crate

    @property
    def high_voltage_board(self):
        """Gets the high_voltage_board of this TpcInstall1t.  # noqa: E501


        :return: The high_voltage_board of this TpcInstall1t.  # noqa: E501
        :rtype: int
        """
        return self._high_voltage_board

    @high_voltage_board.setter
    def high_voltage_board(self, high_voltage_board):
        """Sets the high_voltage_board of this TpcInstall1t.


        :param high_voltage_board: The high_voltage_board of this TpcInstall1t.  # noqa: E501
        :type: int
        """

        self._high_voltage_board = high_voltage_board

    @property
    def high_voltage_channel(self):
        """Gets the high_voltage_channel of this TpcInstall1t.  # noqa: E501


        :return: The high_voltage_channel of this TpcInstall1t.  # noqa: E501
        :rtype: int
        """
        return self._high_voltage_channel

    @high_voltage_channel.setter
    def high_voltage_channel(self, high_voltage_channel):
        """Sets the high_voltage_channel of this TpcInstall1t.


        :param high_voltage_channel: The high_voltage_channel of this TpcInstall1t.  # noqa: E501
        :type: int
        """

        self._high_voltage_channel = high_voltage_channel

    @property
    def high_voltage_connector(self):
        """Gets the high_voltage_connector of this TpcInstall1t.  # noqa: E501


        :return: The high_voltage_connector of this TpcInstall1t.  # noqa: E501
        :rtype: int
        """
        return self._high_voltage_connector

    @high_voltage_connector.setter
    def high_voltage_connector(self, high_voltage_connector):
        """Sets the high_voltage_connector of this TpcInstall1t.


        :param high_voltage_connector: The high_voltage_connector of this TpcInstall1t.  # noqa: E501
        :type: int
        """

        self._high_voltage_connector = high_voltage_connector

    @property
    def high_voltage_feedthrough(self):
        """Gets the high_voltage_feedthrough of this TpcInstall1t.  # noqa: E501


        :return: The high_voltage_feedthrough of this TpcInstall1t.  # noqa: E501
        :rtype: str
        """
        return self._high_voltage_feedthrough

    @high_voltage_feedthrough.setter
    def high_voltage_feedthrough(self, high_voltage_feedthrough):
        """Sets the high_voltage_feedthrough of this TpcInstall1t.


        :param high_voltage_feedthrough: The high_voltage_feedthrough of this TpcInstall1t.  # noqa: E501
        :type: str
        """

        self._high_voltage_feedthrough = high_voltage_feedthrough

    @property
    def high_voltage_return(self):
        """Gets the high_voltage_return of this TpcInstall1t.  # noqa: E501


        :return: The high_voltage_return of this TpcInstall1t.  # noqa: E501
        :rtype: int
        """
        return self._high_voltage_return

    @high_voltage_return.setter
    def high_voltage_return(self, high_voltage_return):
        """Sets the high_voltage_return of this TpcInstall1t.


        :param high_voltage_return: The high_voltage_return of this TpcInstall1t.  # noqa: E501
        :type: int
        """

        self._high_voltage_return = high_voltage_return

    @property
    def serial_number(self):
        """Gets the serial_number of this TpcInstall1t.  # noqa: E501


        :return: The serial_number of this TpcInstall1t.  # noqa: E501
        :rtype: str
        """
        return self._serial_number

    @serial_number.setter
    def serial_number(self, serial_number):
        """Sets the serial_number of this TpcInstall1t.


        :param serial_number: The serial_number of this TpcInstall1t.  # noqa: E501
        :type: str
        """

        self._serial_number = serial_number

    @property
    def signal_channel(self):
        """Gets the signal_channel of this TpcInstall1t.  # noqa: E501


        :return: The signal_channel of this TpcInstall1t.  # noqa: E501
        :rtype: int
        """
        return self._signal_channel

    @signal_channel.setter
    def signal_channel(self, signal_channel):
        """Sets the signal_channel of this TpcInstall1t.


        :param signal_channel: The signal_channel of this TpcInstall1t.  # noqa: E501
        :type: int
        """

        self._signal_channel = signal_channel

    @property
    def signal_connector(self):
        """Gets the signal_connector of this TpcInstall1t.  # noqa: E501


        :return: The signal_connector of this TpcInstall1t.  # noqa: E501
        :rtype: int
        """
        return self._signal_connector

    @signal_connector.setter
    def signal_connector(self, signal_connector):
        """Sets the signal_connector of this TpcInstall1t.


        :param signal_connector: The signal_connector of this TpcInstall1t.  # noqa: E501
        :type: int
        """

        self._signal_connector = signal_connector

    @property
    def signal_feedthrough(self):
        """Gets the signal_feedthrough of this TpcInstall1t.  # noqa: E501


        :return: The signal_feedthrough of this TpcInstall1t.  # noqa: E501
        :rtype: str
        """
        return self._signal_feedthrough

    @signal_feedthrough.setter
    def signal_feedthrough(self, signal_feedthrough):
        """Sets the signal_feedthrough of this TpcInstall1t.


        :param signal_feedthrough: The signal_feedthrough of this TpcInstall1t.  # noqa: E501
        :type: str
        """

        self._signal_feedthrough = signal_feedthrough

    @property
    def id(self):
        """Gets the id of this TpcInstall1t.  # noqa: E501


        :return: The id of this TpcInstall1t.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TpcInstall1t.


        :param id: The id of this TpcInstall1t.  # noqa: E501
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
        if not isinstance(other, TpcInstall1t):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TpcInstall1t):
            return True

        return self.to_dict() != other.to_dict()
