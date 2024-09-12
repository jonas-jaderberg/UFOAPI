from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model import Model
from openapi_server.models.multi_lingual_string_value import MultiLingualStringValue
from openapi_server import util

from openapi_server.models.multi_lingual_string_value import MultiLingualStringValue  # noqa: E501

class MultilingualString(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, values=None):  # noqa: E501
        """MultilingualString - a model defined in OpenAPI

        :param values: The values of this MultilingualString.  # noqa: E501
        :type values: List[MultiLingualStringValue]
        """
        self.openapi_types = {
            'values': List[MultiLingualStringValue]
        }

        self.attribute_map = {
            'values': 'values'
        }

        self._values = values

    @classmethod
    def from_dict(cls, dikt) -> 'MultilingualString':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The MultilingualString of this MultilingualString.  # noqa: E501
        :rtype: MultilingualString
        """
        return util.deserialize_model(dikt, cls)

    @property
    def values(self) -> List[MultiLingualStringValue]:
        """Gets the values of this MultilingualString.


        :return: The values of this MultilingualString.
        :rtype: List[MultiLingualStringValue]
        """
        return self._values

    @values.setter
    def values(self, values: List[MultiLingualStringValue]):
        """Sets the values of this MultilingualString.


        :param values: The values of this MultilingualString.
        :type values: List[MultiLingualStringValue]
        """

        self._values = values
