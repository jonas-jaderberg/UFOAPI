from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model import Model
from openapi_server.models.dynamic_information import DynamicInformation
from openapi_server.models.exchange_context import ExchangeContext
from openapi_server.models.message_type_enum_g import MessageTypeEnumG
from openapi_server import util

from openapi_server.models.dynamic_information import DynamicInformation  # noqa: E501
from openapi_server.models.exchange_context import ExchangeContext  # noqa: E501
from openapi_server.models.message_type_enum_g import MessageTypeEnumG  # noqa: E501

class ExchangheInformation(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, message_type=None, exchange_context=None, dynamic_information=None, exchange_information_extension_g=None):  # noqa: E501
        """ExchangheInformation - a model defined in OpenAPI

        :param message_type: The message_type of this ExchangheInformation.  # noqa: E501
        :type message_type: MessageTypeEnumG
        :param exchange_context: The exchange_context of this ExchangheInformation.  # noqa: E501
        :type exchange_context: ExchangeContext
        :param dynamic_information: The dynamic_information of this ExchangheInformation.  # noqa: E501
        :type dynamic_information: DynamicInformation
        :param exchange_information_extension_g: The exchange_information_extension_g of this ExchangheInformation.  # noqa: E501
        :type exchange_information_extension_g: Dict[str, object]
        """
        self.openapi_types = {
            'message_type': MessageTypeEnumG,
            'exchange_context': ExchangeContext,
            'dynamic_information': DynamicInformation,
            'exchange_information_extension_g': Dict[str, object]
        }

        self.attribute_map = {
            'message_type': 'messageType',
            'exchange_context': 'exchangeContext',
            'dynamic_information': 'dynamicInformation',
            'exchange_information_extension_g': 'exchangeInformationExtensionG'
        }

        self._message_type = message_type
        self._exchange_context = exchange_context
        self._dynamic_information = dynamic_information
        self._exchange_information_extension_g = exchange_information_extension_g

    @classmethod
    def from_dict(cls, dikt) -> 'ExchangheInformation':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ExchangheInformation of this ExchangheInformation.  # noqa: E501
        :rtype: ExchangheInformation
        """
        return util.deserialize_model(dikt, cls)

    @property
    def message_type(self) -> MessageTypeEnumG:
        """Gets the message_type of this ExchangheInformation.


        :return: The message_type of this ExchangheInformation.
        :rtype: MessageTypeEnumG
        """
        return self._message_type

    @message_type.setter
    def message_type(self, message_type: MessageTypeEnumG):
        """Sets the message_type of this ExchangheInformation.


        :param message_type: The message_type of this ExchangheInformation.
        :type message_type: MessageTypeEnumG
        """

        self._message_type = message_type

    @property
    def exchange_context(self) -> ExchangeContext:
        """Gets the exchange_context of this ExchangheInformation.


        :return: The exchange_context of this ExchangheInformation.
        :rtype: ExchangeContext
        """
        return self._exchange_context

    @exchange_context.setter
    def exchange_context(self, exchange_context: ExchangeContext):
        """Sets the exchange_context of this ExchangheInformation.


        :param exchange_context: The exchange_context of this ExchangheInformation.
        :type exchange_context: ExchangeContext
        """
        if exchange_context is None:
            raise ValueError("Invalid value for `exchange_context`, must not be `None`")  # noqa: E501

        self._exchange_context = exchange_context

    @property
    def dynamic_information(self) -> DynamicInformation:
        """Gets the dynamic_information of this ExchangheInformation.


        :return: The dynamic_information of this ExchangheInformation.
        :rtype: DynamicInformation
        """
        return self._dynamic_information

    @dynamic_information.setter
    def dynamic_information(self, dynamic_information: DynamicInformation):
        """Sets the dynamic_information of this ExchangheInformation.


        :param dynamic_information: The dynamic_information of this ExchangheInformation.
        :type dynamic_information: DynamicInformation
        """
        if dynamic_information is None:
            raise ValueError("Invalid value for `dynamic_information`, must not be `None`")  # noqa: E501

        self._dynamic_information = dynamic_information

    @property
    def exchange_information_extension_g(self) -> Dict[str, object]:
        """Gets the exchange_information_extension_g of this ExchangheInformation.


        :return: The exchange_information_extension_g of this ExchangheInformation.
        :rtype: Dict[str, object]
        """
        return self._exchange_information_extension_g

    @exchange_information_extension_g.setter
    def exchange_information_extension_g(self, exchange_information_extension_g: Dict[str, object]):
        """Sets the exchange_information_extension_g of this ExchangheInformation.


        :param exchange_information_extension_g: The exchange_information_extension_g of this ExchangheInformation.
        :type exchange_information_extension_g: Dict[str, object]
        """

        self._exchange_information_extension_g = exchange_information_extension_g
