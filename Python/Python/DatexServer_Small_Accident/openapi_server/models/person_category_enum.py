from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model import Model
from openapi_server import util


class PersonCategoryEnum(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    ADULT = 'adult'
    CHILD = 'child'
    EMERGENCYSERVICESPERSON = 'emergencyServicesPerson'
    FIREMAN = 'fireman'
    INFANT = 'infant'
    MEDICALSTAFF = 'medicalStaff'
    MEMBEROFTHEPUBLIC = 'memberOfThePublic'
    POLICEMAN = 'policeman'
    POLITICIAN = 'politician'
    PUBLICTRANSPORTPASSENGER = 'publicTransportPassenger'
    SICKPERSON = 'sickPerson'
    TRAFFICOFFICER = 'trafficOfficer'
    TRAFFICWARDEN = 'trafficWarden'
    VERYIMPORTANTPERSON = 'veryImportantPerson'
    EXTENDEDG = 'extendedG'
    def __init__(self):  # noqa: E501
        """PersonCategoryEnum - a model defined in OpenAPI

        """
        self.openapi_types = {
        }

        self.attribute_map = {
        }

    @classmethod
    def from_dict(cls, dikt) -> 'PersonCategoryEnum':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The PersonCategoryEnum of this PersonCategoryEnum.  # noqa: E501
        :rtype: PersonCategoryEnum
        """
        return util.deserialize_model(dikt, cls)
