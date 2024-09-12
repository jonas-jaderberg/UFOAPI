from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model import Model
from openapi_server import util


class ServiceActionStatusEnum(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    COMPLIANT = 'compliant'
    FAILED = 'failed'
    NOTCOMPLIANT = 'notCompliant'
    PROCESSING = 'processing'
    REJECTED = 'rejected'
    SCHEDULED = 'scheduled'
    SUCCESS = 'success'
    TIMEDOUT = 'timedOut'
    EXTENDEDG = 'extendedG'
    def __init__(self):  # noqa: E501
        """ServiceActionStatusEnum - a model defined in OpenAPI

        """
        self.openapi_types = {
        }

        self.attribute_map = {
        }

    @classmethod
    def from_dict(cls, dikt) -> 'ServiceActionStatusEnum':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ServiceActionStatusEnum of this ServiceActionStatusEnum.  # noqa: E501
        :rtype: ServiceActionStatusEnum
        """
        return util.deserialize_model(dikt, cls)
