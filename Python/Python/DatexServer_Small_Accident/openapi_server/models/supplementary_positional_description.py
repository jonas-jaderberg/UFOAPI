from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model import Model
from openapi_server.models.carriageway import Carriageway
from openapi_server.models.multilingual_string import MultilingualString
from openapi_server.models.named_area_g import NamedAreaG
from openapi_server.models.road_information_g import RoadInformationG
from openapi_server import util

from openapi_server.models.carriageway import Carriageway  # noqa: E501
from openapi_server.models.multilingual_string import MultilingualString  # noqa: E501
from openapi_server.models.named_area_g import NamedAreaG  # noqa: E501
from openapi_server.models.road_information_g import RoadInformationG  # noqa: E501

class SupplementaryPositionalDescription(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, location_description=None, carriageway=None, named_area=None, road_information=None, supplementary_positional_description_extension_g=None):  # noqa: E501
        """SupplementaryPositionalDescription - a model defined in OpenAPI

        :param location_description: The location_description of this SupplementaryPositionalDescription.  # noqa: E501
        :type location_description: MultilingualString
        :param carriageway: The carriageway of this SupplementaryPositionalDescription.  # noqa: E501
        :type carriageway: List[Carriageway]
        :param named_area: The named_area of this SupplementaryPositionalDescription.  # noqa: E501
        :type named_area: NamedAreaG
        :param road_information: The road_information of this SupplementaryPositionalDescription.  # noqa: E501
        :type road_information: List[RoadInformationG]
        :param supplementary_positional_description_extension_g: The supplementary_positional_description_extension_g of this SupplementaryPositionalDescription.  # noqa: E501
        :type supplementary_positional_description_extension_g: Dict[str, object]
        """
        self.openapi_types = {
            'location_description': MultilingualString,
            'carriageway': List[Carriageway],
            'named_area': NamedAreaG,
            'road_information': List[RoadInformationG],
            'supplementary_positional_description_extension_g': Dict[str, object]
        }

        self.attribute_map = {
            'location_description': 'locationDescription',
            'carriageway': 'carriageway',
            'named_area': 'namedArea',
            'road_information': 'roadInformation',
            'supplementary_positional_description_extension_g': 'supplementaryPositionalDescriptionExtensionG'
        }

        self._location_description = location_description
        self._carriageway = carriageway
        self._named_area = named_area
        self._road_information = road_information
        self._supplementary_positional_description_extension_g = supplementary_positional_description_extension_g

    @classmethod
    def from_dict(cls, dikt) -> 'SupplementaryPositionalDescription':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The SupplementaryPositionalDescription of this SupplementaryPositionalDescription.  # noqa: E501
        :rtype: SupplementaryPositionalDescription
        """
        return util.deserialize_model(dikt, cls)

    @property
    def location_description(self) -> MultilingualString:
        """Gets the location_description of this SupplementaryPositionalDescription.


        :return: The location_description of this SupplementaryPositionalDescription.
        :rtype: MultilingualString
        """
        return self._location_description

    @location_description.setter
    def location_description(self, location_description: MultilingualString):
        """Sets the location_description of this SupplementaryPositionalDescription.


        :param location_description: The location_description of this SupplementaryPositionalDescription.
        :type location_description: MultilingualString
        """

        self._location_description = location_description

    @property
    def carriageway(self) -> List[Carriageway]:
        """Gets the carriageway of this SupplementaryPositionalDescription.


        :return: The carriageway of this SupplementaryPositionalDescription.
        :rtype: List[Carriageway]
        """
        return self._carriageway

    @carriageway.setter
    def carriageway(self, carriageway: List[Carriageway]):
        """Sets the carriageway of this SupplementaryPositionalDescription.


        :param carriageway: The carriageway of this SupplementaryPositionalDescription.
        :type carriageway: List[Carriageway]
        """
        if carriageway is not None and len(carriageway) < 0:
            raise ValueError("Invalid value for `carriageway`, number of items must be greater than or equal to `0`")  # noqa: E501

        self._carriageway = carriageway

    @property
    def named_area(self) -> NamedAreaG:
        """Gets the named_area of this SupplementaryPositionalDescription.


        :return: The named_area of this SupplementaryPositionalDescription.
        :rtype: NamedAreaG
        """
        return self._named_area

    @named_area.setter
    def named_area(self, named_area: NamedAreaG):
        """Sets the named_area of this SupplementaryPositionalDescription.


        :param named_area: The named_area of this SupplementaryPositionalDescription.
        :type named_area: NamedAreaG
        """

        self._named_area = named_area

    @property
    def road_information(self) -> List[RoadInformationG]:
        """Gets the road_information of this SupplementaryPositionalDescription.


        :return: The road_information of this SupplementaryPositionalDescription.
        :rtype: List[RoadInformationG]
        """
        return self._road_information

    @road_information.setter
    def road_information(self, road_information: List[RoadInformationG]):
        """Sets the road_information of this SupplementaryPositionalDescription.


        :param road_information: The road_information of this SupplementaryPositionalDescription.
        :type road_information: List[RoadInformationG]
        """
        if road_information is not None and len(road_information) < 0:
            raise ValueError("Invalid value for `road_information`, number of items must be greater than or equal to `0`")  # noqa: E501

        self._road_information = road_information

    @property
    def supplementary_positional_description_extension_g(self) -> Dict[str, object]:
        """Gets the supplementary_positional_description_extension_g of this SupplementaryPositionalDescription.


        :return: The supplementary_positional_description_extension_g of this SupplementaryPositionalDescription.
        :rtype: Dict[str, object]
        """
        return self._supplementary_positional_description_extension_g

    @supplementary_positional_description_extension_g.setter
    def supplementary_positional_description_extension_g(self, supplementary_positional_description_extension_g: Dict[str, object]):
        """Sets the supplementary_positional_description_extension_g of this SupplementaryPositionalDescription.


        :param supplementary_positional_description_extension_g: The supplementary_positional_description_extension_g of this SupplementaryPositionalDescription.
        :type supplementary_positional_description_extension_g: Dict[str, object]
        """

        self._supplementary_positional_description_extension_g = supplementary_positional_description_extension_g
