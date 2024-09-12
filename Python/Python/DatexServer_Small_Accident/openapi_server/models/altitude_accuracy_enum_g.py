from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model import Model
from openapi_server.models.altitude_accuracy_enum import AltitudeAccuracyEnum
from openapi_server import util

from openapi_server.models.altitude_accuracy_enum import AltitudeAccuracyEnum  # noqa: E501

class AltitudeAccuracyEnumG(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, value=None, extended_value_g=None):  # noqa: E501
        """AltitudeAccuracyEnumG - a model defined in OpenAPI

        :param value: The value of this AltitudeAccuracyEnumG.  # noqa: E501
        :type value: AltitudeAccuracyEnum
        :param extended_value_g: The extended_value_g of this AltitudeAccuracyEnumG.  # noqa: E501
        :type extended_value_g: str
        """
        self.openapi_types = {
            'value': AltitudeAccuracyEnum,
            'extended_value_g': str
        }

        self.attribute_map = {
            'value': 'value',
            'extended_value_g': 'extendedValueG'
        }

        self._value = value
        self._extended_value_g = extended_value_g

    @classmethod
    def from_dict(cls, dikt) -> 'AltitudeAccuracyEnumG':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The AltitudeAccuracyEnumG of this AltitudeAccuracyEnumG.  # noqa: E501
        :rtype: AltitudeAccuracyEnumG
        """
        return util.deserialize_model(dikt, cls)

    @property
    def value(self) -> AltitudeAccuracyEnum:
        """Gets the value of this AltitudeAccuracyEnumG.


        :return: The value of this AltitudeAccuracyEnumG.
        :rtype: AltitudeAccuracyEnum
        """
        return self._value

    @value.setter
    def value(self, value: AltitudeAccuracyEnum):
        """Sets the value of this AltitudeAccuracyEnumG.


        :param value: The value of this AltitudeAccuracyEnumG.
        :type value: AltitudeAccuracyEnum
        """
        if value is None:
            raise ValueError("Invalid value for `value`, must not be `None`")  # noqa: E501

        self._value = value

    @property
    def extended_value_g(self) -> str:
        """Gets the extended_value_g of this AltitudeAccuracyEnumG.


        :return: The extended_value_g of this AltitudeAccuracyEnumG.
        :rtype: str
        """
        return self._extended_value_g

    @extended_value_g.setter
    def extended_value_g(self, extended_value_g: str):
        """Sets the extended_value_g of this AltitudeAccuracyEnumG.


        :param extended_value_g: The extended_value_g of this AltitudeAccuracyEnumG.
        :type extended_value_g: str
        """

        self._extended_value_g = extended_value_g
