from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model import Model
from openapi_server.models.information_managed_resource_list import InformationManagedResourceList
from openapi_server import util

from openapi_server.models.information_managed_resource_list import InformationManagedResourceList  # noqa: E501

class InformationManagement(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, information_managed_resource_list=None, information_management_extension_g=None):  # noqa: E501
        """InformationManagement - a model defined in OpenAPI

        :param information_managed_resource_list: The information_managed_resource_list of this InformationManagement.  # noqa: E501
        :type information_managed_resource_list: InformationManagedResourceList
        :param information_management_extension_g: The information_management_extension_g of this InformationManagement.  # noqa: E501
        :type information_management_extension_g: Dict[str, object]
        """
        self.openapi_types = {
            'information_managed_resource_list': InformationManagedResourceList,
            'information_management_extension_g': Dict[str, object]
        }

        self.attribute_map = {
            'information_managed_resource_list': 'informationManagedResourceList',
            'information_management_extension_g': 'informationManagementExtensionG'
        }

        self._information_managed_resource_list = information_managed_resource_list
        self._information_management_extension_g = information_management_extension_g

    @classmethod
    def from_dict(cls, dikt) -> 'InformationManagement':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The InformationManagement of this InformationManagement.  # noqa: E501
        :rtype: InformationManagement
        """
        return util.deserialize_model(dikt, cls)

    @property
    def information_managed_resource_list(self) -> InformationManagedResourceList:
        """Gets the information_managed_resource_list of this InformationManagement.


        :return: The information_managed_resource_list of this InformationManagement.
        :rtype: InformationManagedResourceList
        """
        return self._information_managed_resource_list

    @information_managed_resource_list.setter
    def information_managed_resource_list(self, information_managed_resource_list: InformationManagedResourceList):
        """Sets the information_managed_resource_list of this InformationManagement.


        :param information_managed_resource_list: The information_managed_resource_list of this InformationManagement.
        :type information_managed_resource_list: InformationManagedResourceList
        """

        self._information_managed_resource_list = information_managed_resource_list

    @property
    def information_management_extension_g(self) -> Dict[str, object]:
        """Gets the information_management_extension_g of this InformationManagement.


        :return: The information_management_extension_g of this InformationManagement.
        :rtype: Dict[str, object]
        """
        return self._information_management_extension_g

    @information_management_extension_g.setter
    def information_management_extension_g(self, information_management_extension_g: Dict[str, object]):
        """Sets the information_management_extension_g of this InformationManagement.


        :param information_management_extension_g: The information_management_extension_g of this InformationManagement.
        :type information_management_extension_g: Dict[str, object]
        """

        self._information_management_extension_g = information_management_extension_g
