from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model import Model
from openapi_server.models.emissions_extension import EmissionsExtension
from openapi_server import util

from openapi_server.models.emissions_extension import EmissionsExtension  # noqa: E501

class EmissionsExtensionTypeG(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, emissions_extension=None):  # noqa: E501
        """EmissionsExtensionTypeG - a model defined in OpenAPI

        :param emissions_extension: The emissions_extension of this EmissionsExtensionTypeG.  # noqa: E501
        :type emissions_extension: EmissionsExtension
        """
        self.openapi_types = {
            'emissions_extension': EmissionsExtension
        }

        self.attribute_map = {
            'emissions_extension': 'EmissionsExtension'
        }

        self._emissions_extension = emissions_extension

    @classmethod
    def from_dict(cls, dikt) -> 'EmissionsExtensionTypeG':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The EmissionsExtensionTypeG of this EmissionsExtensionTypeG.  # noqa: E501
        :rtype: EmissionsExtensionTypeG
        """
        return util.deserialize_model(dikt, cls)

    @property
    def emissions_extension(self) -> EmissionsExtension:
        """Gets the emissions_extension of this EmissionsExtensionTypeG.


        :return: The emissions_extension of this EmissionsExtensionTypeG.
        :rtype: EmissionsExtension
        """
        return self._emissions_extension

    @emissions_extension.setter
    def emissions_extension(self, emissions_extension: EmissionsExtension):
        """Sets the emissions_extension of this EmissionsExtensionTypeG.


        :param emissions_extension: The emissions_extension of this EmissionsExtensionTypeG.
        :type emissions_extension: EmissionsExtension
        """

        self._emissions_extension = emissions_extension
