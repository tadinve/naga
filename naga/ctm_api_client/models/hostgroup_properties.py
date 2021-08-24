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

from naga.ctm_api_client.configuration import Configuration


class HostgroupProperties(object):
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
        'agentslist': 'list[AgentInGroupParams]',
        'tag': 'str'
    }

    attribute_map = {
        'agentslist': 'agentslist',
        'tag': 'tag'
    }

    def __init__(self, agentslist=None, tag=None, _configuration=None):  # noqa: E501
        """HostgroupProperties - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._agentslist = None
        self._tag = None
        self.discriminator = None

        if agentslist is not None:
            self.agentslist = agentslist
        if tag is not None:
            self.tag = tag

    @property
    def agentslist(self):
        """Gets the agentslist of this HostgroupProperties.  # noqa: E501

        Agents list. HIDDEN.  # noqa: E501

        :return: The agentslist of this HostgroupProperties.  # noqa: E501
        :rtype: list[AgentInGroupParams]
        """
        return self._agentslist

    @agentslist.setter
    def agentslist(self, agentslist):
        """Sets the agentslist of this HostgroupProperties.

        Agents list. HIDDEN.  # noqa: E501

        :param agentslist: The agentslist of this HostgroupProperties.  # noqa: E501
        :type: list[AgentInGroupParams]
        """

        self._agentslist = agentslist

    @property
    def tag(self):
        """Gets the tag of this HostgroupProperties.  # noqa: E501

        Host Group tag. HIDDEN.  # noqa: E501

        :return: The tag of this HostgroupProperties.  # noqa: E501
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """Sets the tag of this HostgroupProperties.

        Host Group tag. HIDDEN.  # noqa: E501

        :param tag: The tag of this HostgroupProperties.  # noqa: E501
        :type: str
        """

        self._tag = tag

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
        if issubclass(HostgroupProperties, dict):
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
        if not isinstance(other, HostgroupProperties):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, HostgroupProperties):
            return True

        return self.to_dict() != other.to_dict()