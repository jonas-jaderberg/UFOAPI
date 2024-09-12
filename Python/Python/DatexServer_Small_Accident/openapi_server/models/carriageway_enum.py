from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model import Model
from openapi_server import util


class CarriagewayEnum(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    CONNECTINGCARRIAGEWAY = 'connectingCarriageway'
    CYCLETRACK = 'cycleTrack'
    ENTRYSLIPROAD = 'entrySlipRoad'
    EXITSLIPROAD = 'exitSlipRoad'
    FLYOVER = 'flyover'
    FOOTPATH = 'footpath'
    LEFTHANDPARALLELCARRIAGEWAY = 'leftHandParallelCarriageway'
    LEFTHANDFEEDERROAD = 'leftHandFeederRoad'
    MAINCARRIAGEWAY = 'mainCarriageway'
    OPPOSITECARRIAGEWAY = 'oppositeCarriageway'
    PARALLELCARRIAGEWAY = 'parallelCarriageway'
    RIGHTHANDFEEDERROAD = 'rightHandFeederRoad'
    RIGHTHANDPARALLELCARRIAGEWAY = 'rightHandParallelCarriageway'
    ROUNDABOUT = 'roundabout'
    SERVICEROAD = 'serviceRoad'
    SLIPROADS = 'slipRoads'
    UNDERPASS = 'underpass'
    UNSPECIFIEDCARRIAGEWAY = 'unspecifiedCarriageway'
    EXTENDEDG = 'extendedG'
    def __init__(self):  # noqa: E501
        """CarriagewayEnum - a model defined in OpenAPI

        """
        self.openapi_types = {
        }

        self.attribute_map = {
        }

    @classmethod
    def from_dict(cls, dikt) -> 'CarriagewayEnum':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The CarriagewayEnum of this CarriagewayEnum.  # noqa: E501
        :rtype: CarriagewayEnum
        """
        return util.deserialize_model(dikt, cls)
