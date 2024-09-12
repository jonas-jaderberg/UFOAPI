from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model import Model
from openapi_server.models.alert_c_location import AlertCLocation
from openapi_server import util

from openapi_server.models.alert_c_location import AlertCLocation  # noqa: E501

class AlertCMethod2SecondaryPointLocation(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, alert_c_location=None, alert_c_method2_secondary_point_location_extension_g=None):  # noqa: E501
        """AlertCMethod2SecondaryPointLocation - a model defined in OpenAPI

        :param alert_c_location: The alert_c_location of this AlertCMethod2SecondaryPointLocation.  # noqa: E501
        :type alert_c_location: AlertCLocation
        :param alert_c_method2_secondary_point_location_extension_g: The alert_c_method2_secondary_point_location_extension_g of this AlertCMethod2SecondaryPointLocation.  # noqa: E501
        :type alert_c_method2_secondary_point_location_extension_g: Dict[str, object]
        """
        self.openapi_types = {
            'alert_c_location': AlertCLocation,
            'alert_c_method2_secondary_point_location_extension_g': Dict[str, object]
        }

        self.attribute_map = {
            'alert_c_location': 'alertCLocation',
            'alert_c_method2_secondary_point_location_extension_g': 'alertCMethod2SecondaryPointLocationExtensionG'
        }

        self._alert_c_location = alert_c_location
        self._alert_c_method2_secondary_point_location_extension_g = alert_c_method2_secondary_point_location_extension_g

    @classmethod
    def from_dict(cls, dikt) -> 'AlertCMethod2SecondaryPointLocation':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The AlertCMethod2SecondaryPointLocation of this AlertCMethod2SecondaryPointLocation.  # noqa: E501
        :rtype: AlertCMethod2SecondaryPointLocation
        """
        return util.deserialize_model(dikt, cls)

    @property
    def alert_c_location(self) -> AlertCLocation:
        """Gets the alert_c_location of this AlertCMethod2SecondaryPointLocation.


        :return: The alert_c_location of this AlertCMethod2SecondaryPointLocation.
        :rtype: AlertCLocation
        """
        return self._alert_c_location

    @alert_c_location.setter
    def alert_c_location(self, alert_c_location: AlertCLocation):
        """Sets the alert_c_location of this AlertCMethod2SecondaryPointLocation.


        :param alert_c_location: The alert_c_location of this AlertCMethod2SecondaryPointLocation.
        :type alert_c_location: AlertCLocation
        """
        if alert_c_location is None:
            raise ValueError("Invalid value for `alert_c_location`, must not be `None`")  # noqa: E501

        self._alert_c_location = alert_c_location

    @property
    def alert_c_method2_secondary_point_location_extension_g(self) -> Dict[str, object]:
        """Gets the alert_c_method2_secondary_point_location_extension_g of this AlertCMethod2SecondaryPointLocation.


        :return: The alert_c_method2_secondary_point_location_extension_g of this AlertCMethod2SecondaryPointLocation.
        :rtype: Dict[str, object]
        """
        return self._alert_c_method2_secondary_point_location_extension_g

    @alert_c_method2_secondary_point_location_extension_g.setter
    def alert_c_method2_secondary_point_location_extension_g(self, alert_c_method2_secondary_point_location_extension_g: Dict[str, object]):
        """Sets the alert_c_method2_secondary_point_location_extension_g of this AlertCMethod2SecondaryPointLocation.


        :param alert_c_method2_secondary_point_location_extension_g: The alert_c_method2_secondary_point_location_extension_g of this AlertCMethod2SecondaryPointLocation.
        :type alert_c_method2_secondary_point_location_extension_g: Dict[str, object]
        """

        self._alert_c_method2_secondary_point_location_extension_g = alert_c_method2_secondary_point_location_extension_g
