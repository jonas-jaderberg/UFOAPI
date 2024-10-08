from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model import Model
from openapi_server.models.multilingual_string import MultilingualString
from openapi_server.models.named_area_type_enum_g import NamedAreaTypeEnumG
from openapi_server.models.nuts_code_type_enum_g import NutsCodeTypeEnumG
from openapi_server import util

from openapi_server.models.multilingual_string import MultilingualString  # noqa: E501
from openapi_server.models.named_area_type_enum_g import NamedAreaTypeEnumG  # noqa: E501
from openapi_server.models.nuts_code_type_enum_g import NutsCodeTypeEnumG  # noqa: E501

class NutsNamedArea(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, area_name=None, named_area_type=None, country=None, nuts_code_type=None, nuts_code=None, named_area_extension_g=None):  # noqa: E501
        """NutsNamedArea - a model defined in OpenAPI

        :param area_name: The area_name of this NutsNamedArea.  # noqa: E501
        :type area_name: MultilingualString
        :param named_area_type: The named_area_type of this NutsNamedArea.  # noqa: E501
        :type named_area_type: NamedAreaTypeEnumG
        :param country: The country of this NutsNamedArea.  # noqa: E501
        :type country: str
        :param nuts_code_type: The nuts_code_type of this NutsNamedArea.  # noqa: E501
        :type nuts_code_type: NutsCodeTypeEnumG
        :param nuts_code: The nuts_code of this NutsNamedArea.  # noqa: E501
        :type nuts_code: str
        :param named_area_extension_g: The named_area_extension_g of this NutsNamedArea.  # noqa: E501
        :type named_area_extension_g: Dict[str, object]
        """
        self.openapi_types = {
            'area_name': MultilingualString,
            'named_area_type': NamedAreaTypeEnumG,
            'country': str,
            'nuts_code_type': NutsCodeTypeEnumG,
            'nuts_code': str,
            'named_area_extension_g': Dict[str, object]
        }

        self.attribute_map = {
            'area_name': 'areaName',
            'named_area_type': 'namedAreaType',
            'country': 'country',
            'nuts_code_type': 'nutsCodeType',
            'nuts_code': 'nutsCode',
            'named_area_extension_g': 'namedAreaExtensionG'
        }

        self._area_name = area_name
        self._named_area_type = named_area_type
        self._country = country
        self._nuts_code_type = nuts_code_type
        self._nuts_code = nuts_code
        self._named_area_extension_g = named_area_extension_g

    @classmethod
    def from_dict(cls, dikt) -> 'NutsNamedArea':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The NutsNamedArea of this NutsNamedArea.  # noqa: E501
        :rtype: NutsNamedArea
        """
        return util.deserialize_model(dikt, cls)

    @property
    def area_name(self) -> MultilingualString:
        """Gets the area_name of this NutsNamedArea.


        :return: The area_name of this NutsNamedArea.
        :rtype: MultilingualString
        """
        return self._area_name

    @area_name.setter
    def area_name(self, area_name: MultilingualString):
        """Sets the area_name of this NutsNamedArea.


        :param area_name: The area_name of this NutsNamedArea.
        :type area_name: MultilingualString
        """
        if area_name is None:
            raise ValueError("Invalid value for `area_name`, must not be `None`")  # noqa: E501

        self._area_name = area_name

    @property
    def named_area_type(self) -> NamedAreaTypeEnumG:
        """Gets the named_area_type of this NutsNamedArea.


        :return: The named_area_type of this NutsNamedArea.
        :rtype: NamedAreaTypeEnumG
        """
        return self._named_area_type

    @named_area_type.setter
    def named_area_type(self, named_area_type: NamedAreaTypeEnumG):
        """Sets the named_area_type of this NutsNamedArea.


        :param named_area_type: The named_area_type of this NutsNamedArea.
        :type named_area_type: NamedAreaTypeEnumG
        """

        self._named_area_type = named_area_type

    @property
    def country(self) -> str:
        """Gets the country of this NutsNamedArea.


        :return: The country of this NutsNamedArea.
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country: str):
        """Sets the country of this NutsNamedArea.


        :param country: The country of this NutsNamedArea.
        :type country: str
        """
        if country is not None and len(country) > 1024:
            raise ValueError("Invalid value for `country`, length must be less than or equal to `1024`")  # noqa: E501

        self._country = country

    @property
    def nuts_code_type(self) -> NutsCodeTypeEnumG:
        """Gets the nuts_code_type of this NutsNamedArea.


        :return: The nuts_code_type of this NutsNamedArea.
        :rtype: NutsCodeTypeEnumG
        """
        return self._nuts_code_type

    @nuts_code_type.setter
    def nuts_code_type(self, nuts_code_type: NutsCodeTypeEnumG):
        """Sets the nuts_code_type of this NutsNamedArea.


        :param nuts_code_type: The nuts_code_type of this NutsNamedArea.
        :type nuts_code_type: NutsCodeTypeEnumG
        """
        if nuts_code_type is None:
            raise ValueError("Invalid value for `nuts_code_type`, must not be `None`")  # noqa: E501

        self._nuts_code_type = nuts_code_type

    @property
    def nuts_code(self) -> str:
        """Gets the nuts_code of this NutsNamedArea.


        :return: The nuts_code of this NutsNamedArea.
        :rtype: str
        """
        return self._nuts_code

    @nuts_code.setter
    def nuts_code(self, nuts_code: str):
        """Sets the nuts_code of this NutsNamedArea.


        :param nuts_code: The nuts_code of this NutsNamedArea.
        :type nuts_code: str
        """
        if nuts_code is None:
            raise ValueError("Invalid value for `nuts_code`, must not be `None`")  # noqa: E501
        if nuts_code is not None and len(nuts_code) > 1024:
            raise ValueError("Invalid value for `nuts_code`, length must be less than or equal to `1024`")  # noqa: E501

        self._nuts_code = nuts_code

    @property
    def named_area_extension_g(self) -> Dict[str, object]:
        """Gets the named_area_extension_g of this NutsNamedArea.


        :return: The named_area_extension_g of this NutsNamedArea.
        :rtype: Dict[str, object]
        """
        return self._named_area_extension_g

    @named_area_extension_g.setter
    def named_area_extension_g(self, named_area_extension_g: Dict[str, object]):
        """Sets the named_area_extension_g of this NutsNamedArea.


        :param named_area_extension_g: The named_area_extension_g of this NutsNamedArea.
        :type named_area_extension_g: Dict[str, object]
        """

        self._named_area_extension_g = named_area_extension_g
