from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model import Model
from openapi_server.models.alert_c_linear_by_code import AlertCLinearByCode
from openapi_server.models.alert_c_method2_linear import AlertCMethod2Linear
from openapi_server.models.alert_c_method4_linear import AlertCMethod4Linear
from openapi_server import util

from openapi_server.models.alert_c_linear_by_code import AlertCLinearByCode  # noqa: E501
from openapi_server.models.alert_c_method2_linear import AlertCMethod2Linear  # noqa: E501
from openapi_server.models.alert_c_method4_linear import AlertCMethod4Linear  # noqa: E501

class AlertCLinearG(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, loc_alert_c_linear_by_code=None, loc_alert_c_method4_linear=None, loc_alert_c_method2_linear=None):  # noqa: E501
        """AlertCLinearG - a model defined in OpenAPI

        :param loc_alert_c_linear_by_code: The loc_alert_c_linear_by_code of this AlertCLinearG.  # noqa: E501
        :type loc_alert_c_linear_by_code: AlertCLinearByCode
        :param loc_alert_c_method4_linear: The loc_alert_c_method4_linear of this AlertCLinearG.  # noqa: E501
        :type loc_alert_c_method4_linear: AlertCMethod4Linear
        :param loc_alert_c_method2_linear: The loc_alert_c_method2_linear of this AlertCLinearG.  # noqa: E501
        :type loc_alert_c_method2_linear: AlertCMethod2Linear
        """
        self.openapi_types = {
            'loc_alert_c_linear_by_code': AlertCLinearByCode,
            'loc_alert_c_method4_linear': AlertCMethod4Linear,
            'loc_alert_c_method2_linear': AlertCMethod2Linear
        }

        self.attribute_map = {
            'loc_alert_c_linear_by_code': 'locAlertCLinearByCode',
            'loc_alert_c_method4_linear': 'locAlertCMethod4Linear',
            'loc_alert_c_method2_linear': 'locAlertCMethod2Linear'
        }

        self._loc_alert_c_linear_by_code = loc_alert_c_linear_by_code
        self._loc_alert_c_method4_linear = loc_alert_c_method4_linear
        self._loc_alert_c_method2_linear = loc_alert_c_method2_linear

    @classmethod
    def from_dict(cls, dikt) -> 'AlertCLinearG':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The AlertCLinearG of this AlertCLinearG.  # noqa: E501
        :rtype: AlertCLinearG
        """
        return util.deserialize_model(dikt, cls)

    @property
    def loc_alert_c_linear_by_code(self) -> AlertCLinearByCode:
        """Gets the loc_alert_c_linear_by_code of this AlertCLinearG.


        :return: The loc_alert_c_linear_by_code of this AlertCLinearG.
        :rtype: AlertCLinearByCode
        """
        return self._loc_alert_c_linear_by_code

    @loc_alert_c_linear_by_code.setter
    def loc_alert_c_linear_by_code(self, loc_alert_c_linear_by_code: AlertCLinearByCode):
        """Sets the loc_alert_c_linear_by_code of this AlertCLinearG.


        :param loc_alert_c_linear_by_code: The loc_alert_c_linear_by_code of this AlertCLinearG.
        :type loc_alert_c_linear_by_code: AlertCLinearByCode
        """

        self._loc_alert_c_linear_by_code = loc_alert_c_linear_by_code

    @property
    def loc_alert_c_method4_linear(self) -> AlertCMethod4Linear:
        """Gets the loc_alert_c_method4_linear of this AlertCLinearG.


        :return: The loc_alert_c_method4_linear of this AlertCLinearG.
        :rtype: AlertCMethod4Linear
        """
        return self._loc_alert_c_method4_linear

    @loc_alert_c_method4_linear.setter
    def loc_alert_c_method4_linear(self, loc_alert_c_method4_linear: AlertCMethod4Linear):
        """Sets the loc_alert_c_method4_linear of this AlertCLinearG.


        :param loc_alert_c_method4_linear: The loc_alert_c_method4_linear of this AlertCLinearG.
        :type loc_alert_c_method4_linear: AlertCMethod4Linear
        """

        self._loc_alert_c_method4_linear = loc_alert_c_method4_linear

    @property
    def loc_alert_c_method2_linear(self) -> AlertCMethod2Linear:
        """Gets the loc_alert_c_method2_linear of this AlertCLinearG.


        :return: The loc_alert_c_method2_linear of this AlertCLinearG.
        :rtype: AlertCMethod2Linear
        """
        return self._loc_alert_c_method2_linear

    @loc_alert_c_method2_linear.setter
    def loc_alert_c_method2_linear(self, loc_alert_c_method2_linear: AlertCMethod2Linear):
        """Sets the loc_alert_c_method2_linear of this AlertCLinearG.


        :param loc_alert_c_method2_linear: The loc_alert_c_method2_linear of this AlertCLinearG.
        :type loc_alert_c_method2_linear: AlertCMethod2Linear
        """

        self._loc_alert_c_method2_linear = loc_alert_c_method2_linear
