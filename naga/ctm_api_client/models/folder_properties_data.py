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


class FolderPropertiesData(object):
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
        'authorized_internal_users': 'list[str]',
        'authorized_external_users_and_groups': 'list[str]',
        'delete_files_after_download': 'bool',
        'notify_by_email_when_file_arrive': 'bool',
        'retention_policy': 'int',
        'size_limit': 'int',
        'allowed_file_pattern': 'str',
        'blocked_file_pattern': 'str',
        'access_type': 'str'
    }

    attribute_map = {
        'name': 'name',
        'authorized_internal_users': 'authorizedInternalUsers',
        'authorized_external_users_and_groups': 'authorizedExternalUsersAndGroups',
        'delete_files_after_download': 'deleteFilesAfterDownload',
        'notify_by_email_when_file_arrive': 'notifyByEmailWhenFileArrive',
        'retention_policy': 'retentionPolicy',
        'size_limit': 'sizeLimit',
        'allowed_file_pattern': 'allowedFilePattern',
        'blocked_file_pattern': 'blockedFilePattern',
        'access_type': 'accessType'
    }

    def __init__(self, name=None, authorized_internal_users=None, authorized_external_users_and_groups=None, delete_files_after_download=None, notify_by_email_when_file_arrive=None, retention_policy=None, size_limit=None, allowed_file_pattern=None, blocked_file_pattern=None, access_type=None, _configuration=None):  # noqa: E501
        """FolderPropertiesData - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._name = None
        self._authorized_internal_users = None
        self._authorized_external_users_and_groups = None
        self._delete_files_after_download = None
        self._notify_by_email_when_file_arrive = None
        self._retention_policy = None
        self._size_limit = None
        self._allowed_file_pattern = None
        self._blocked_file_pattern = None
        self._access_type = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if authorized_internal_users is not None:
            self.authorized_internal_users = authorized_internal_users
        if authorized_external_users_and_groups is not None:
            self.authorized_external_users_and_groups = authorized_external_users_and_groups
        if delete_files_after_download is not None:
            self.delete_files_after_download = delete_files_after_download
        if notify_by_email_when_file_arrive is not None:
            self.notify_by_email_when_file_arrive = notify_by_email_when_file_arrive
        if retention_policy is not None:
            self.retention_policy = retention_policy
        if size_limit is not None:
            self.size_limit = size_limit
        if allowed_file_pattern is not None:
            self.allowed_file_pattern = allowed_file_pattern
        if blocked_file_pattern is not None:
            self.blocked_file_pattern = blocked_file_pattern
        if access_type is not None:
            self.access_type = access_type

    @property
    def name(self):
        """Gets the name of this FolderPropertiesData.  # noqa: E501

        The name of the folder. REQUIRED:addMFTFolder | HIDDEN  # noqa: E501

        :return: The name of this FolderPropertiesData.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this FolderPropertiesData.

        The name of the folder. REQUIRED:addMFTFolder | HIDDEN  # noqa: E501

        :param name: The name of this FolderPropertiesData.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def authorized_internal_users(self):
        """Gets the authorized_internal_users of this FolderPropertiesData.  # noqa: E501

        Authorized Internal Users. HIDDEN  # noqa: E501

        :return: The authorized_internal_users of this FolderPropertiesData.  # noqa: E501
        :rtype: list[str]
        """
        return self._authorized_internal_users

    @authorized_internal_users.setter
    def authorized_internal_users(self, authorized_internal_users):
        """Sets the authorized_internal_users of this FolderPropertiesData.

        Authorized Internal Users. HIDDEN  # noqa: E501

        :param authorized_internal_users: The authorized_internal_users of this FolderPropertiesData.  # noqa: E501
        :type: list[str]
        """

        self._authorized_internal_users = authorized_internal_users

    @property
    def authorized_external_users_and_groups(self):
        """Gets the authorized_external_users_and_groups of this FolderPropertiesData.  # noqa: E501

        Authorized External Users And User Groups. HIDDEN  # noqa: E501

        :return: The authorized_external_users_and_groups of this FolderPropertiesData.  # noqa: E501
        :rtype: list[str]
        """
        return self._authorized_external_users_and_groups

    @authorized_external_users_and_groups.setter
    def authorized_external_users_and_groups(self, authorized_external_users_and_groups):
        """Sets the authorized_external_users_and_groups of this FolderPropertiesData.

        Authorized External Users And User Groups. HIDDEN  # noqa: E501

        :param authorized_external_users_and_groups: The authorized_external_users_and_groups of this FolderPropertiesData.  # noqa: E501
        :type: list[str]
        """

        self._authorized_external_users_and_groups = authorized_external_users_and_groups

    @property
    def delete_files_after_download(self):
        """Gets the delete_files_after_download of this FolderPropertiesData.  # noqa: E501

        Delete file after downloaded from incoming folder. HIDDEN  # noqa: E501

        :return: The delete_files_after_download of this FolderPropertiesData.  # noqa: E501
        :rtype: bool
        """
        return self._delete_files_after_download

    @delete_files_after_download.setter
    def delete_files_after_download(self, delete_files_after_download):
        """Sets the delete_files_after_download of this FolderPropertiesData.

        Delete file after downloaded from incoming folder. HIDDEN  # noqa: E501

        :param delete_files_after_download: The delete_files_after_download of this FolderPropertiesData.  # noqa: E501
        :type: bool
        """

        self._delete_files_after_download = delete_files_after_download

    @property
    def notify_by_email_when_file_arrive(self):
        """Gets the notify_by_email_when_file_arrive of this FolderPropertiesData.  # noqa: E501

        Send email notification to external users when a new file arrives. HIDDEN  # noqa: E501

        :return: The notify_by_email_when_file_arrive of this FolderPropertiesData.  # noqa: E501
        :rtype: bool
        """
        return self._notify_by_email_when_file_arrive

    @notify_by_email_when_file_arrive.setter
    def notify_by_email_when_file_arrive(self, notify_by_email_when_file_arrive):
        """Sets the notify_by_email_when_file_arrive of this FolderPropertiesData.

        Send email notification to external users when a new file arrives. HIDDEN  # noqa: E501

        :param notify_by_email_when_file_arrive: The notify_by_email_when_file_arrive of this FolderPropertiesData.  # noqa: E501
        :type: bool
        """

        self._notify_by_email_when_file_arrive = notify_by_email_when_file_arrive

    @property
    def retention_policy(self):
        """Gets the retention_policy of this FolderPropertiesData.  # noqa: E501

        Retention Time in hours. HIDDEN  # noqa: E501

        :return: The retention_policy of this FolderPropertiesData.  # noqa: E501
        :rtype: int
        """
        return self._retention_policy

    @retention_policy.setter
    def retention_policy(self, retention_policy):
        """Sets the retention_policy of this FolderPropertiesData.

        Retention Time in hours. HIDDEN  # noqa: E501

        :param retention_policy: The retention_policy of this FolderPropertiesData.  # noqa: E501
        :type: int
        """

        self._retention_policy = retention_policy

    @property
    def size_limit(self):
        """Gets the size_limit of this FolderPropertiesData.  # noqa: E501

        Size limit for folder (in Gigabyte). HIDDEN  # noqa: E501

        :return: The size_limit of this FolderPropertiesData.  # noqa: E501
        :rtype: int
        """
        return self._size_limit

    @size_limit.setter
    def size_limit(self, size_limit):
        """Sets the size_limit of this FolderPropertiesData.

        Size limit for folder (in Gigabyte). HIDDEN  # noqa: E501

        :param size_limit: The size_limit of this FolderPropertiesData.  # noqa: E501
        :type: int
        """

        self._size_limit = size_limit

    @property
    def allowed_file_pattern(self):
        """Gets the allowed_file_pattern of this FolderPropertiesData.  # noqa: E501

        allowed file pattern wildcard. HIDDEN  # noqa: E501

        :return: The allowed_file_pattern of this FolderPropertiesData.  # noqa: E501
        :rtype: str
        """
        return self._allowed_file_pattern

    @allowed_file_pattern.setter
    def allowed_file_pattern(self, allowed_file_pattern):
        """Sets the allowed_file_pattern of this FolderPropertiesData.

        allowed file pattern wildcard. HIDDEN  # noqa: E501

        :param allowed_file_pattern: The allowed_file_pattern of this FolderPropertiesData.  # noqa: E501
        :type: str
        """

        self._allowed_file_pattern = allowed_file_pattern

    @property
    def blocked_file_pattern(self):
        """Gets the blocked_file_pattern of this FolderPropertiesData.  # noqa: E501

        blocked file pattern wildcard. HIDDEN  # noqa: E501

        :return: The blocked_file_pattern of this FolderPropertiesData.  # noqa: E501
        :rtype: str
        """
        return self._blocked_file_pattern

    @blocked_file_pattern.setter
    def blocked_file_pattern(self, blocked_file_pattern):
        """Sets the blocked_file_pattern of this FolderPropertiesData.

        blocked file pattern wildcard. HIDDEN  # noqa: E501

        :param blocked_file_pattern: The blocked_file_pattern of this FolderPropertiesData.  # noqa: E501
        :type: str
        """

        self._blocked_file_pattern = blocked_file_pattern

    @property
    def access_type(self):
        """Gets the access_type of this FolderPropertiesData.  # noqa: E501

        Folder's access type (Limited, Unlimited). HIDDEN  # noqa: E501

        :return: The access_type of this FolderPropertiesData.  # noqa: E501
        :rtype: str
        """
        return self._access_type

    @access_type.setter
    def access_type(self, access_type):
        """Sets the access_type of this FolderPropertiesData.

        Folder's access type (Limited, Unlimited). HIDDEN  # noqa: E501

        :param access_type: The access_type of this FolderPropertiesData.  # noqa: E501
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
        if issubclass(FolderPropertiesData, dict):
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
        if not isinstance(other, FolderPropertiesData):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FolderPropertiesData):
            return True

        return self.to_dict() != other.to_dict()
