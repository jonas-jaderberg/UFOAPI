from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model import Model
from openapi_server import util


class InternationalIdentifier(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, country=None, national_identifier=None, international_identifier_extension_g=None):  # noqa: E501
        """InternationalIdentifier - a model defined in OpenAPI

        :param country: The country of this InternationalIdentifier.  # noqa: E501
        :type country: str
        :param national_identifier: The national_identifier of this InternationalIdentifier.  # noqa: E501
        :type national_identifier: str
        :param international_identifier_extension_g: The international_identifier_extension_g of this InternationalIdentifier.  # noqa: E501
        :type international_identifier_extension_g: Dict[str, object]
        """
        self.openapi_types = {
            'country': str,
            'national_identifier': str,
            'international_identifier_extension_g': Dict[str, object]
        }

        self.attribute_map = {
            'country': 'country',
            'national_identifier': 'nationalIdentifier',
            'international_identifier_extension_g': 'internationalIdentifierExtensionG'
        }

        self._country = country
        self._national_identifier = national_identifier
        self._international_identifier_extension_g = international_identifier_extension_g

    @classmethod
    def from_dict(cls, dikt) -> 'InternationalIdentifier':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The InternationalIdentifier of this InternationalIdentifier.  # noqa: E501
        :rtype: InternationalIdentifier
        """
        return util.deserialize_model(dikt, cls)

    @property
    def country(self) -> str:
        """Gets the country of this InternationalIdentifier.


        :return: The country of this InternationalIdentifier.
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country: str):
        """Sets the country of this InternationalIdentifier.


        :param country: The country of this InternationalIdentifier.
        :type country: str
        """
        if country is None:
            raise ValueError("Invalid value for `country`, must not be `None`")  # noqa: E501
        if country is not None and len(country) > 1024:
            raise ValueError("Invalid value for `country`, length must be less than or equal to `1024`")  # noqa: E501

        self._country = country

    @property
    def national_identifier(self) -> str:
        """Gets the national_identifier of this InternationalIdentifier.


        :return: The national_identifier of this InternationalIdentifier.
        :rtype: str
        """
        return self._national_identifier

    @national_identifier.setter
    def national_identifier(self, national_identifier: str):
        """Sets the national_identifier of this InternationalIdentifier.


        :param national_identifier: The national_identifier of this InternationalIdentifier.
        :type national_identifier: str
        """
        if national_identifier is None:
            raise ValueError("Invalid value for `national_identifier`, must not be `None`")  # noqa: E501
        if national_identifier is not None and len(national_identifier) > 1024:
            raise ValueError("Invalid value for `national_identifier`, length must be less than or equal to `1024`")  # noqa: E501

        self._national_identifier = national_identifier

    @property
    def international_identifier_extension_g(self) -> Dict[str, object]:
        """Gets the international_identifier_extension_g of this InternationalIdentifier.


        :return: The international_identifier_extension_g of this InternationalIdentifier.
        :rtype: Dict[str, object]
        """
        return self._international_identifier_extension_g

    @international_identifier_extension_g.setter
    def international_identifier_extension_g(self, international_identifier_extension_g: Dict[str, object]):
        """Sets the international_identifier_extension_g of this InternationalIdentifier.


        :param international_identifier_extension_g: The international_identifier_extension_g of this InternationalIdentifier.
        :type international_identifier_extension_g: Dict[str, object]
        """

        self._international_identifier_extension_g = international_identifier_extension_g
