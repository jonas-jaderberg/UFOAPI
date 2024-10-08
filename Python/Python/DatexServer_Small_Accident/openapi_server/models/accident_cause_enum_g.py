from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model import Model
from openapi_server.models.accident_cause_enum import AccidentCauseEnum
from openapi_server import util

from openapi_server.models.accident_cause_enum import AccidentCauseEnum  # noqa: E501

class AccidentCauseEnumG(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, value=None, extended_value_g=None):  # noqa: E501
        """AccidentCauseEnumG - a model defined in OpenAPI

        :param value: The value of this AccidentCauseEnumG.  # noqa: E501
        :type value: AccidentCauseEnum
        :param extended_value_g: The extended_value_g of this AccidentCauseEnumG.  # noqa: E501
        :type extended_value_g: str
        """
        self.openapi_types = {
            'value': AccidentCauseEnum,
            'extended_value_g': str
        }

        self.attribute_map = {
            'value': 'value',
            'extended_value_g': 'extendedValueG'
        }

        self._value = value
        self._extended_value_g = extended_value_g

    @classmethod
    def from_dict(cls, dikt) -> 'AccidentCauseEnumG':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The AccidentCauseEnumG of this AccidentCauseEnumG.  # noqa: E501
        :rtype: AccidentCauseEnumG
        """
        return util.deserialize_model(dikt, cls)

    @property
    def value(self) -> AccidentCauseEnum:
        """Gets the value of this AccidentCauseEnumG.


        :return: The value of this AccidentCauseEnumG.
        :rtype: AccidentCauseEnum
        """
        return self._value

    @value.setter
    def value(self, value: AccidentCauseEnum):
        """Sets the value of this AccidentCauseEnumG.


        :param value: The value of this AccidentCauseEnumG.
        :type value: AccidentCauseEnum
        """
        if value is None:
            raise ValueError("Invalid value for `value`, must not be `None`")  # noqa: E501

        self._value = value

    @property
    def extended_value_g(self) -> str:
        """Gets the extended_value_g of this AccidentCauseEnumG.


        :return: The extended_value_g of this AccidentCauseEnumG.
        :rtype: str
        """
        return self._extended_value_g

    @extended_value_g.setter
    def extended_value_g(self, extended_value_g: str):
        """Sets the extended_value_g of this AccidentCauseEnumG.


        :param extended_value_g: The extended_value_g of this AccidentCauseEnumG.
        :type extended_value_g: str
        """

        self._extended_value_g = extended_value_g
