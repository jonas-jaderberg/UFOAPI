from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model import Model
from openapi_server.models.vehicle_status_enum import VehicleStatusEnum
from openapi_server import util

from openapi_server.models.vehicle_status_enum import VehicleStatusEnum  # noqa: E501

class VehicleStatusEnumG(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, value=None, extended_value_g=None):  # noqa: E501
        """VehicleStatusEnumG - a model defined in OpenAPI

        :param value: The value of this VehicleStatusEnumG.  # noqa: E501
        :type value: VehicleStatusEnum
        :param extended_value_g: The extended_value_g of this VehicleStatusEnumG.  # noqa: E501
        :type extended_value_g: str
        """
        self.openapi_types = {
            'value': VehicleStatusEnum,
            'extended_value_g': str
        }

        self.attribute_map = {
            'value': 'value',
            'extended_value_g': 'extendedValueG'
        }

        self._value = value
        self._extended_value_g = extended_value_g

    @classmethod
    def from_dict(cls, dikt) -> 'VehicleStatusEnumG':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The VehicleStatusEnumG of this VehicleStatusEnumG.  # noqa: E501
        :rtype: VehicleStatusEnumG
        """
        return util.deserialize_model(dikt, cls)

    @property
    def value(self) -> VehicleStatusEnum:
        """Gets the value of this VehicleStatusEnumG.


        :return: The value of this VehicleStatusEnumG.
        :rtype: VehicleStatusEnum
        """
        return self._value

    @value.setter
    def value(self, value: VehicleStatusEnum):
        """Sets the value of this VehicleStatusEnumG.


        :param value: The value of this VehicleStatusEnumG.
        :type value: VehicleStatusEnum
        """
        if value is None:
            raise ValueError("Invalid value for `value`, must not be `None`")  # noqa: E501

        self._value = value

    @property
    def extended_value_g(self) -> str:
        """Gets the extended_value_g of this VehicleStatusEnumG.


        :return: The extended_value_g of this VehicleStatusEnumG.
        :rtype: str
        """
        return self._extended_value_g

    @extended_value_g.setter
    def extended_value_g(self, extended_value_g: str):
        """Sets the extended_value_g of this VehicleStatusEnumG.


        :param extended_value_g: The extended_value_g of this VehicleStatusEnumG.
        :type extended_value_g: str
        """

        self._extended_value_g = extended_value_g
