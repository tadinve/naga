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


class FolderProperties(object):
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
        'allowed_internal_user_names': 'list[str]',
        'allowed_user_names': 'list[str]',
        'allowed_group_names': 'list[str]',
        'delete_files_after_processing': 'bool',
        'notify_by_email_when_file_arrived': 'bool',
        'retention_hours': 'int',
        'size_limit': 'int',
        'allowed_file_pattern': 'str',
        'exclude_file_pattern': 'str',
        'access_type': 'str'
    }

    attribute_map = {
        'name': 'name',
        'allowed_internal_user_names': 'allowedInternalUserNames',
        'allowed_user_names': 'allowedUserNames',
        'allowed_group_names': 'allowedGroupNames',
        'delete_files_after_processing': 'deleteFilesAfterProcessing',
        'notify_by_email_when_file_arrived': 'notifyByEmailWhenFileArrived',
        'retention_hours': 'retentionHours',
        'size_limit': 'sizeLimit',
        'allowed_file_pattern': 'allowedFilePattern',
        'exclude_file_pattern': 'excludeFilePattern',
        'access_type': 'accessType'
    }

    def __init__(self, name=None, allowed_internal_user_names=None, allowed_user_names=None, allowed_group_names=None, delete_files_after_processing=None, notify_by_email_when_file_arrived=None, retention_hours=None, size_limit=None, allowed_file_pattern=None, exclude_file_pattern=None, access_type=None, _configuration=None):  # noqa: E501
        """FolderProperties - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._name = None
        self._allowed_internal_user_names = None
        self._allowed_user_names = None
        self._allowed_group_names = None
        self._delete_files_after_processing = None
        self._notify_by_email_when_file_arrived = None
        self._retention_hours = None
        self._size_limit = None
        self._allowed_file_pattern = None
        self._exclude_file_pattern = None
        self._access_type = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if allowed_internal_user_names is not None:
            self.allowed_internal_user_names = allowed_internal_user_names
        if allowed_user_names is not None:
            self.allowed_user_names = allowed_user_names
        if allowed_group_names is not None:
            self.allowed_group_names = allowed_group_names
        if delete_files_after_processing is not None:
            self.delete_files_after_processing = delete_files_after_processing
        if notify_by_email_when_file_arrived is not None:
            self.notify_by_email_when_file_arrived = notify_by_email_when_file_arrived
        if retention_hours is not None:
            self.retention_hours = retention_hours
        if size_limit is not None:
            self.size_limit = size_limit
        if allowed_file_pattern is not None:
            self.allowed_file_pattern = allowed_file_pattern
        if exclude_file_pattern is not None:
            self.exclude_file_pattern = exclude_file_pattern
        if access_type is not None:
            self.access_type = access_type

    @property
    def name(self):
        """Gets the name of this FolderProperties.  # noqa: E501

        The name of the folder. REQUIRED:addMFTFolder | HIDDEN  # noqa: E501

        :return: The name of this FolderProperties.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this FolderProperties.

        The name of the folder. REQUIRED:addMFTFolder | HIDDEN  # noqa: E501

        :param name: The name of this FolderProperties.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def allowed_internal_user_names(self):
        """Gets the allowed_internal_user_names of this FolderProperties.  # noqa: E501

        Authorized Internal Users. HIDDEN  # noqa: E501

        :return: The allowed_internal_user_names of this FolderProperties.  # noqa: E501
        :rtype: list[str]
        """
        return self._allowed_internal_user_names

    @allowed_internal_user_names.setter
    def allowed_internal_user_names(self, allowed_internal_user_names):
        """Sets the allowed_internal_user_names of this FolderProperties.

        Authorized Internal Users. HIDDEN  # noqa: E501

        :param allowed_internal_user_names: The allowed_internal_user_names of this FolderProperties.  # noqa: E501
        :type: list[str]
        """

        self._allowed_internal_user_names = allowed_internal_user_names

    @property
    def allowed_user_names(self):
        """Gets the allowed_user_names of this FolderProperties.  # noqa: E501

        Authorized External Users And User Groups. HIDDEN  # noqa: E501

        :return: The allowed_user_names of this FolderProperties.  # noqa: E501
        :rtype: list[str]
        """
        return self._allowed_user_names

    @allowed_user_names.setter
    def allowed_user_names(self, allowed_user_names):
        """Sets the allowed_user_names of this FolderProperties.

        Authorized External Users And User Groups. HIDDEN  # noqa: E501

        :param allowed_user_names: The allowed_user_names of this FolderProperties.  # noqa: E501
        :type: list[str]
        """

        self._allowed_user_names = allowed_user_names

    @property
    def allowed_group_names(self):
        """Gets the allowed_group_names of this FolderProperties.  # noqa: E501

        Array of allowed group names. HIDDEN  # noqa: E501

        :return: The allowed_group_names of this FolderProperties.  # noqa: E501
        :rtype: list[str]
        """
        return self._allowed_group_names

    @allowed_group_names.setter
    def allowed_group_names(self, allowed_group_names):
        """Sets the allowed_group_names of this FolderProperties.

        Array of allowed group names. HIDDEN  # noqa: E501

        :param allowed_group_names: The allowed_group_names of this FolderProperties.  # noqa: E501
        :type: list[str]
        """

        self._allowed_group_names = allowed_group_names

    @property
    def delete_files_after_processing(self):
        """Gets the delete_files_after_processing of this FolderProperties.  # noqa: E501

        Delete file after downloaded from incoming folder. HIDDEN  # noqa: E501

        :return: The delete_files_after_processing of this FolderProperties.  # noqa: E501
        :rtype: bool
        """
        return self._delete_files_after_processing

    @delete_files_after_processing.setter
    def delete_files_after_processing(self, delete_files_after_processing):
        """Sets the delete_files_after_processing of this FolderProperties.

        Delete file after downloaded from incoming folder. HIDDEN  # noqa: E501

        :param delete_files_after_processing: The delete_files_after_processing of this FolderProperties.  # noqa: E501
        :type: bool
        """

        self._delete_files_after_processing = delete_files_after_processing

    @property
    def notify_by_email_when_file_arrived(self):
        """Gets the notify_by_email_when_file_arrived of this FolderProperties.  # noqa: E501

        Send email notification to external users when a new file arrives. HIDDEN  # noqa: E501

        :return: The notify_by_email_when_file_arrived of this FolderProperties.  # noqa: E501
        :rtype: bool
        """
        return self._notify_by_email_when_file_arrived

    @notify_by_email_when_file_arrived.setter
    def notify_by_email_when_file_arrived(self, notify_by_email_when_file_arrived):
        """Sets the notify_by_email_when_file_arrived of this FolderProperties.

        Send email notification to external users when a new file arrives. HIDDEN  # noqa: E501

        :param notify_by_email_when_file_arrived: The notify_by_email_when_file_arrived of this FolderProperties.  # noqa: E501
        :type: bool
        """

        self._notify_by_email_when_file_arrived = notify_by_email_when_file_arrived

    @property
    def retention_hours(self):
        """Gets the retention_hours of this FolderProperties.  # noqa: E501

        Retention Time in hours. HIDDEN  # noqa: E501

        :return: The retention_hours of this FolderProperties.  # noqa: E501
        :rtype: int
        """
        return self._retention_hours

    @retention_hours.setter
    def retention_hours(self, retention_hours):
        """Sets the retention_hours of this FolderProperties.

        Retention Time in hours. HIDDEN  # noqa: E501

        :param retention_hours: The retention_hours of this FolderProperties.  # noqa: E501
        :type: int
        """

        self._retention_hours = retention_hours

    @property
    def size_limit(self):
        """Gets the size_limit of this FolderProperties.  # noqa: E501

        Size limit for folder (in Gigabyte). HIDDEN  # noqa: E501

        :return: The size_limit of this FolderProperties.  # noqa: E501
        :rtype: int
        """
        return self._size_limit

    @size_limit.setter
    def size_limit(self, size_limit):
        """Sets the size_limit of this FolderProperties.

        Size limit for folder (in Gigabyte). HIDDEN  # noqa: E501

        :param size_limit: The size_limit of this FolderProperties.  # noqa: E501
        :type: int
        """

        self._size_limit = size_limit

    @property
    def allowed_file_pattern(self):
        """Gets the allowed_file_pattern of this FolderProperties.  # noqa: E501

        allowed file pattern wildcard. HIDDEN  # noqa: E501

        :return: The allowed_file_pattern of this FolderProperties.  # noqa: E501
        :rtype: str
        """
        return self._allowed_file_pattern

    @allowed_file_pattern.setter
    def allowed_file_pattern(self, allowed_file_pattern):
        """Sets the allowed_file_pattern of this FolderProperties.

        allowed file pattern wildcard. HIDDEN  # noqa: E501

        :param allowed_file_pattern: The allowed_file_pattern of this FolderProperties.  # noqa: E501
        :type: str
        """

        self._allowed_file_pattern = allowed_file_pattern

    @property
    def exclude_file_pattern(self):
        """Gets the exclude_file_pattern of this FolderProperties.  # noqa: E501

        blocked file pattern wildcard. HIDDEN  # noqa: E501

        :return: The exclude_file_pattern of this FolderProperties.  # noqa: E501
        :rtype: str
        """
        return self._exclude_file_pattern

    @exclude_file_pattern.setter
    def exclude_file_pattern(self, exclude_file_pattern):
        """Sets the exclude_file_pattern of this FolderProperties.

        blocked file pattern wildcard. HIDDEN  # noqa: E501

        :param exclude_file_pattern: The exclude_file_pattern of this FolderProperties.  # noqa: E501
        :type: str
        """

        self._exclude_file_pattern = exclude_file_pattern

    @property
    def access_type(self):
        """Gets the access_type of this FolderProperties.  # noqa: E501

        Folder's access type (Limited, Unlimited). HIDDEN  # noqa: E501

        :return: The access_type of this FolderProperties.  # noqa: E501
        :rtype: str
        """
        return self._access_type

    @access_type.setter
    def access_type(self, access_type):
        """Sets the access_type of this FolderProperties.

        Folder's access type (Limited, Unlimited). HIDDEN  # noqa: E501

        :param access_type: The access_type of this FolderProperties.  # noqa: E501
        :type: str
        """

        self._access_type = access_type

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
        if issubclass(FolderProperties, dict):
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
        if not isinstance(other, FolderProperties):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FolderProperties):
            return True

        return self.to_dict() != other.to_dict()
