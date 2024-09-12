from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model import Model
from openapi_server import util


class LaneEnum(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    ALLLANESCOMPLETECARRIAGEWAY = 'allLanesCompleteCarriageway'
    BUSLANE = 'busLane'
    BUSSTOP = 'busStop'
    CARPOOLLANE = 'carPoolLane'
    CENTRALRESERVATION = 'centralReservation'
    CRAWLERLANE = 'crawlerLane'
    CYCLELANE = 'cycleLane'
    EMERGENCYLANE = 'emergencyLane'
    ESCAPELANE = 'escapeLane'
    EXPRESSLANE = 'expressLane'
    HARDSHOULDER = 'hardShoulder'
    HEAVYVEHICLELANE = 'heavyVehicleLane'
    LAYBY = 'layBy'
    LEFTHANDTURNINGLANE = 'leftHandTurningLane'
    LEFTLANE = 'leftLane'
    LOCALTRAFFICLANE = 'localTrafficLane'
    MIDDLELANE = 'middleLane'
    OVERTAKINGLANE = 'overtakingLane'
    RIGHTHANDTURNINGLANE = 'rightHandTurningLane'
    RIGHTLANE = 'rightLane'
    RUSHHOURLANE = 'rushHourLane'
    SETDOWNAREA = 'setDownArea'
    SLOWVEHICLELANE = 'slowVehicleLane'
    THROUGHTRAFFICLANE = 'throughTrafficLane'
    TIDALFLOWLANE = 'tidalFlowLane'
    TURNINGLANE = 'turningLane'
    VERGE = 'verge'
    EXTENDEDG = 'extendedG'
    def __init__(self):  # noqa: E501
        """LaneEnum - a model defined in OpenAPI

        """
        self.openapi_types = {
        }

        self.attribute_map = {
        }

    @classmethod
    def from_dict(cls, dikt) -> 'LaneEnum':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The LaneEnum of this LaneEnum.  # noqa: E501
        :rtype: LaneEnum
        """
        return util.deserialize_model(dikt, cls)
