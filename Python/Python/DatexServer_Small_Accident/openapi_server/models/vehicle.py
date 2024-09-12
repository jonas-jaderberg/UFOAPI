from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model import Model
from openapi_server.models.axle_spacing import AxleSpacing
from openapi_server.models.axle_weight import AxleWeight
from openapi_server.models.hazardous_materials import HazardousMaterials
from openapi_server.models.multilingual_string import MultilingualString
from openapi_server.models.vehicle_characteristics import VehicleCharacteristics
from openapi_server.models.vehicle_status_enum_g import VehicleStatusEnumG
from openapi_server import util

from openapi_server.models.axle_spacing import AxleSpacing  # noqa: E501
from openapi_server.models.axle_weight import AxleWeight  # noqa: E501
from openapi_server.models.hazardous_materials import HazardousMaterials  # noqa: E501
from openapi_server.models.multilingual_string import MultilingualString  # noqa: E501
from openapi_server.models.vehicle_characteristics import VehicleCharacteristics  # noqa: E501
from openapi_server.models.vehicle_status_enum_g import VehicleStatusEnumG  # noqa: E501

class Vehicle(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, anonymized_vehicle_reference=None, vehicle_colour=None, vehicle_country_of_origin=None, vehicle_identifier=None, vehicle_manufacturer=None, vehicle_model=None, vehicle_registration_plate_identifier=None, vehicle_status=None, vehicle_characteristics=None, axle_spacing_on_vehicle=None, specific_axle_weight=None, hazardous_goods_associated_with_vehicle=None, vehicle_extension_g=None):  # noqa: E501
        """Vehicle - a model defined in OpenAPI

        :param anonymized_vehicle_reference: The anonymized_vehicle_reference of this Vehicle.  # noqa: E501
        :type anonymized_vehicle_reference: str
        :param vehicle_colour: The vehicle_colour of this Vehicle.  # noqa: E501
        :type vehicle_colour: MultilingualString
        :param vehicle_country_of_origin: The vehicle_country_of_origin of this Vehicle.  # noqa: E501
        :type vehicle_country_of_origin: str
        :param vehicle_identifier: The vehicle_identifier of this Vehicle.  # noqa: E501
        :type vehicle_identifier: str
        :param vehicle_manufacturer: The vehicle_manufacturer of this Vehicle.  # noqa: E501
        :type vehicle_manufacturer: str
        :param vehicle_model: The vehicle_model of this Vehicle.  # noqa: E501
        :type vehicle_model: str
        :param vehicle_registration_plate_identifier: The vehicle_registration_plate_identifier of this Vehicle.  # noqa: E501
        :type vehicle_registration_plate_identifier: str
        :param vehicle_status: The vehicle_status of this Vehicle.  # noqa: E501
        :type vehicle_status: VehicleStatusEnumG
        :param vehicle_characteristics: The vehicle_characteristics of this Vehicle.  # noqa: E501
        :type vehicle_characteristics: VehicleCharacteristics
        :param axle_spacing_on_vehicle: The axle_spacing_on_vehicle of this Vehicle.  # noqa: E501
        :type axle_spacing_on_vehicle: List[AxleSpacing]
        :param specific_axle_weight: The specific_axle_weight of this Vehicle.  # noqa: E501
        :type specific_axle_weight: List[AxleWeight]
        :param hazardous_goods_associated_with_vehicle: The hazardous_goods_associated_with_vehicle of this Vehicle.  # noqa: E501
        :type hazardous_goods_associated_with_vehicle: HazardousMaterials
        :param vehicle_extension_g: The vehicle_extension_g of this Vehicle.  # noqa: E501
        :type vehicle_extension_g: Dict[str, object]
        """
        self.openapi_types = {
            'anonymized_vehicle_reference': str,
            'vehicle_colour': MultilingualString,
            'vehicle_country_of_origin': str,
            'vehicle_identifier': str,
            'vehicle_manufacturer': str,
            'vehicle_model': str,
            'vehicle_registration_plate_identifier': str,
            'vehicle_status': VehicleStatusEnumG,
            'vehicle_characteristics': VehicleCharacteristics,
            'axle_spacing_on_vehicle': List[AxleSpacing],
            'specific_axle_weight': List[AxleWeight],
            'hazardous_goods_associated_with_vehicle': HazardousMaterials,
            'vehicle_extension_g': Dict[str, object]
        }

        self.attribute_map = {
            'anonymized_vehicle_reference': 'anonymizedVehicleReference',
            'vehicle_colour': 'vehicleColour',
            'vehicle_country_of_origin': 'vehicleCountryOfOrigin',
            'vehicle_identifier': 'vehicleIdentifier',
            'vehicle_manufacturer': 'vehicleManufacturer',
            'vehicle_model': 'vehicleModel',
            'vehicle_registration_plate_identifier': 'vehicleRegistrationPlateIdentifier',
            'vehicle_status': 'vehicleStatus',
            'vehicle_characteristics': 'vehicleCharacteristics',
            'axle_spacing_on_vehicle': 'axleSpacingOnVehicle',
            'specific_axle_weight': 'specificAxleWeight',
            'hazardous_goods_associated_with_vehicle': 'hazardousGoodsAssociatedWithVehicle',
            'vehicle_extension_g': 'vehicleExtensionG'
        }

        self._anonymized_vehicle_reference = anonymized_vehicle_reference
        self._vehicle_colour = vehicle_colour
        self._vehicle_country_of_origin = vehicle_country_of_origin
        self._vehicle_identifier = vehicle_identifier
        self._vehicle_manufacturer = vehicle_manufacturer
        self._vehicle_model = vehicle_model
        self._vehicle_registration_plate_identifier = vehicle_registration_plate_identifier
        self._vehicle_status = vehicle_status
        self._vehicle_characteristics = vehicle_characteristics
        self._axle_spacing_on_vehicle = axle_spacing_on_vehicle
        self._specific_axle_weight = specific_axle_weight
        self._hazardous_goods_associated_with_vehicle = hazardous_goods_associated_with_vehicle
        self._vehicle_extension_g = vehicle_extension_g

    @classmethod
    def from_dict(cls, dikt) -> 'Vehicle':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Vehicle of this Vehicle.  # noqa: E501
        :rtype: Vehicle
        """
        return util.deserialize_model(dikt, cls)

    @property
    def anonymized_vehicle_reference(self) -> str:
        """Gets the anonymized_vehicle_reference of this Vehicle.


        :return: The anonymized_vehicle_reference of this Vehicle.
        :rtype: str
        """
        return self._anonymized_vehicle_reference

    @anonymized_vehicle_reference.setter
    def anonymized_vehicle_reference(self, anonymized_vehicle_reference: str):
        """Sets the anonymized_vehicle_reference of this Vehicle.


        :param anonymized_vehicle_reference: The anonymized_vehicle_reference of this Vehicle.
        :type anonymized_vehicle_reference: str
        """
        if anonymized_vehicle_reference is not None and len(anonymized_vehicle_reference) > 1024:
            raise ValueError("Invalid value for `anonymized_vehicle_reference`, length must be less than or equal to `1024`")  # noqa: E501

        self._anonymized_vehicle_reference = anonymized_vehicle_reference

    @property
    def vehicle_colour(self) -> MultilingualString:
        """Gets the vehicle_colour of this Vehicle.


        :return: The vehicle_colour of this Vehicle.
        :rtype: MultilingualString
        """
        return self._vehicle_colour

    @vehicle_colour.setter
    def vehicle_colour(self, vehicle_colour: MultilingualString):
        """Sets the vehicle_colour of this Vehicle.


        :param vehicle_colour: The vehicle_colour of this Vehicle.
        :type vehicle_colour: MultilingualString
        """

        self._vehicle_colour = vehicle_colour

    @property
    def vehicle_country_of_origin(self) -> str:
        """Gets the vehicle_country_of_origin of this Vehicle.


        :return: The vehicle_country_of_origin of this Vehicle.
        :rtype: str
        """
        return self._vehicle_country_of_origin

    @vehicle_country_of_origin.setter
    def vehicle_country_of_origin(self, vehicle_country_of_origin: str):
        """Sets the vehicle_country_of_origin of this Vehicle.


        :param vehicle_country_of_origin: The vehicle_country_of_origin of this Vehicle.
        :type vehicle_country_of_origin: str
        """
        if vehicle_country_of_origin is not None and len(vehicle_country_of_origin) > 1024:
            raise ValueError("Invalid value for `vehicle_country_of_origin`, length must be less than or equal to `1024`")  # noqa: E501

        self._vehicle_country_of_origin = vehicle_country_of_origin

    @property
    def vehicle_identifier(self) -> str:
        """Gets the vehicle_identifier of this Vehicle.


        :return: The vehicle_identifier of this Vehicle.
        :rtype: str
        """
        return self._vehicle_identifier

    @vehicle_identifier.setter
    def vehicle_identifier(self, vehicle_identifier: str):
        """Sets the vehicle_identifier of this Vehicle.


        :param vehicle_identifier: The vehicle_identifier of this Vehicle.
        :type vehicle_identifier: str
        """
        if vehicle_identifier is not None and len(vehicle_identifier) > 1024:
            raise ValueError("Invalid value for `vehicle_identifier`, length must be less than or equal to `1024`")  # noqa: E501

        self._vehicle_identifier = vehicle_identifier

    @property
    def vehicle_manufacturer(self) -> str:
        """Gets the vehicle_manufacturer of this Vehicle.


        :return: The vehicle_manufacturer of this Vehicle.
        :rtype: str
        """
        return self._vehicle_manufacturer

    @vehicle_manufacturer.setter
    def vehicle_manufacturer(self, vehicle_manufacturer: str):
        """Sets the vehicle_manufacturer of this Vehicle.


        :param vehicle_manufacturer: The vehicle_manufacturer of this Vehicle.
        :type vehicle_manufacturer: str
        """
        if vehicle_manufacturer is not None and len(vehicle_manufacturer) > 1024:
            raise ValueError("Invalid value for `vehicle_manufacturer`, length must be less than or equal to `1024`")  # noqa: E501

        self._vehicle_manufacturer = vehicle_manufacturer

    @property
    def vehicle_model(self) -> str:
        """Gets the vehicle_model of this Vehicle.


        :return: The vehicle_model of this Vehicle.
        :rtype: str
        """
        return self._vehicle_model

    @vehicle_model.setter
    def vehicle_model(self, vehicle_model: str):
        """Sets the vehicle_model of this Vehicle.


        :param vehicle_model: The vehicle_model of this Vehicle.
        :type vehicle_model: str
        """
        if vehicle_model is not None and len(vehicle_model) > 1024:
            raise ValueError("Invalid value for `vehicle_model`, length must be less than or equal to `1024`")  # noqa: E501

        self._vehicle_model = vehicle_model

    @property
    def vehicle_registration_plate_identifier(self) -> str:
        """Gets the vehicle_registration_plate_identifier of this Vehicle.


        :return: The vehicle_registration_plate_identifier of this Vehicle.
        :rtype: str
        """
        return self._vehicle_registration_plate_identifier

    @vehicle_registration_plate_identifier.setter
    def vehicle_registration_plate_identifier(self, vehicle_registration_plate_identifier: str):
        """Sets the vehicle_registration_plate_identifier of this Vehicle.


        :param vehicle_registration_plate_identifier: The vehicle_registration_plate_identifier of this Vehicle.
        :type vehicle_registration_plate_identifier: str
        """
        if vehicle_registration_plate_identifier is not None and len(vehicle_registration_plate_identifier) > 1024:
            raise ValueError("Invalid value for `vehicle_registration_plate_identifier`, length must be less than or equal to `1024`")  # noqa: E501

        self._vehicle_registration_plate_identifier = vehicle_registration_plate_identifier

    @property
    def vehicle_status(self) -> VehicleStatusEnumG:
        """Gets the vehicle_status of this Vehicle.


        :return: The vehicle_status of this Vehicle.
        :rtype: VehicleStatusEnumG
        """
        return self._vehicle_status

    @vehicle_status.setter
    def vehicle_status(self, vehicle_status: VehicleStatusEnumG):
        """Sets the vehicle_status of this Vehicle.


        :param vehicle_status: The vehicle_status of this Vehicle.
        :type vehicle_status: VehicleStatusEnumG
        """

        self._vehicle_status = vehicle_status

    @property
    def vehicle_characteristics(self) -> VehicleCharacteristics:
        """Gets the vehicle_characteristics of this Vehicle.


        :return: The vehicle_characteristics of this Vehicle.
        :rtype: VehicleCharacteristics
        """
        return self._vehicle_characteristics

    @vehicle_characteristics.setter
    def vehicle_characteristics(self, vehicle_characteristics: VehicleCharacteristics):
        """Sets the vehicle_characteristics of this Vehicle.


        :param vehicle_characteristics: The vehicle_characteristics of this Vehicle.
        :type vehicle_characteristics: VehicleCharacteristics
        """

        self._vehicle_characteristics = vehicle_characteristics

    @property
    def axle_spacing_on_vehicle(self) -> List[AxleSpacing]:
        """Gets the axle_spacing_on_vehicle of this Vehicle.


        :return: The axle_spacing_on_vehicle of this Vehicle.
        :rtype: List[AxleSpacing]
        """
        return self._axle_spacing_on_vehicle

    @axle_spacing_on_vehicle.setter
    def axle_spacing_on_vehicle(self, axle_spacing_on_vehicle: List[AxleSpacing]):
        """Sets the axle_spacing_on_vehicle of this Vehicle.


        :param axle_spacing_on_vehicle: The axle_spacing_on_vehicle of this Vehicle.
        :type axle_spacing_on_vehicle: List[AxleSpacing]
        """
        if axle_spacing_on_vehicle is not None and len(axle_spacing_on_vehicle) < 0:
            raise ValueError("Invalid value for `axle_spacing_on_vehicle`, number of items must be greater than or equal to `0`")  # noqa: E501

        self._axle_spacing_on_vehicle = axle_spacing_on_vehicle

    @property
    def specific_axle_weight(self) -> List[AxleWeight]:
        """Gets the specific_axle_weight of this Vehicle.


        :return: The specific_axle_weight of this Vehicle.
        :rtype: List[AxleWeight]
        """
        return self._specific_axle_weight

    @specific_axle_weight.setter
    def specific_axle_weight(self, specific_axle_weight: List[AxleWeight]):
        """Sets the specific_axle_weight of this Vehicle.


        :param specific_axle_weight: The specific_axle_weight of this Vehicle.
        :type specific_axle_weight: List[AxleWeight]
        """
        if specific_axle_weight is not None and len(specific_axle_weight) < 0:
            raise ValueError("Invalid value for `specific_axle_weight`, number of items must be greater than or equal to `0`")  # noqa: E501

        self._specific_axle_weight = specific_axle_weight

    @property
    def hazardous_goods_associated_with_vehicle(self) -> HazardousMaterials:
        """Gets the hazardous_goods_associated_with_vehicle of this Vehicle.


        :return: The hazardous_goods_associated_with_vehicle of this Vehicle.
        :rtype: HazardousMaterials
        """
        return self._hazardous_goods_associated_with_vehicle

    @hazardous_goods_associated_with_vehicle.setter
    def hazardous_goods_associated_with_vehicle(self, hazardous_goods_associated_with_vehicle: HazardousMaterials):
        """Sets the hazardous_goods_associated_with_vehicle of this Vehicle.


        :param hazardous_goods_associated_with_vehicle: The hazardous_goods_associated_with_vehicle of this Vehicle.
        :type hazardous_goods_associated_with_vehicle: HazardousMaterials
        """

        self._hazardous_goods_associated_with_vehicle = hazardous_goods_associated_with_vehicle

    @property
    def vehicle_extension_g(self) -> Dict[str, object]:
        """Gets the vehicle_extension_g of this Vehicle.


        :return: The vehicle_extension_g of this Vehicle.
        :rtype: Dict[str, object]
        """
        return self._vehicle_extension_g

    @vehicle_extension_g.setter
    def vehicle_extension_g(self, vehicle_extension_g: Dict[str, object]):
        """Sets the vehicle_extension_g of this Vehicle.


        :param vehicle_extension_g: The vehicle_extension_g of this Vehicle.
        :type vehicle_extension_g: Dict[str, object]
        """

        self._vehicle_extension_g = vehicle_extension_g
