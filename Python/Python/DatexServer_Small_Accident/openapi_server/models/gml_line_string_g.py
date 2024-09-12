from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model import Model
from openapi_server.models.gml_line_string import GmlLineString
from openapi_server.models.gml_linear_ring import GmlLinearRing
from openapi_server import util

from openapi_server.models.gml_line_string import GmlLineString  # noqa: E501
from openapi_server.models.gml_linear_ring import GmlLinearRing  # noqa: E501

class GmlLineStringG(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, loc_gml_line_string=None, loc_gml_linear_ring=None):  # noqa: E501
        """GmlLineStringG - a model defined in OpenAPI

        :param loc_gml_line_string: The loc_gml_line_string of this GmlLineStringG.  # noqa: E501
        :type loc_gml_line_string: GmlLineString
        :param loc_gml_linear_ring: The loc_gml_linear_ring of this GmlLineStringG.  # noqa: E501
        :type loc_gml_linear_ring: GmlLinearRing
        """
        self.openapi_types = {
            'loc_gml_line_string': GmlLineString,
            'loc_gml_linear_ring': GmlLinearRing
        }

        self.attribute_map = {
            'loc_gml_line_string': 'locGmlLineString',
            'loc_gml_linear_ring': 'locGmlLinearRing'
        }

        self._loc_gml_line_string = loc_gml_line_string
        self._loc_gml_linear_ring = loc_gml_linear_ring

    @classmethod
    def from_dict(cls, dikt) -> 'GmlLineStringG':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The GmlLineStringG of this GmlLineStringG.  # noqa: E501
        :rtype: GmlLineStringG
        """
        return util.deserialize_model(dikt, cls)

    @property
    def loc_gml_line_string(self) -> GmlLineString:
        """Gets the loc_gml_line_string of this GmlLineStringG.


        :return: The loc_gml_line_string of this GmlLineStringG.
        :rtype: GmlLineString
        """
        return self._loc_gml_line_string

    @loc_gml_line_string.setter
    def loc_gml_line_string(self, loc_gml_line_string: GmlLineString):
        """Sets the loc_gml_line_string of this GmlLineStringG.


        :param loc_gml_line_string: The loc_gml_line_string of this GmlLineStringG.
        :type loc_gml_line_string: GmlLineString
        """

        self._loc_gml_line_string = loc_gml_line_string

    @property
    def loc_gml_linear_ring(self) -> GmlLinearRing:
        """Gets the loc_gml_linear_ring of this GmlLineStringG.


        :return: The loc_gml_linear_ring of this GmlLineStringG.
        :rtype: GmlLinearRing
        """
        return self._loc_gml_linear_ring

    @loc_gml_linear_ring.setter
    def loc_gml_linear_ring(self, loc_gml_linear_ring: GmlLinearRing):
        """Sets the loc_gml_linear_ring of this GmlLineStringG.


        :param loc_gml_linear_ring: The loc_gml_linear_ring of this GmlLineStringG.
        :type loc_gml_linear_ring: GmlLinearRing
        """

        self._loc_gml_linear_ring = loc_gml_linear_ring
