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


class PluginMngAuth(object):
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
        'controlm_server': 'str',
        'agent': 'str',
        'plugin_type': 'str',
        'privilege': 'str'
    }

    attribute_map = {
        'controlm_server': 'ControlmServer',
        'agent': 'Agent',
        'plugin_type': 'PluginType',
        'privilege': 'Privilege'
    }

    def __init__(self, controlm_server=None, agent=None, plugin_type=None, privilege=None, _configuration=None):  # noqa: E501
        """PluginMngAuth - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._controlm_server = None
        self._agent = None
        self._plugin_type = None
        self._privilege = None
        self.discriminator = None

        if controlm_server is not None:
            self.controlm_server = controlm_server
        if agent is not None:
            self.agent = agent
        if plugin_type is not None:
            self.plugin_type = plugin_type
        if privilege is not None:
            self.privilege = privilege

    @property
    def controlm_server(self):
        """Gets the controlm_server of this PluginMngAuth.  # noqa: E501

        control-M server name  # noqa: E501

        :return: The controlm_server of this PluginMngAuth.  # noqa: E501
        :rtype: str
        """
        return self._controlm_server

    @controlm_server.setter
    def controlm_server(self, controlm_server):
        """Sets the controlm_server of this PluginMngAuth.

        control-M server name  # noqa: E501

        :param controlm_server: The controlm_server of this PluginMngAuth.  # noqa: E501
        :type: str
        """

        self._controlm_server = controlm_server

    @property
    def agent(self):
        """Gets the agent of this PluginMngAuth.  # noqa: E501

        agent name  # noqa: E501

        :return: The agent of this PluginMngAuth.  # noqa: E501
        :rtype: str
        """
        return self._agent

    @agent.setter
    def agent(self, agent):
        """Sets the agent of this PluginMngAuth.

        agent name  # noqa: E501

        :param agent: The agent of this PluginMngAuth.  # noqa: E501
        :type: str
        """

        self._agent = agent

    @property
    def plugin_type(self):
        """Gets the plugin_type of this PluginMngAuth.  # noqa: E501

        plugin type  # noqa: E501

        :return: The plugin_type of this PluginMngAuth.  # noqa: E501
        :rtype: str
        """
        return self._plugin_type

    @plugin_type.setter
    def plugin_type(self, plugin_type):
        """Sets the plugin_type of this PluginMngAuth.

        plugin type  # noqa: E501

        :param plugin_type: The plugin_type of this PluginMngAuth.  # noqa: E501
        :type: str
        """

        self._plugin_type = plugin_type

    @property
    def privilege(self):
        """Gets the privilege of this PluginMngAuth.  # noqa: E501

        access level (full, update, browse)  # noqa: E501

        :return: The privilege of this PluginMngAuth.  # noqa: E501
        :rtype: str
        """
        return self._privilege

    @privilege.setter
    def privilege(self, privilege):
        """Sets the privilege of this PluginMngAuth.

        access level (full, update, browse)  # noqa: E501

        :param privilege: The privilege of this PluginMngAuth.  # noqa: E501
        :type: str
        """

        self._privilege = privilege

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
        if issubclass(PluginMngAuth, dict):
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
        if not isinstance(other, PluginMngAuth):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PluginMngAuth):
            return True

        return self.to_dict() != other.to_dict()
