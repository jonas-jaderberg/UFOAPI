from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model import Model
from openapi_server.models.collision_type_enum import CollisionTypeEnum
from openapi_server import util

from openapi_server.models.collision_type_enum import CollisionTypeEnum  # noqa: E501

class CollisionTypeEnumG(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, value=None, extended_value_g=None):  # noqa: E501
        """CollisionTypeEnumG - a model defined in OpenAPI

        :param value: The value of this CollisionTypeEnumG.  # noqa: E501
        :type value: CollisionTypeEnum
        :param extended_value_g: The extended_value_g of this CollisionTypeEnumG.  # noqa: E501
        :type extended_value_g: str
        """
        self.openapi_types = {
            'value': CollisionTypeEnum,
            'extended_value_g': str
        }

        self.attribute_map = {
            'value': 'value',
            'extended_value_g': 'extendedValueG'
        }

        self._value = value
        self._extended_value_g = extended_value_g

    @classmethod
    def from_dict(cls, dikt) -> 'CollisionTypeEnumG':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The CollisionTypeEnumG of this CollisionTypeEnumG.  # noqa: E501
        :rtype: CollisionTypeEnumG
        """
        return util.deserialize_model(dikt, cls)

    @property
    def value(self) -> CollisionTypeEnum:
        """Gets the value of this CollisionTypeEnumG.


        :return: The value of this CollisionTypeEnumG.
        :rtype: CollisionTypeEnum
        """
        return self._value

    @value.setter
    def value(self, value: CollisionTypeEnum):
        """Sets the value of this CollisionTypeEnumG.


        :param value: The value of this CollisionTypeEnumG.
        :type value: CollisionTypeEnum
        """
        if value is None:
            raise ValueError("Invalid value for `value`, must not be `None`")  # noqa: E501

        self._value = value

    @property
    def extended_value_g(self) -> str:
        """Gets the extended_value_g of this CollisionTypeEnumG.


        :return: The extended_value_g of this CollisionTypeEnumG.
        :rtype: str
        """
        return self._extended_value_g

    @extended_value_g.setter
    def extended_value_g(self, extended_value_g: str):
        """Sets the extended_value_g of this CollisionTypeEnumG.


        :param extended_value_g: The extended_value_g of this CollisionTypeEnumG.
        :type extended_value_g: str
        """

        self._extended_value_g = extended_value_g
