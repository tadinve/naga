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


class ActiveServices(object):
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
        'service_last_updated_time': 'str',
        'active_services': 'list[SLAService]'
    }

    attribute_map = {
        'service_last_updated_time': 'serviceLastUpdatedTime',
        'active_services': 'activeServices'
    }

    def __init__(self, service_last_updated_time=None, active_services=None, _configuration=None):  # noqa: E501
        """ActiveServices - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._service_last_updated_time = None
        self._active_services = None
        self.discriminator = None

        if service_last_updated_time is not None:
            self.service_last_updated_time = service_last_updated_time
        if active_services is not None:
            self.active_services = active_services

    @property
    def service_last_updated_time(self):
        """Gets the service_last_updated_time of this ActiveServices.  # noqa: E501


        :return: The service_last_updated_time of this ActiveServices.  # noqa: E501
        :rtype: str
        """
        return self._service_last_updated_time

    @service_last_updated_time.setter
    def service_last_updated_time(self, service_last_updated_time):
        """Sets the service_last_updated_time of this ActiveServices.


        :param service_last_updated_time: The service_last_updated_time of this ActiveServices.  # noqa: E501
        :type: str
        """

        self._service_last_updated_time = service_last_updated_time

    @property
    def active_services(self):
        """Gets the active_services of this ActiveServices.  # noqa: E501


        :return: The active_services of this ActiveServices.  # noqa: E501
        :rtype: list[SLAService]
        """
        return self._active_services

    @active_services.setter
    def active_services(self, active_services):
        """Sets the active_services of this ActiveServices.


        :param active_services: The active_services of this ActiveServices.  # noqa: E501
        :type: list[SLAService]
        """

        self._active_services = active_services

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
        if issubclass(ActiveServices, dict):
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
        if not isinstance(other, ActiveServices):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ActiveServices):
            return True

        return self.to_dict() != other.to_dict()
