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

from ctm-python-client.ctm_api_client.configuration import Configuration


class FtsAuthenticationDetails(object):
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
        'ldap_authentication_details': 'FtsLdapAuthenticationDetails',
        'pam_authentication_details': 'FtsPamAuthenticationDetails'
    }

    attribute_map = {
        'ldap_authentication_details': 'ldapAuthenticationDetails',
        'pam_authentication_details': 'pamAuthenticationDetails'
    }

    def __init__(self, ldap_authentication_details=None, pam_authentication_details=None, _configuration=None):  # noqa: E501
        """FtsAuthenticationDetails - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._ldap_authentication_details = None
        self._pam_authentication_details = None
        self.discriminator = None

        if ldap_authentication_details is not None:
            self.ldap_authentication_details = ldap_authentication_details
        if pam_authentication_details is not None:
            self.pam_authentication_details = pam_authentication_details

    @property
    def ldap_authentication_details(self):
        """Gets the ldap_authentication_details of this FtsAuthenticationDetails.  # noqa: E501


        :return: The ldap_authentication_details of this FtsAuthenticationDetails.  # noqa: E501
        :rtype: FtsLdapAuthenticationDetails
        """
        return self._ldap_authentication_details

    @ldap_authentication_details.setter
    def ldap_authentication_details(self, ldap_authentication_details):
        """Sets the ldap_authentication_details of this FtsAuthenticationDetails.


        :param ldap_authentication_details: The ldap_authentication_details of this FtsAuthenticationDetails.  # noqa: E501
        :type: FtsLdapAuthenticationDetails
        """

        self._ldap_authentication_details = ldap_authentication_details

    @property
    def pam_authentication_details(self):
        """Gets the pam_authentication_details of this FtsAuthenticationDetails.  # noqa: E501


        :return: The pam_authentication_details of this FtsAuthenticationDetails.  # noqa: E501
        :rtype: FtsPamAuthenticationDetails
        """
        return self._pam_authentication_details

    @pam_authentication_details.setter
    def pam_authentication_details(self, pam_authentication_details):
        """Sets the pam_authentication_details of this FtsAuthenticationDetails.


        :param pam_authentication_details: The pam_authentication_details of this FtsAuthenticationDetails.  # noqa: E501
        :type: FtsPamAuthenticationDetails
        """

        self._pam_authentication_details = pam_authentication_details

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
        if issubclass(FtsAuthenticationDetails, dict):
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
        if not isinstance(other, FtsAuthenticationDetails):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FtsAuthenticationDetails):
            return True

        return self.to_dict() != other.to_dict()