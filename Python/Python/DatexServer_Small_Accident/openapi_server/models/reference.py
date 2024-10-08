from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model import Model
from openapi_server import util


class Reference(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, id_g=None):  # noqa: E501
        """Reference - a model defined in OpenAPI

        :param id_g: The id_g of this Reference.  # noqa: E501
        :type id_g: str
        """
        self.openapi_types = {
            'id_g': str
        }

        self.attribute_map = {
            'id_g': 'idG'
        }

        self._id_g = id_g

    @classmethod
    def from_dict(cls, dikt) -> 'Reference':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Reference of this Reference.  # noqa: E501
        :rtype: Reference
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id_g(self) -> str:
        """Gets the id_g of this Reference.


        :return: The id_g of this Reference.
        :rtype: str
        """
        return self._id_g

    @id_g.setter
    def id_g(self, id_g: str):
        """Sets the id_g of this Reference.


        :param id_g: The id_g of this Reference.
        :type id_g: str
        """
        if id_g is None:
            raise ValueError("Invalid value for `id_g`, must not be `None`")  # noqa: E501

        self._id_g = id_g
