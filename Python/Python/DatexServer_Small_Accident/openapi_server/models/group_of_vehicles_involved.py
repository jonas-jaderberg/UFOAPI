from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model import Model
from openapi_server.models.vehicle_characteristics import VehicleCharacteristics
from openapi_server.models.vehicle_status_enum_g import VehicleStatusEnumG
from openapi_server import util

from openapi_server.models.vehicle_characteristics import VehicleCharacteristics  # noqa: E501
from openapi_server.models.vehicle_status_enum_g import VehicleStatusEnumG  # noqa: E501

class GroupOfVehiclesInvolved(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, number_of_vehicles=None, vehicle_status=None, vehicle_characteristics=None, group_of_vehicles_involved_extension_g=None):  # noqa: E501
        """GroupOfVehiclesInvolved - a model defined in OpenAPI

        :param number_of_vehicles: The number_of_vehicles of this GroupOfVehiclesInvolved.  # noqa: E501
        :type number_of_vehicles: int
        :param vehicle_status: The vehicle_status of this GroupOfVehiclesInvolved.  # noqa: E501
        :type vehicle_status: VehicleStatusEnumG
        :param vehicle_characteristics: The vehicle_characteristics of this GroupOfVehiclesInvolved.  # noqa: E501
        :type vehicle_characteristics: VehicleCharacteristics
        :param group_of_vehicles_involved_extension_g: The group_of_vehicles_involved_extension_g of this GroupOfVehiclesInvolved.  # noqa: E501
        :type group_of_vehicles_involved_extension_g: Dict[str, object]
        """
        self.openapi_types = {
            'number_of_vehicles': int,
            'vehicle_status': VehicleStatusEnumG,
            'vehicle_characteristics': VehicleCharacteristics,
            'group_of_vehicles_involved_extension_g': Dict[str, object]
        }

        self.attribute_map = {
            'number_of_vehicles': 'numberOfVehicles',
            'vehicle_status': 'vehicleStatus',
            'vehicle_characteristics': 'vehicleCharacteristics',
            'group_of_vehicles_involved_extension_g': 'groupOfVehiclesInvolvedExtensionG'
        }

        self._number_of_vehicles = number_of_vehicles
        self._vehicle_status = vehicle_status
        self._vehicle_characteristics = vehicle_characteristics
        self._group_of_vehicles_involved_extension_g = group_of_vehicles_involved_extension_g

    @classmethod
    def from_dict(cls, dikt) -> 'GroupOfVehiclesInvolved':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The GroupOfVehiclesInvolved of this GroupOfVehiclesInvolved.  # noqa: E501
        :rtype: GroupOfVehiclesInvolved
        """
        return util.deserialize_model(dikt, cls)

    @property
    def number_of_vehicles(self) -> int:
        """Gets the number_of_vehicles of this GroupOfVehiclesInvolved.


        :return: The number_of_vehicles of this GroupOfVehiclesInvolved.
        :rtype: int
        """
        return self._number_of_vehicles

    @number_of_vehicles.setter
    def number_of_vehicles(self, number_of_vehicles: int):
        """Sets the number_of_vehicles of this GroupOfVehiclesInvolved.


        :param number_of_vehicles: The number_of_vehicles of this GroupOfVehiclesInvolved.
        :type number_of_vehicles: int
        """
        if number_of_vehicles is not None and number_of_vehicles < 0:  # noqa: E501
            raise ValueError("Invalid value for `number_of_vehicles`, must be a value greater than or equal to `0`")  # noqa: E501

        self._number_of_vehicles = number_of_vehicles

    @property
    def vehicle_status(self) -> VehicleStatusEnumG:
        """Gets the vehicle_status of this GroupOfVehiclesInvolved.


        :return: The vehicle_status of this GroupOfVehiclesInvolved.
        :rtype: VehicleStatusEnumG
        """
        return self._vehicle_status

    @vehicle_status.setter
    def vehicle_status(self, vehicle_status: VehicleStatusEnumG):
        """Sets the vehicle_status of this GroupOfVehiclesInvolved.


        :param vehicle_status: The vehicle_status of this GroupOfVehiclesInvolved.
        :type vehicle_status: VehicleStatusEnumG
        """

        self._vehicle_status = vehicle_status

    @property
    def vehicle_characteristics(self) -> VehicleCharacteristics:
        """Gets the vehicle_characteristics of this GroupOfVehiclesInvolved.


        :return: The vehicle_characteristics of this GroupOfVehiclesInvolved.
        :rtype: VehicleCharacteristics
        """
        return self._vehicle_characteristics

    @vehicle_characteristics.setter
    def vehicle_characteristics(self, vehicle_characteristics: VehicleCharacteristics):
        """Sets the vehicle_characteristics of this GroupOfVehiclesInvolved.


        :param vehicle_characteristics: The vehicle_characteristics of this GroupOfVehiclesInvolved.
        :type vehicle_characteristics: VehicleCharacteristics
        """

        self._vehicle_characteristics = vehicle_characteristics

    @property
    def group_of_vehicles_involved_extension_g(self) -> Dict[str, object]:
        """Gets the group_of_vehicles_involved_extension_g of this GroupOfVehiclesInvolved.


        :return: The group_of_vehicles_involved_extension_g of this GroupOfVehiclesInvolved.
        :rtype: Dict[str, object]
        """
        return self._group_of_vehicles_involved_extension_g

    @group_of_vehicles_involved_extension_g.setter
    def group_of_vehicles_involved_extension_g(self, group_of_vehicles_involved_extension_g: Dict[str, object]):
        """Sets the group_of_vehicles_involved_extension_g of this GroupOfVehiclesInvolved.


        :param group_of_vehicles_involved_extension_g: The group_of_vehicles_involved_extension_g of this GroupOfVehiclesInvolved.
        :type group_of_vehicles_involved_extension_g: Dict[str, object]
        """

        self._group_of_vehicles_involved_extension_g = group_of_vehicles_involved_extension_g
