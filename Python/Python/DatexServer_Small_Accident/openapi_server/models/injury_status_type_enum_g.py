from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model import Model
from openapi_server.models.injury_status_type_enum import InjuryStatusTypeEnum
from openapi_server import util

from openapi_server.models.injury_status_type_enum import InjuryStatusTypeEnum  # noqa: E501

class InjuryStatusTypeEnumG(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, value=None, extended_value_g=None):  # noqa: E501
        """InjuryStatusTypeEnumG - a model defined in OpenAPI

        :param value: The value of this InjuryStatusTypeEnumG.  # noqa: E501
        :type value: InjuryStatusTypeEnum
        :param extended_value_g: The extended_value_g of this InjuryStatusTypeEnumG.  # noqa: E501
        :type extended_value_g: str
        """
        self.openapi_types = {
            'value': InjuryStatusTypeEnum,
            'extended_value_g': str
        }

        self.attribute_map = {
            'value': 'value',
            'extended_value_g': 'extendedValueG'
        }

        self._value = value
        self._extended_value_g = extended_value_g

    @classmethod
    def from_dict(cls, dikt) -> 'InjuryStatusTypeEnumG':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The InjuryStatusTypeEnumG of this InjuryStatusTypeEnumG.  # noqa: E501
        :rtype: InjuryStatusTypeEnumG
        """
        return util.deserialize_model(dikt, cls)

    @property
    def value(self) -> InjuryStatusTypeEnum:
        """Gets the value of this InjuryStatusTypeEnumG.


        :return: The value of this InjuryStatusTypeEnumG.
        :rtype: InjuryStatusTypeEnum
        """
        return self._value

    @value.setter
    def value(self, value: InjuryStatusTypeEnum):
        """Sets the value of this InjuryStatusTypeEnumG.


        :param value: The value of this InjuryStatusTypeEnumG.
        :type value: InjuryStatusTypeEnum
        """
        if value is None:
            raise ValueError("Invalid value for `value`, must not be `None`")  # noqa: E501

        self._value = value

    @property
    def extended_value_g(self) -> str:
        """Gets the extended_value_g of this InjuryStatusTypeEnumG.


        :return: The extended_value_g of this InjuryStatusTypeEnumG.
        :rtype: str
        """
        return self._extended_value_g

    @extended_value_g.setter
    def extended_value_g(self, extended_value_g: str):
        """Sets the extended_value_g of this InjuryStatusTypeEnumG.


        :param extended_value_g: The extended_value_g of this InjuryStatusTypeEnumG.
        :type extended_value_g: str
        """

        self._extended_value_g = extended_value_g
