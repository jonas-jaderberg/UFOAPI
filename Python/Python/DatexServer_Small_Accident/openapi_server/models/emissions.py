from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model import Model
from openapi_server.models.emission_classification_euro_enum_g import EmissionClassificationEuroEnumG
from openapi_server.models.emissions_extension_type_g import EmissionsExtensionTypeG
from openapi_server.models.low_emission_level_enum_g import LowEmissionLevelEnumG
from openapi_server import util

from openapi_server.models.emission_classification_euro_enum_g import EmissionClassificationEuroEnumG  # noqa: E501
from openapi_server.models.emissions_extension_type_g import EmissionsExtensionTypeG  # noqa: E501
from openapi_server.models.low_emission_level_enum_g import LowEmissionLevelEnumG  # noqa: E501

class Emissions(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, emission_classification_euro=None, emission_classification_other=None, emission_level=None, emissions_extension_g=None):  # noqa: E501
        """Emissions - a model defined in OpenAPI

        :param emission_classification_euro: The emission_classification_euro of this Emissions.  # noqa: E501
        :type emission_classification_euro: EmissionClassificationEuroEnumG
        :param emission_classification_other: The emission_classification_other of this Emissions.  # noqa: E501
        :type emission_classification_other: List[str]
        :param emission_level: The emission_level of this Emissions.  # noqa: E501
        :type emission_level: LowEmissionLevelEnumG
        :param emissions_extension_g: The emissions_extension_g of this Emissions.  # noqa: E501
        :type emissions_extension_g: EmissionsExtensionTypeG
        """
        self.openapi_types = {
            'emission_classification_euro': EmissionClassificationEuroEnumG,
            'emission_classification_other': List[str],
            'emission_level': LowEmissionLevelEnumG,
            'emissions_extension_g': EmissionsExtensionTypeG
        }

        self.attribute_map = {
            'emission_classification_euro': 'emissionClassificationEuro',
            'emission_classification_other': 'emissionClassificationOther',
            'emission_level': 'emissionLevel',
            'emissions_extension_g': 'emissionsExtensionG'
        }

        self._emission_classification_euro = emission_classification_euro
        self._emission_classification_other = emission_classification_other
        self._emission_level = emission_level
        self._emissions_extension_g = emissions_extension_g

    @classmethod
    def from_dict(cls, dikt) -> 'Emissions':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Emissions of this Emissions.  # noqa: E501
        :rtype: Emissions
        """
        return util.deserialize_model(dikt, cls)

    @property
    def emission_classification_euro(self) -> EmissionClassificationEuroEnumG:
        """Gets the emission_classification_euro of this Emissions.


        :return: The emission_classification_euro of this Emissions.
        :rtype: EmissionClassificationEuroEnumG
        """
        return self._emission_classification_euro

    @emission_classification_euro.setter
    def emission_classification_euro(self, emission_classification_euro: EmissionClassificationEuroEnumG):
        """Sets the emission_classification_euro of this Emissions.


        :param emission_classification_euro: The emission_classification_euro of this Emissions.
        :type emission_classification_euro: EmissionClassificationEuroEnumG
        """

        self._emission_classification_euro = emission_classification_euro

    @property
    def emission_classification_other(self) -> List[str]:
        """Gets the emission_classification_other of this Emissions.


        :return: The emission_classification_other of this Emissions.
        :rtype: List[str]
        """
        return self._emission_classification_other

    @emission_classification_other.setter
    def emission_classification_other(self, emission_classification_other: List[str]):
        """Sets the emission_classification_other of this Emissions.


        :param emission_classification_other: The emission_classification_other of this Emissions.
        :type emission_classification_other: List[str]
        """
        if emission_classification_other is not None and len(emission_classification_other) < 0:
            raise ValueError("Invalid value for `emission_classification_other`, number of items must be greater than or equal to `0`")  # noqa: E501

        self._emission_classification_other = emission_classification_other

    @property
    def emission_level(self) -> LowEmissionLevelEnumG:
        """Gets the emission_level of this Emissions.


        :return: The emission_level of this Emissions.
        :rtype: LowEmissionLevelEnumG
        """
        return self._emission_level

    @emission_level.setter
    def emission_level(self, emission_level: LowEmissionLevelEnumG):
        """Sets the emission_level of this Emissions.


        :param emission_level: The emission_level of this Emissions.
        :type emission_level: LowEmissionLevelEnumG
        """

        self._emission_level = emission_level

    @property
    def emissions_extension_g(self) -> EmissionsExtensionTypeG:
        """Gets the emissions_extension_g of this Emissions.


        :return: The emissions_extension_g of this Emissions.
        :rtype: EmissionsExtensionTypeG
        """
        return self._emissions_extension_g

    @emissions_extension_g.setter
    def emissions_extension_g(self, emissions_extension_g: EmissionsExtensionTypeG):
        """Sets the emissions_extension_g of this Emissions.


        :param emissions_extension_g: The emissions_extension_g of this Emissions.
        :type emissions_extension_g: EmissionsExtensionTypeG
        """

        self._emissions_extension_g = emissions_extension_g
