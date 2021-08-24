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


class GatewayData(object):
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
        'host': 'str',
        'port': 'str',
        'status': 'str',
        'message': 'str'
    }

    attribute_map = {
        'host': 'host',
        'port': 'port',
        'status': 'status',
        'message': 'message'
    }

    def __init__(self, host=None, port=None, status=None, message=None, _configuration=None):  # noqa: E501
        """GatewayData - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._host = None
        self._port = None
        self._status = None
        self._message = None
        self.discriminator = None

        if host is not None:
            self.host = host
        if port is not None:
            self.port = port
        if status is not None:
            self.status = status
        if message is not None:
            self.message = message

    @property
    def host(self):
        """Gets the host of this GatewayData.  # noqa: E501

        gateway host name REQUIRED  # noqa: E501

        :return: The host of this GatewayData.  # noqa: E501
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        """Sets the host of this GatewayData.

        gateway host name REQUIRED  # noqa: E501

        :param host: The host of this GatewayData.  # noqa: E501
        :type: str
        """

        self._host = host

    @property
    def port(self):
        """Gets the port of this GatewayData.  # noqa: E501

        gateway port REQUIRED  # noqa: E501

        :return: The port of this GatewayData.  # noqa: E501
        :rtype: str
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this GatewayData.

        gateway port REQUIRED  # noqa: E501

        :param port: The port of this GatewayData.  # noqa: E501
        :type: str
        """

        self._port = port

    @property
    def status(self):
        """Gets the status of this GatewayData.  # noqa: E501

        gateway status HIDDEN  # noqa: E501

        :return: The status of this GatewayData.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this GatewayData.

        gateway status HIDDEN  # noqa: E501

        :param status: The status of this GatewayData.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def message(self):
        """Gets the message of this GatewayData.  # noqa: E501

        general message HIDDEN  # noqa: E501

        :return: The message of this GatewayData.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this GatewayData.

        general message HIDDEN  # noqa: E501

        :param message: The message of this GatewayData.  # noqa: E501
        :type: str
        """

        self._message = message

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
        if issubclass(GatewayData, dict):
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
        if not isinstance(other, GatewayData):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GatewayData):
            return True

        return self.to_dict() != other.to_dict()
