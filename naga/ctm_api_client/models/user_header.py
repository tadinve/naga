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


class UserHeader(object):
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
        'full_name': 'str',
        'description': 'str',
        'status': 'str',
        'last_updated': 'str',
        'created': 'str',
        'member_of': 'list[str]'
    }

    attribute_map = {
        'name': 'name',
        'full_name': 'fullName',
        'description': 'description',
        'status': 'status',
        'last_updated': 'lastUpdated',
        'created': 'created',
        'member_of': 'memberOf'
    }

    def __init__(self, name=None, full_name=None, description=None, status=None, last_updated=None, created=None, member_of=None, _configuration=None):  # noqa: E501
        """UserHeader - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._name = None
        self._full_name = None
        self._description = None
        self._status = None
        self._last_updated = None
        self._created = None
        self._member_of = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if full_name is not None:
            self.full_name = full_name
        if description is not None:
            self.description = description
        if status is not None:
            self.status = status
        if last_updated is not None:
            self.last_updated = last_updated
        if created is not None:
            self.created = created
        if member_of is not None:
            self.member_of = member_of

    @property
    def name(self):
        """Gets the name of this UserHeader.  # noqa: E501

        user name  # noqa: E501

        :return: The name of this UserHeader.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UserHeader.

        user name  # noqa: E501

        :param name: The name of this UserHeader.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def full_name(self):
        """Gets the full_name of this UserHeader.  # noqa: E501

        full user name  # noqa: E501

        :return: The full_name of this UserHeader.  # noqa: E501
        :rtype: str
        """
        return self._full_name

    @full_name.setter
    def full_name(self, full_name):
        """Sets the full_name of this UserHeader.

        full user name  # noqa: E501

        :param full_name: The full_name of this UserHeader.  # noqa: E501
        :type: str
        """

        self._full_name = full_name

    @property
    def description(self):
        """Gets the description of this UserHeader.  # noqa: E501

        user description  # noqa: E501

        :return: The description of this UserHeader.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UserHeader.

        user description  # noqa: E501

        :param description: The description of this UserHeader.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def status(self):
        """Gets the status of this UserHeader.  # noqa: E501

        user status (output only)  # noqa: E501

        :return: The status of this UserHeader.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this UserHeader.

        user status (output only)  # noqa: E501

        :param status: The status of this UserHeader.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def last_updated(self):
        """Gets the last_updated of this UserHeader.  # noqa: E501

        updated date (output only)  # noqa: E501

        :return: The last_updated of this UserHeader.  # noqa: E501
        :rtype: str
        """
        return self._last_updated

    @last_updated.setter
    def last_updated(self, last_updated):
        """Sets the last_updated of this UserHeader.

        updated date (output only)  # noqa: E501

        :param last_updated: The last_updated of this UserHeader.  # noqa: E501
        :type: str
        """

        self._last_updated = last_updated

    @property
    def created(self):
        """Gets the created of this UserHeader.  # noqa: E501

        create date (output only)  # noqa: E501

        :return: The created of this UserHeader.  # noqa: E501
        :rtype: str
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this UserHeader.

        create date (output only)  # noqa: E501

        :param created: The created of this UserHeader.  # noqa: E501
        :type: str
        """

        self._created = created

    @property
    def member_of(self):
        """Gets the member_of of this UserHeader.  # noqa: E501

        list of groups user belongs to  # noqa: E501

        :return: The member_of of this UserHeader.  # noqa: E501
        :rtype: list[str]
        """
        return self._member_of

    @member_of.setter
    def member_of(self, member_of):
        """Sets the member_of of this UserHeader.

        list of groups user belongs to  # noqa: E501

        :param member_of: The member_of of this UserHeader.  # noqa: E501
        :type: list[str]
        """

        self._member_of = member_of

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
        if issubclass(UserHeader, dict):
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
        if not isinstance(other, UserHeader):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UserHeader):
            return True

        return self.to_dict() != other.to_dict()
