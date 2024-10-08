from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model import Model
from openapi_server.models.multilingual_string import MultilingualString
from openapi_server.models.named_area_type_enum_g import NamedAreaTypeEnumG
from openapi_server import util

from openapi_server.models.multilingual_string import MultilingualString  # noqa: E501
from openapi_server.models.named_area_type_enum_g import NamedAreaTypeEnumG  # noqa: E501

class NamedArea(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, area_name=None, named_area_type=None, country=None, named_area_extension_g=None):  # noqa: E501
        """NamedArea - a model defined in OpenAPI

        :param area_name: The area_name of this NamedArea.  # noqa: E501
        :type area_name: MultilingualString
        :param named_area_type: The named_area_type of this NamedArea.  # noqa: E501
        :type named_area_type: NamedAreaTypeEnumG
        :param country: The country of this NamedArea.  # noqa: E501
        :type country: str
        :param named_area_extension_g: The named_area_extension_g of this NamedArea.  # noqa: E501
        :type named_area_extension_g: Dict[str, object]
        """
        self.openapi_types = {
            'area_name': MultilingualString,
            'named_area_type': NamedAreaTypeEnumG,
            'country': str,
            'named_area_extension_g': Dict[str, object]
        }

        self.attribute_map = {
            'area_name': 'areaName',
            'named_area_type': 'namedAreaType',
            'country': 'country',
            'named_area_extension_g': 'namedAreaExtensionG'
        }

        self._area_name = area_name
        self._named_area_type = named_area_type
        self._country = country
        self._named_area_extension_g = named_area_extension_g

    @classmethod
    def from_dict(cls, dikt) -> 'NamedArea':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The NamedArea of this NamedArea.  # noqa: E501
        :rtype: NamedArea
        """
        return util.deserialize_model(dikt, cls)

    @property
    def area_name(self) -> MultilingualString:
        """Gets the area_name of this NamedArea.


        :return: The area_name of this NamedArea.
        :rtype: MultilingualString
        """
        return self._area_name

    @area_name.setter
    def area_name(self, area_name: MultilingualString):
        """Sets the area_name of this NamedArea.


        :param area_name: The area_name of this NamedArea.
        :type area_name: MultilingualString
        """
        if area_name is None:
            raise ValueError("Invalid value for `area_name`, must not be `None`")  # noqa: E501

        self._area_name = area_name

    @property
    def named_area_type(self) -> NamedAreaTypeEnumG:
        """Gets the named_area_type of this NamedArea.


        :return: The named_area_type of this NamedArea.
        :rtype: NamedAreaTypeEnumG
        """
        return self._named_area_type

    @named_area_type.setter
    def named_area_type(self, named_area_type: NamedAreaTypeEnumG):
        """Sets the named_area_type of this NamedArea.


        :param named_area_type: The named_area_type of this NamedArea.
        :type named_area_type: NamedAreaTypeEnumG
        """

        self._named_area_type = named_area_type

    @property
    def country(self) -> str:
        """Gets the country of this NamedArea.


        :return: The country of this NamedArea.
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country: str):
        """Sets the country of this NamedArea.


        :param country: The country of this NamedArea.
        :type country: str
        """
        if country is not None and len(country) > 1024:
            raise ValueError("Invalid value for `country`, length must be less than or equal to `1024`")  # noqa: E501

        self._country = country

    @property
    def named_area_extension_g(self) -> Dict[str, object]:
        """Gets the named_area_extension_g of this NamedArea.


        :return: The named_area_extension_g of this NamedArea.
        :rtype: Dict[str, object]
        """
        return self._named_area_extension_g

    @named_area_extension_g.setter
    def named_area_extension_g(self, named_area_extension_g: Dict[str, object]):
        """Sets the named_area_extension_g of this NamedArea.


        :param named_area_extension_g: The named_area_extension_g of this NamedArea.
        :type named_area_extension_g: Dict[str, object]
        """

        self._named_area_extension_g = named_area_extension_g
