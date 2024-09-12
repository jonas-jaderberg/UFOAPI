from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model import Model
from openapi_server.models.comparison_operator_enum_g import ComparisonOperatorEnumG
from openapi_server import util

from openapi_server.models.comparison_operator_enum_g import ComparisonOperatorEnumG  # noqa: E501

class HeightCharacteristic(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, comparison_operator=None, vehicle_height=None, height_characteristic_extension_g=None):  # noqa: E501
        """HeightCharacteristic - a model defined in OpenAPI

        :param comparison_operator: The comparison_operator of this HeightCharacteristic.  # noqa: E501
        :type comparison_operator: ComparisonOperatorEnumG
        :param vehicle_height: The vehicle_height of this HeightCharacteristic.  # noqa: E501
        :type vehicle_height: float
        :param height_characteristic_extension_g: The height_characteristic_extension_g of this HeightCharacteristic.  # noqa: E501
        :type height_characteristic_extension_g: Dict[str, object]
        """
        self.openapi_types = {
            'comparison_operator': ComparisonOperatorEnumG,
            'vehicle_height': float,
            'height_characteristic_extension_g': Dict[str, object]
        }

        self.attribute_map = {
            'comparison_operator': 'comparisonOperator',
            'vehicle_height': 'vehicleHeight',
            'height_characteristic_extension_g': 'heightCharacteristicExtensionG'
        }

        self._comparison_operator = comparison_operator
        self._vehicle_height = vehicle_height
        self._height_characteristic_extension_g = height_characteristic_extension_g

    @classmethod
    def from_dict(cls, dikt) -> 'HeightCharacteristic':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The HeightCharacteristic of this HeightCharacteristic.  # noqa: E501
        :rtype: HeightCharacteristic
        """
        return util.deserialize_model(dikt, cls)

    @property
    def comparison_operator(self) -> ComparisonOperatorEnumG:
        """Gets the comparison_operator of this HeightCharacteristic.


        :return: The comparison_operator of this HeightCharacteristic.
        :rtype: ComparisonOperatorEnumG
        """
        return self._comparison_operator

    @comparison_operator.setter
    def comparison_operator(self, comparison_operator: ComparisonOperatorEnumG):
        """Sets the comparison_operator of this HeightCharacteristic.


        :param comparison_operator: The comparison_operator of this HeightCharacteristic.
        :type comparison_operator: ComparisonOperatorEnumG
        """
        if comparison_operator is None:
            raise ValueError("Invalid value for `comparison_operator`, must not be `None`")  # noqa: E501

        self._comparison_operator = comparison_operator

    @property
    def vehicle_height(self) -> float:
        """Gets the vehicle_height of this HeightCharacteristic.


        :return: The vehicle_height of this HeightCharacteristic.
        :rtype: float
        """
        return self._vehicle_height

    @vehicle_height.setter
    def vehicle_height(self, vehicle_height: float):
        """Sets the vehicle_height of this HeightCharacteristic.


        :param vehicle_height: The vehicle_height of this HeightCharacteristic.
        :type vehicle_height: float
        """
        if vehicle_height is None:
            raise ValueError("Invalid value for `vehicle_height`, must not be `None`")  # noqa: E501

        self._vehicle_height = vehicle_height

    @property
    def height_characteristic_extension_g(self) -> Dict[str, object]:
        """Gets the height_characteristic_extension_g of this HeightCharacteristic.


        :return: The height_characteristic_extension_g of this HeightCharacteristic.
        :rtype: Dict[str, object]
        """
        return self._height_characteristic_extension_g

    @height_characteristic_extension_g.setter
    def height_characteristic_extension_g(self, height_characteristic_extension_g: Dict[str, object]):
        """Sets the height_characteristic_extension_g of this HeightCharacteristic.


        :param height_characteristic_extension_g: The height_characteristic_extension_g of this HeightCharacteristic.
        :type height_characteristic_extension_g: Dict[str, object]
        """

        self._height_characteristic_extension_g = height_characteristic_extension_g
