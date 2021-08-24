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


class ReportDateTimeSettings(object):
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
        'date_format': 'str',
        'time_format': 'str',
        'date_time_format': 'str'
    }

    attribute_map = {
        'date_format': 'dateFormat',
        'time_format': 'timeFormat',
        'date_time_format': 'dateTimeFormat'
    }

    def __init__(self, date_format=None, time_format=None, date_time_format=None, _configuration=None):  # noqa: E501
        """ReportDateTimeSettings - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._date_format = None
        self._time_format = None
        self._date_time_format = None
        self.discriminator = None

        if date_format is not None:
            self.date_format = date_format
        if time_format is not None:
            self.time_format = time_format
        if date_time_format is not None:
            self.date_time_format = date_time_format

    @property
    def date_format(self):
        """Gets the date_format of this ReportDateTimeSettings.  # noqa: E501


        :return: The date_format of this ReportDateTimeSettings.  # noqa: E501
        :rtype: str
        """
        return self._date_format

    @date_format.setter
    def date_format(self, date_format):
        """Sets the date_format of this ReportDateTimeSettings.


        :param date_format: The date_format of this ReportDateTimeSettings.  # noqa: E501
        :type: str
        """

        self._date_format = date_format

    @property
    def time_format(self):
        """Gets the time_format of this ReportDateTimeSettings.  # noqa: E501


        :return: The time_format of this ReportDateTimeSettings.  # noqa: E501
        :rtype: str
        """
        return self._time_format

    @time_format.setter
    def time_format(self, time_format):
        """Sets the time_format of this ReportDateTimeSettings.


        :param time_format: The time_format of this ReportDateTimeSettings.  # noqa: E501
        :type: str
        """

        self._time_format = time_format

    @property
    def date_time_format(self):
        """Gets the date_time_format of this ReportDateTimeSettings.  # noqa: E501


        :return: The date_time_format of this ReportDateTimeSettings.  # noqa: E501
        :rtype: str
        """
        return self._date_time_format

    @date_time_format.setter
    def date_time_format(self, date_time_format):
        """Sets the date_time_format of this ReportDateTimeSettings.


        :param date_time_format: The date_time_format of this ReportDateTimeSettings.  # noqa: E501
        :type: str
        """

        self._date_time_format = date_time_format

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
        if issubclass(ReportDateTimeSettings, dict):
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
        if not isinstance(other, ReportDateTimeSettings):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ReportDateTimeSettings):
            return True

        return self.to_dict() != other.to_dict()
