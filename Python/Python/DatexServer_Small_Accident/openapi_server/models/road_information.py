from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model import Model
from openapi_server import util


class RoadInformation(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, road_destination=None, road_name=None, road_number=None, road_information_extension_g=None):  # noqa: E501
        """RoadInformation - a model defined in OpenAPI

        :param road_destination: The road_destination of this RoadInformation.  # noqa: E501
        :type road_destination: str
        :param road_name: The road_name of this RoadInformation.  # noqa: E501
        :type road_name: str
        :param road_number: The road_number of this RoadInformation.  # noqa: E501
        :type road_number: str
        :param road_information_extension_g: The road_information_extension_g of this RoadInformation.  # noqa: E501
        :type road_information_extension_g: Dict[str, object]
        """
        self.openapi_types = {
            'road_destination': str,
            'road_name': str,
            'road_number': str,
            'road_information_extension_g': Dict[str, object]
        }

        self.attribute_map = {
            'road_destination': 'roadDestination',
            'road_name': 'roadName',
            'road_number': 'roadNumber',
            'road_information_extension_g': 'roadInformationExtensionG'
        }

        self._road_destination = road_destination
        self._road_name = road_name
        self._road_number = road_number
        self._road_information_extension_g = road_information_extension_g

    @classmethod
    def from_dict(cls, dikt) -> 'RoadInformation':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The RoadInformation of this RoadInformation.  # noqa: E501
        :rtype: RoadInformation
        """
        return util.deserialize_model(dikt, cls)

    @property
    def road_destination(self) -> str:
        """Gets the road_destination of this RoadInformation.


        :return: The road_destination of this RoadInformation.
        :rtype: str
        """
        return self._road_destination

    @road_destination.setter
    def road_destination(self, road_destination: str):
        """Sets the road_destination of this RoadInformation.


        :param road_destination: The road_destination of this RoadInformation.
        :type road_destination: str
        """
        if road_destination is not None and len(road_destination) > 1024:
            raise ValueError("Invalid value for `road_destination`, length must be less than or equal to `1024`")  # noqa: E501

        self._road_destination = road_destination

    @property
    def road_name(self) -> str:
        """Gets the road_name of this RoadInformation.


        :return: The road_name of this RoadInformation.
        :rtype: str
        """
        return self._road_name

    @road_name.setter
    def road_name(self, road_name: str):
        """Sets the road_name of this RoadInformation.


        :param road_name: The road_name of this RoadInformation.
        :type road_name: str
        """
        if road_name is not None and len(road_name) > 1024:
            raise ValueError("Invalid value for `road_name`, length must be less than or equal to `1024`")  # noqa: E501

        self._road_name = road_name

    @property
    def road_number(self) -> str:
        """Gets the road_number of this RoadInformation.


        :return: The road_number of this RoadInformation.
        :rtype: str
        """
        return self._road_number

    @road_number.setter
    def road_number(self, road_number: str):
        """Sets the road_number of this RoadInformation.


        :param road_number: The road_number of this RoadInformation.
        :type road_number: str
        """
        if road_number is not None and len(road_number) > 1024:
            raise ValueError("Invalid value for `road_number`, length must be less than or equal to `1024`")  # noqa: E501

        self._road_number = road_number

    @property
    def road_information_extension_g(self) -> Dict[str, object]:
        """Gets the road_information_extension_g of this RoadInformation.


        :return: The road_information_extension_g of this RoadInformation.
        :rtype: Dict[str, object]
        """
        return self._road_information_extension_g

    @road_information_extension_g.setter
    def road_information_extension_g(self, road_information_extension_g: Dict[str, object]):
        """Sets the road_information_extension_g of this RoadInformation.


        :param road_information_extension_g: The road_information_extension_g of this RoadInformation.
        :type road_information_extension_g: Dict[str, object]
        """

        self._road_information_extension_g = road_information_extension_g
