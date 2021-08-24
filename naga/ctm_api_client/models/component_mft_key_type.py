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


class ComponentMftKeyType(object):
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
        'type': 'str',
        'name': 'str',
        'host': 'str',
        'node_id': 'str',
        'appl_type': 'str',
        'appl_ver': 'str',
        'cm_ver': 'str'
    }

    attribute_map = {
        'type': 'type',
        'name': 'name',
        'host': 'host',
        'node_id': 'nodeId',
        'appl_type': 'applType',
        'appl_ver': 'applVer',
        'cm_ver': 'cmVer'
    }

    def __init__(self, type=None, name=None, host=None, node_id=None, appl_type=None, appl_ver=None, cm_ver=None, _configuration=None):  # noqa: E501
        """ComponentMftKeyType - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._type = None
        self._name = None
        self._host = None
        self._node_id = None
        self._appl_type = None
        self._appl_ver = None
        self._cm_ver = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if name is not None:
            self.name = name
        if host is not None:
            self.host = host
        if node_id is not None:
            self.node_id = node_id
        if appl_type is not None:
            self.appl_type = appl_type
        if appl_ver is not None:
            self.appl_ver = appl_ver
        if cm_ver is not None:
            self.cm_ver = cm_ver

    @property
    def type(self):
        """Gets the type of this ComponentMftKeyType.  # noqa: E501

        type  # noqa: E501

        :return: The type of this ComponentMftKeyType.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ComponentMftKeyType.

        type  # noqa: E501

        :param type: The type of this ComponentMftKeyType.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def name(self):
        """Gets the name of this ComponentMftKeyType.  # noqa: E501

        name  # noqa: E501

        :return: The name of this ComponentMftKeyType.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ComponentMftKeyType.

        name  # noqa: E501

        :param name: The name of this ComponentMftKeyType.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def host(self):
        """Gets the host of this ComponentMftKeyType.  # noqa: E501

        host  # noqa: E501

        :return: The host of this ComponentMftKeyType.  # noqa: E501
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        """Sets the host of this ComponentMftKeyType.

        host  # noqa: E501

        :param host: The host of this ComponentMftKeyType.  # noqa: E501
        :type: str
        """

        self._host = host

    @property
    def node_id(self):
        """Gets the node_id of this ComponentMftKeyType.  # noqa: E501

        node id  # noqa: E501

        :return: The node_id of this ComponentMftKeyType.  # noqa: E501
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        """Sets the node_id of this ComponentMftKeyType.

        node id  # noqa: E501

        :param node_id: The node_id of this ComponentMftKeyType.  # noqa: E501
        :type: str
        """

        self._node_id = node_id

    @property
    def appl_type(self):
        """Gets the appl_type of this ComponentMftKeyType.  # noqa: E501

        application type  # noqa: E501

        :return: The appl_type of this ComponentMftKeyType.  # noqa: E501
        :rtype: str
        """
        return self._appl_type

    @appl_type.setter
    def appl_type(self, appl_type):
        """Sets the appl_type of this ComponentMftKeyType.

        application type  # noqa: E501

        :param appl_type: The appl_type of this ComponentMftKeyType.  # noqa: E501
        :type: str
        """

        self._appl_type = appl_type

    @property
    def appl_ver(self):
        """Gets the appl_ver of this ComponentMftKeyType.  # noqa: E501

        application version  # noqa: E501

        :return: The appl_ver of this ComponentMftKeyType.  # noqa: E501
        :rtype: str
        """
        return self._appl_ver

    @appl_ver.setter
    def appl_ver(self, appl_ver):
        """Sets the appl_ver of this ComponentMftKeyType.

        application version  # noqa: E501

        :param appl_ver: The appl_ver of this ComponentMftKeyType.  # noqa: E501
        :type: str
        """

        self._appl_ver = appl_ver

    @property
    def cm_ver(self):
        """Gets the cm_ver of this ComponentMftKeyType.  # noqa: E501

        cm version  # noqa: E501

        :return: The cm_ver of this ComponentMftKeyType.  # noqa: E501
        :rtype: str
        """
        return self._cm_ver

    @cm_ver.setter
    def cm_ver(self, cm_ver):
        """Sets the cm_ver of this ComponentMftKeyType.

        cm version  # noqa: E501

        :param cm_ver: The cm_ver of this ComponentMftKeyType.  # noqa: E501
        :type: str
        """

        self._cm_ver = cm_ver

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
        if issubclass(ComponentMftKeyType, dict):
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
        if not isinstance(other, ComponentMftKeyType):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ComponentMftKeyType):
            return True

        return self.to_dict() != other.to_dict()
