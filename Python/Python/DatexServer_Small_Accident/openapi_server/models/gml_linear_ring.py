from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model import Model
from openapi_server import util


class GmlLinearRing(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, srs_dimension=None, srs_name=None, pos_list=None, gml_line_string_extension_g=None, gml_linear_ring_extension_g=None):  # noqa: E501
        """GmlLinearRing - a model defined in OpenAPI

        :param srs_dimension: The srs_dimension of this GmlLinearRing.  # noqa: E501
        :type srs_dimension: int
        :param srs_name: The srs_name of this GmlLinearRing.  # noqa: E501
        :type srs_name: str
        :param pos_list: The pos_list of this GmlLinearRing.  # noqa: E501
        :type pos_list: str
        :param gml_line_string_extension_g: The gml_line_string_extension_g of this GmlLinearRing.  # noqa: E501
        :type gml_line_string_extension_g: Dict[str, object]
        :param gml_linear_ring_extension_g: The gml_linear_ring_extension_g of this GmlLinearRing.  # noqa: E501
        :type gml_linear_ring_extension_g: Dict[str, object]
        """
        self.openapi_types = {
            'srs_dimension': int,
            'srs_name': str,
            'pos_list': str,
            'gml_line_string_extension_g': Dict[str, object],
            'gml_linear_ring_extension_g': Dict[str, object]
        }

        self.attribute_map = {
            'srs_dimension': 'srsDimension',
            'srs_name': 'srsName',
            'pos_list': 'posList',
            'gml_line_string_extension_g': 'gmlLineStringExtensionG',
            'gml_linear_ring_extension_g': 'gmlLinearRingExtensionG'
        }

        self._srs_dimension = srs_dimension
        self._srs_name = srs_name
        self._pos_list = pos_list
        self._gml_line_string_extension_g = gml_line_string_extension_g
        self._gml_linear_ring_extension_g = gml_linear_ring_extension_g

    @classmethod
    def from_dict(cls, dikt) -> 'GmlLinearRing':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The GmlLinearRing of this GmlLinearRing.  # noqa: E501
        :rtype: GmlLinearRing
        """
        return util.deserialize_model(dikt, cls)

    @property
    def srs_dimension(self) -> int:
        """Gets the srs_dimension of this GmlLinearRing.


        :return: The srs_dimension of this GmlLinearRing.
        :rtype: int
        """
        return self._srs_dimension

    @srs_dimension.setter
    def srs_dimension(self, srs_dimension: int):
        """Sets the srs_dimension of this GmlLinearRing.


        :param srs_dimension: The srs_dimension of this GmlLinearRing.
        :type srs_dimension: int
        """
        if srs_dimension is not None and srs_dimension < 0:  # noqa: E501
            raise ValueError("Invalid value for `srs_dimension`, must be a value greater than or equal to `0`")  # noqa: E501

        self._srs_dimension = srs_dimension

    @property
    def srs_name(self) -> str:
        """Gets the srs_name of this GmlLinearRing.


        :return: The srs_name of this GmlLinearRing.
        :rtype: str
        """
        return self._srs_name

    @srs_name.setter
    def srs_name(self, srs_name: str):
        """Sets the srs_name of this GmlLinearRing.


        :param srs_name: The srs_name of this GmlLinearRing.
        :type srs_name: str
        """
        if srs_name is not None and len(srs_name) > 1024:
            raise ValueError("Invalid value for `srs_name`, length must be less than or equal to `1024`")  # noqa: E501

        self._srs_name = srs_name

    @property
    def pos_list(self) -> str:
        """Gets the pos_list of this GmlLinearRing.


        :return: The pos_list of this GmlLinearRing.
        :rtype: str
        """
        return self._pos_list

    @pos_list.setter
    def pos_list(self, pos_list: str):
        """Sets the pos_list of this GmlLinearRing.


        :param pos_list: The pos_list of this GmlLinearRing.
        :type pos_list: str
        """
        if pos_list is None:
            raise ValueError("Invalid value for `pos_list`, must not be `None`")  # noqa: E501

        self._pos_list = pos_list

    @property
    def gml_line_string_extension_g(self) -> Dict[str, object]:
        """Gets the gml_line_string_extension_g of this GmlLinearRing.


        :return: The gml_line_string_extension_g of this GmlLinearRing.
        :rtype: Dict[str, object]
        """
        return self._gml_line_string_extension_g

    @gml_line_string_extension_g.setter
    def gml_line_string_extension_g(self, gml_line_string_extension_g: Dict[str, object]):
        """Sets the gml_line_string_extension_g of this GmlLinearRing.


        :param gml_line_string_extension_g: The gml_line_string_extension_g of this GmlLinearRing.
        :type gml_line_string_extension_g: Dict[str, object]
        """

        self._gml_line_string_extension_g = gml_line_string_extension_g

    @property
    def gml_linear_ring_extension_g(self) -> Dict[str, object]:
        """Gets the gml_linear_ring_extension_g of this GmlLinearRing.


        :return: The gml_linear_ring_extension_g of this GmlLinearRing.
        :rtype: Dict[str, object]
        """
        return self._gml_linear_ring_extension_g

    @gml_linear_ring_extension_g.setter
    def gml_linear_ring_extension_g(self, gml_linear_ring_extension_g: Dict[str, object]):
        """Sets the gml_linear_ring_extension_g of this GmlLinearRing.


        :param gml_linear_ring_extension_g: The gml_linear_ring_extension_g of this GmlLinearRing.
        :type gml_linear_ring_extension_g: Dict[str, object]
        """

        self._gml_linear_ring_extension_g = gml_linear_ring_extension_g
