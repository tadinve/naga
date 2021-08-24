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


class HostnamePortPair(object):
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
        'physical_hostname': 'str',
        'port': 'str'
    }

    attribute_map = {
        'physical_hostname': 'physicalHostname',
        'port': 'port'
    }

    def __init__(self, physical_hostname=None, port=None, _configuration=None):  # noqa: E501
        """HostnamePortPair - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._physical_hostname = None
        self._port = None
        self.discriminator = None

        if physical_hostname is not None:
            self.physical_hostname = physical_hostname
        if port is not None:
            self.port = port

    @property
    def physical_hostname(self):
        """Gets the physical_hostname of this HostnamePortPair.  # noqa: E501

        host name  # noqa: E501

        :return: The physical_hostname of this HostnamePortPair.  # noqa: E501
        :rtype: str
        """
        return self._physical_hostname

    @physical_hostname.setter
    def physical_hostname(self, physical_hostname):
        """Sets the physical_hostname of this HostnamePortPair.

        host name  # noqa: E501

        :param physical_hostname: The physical_hostname of this HostnamePortPair.  # noqa: E501
        :type: str
        """

        self._physical_hostname = physical_hostname

    @property
    def port(self):
        """Gets the port of this HostnamePortPair.  # noqa: E501

        port  # noqa: E501

        :return: The port of this HostnamePortPair.  # noqa: E501
        :rtype: str
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this HostnamePortPair.

        port  # noqa: E501

        :param port: The port of this HostnamePortPair.  # noqa: E501
        :type: str
        """

        self._port = port

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
        if issubclass(HostnamePortPair, dict):
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
        if not isinstance(other, HostnamePortPair):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, HostnamePortPair):
            return True

        return self.to_dict() != other.to_dict()
