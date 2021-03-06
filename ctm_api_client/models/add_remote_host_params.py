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


class AddRemoteHostParams(object):
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
        "remotehost": "str",
        "port": "int",
        "encrypt_algorithm": "str",
        "compression": "bool",
        "authorize": "bool",
        "agents": "list[str]",
    }

    attribute_map = {
        "remotehost": "remotehost",
        "port": "port",
        "encrypt_algorithm": "encryptAlgorithm",
        "compression": "compression",
        "authorize": "authorize",
        "agents": "agents",
    }

    def __init__(
        self,
        remotehost=None,
        port=None,
        encrypt_algorithm=None,
        compression=None,
        authorize=None,
        agents=None,
        _configuration=None,
    ):  # noqa: E501
        """AddRemoteHostParams - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._remotehost = None
        self._port = None
        self._encrypt_algorithm = None
        self._compression = None
        self._authorize = None
        self._agents = None
        self.discriminator = None

        if remotehost is not None:
            self.remotehost = remotehost
        if port is not None:
            self.port = port
        if encrypt_algorithm is not None:
            self.encrypt_algorithm = encrypt_algorithm
        if compression is not None:
            self.compression = compression
        if authorize is not None:
            self.authorize = authorize
        if agents is not None:
            self.agents = agents

    @property
    def remotehost(self):
        """Gets the remotehost of this AddRemoteHostParams.  # noqa: E501

        The remote host (name) which will execute the commands. REQUIRED.  # noqa: E501

        :return: The remotehost of this AddRemoteHostParams.  # noqa: E501
        :rtype: str
        """
        return self._remotehost

    @remotehost.setter
    def remotehost(self, remotehost):
        """Sets the remotehost of this AddRemoteHostParams.

        The remote host (name) which will execute the commands. REQUIRED.  # noqa: E501

        :param remotehost: The remotehost of this AddRemoteHostParams.  # noqa: E501
        :type: str
        """

        self._remotehost = remotehost

    @property
    def port(self):
        """Gets the port of this AddRemoteHostParams.  # noqa: E501

        The remote host SSH port.  # noqa: E501

        :return: The port of this AddRemoteHostParams.  # noqa: E501
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this AddRemoteHostParams.

        The remote host SSH port.  # noqa: E501

        :param port: The port of this AddRemoteHostParams.  # noqa: E501
        :type: int
        """

        self._port = port

    @property
    def encrypt_algorithm(self):
        """Gets the encrypt_algorithm of this AddRemoteHostParams.  # noqa: E501

        The SSH encrypt algorithm to be used. HIDDEN.  # noqa: E501

        :return: The encrypt_algorithm of this AddRemoteHostParams.  # noqa: E501
        :rtype: str
        """
        return self._encrypt_algorithm

    @encrypt_algorithm.setter
    def encrypt_algorithm(self, encrypt_algorithm):
        """Sets the encrypt_algorithm of this AddRemoteHostParams.

        The SSH encrypt algorithm to be used. HIDDEN.  # noqa: E501

        :param encrypt_algorithm: The encrypt_algorithm of this AddRemoteHostParams.  # noqa: E501
        :type: str
        """

        self._encrypt_algorithm = encrypt_algorithm

    @property
    def compression(self):
        """Gets the compression of this AddRemoteHostParams.  # noqa: E501

        Is compression used. HIDDEN.  # noqa: E501

        :return: The compression of this AddRemoteHostParams.  # noqa: E501
        :rtype: bool
        """
        return self._compression

    @compression.setter
    def compression(self, compression):
        """Sets the compression of this AddRemoteHostParams.

        Is compression used. HIDDEN.  # noqa: E501

        :param compression: The compression of this AddRemoteHostParams.  # noqa: E501
        :type: bool
        """

        self._compression = compression

    @property
    def authorize(self):
        """Gets the authorize of this AddRemoteHostParams.  # noqa: E501

        authorize SSL remote host while creating the remote host. HIDDEN.  # noqa: E501

        :return: The authorize of this AddRemoteHostParams.  # noqa: E501
        :rtype: bool
        """
        return self._authorize

    @authorize.setter
    def authorize(self, authorize):
        """Sets the authorize of this AddRemoteHostParams.

        authorize SSL remote host while creating the remote host. HIDDEN.  # noqa: E501

        :param authorize: The authorize of this AddRemoteHostParams.  # noqa: E501
        :type: bool
        """

        self._authorize = authorize

    @property
    def agents(self):
        """Gets the agents of this AddRemoteHostParams.  # noqa: E501

        Agents to execute the commands on. HIDDEN.  # noqa: E501

        :return: The agents of this AddRemoteHostParams.  # noqa: E501
        :rtype: list[str]
        """
        return self._agents

    @agents.setter
    def agents(self, agents):
        """Sets the agents of this AddRemoteHostParams.

        Agents to execute the commands on. HIDDEN.  # noqa: E501

        :param agents: The agents of this AddRemoteHostParams.  # noqa: E501
        :type: list[str]
        """

        self._agents = agents

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(
                    map(lambda x: x.to_dict() if hasattr(x, "to_dict") else x, value)
                )
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(
                    map(
                        lambda item: (item[0], item[1].to_dict())
                        if hasattr(item[1], "to_dict")
                        else item,
                        value.items(),
                    )
                )
            else:
                result[attr] = value
        if issubclass(AddRemoteHostParams, dict):
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
        if not isinstance(other, AddRemoteHostParams):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AddRemoteHostParams):
            return True

        return self.to_dict() != other.to_dict()
