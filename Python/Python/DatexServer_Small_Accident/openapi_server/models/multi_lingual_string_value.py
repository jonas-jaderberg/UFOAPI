from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model import Model
from openapi_server import util


class MultiLingualStringValue(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, lang=None, value=None):  # noqa: E501
        """MultiLingualStringValue - a model defined in OpenAPI

        :param lang: The lang of this MultiLingualStringValue.  # noqa: E501
        :type lang: str
        :param value: The value of this MultiLingualStringValue.  # noqa: E501
        :type value: str
        """
        self.openapi_types = {
            'lang': str,
            'value': str
        }

        self.attribute_map = {
            'lang': 'lang',
            'value': 'value'
        }

        self._lang = lang
        self._value = value

    @classmethod
    def from_dict(cls, dikt) -> 'MultiLingualStringValue':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The MultiLingualStringValue of this MultiLingualStringValue.  # noqa: E501
        :rtype: MultiLingualStringValue
        """
        return util.deserialize_model(dikt, cls)

    @property
    def lang(self) -> str:
        """Gets the lang of this MultiLingualStringValue.


        :return: The lang of this MultiLingualStringValue.
        :rtype: str
        """
        return self._lang

    @lang.setter
    def lang(self, lang: str):
        """Sets the lang of this MultiLingualStringValue.


        :param lang: The lang of this MultiLingualStringValue.
        :type lang: str
        """
        if lang is None:
            raise ValueError("Invalid value for `lang`, must not be `None`")  # noqa: E501

        self._lang = lang

    @property
    def value(self) -> str:
        """Gets the value of this MultiLingualStringValue.


        :return: The value of this MultiLingualStringValue.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value: str):
        """Sets the value of this MultiLingualStringValue.


        :param value: The value of this MultiLingualStringValue.
        :type value: str
        """
        if value is None:
            raise ValueError("Invalid value for `value`, must not be `None`")  # noqa: E501

        self._value = value
