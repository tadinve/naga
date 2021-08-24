# coding: utf-8

"""
    Control-M Services

    Provides access to BMC Control-M Services  # noqa: E501

    OpenAPI spec version: 9.20.215
    Contact: customer_support@bmc.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from ctm_api_client.configuration import Configuration


class ZosTemplateData(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'name': 'str',
        'record_format': 'str',
        'logical_record_length': 'int',
        'block_size': 'int',
        'translation_table': 'str',
        'transfer_mode': 'str',
        'sms_managment_class': 'str',
        'allocation_units': 'str',
        'volume': 'str',
        'unit': 'str',
        'primary_allocation': 'int',
        'secondary_allocation': 'int',
        'sms_data_class': 'str',
        'dbcs_encoding': 'str',
        'transfer_to_unique_file': 'bool',
        'additional_options_host1': 'str',
        'additional_options_host2': 'str'
    }

    attribute_map = {
        'name': 'name',
        'record_format': 'recordFormat',
        'logical_record_length': 'logicalRecordLength',
        'block_size': 'blockSize',
        'translation_table': 'translationTable',
        'transfer_mode': 'transferMode',
        'sms_managment_class': 'smsManagmentClass',
        'allocation_units': 'allocationUnits',
        'volume': 'volume',
        'unit': 'unit',
        'primary_allocation': 'primaryAllocation',
        'secondary_allocation': 'secondaryAllocation',
        'sms_data_class': 'smsDataClass',
        'dbcs_encoding': 'dbcsEncoding',
        'transfer_to_unique_file': 'transferToUniqueFile',
        'additional_options_host1': 'additionalOptionsHost1',
        'additional_options_host2': 'additionalOptionsHost2'
    }

    def __init__(self, name=None, record_format=None, logical_record_length=None, block_size=None, translation_table=None, transfer_mode=None, sms_managment_class=None, allocation_units=None, volume=None, unit=None, primary_allocation=None, secondary_allocation=None, sms_data_class=None, dbcs_encoding=None, transfer_to_unique_file=None, additional_options_host1=None, additional_options_host2=None, _configuration=None):  # noqa: E501
        """ZosTemplateData - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._name = None
        self._record_format = None
        self._logical_record_length = None
        self._block_size = None
        self._translation_table = None
        self._transfer_mode = None
        self._sms_managment_class = None
        self._allocation_units = None
        self._volume = None
        self._unit = None
        self._primary_allocation = None
        self._secondary_allocation = None
        self._sms_data_class = None
        self._dbcs_encoding = None
        self._transfer_to_unique_file = None
        self._additional_options_host1 = None
        self._additional_options_host2 = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if record_format is not None:
            self.record_format = record_format
        if logical_record_length is not None:
            self.logical_record_length = logical_record_length
        if block_size is not None:
            self.block_size = block_size
        if translation_table is not None:
            self.translation_table = translation_table
        if transfer_mode is not None:
            self.transfer_mode = transfer_mode
        if sms_managment_class is not None:
            self.sms_managment_class = sms_managment_class
        if allocation_units is not None:
            self.allocation_units = allocation_units
        if volume is not None:
            self.volume = volume
        if unit is not None:
            self.unit = unit
        if primary_allocation is not None:
            self.primary_allocation = primary_allocation
        if secondary_allocation is not None:
            self.secondary_allocation = secondary_allocation
        if sms_data_class is not None:
            self.sms_data_class = sms_data_class
        if dbcs_encoding is not None:
            self.dbcs_encoding = dbcs_encoding
        if transfer_to_unique_file is not None:
            self.transfer_to_unique_file = transfer_to_unique_file
        if additional_options_host1 is not None:
            self.additional_options_host1 = additional_options_host1
        if additional_options_host2 is not None:
            self.additional_options_host2 = additional_options_host2

    @property
    def name(self):
        """Gets the name of this ZosTemplateData.  # noqa: E501

        Template name HIDDEN  # noqa: E501

        :return: The name of this ZosTemplateData.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ZosTemplateData.

        Template name HIDDEN  # noqa: E501

        :param name: The name of this ZosTemplateData.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def record_format(self):
        """Gets the record_format of this ZosTemplateData.  # noqa: E501

        Record format HIDDEN  # noqa: E501

        :return: The record_format of this ZosTemplateData.  # noqa: E501
        :rtype: str
        """
        return self._record_format

    @record_format.setter
    def record_format(self, record_format):
        """Sets the record_format of this ZosTemplateData.

        Record format HIDDEN  # noqa: E501

        :param record_format: The record_format of this ZosTemplateData.  # noqa: E501
        :type: str
        """

        self._record_format = record_format

    @property
    def logical_record_length(self):
        """Gets the logical_record_length of this ZosTemplateData.  # noqa: E501

        Logical record length HIDDEN  # noqa: E501

        :return: The logical_record_length of this ZosTemplateData.  # noqa: E501
        :rtype: int
        """
        return self._logical_record_length

    @logical_record_length.setter
    def logical_record_length(self, logical_record_length):
        """Sets the logical_record_length of this ZosTemplateData.

        Logical record length HIDDEN  # noqa: E501

        :param logical_record_length: The logical_record_length of this ZosTemplateData.  # noqa: E501
        :type: int
        """

        self._logical_record_length = logical_record_length

    @property
    def block_size(self):
        """Gets the block_size of this ZosTemplateData.  # noqa: E501

        Block Size HIDDEN  # noqa: E501

        :return: The block_size of this ZosTemplateData.  # noqa: E501
        :rtype: int
        """
        return self._block_size

    @block_size.setter
    def block_size(self, block_size):
        """Sets the block_size of this ZosTemplateData.

        Block Size HIDDEN  # noqa: E501

        :param block_size: The block_size of this ZosTemplateData.  # noqa: E501
        :type: int
        """

        self._block_size = block_size

    @property
    def translation_table(self):
        """Gets the translation_table of this ZosTemplateData.  # noqa: E501

        Translation table HIDDEN  # noqa: E501

        :return: The translation_table of this ZosTemplateData.  # noqa: E501
        :rtype: str
        """
        return self._translation_table

    @translation_table.setter
    def translation_table(self, translation_table):
        """Sets the translation_table of this ZosTemplateData.

        Translation table HIDDEN  # noqa: E501

        :param translation_table: The translation_table of this ZosTemplateData.  # noqa: E501
        :type: str
        """

        self._translation_table = translation_table

    @property
    def transfer_mode(self):
        """Gets the transfer_mode of this ZosTemplateData.  # noqa: E501

        Transfer mode HIDDEN  # noqa: E501

        :return: The transfer_mode of this ZosTemplateData.  # noqa: E501
        :rtype: str
        """
        return self._transfer_mode

    @transfer_mode.setter
    def transfer_mode(self, transfer_mode):
        """Sets the transfer_mode of this ZosTemplateData.

        Transfer mode HIDDEN  # noqa: E501

        :param transfer_mode: The transfer_mode of this ZosTemplateData.  # noqa: E501
        :type: str
        """

        self._transfer_mode = transfer_mode

    @property
    def sms_managment_class(self):
        """Gets the sms_managment_class of this ZosTemplateData.  # noqa: E501

        Management class HIDDEN  # noqa: E501

        :return: The sms_managment_class of this ZosTemplateData.  # noqa: E501
        :rtype: str
        """
        return self._sms_managment_class

    @sms_managment_class.setter
    def sms_managment_class(self, sms_managment_class):
        """Sets the sms_managment_class of this ZosTemplateData.

        Management class HIDDEN  # noqa: E501

        :param sms_managment_class: The sms_managment_class of this ZosTemplateData.  # noqa: E501
        :type: str
        """

        self._sms_managment_class = sms_managment_class

    @property
    def allocation_units(self):
        """Gets the allocation_units of this ZosTemplateData.  # noqa: E501

        Allocation units HIDDEN  # noqa: E501

        :return: The allocation_units of this ZosTemplateData.  # noqa: E501
        :rtype: str
        """
        return self._allocation_units

    @allocation_units.setter
    def allocation_units(self, allocation_units):
        """Sets the allocation_units of this ZosTemplateData.

        Allocation units HIDDEN  # noqa: E501

        :param allocation_units: The allocation_units of this ZosTemplateData.  # noqa: E501
        :type: str
        """

        self._allocation_units = allocation_units

    @property
    def volume(self):
        """Gets the volume of this ZosTemplateData.  # noqa: E501

        Volume HIDDEN  # noqa: E501

        :return: The volume of this ZosTemplateData.  # noqa: E501
        :rtype: str
        """
        return self._volume

    @volume.setter
    def volume(self, volume):
        """Sets the volume of this ZosTemplateData.

        Volume HIDDEN  # noqa: E501

        :param volume: The volume of this ZosTemplateData.  # noqa: E501
        :type: str
        """

        self._volume = volume

    @property
    def unit(self):
        """Gets the unit of this ZosTemplateData.  # noqa: E501

        Unit HIDDEN  # noqa: E501

        :return: The unit of this ZosTemplateData.  # noqa: E501
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        """Sets the unit of this ZosTemplateData.

        Unit HIDDEN  # noqa: E501

        :param unit: The unit of this ZosTemplateData.  # noqa: E501
        :type: str
        """

        self._unit = unit

    @property
    def primary_allocation(self):
        """Gets the primary_allocation of this ZosTemplateData.  # noqa: E501

        Primary Allocation HIDDEN  # noqa: E501

        :return: The primary_allocation of this ZosTemplateData.  # noqa: E501
        :rtype: int
        """
        return self._primary_allocation

    @primary_allocation.setter
    def primary_allocation(self, primary_allocation):
        """Sets the primary_allocation of this ZosTemplateData.

        Primary Allocation HIDDEN  # noqa: E501

        :param primary_allocation: The primary_allocation of this ZosTemplateData.  # noqa: E501
        :type: int
        """

        self._primary_allocation = primary_allocation

    @property
    def secondary_allocation(self):
        """Gets the secondary_allocation of this ZosTemplateData.  # noqa: E501

        Secondary allocation HIDDEN  # noqa: E501

        :return: The secondary_allocation of this ZosTemplateData.  # noqa: E501
        :rtype: int
        """
        return self._secondary_allocation

    @secondary_allocation.setter
    def secondary_allocation(self, secondary_allocation):
        """Sets the secondary_allocation of this ZosTemplateData.

        Secondary allocation HIDDEN  # noqa: E501

        :param secondary_allocation: The secondary_allocation of this ZosTemplateData.  # noqa: E501
        :type: int
        """

        self._secondary_allocation = secondary_allocation

    @property
    def sms_data_class(self):
        """Gets the sms_data_class of this ZosTemplateData.  # noqa: E501

        Data class HIDDEN  # noqa: E501

        :return: The sms_data_class of this ZosTemplateData.  # noqa: E501
        :rtype: str
        """
        return self._sms_data_class

    @sms_data_class.setter
    def sms_data_class(self, sms_data_class):
        """Sets the sms_data_class of this ZosTemplateData.

        Data class HIDDEN  # noqa: E501

        :param sms_data_class: The sms_data_class of this ZosTemplateData.  # noqa: E501
        :type: str
        """

        self._sms_data_class = sms_data_class

    @property
    def dbcs_encoding(self):
        """Gets the dbcs_encoding of this ZosTemplateData.  # noqa: E501

        DBCS name HIDDEN  # noqa: E501

        :return: The dbcs_encoding of this ZosTemplateData.  # noqa: E501
        :rtype: str
        """
        return self._dbcs_encoding

    @dbcs_encoding.setter
    def dbcs_encoding(self, dbcs_encoding):
        """Sets the dbcs_encoding of this ZosTemplateData.

        DBCS name HIDDEN  # noqa: E501

        :param dbcs_encoding: The dbcs_encoding of this ZosTemplateData.  # noqa: E501
        :type: str
        """

        self._dbcs_encoding = dbcs_encoding

    @property
    def transfer_to_unique_file(self):
        """Gets the transfer_to_unique_file of this ZosTemplateData.  # noqa: E501

        Transfer to unique file HIDDEN  # noqa: E501

        :return: The transfer_to_unique_file of this ZosTemplateData.  # noqa: E501
        :rtype: bool
        """
        return self._transfer_to_unique_file

    @transfer_to_unique_file.setter
    def transfer_to_unique_file(self, transfer_to_unique_file):
        """Sets the transfer_to_unique_file of this ZosTemplateData.

        Transfer to unique file HIDDEN  # noqa: E501

        :param transfer_to_unique_file: The transfer_to_unique_file of this ZosTemplateData.  # noqa: E501
        :type: bool
        """

        self._transfer_to_unique_file = transfer_to_unique_file

    @property
    def additional_options_host1(self):
        """Gets the additional_options_host1 of this ZosTemplateData.  # noqa: E501

        Additional options host 1 HIDDEN  # noqa: E501

        :return: The additional_options_host1 of this ZosTemplateData.  # noqa: E501
        :rtype: str
        """
        return self._additional_options_host1

    @additional_options_host1.setter
    def additional_options_host1(self, additional_options_host1):
        """Sets the additional_options_host1 of this ZosTemplateData.

        Additional options host 1 HIDDEN  # noqa: E501

        :param additional_options_host1: The additional_options_host1 of this ZosTemplateData.  # noqa: E501
        :type: str
        """

        self._additional_options_host1 = additional_options_host1

    @property
    def additional_options_host2(self):
        """Gets the additional_options_host2 of this ZosTemplateData.  # noqa: E501

        Additional options host 1 HIDDEN  # noqa: E501

        :return: The additional_options_host2 of this ZosTemplateData.  # noqa: E501
        :rtype: str
        """
        return self._additional_options_host2

    @additional_options_host2.setter
    def additional_options_host2(self, additional_options_host2):
        """Sets the additional_options_host2 of this ZosTemplateData.

        Additional options host 1 HIDDEN  # noqa: E501

        :param additional_options_host2: The additional_options_host2 of this ZosTemplateData.  # noqa: E501
        :type: str
        """

        self._additional_options_host2 = additional_options_host2

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(ZosTemplateData, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ZosTemplateData):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ZosTemplateData):
            return True

        return self.to_dict() != other.to_dict()
