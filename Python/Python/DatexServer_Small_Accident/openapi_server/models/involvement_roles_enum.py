from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model import Model
from openapi_server import util


class InvolvementRolesEnum(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    CYCLIST = 'cyclist'
    MOTORCYCLIST = 'motorcyclist'
    PEDESTRIAN = 'pedestrian'
    UNKNOWN = 'unknown'
    VEHICLEDRIVER = 'vehicleDriver'
    VEHICLEOCCUPANT = 'vehicleOccupant'
    VEHICLEPASSENGER = 'vehiclePassenger'
    WITNESS = 'witness'
    EXTENDEDG = 'extendedG'
    def __init__(self):  # noqa: E501
        """InvolvementRolesEnum - a model defined in OpenAPI

        """
        self.openapi_types = {
        }

        self.attribute_map = {
        }

    @classmethod
    def from_dict(cls, dikt) -> 'InvolvementRolesEnum':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The InvolvementRolesEnum of this InvolvementRolesEnum.  # noqa: E501
        :rtype: InvolvementRolesEnum
        """
        return util.deserialize_model(dikt, cls)
