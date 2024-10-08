from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model import Model
from openapi_server.models.person_category_enum import PersonCategoryEnum
from openapi_server import util

from openapi_server.models.person_category_enum import PersonCategoryEnum  # noqa: E501

class PersonCategoryEnumG(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, value=None, extended_value_g=None):  # noqa: E501
        """PersonCategoryEnumG - a model defined in OpenAPI

        :param value: The value of this PersonCategoryEnumG.  # noqa: E501
        :type value: PersonCategoryEnum
        :param extended_value_g: The extended_value_g of this PersonCategoryEnumG.  # noqa: E501
        :type extended_value_g: str
        """
        self.openapi_types = {
            'value': PersonCategoryEnum,
            'extended_value_g': str
        }

        self.attribute_map = {
            'value': 'value',
            'extended_value_g': 'extendedValueG'
        }

        self._value = value
        self._extended_value_g = extended_value_g

    @classmethod
    def from_dict(cls, dikt) -> 'PersonCategoryEnumG':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The PersonCategoryEnumG of this PersonCategoryEnumG.  # noqa: E501
        :rtype: PersonCategoryEnumG
        """
        return util.deserialize_model(dikt, cls)

    @property
    def value(self) -> PersonCategoryEnum:
        """Gets the value of this PersonCategoryEnumG.


        :return: The value of this PersonCategoryEnumG.
        :rtype: PersonCategoryEnum
        """
        return self._value

    @value.setter
    def value(self, value: PersonCategoryEnum):
        """Sets the value of this PersonCategoryEnumG.


        :param value: The value of this PersonCategoryEnumG.
        :type value: PersonCategoryEnum
        """
        if value is None:
            raise ValueError("Invalid value for `value`, must not be `None`")  # noqa: E501

        self._value = value

    @property
    def extended_value_g(self) -> str:
        """Gets the extended_value_g of this PersonCategoryEnumG.


        :return: The extended_value_g of this PersonCategoryEnumG.
        :rtype: str
        """
        return self._extended_value_g

    @extended_value_g.setter
    def extended_value_g(self, extended_value_g: str):
        """Sets the extended_value_g of this PersonCategoryEnumG.


        :param extended_value_g: The extended_value_g of this PersonCategoryEnumG.
        :type extended_value_g: str
        """

        self._extended_value_g = extended_value_g
