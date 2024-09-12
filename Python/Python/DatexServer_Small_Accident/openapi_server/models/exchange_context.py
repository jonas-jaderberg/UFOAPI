from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model import Model
from openapi_server.models.agent import Agent
from openapi_server.models.operating_mode_enum_g import OperatingModeEnumG
from openapi_server.models.protocol_type_enum_g import ProtocolTypeEnumG
from openapi_server.models.subscription import Subscription
from openapi_server.models.update_method_enum_g import UpdateMethodEnumG
from openapi_server import util

from openapi_server.models.agent import Agent  # noqa: E501
from openapi_server.models.operating_mode_enum_g import OperatingModeEnumG  # noqa: E501
from openapi_server.models.protocol_type_enum_g import ProtocolTypeEnumG  # noqa: E501
from openapi_server.models.subscription import Subscription  # noqa: E501
from openapi_server.models.update_method_enum_g import UpdateMethodEnumG  # noqa: E501

class ExchangeContext(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, coded_exchange_protocol=None, exchange_specification_version=None, operating_mode=None, update_method=None, non_coded_exchange_protocol=None, supplier_or_cis_requester=None, client_or_cis_provider=None, subscription=None, exchange_context_extension_g=None):  # noqa: E501
        """ExchangeContext - a model defined in OpenAPI

        :param coded_exchange_protocol: The coded_exchange_protocol of this ExchangeContext.  # noqa: E501
        :type coded_exchange_protocol: ProtocolTypeEnumG
        :param exchange_specification_version: The exchange_specification_version of this ExchangeContext.  # noqa: E501
        :type exchange_specification_version: str
        :param operating_mode: The operating_mode of this ExchangeContext.  # noqa: E501
        :type operating_mode: OperatingModeEnumG
        :param update_method: The update_method of this ExchangeContext.  # noqa: E501
        :type update_method: UpdateMethodEnumG
        :param non_coded_exchange_protocol: The non_coded_exchange_protocol of this ExchangeContext.  # noqa: E501
        :type non_coded_exchange_protocol: str
        :param supplier_or_cis_requester: The supplier_or_cis_requester of this ExchangeContext.  # noqa: E501
        :type supplier_or_cis_requester: Agent
        :param client_or_cis_provider: The client_or_cis_provider of this ExchangeContext.  # noqa: E501
        :type client_or_cis_provider: List[Agent]
        :param subscription: The subscription of this ExchangeContext.  # noqa: E501
        :type subscription: Subscription
        :param exchange_context_extension_g: The exchange_context_extension_g of this ExchangeContext.  # noqa: E501
        :type exchange_context_extension_g: Dict[str, object]
        """
        self.openapi_types = {
            'coded_exchange_protocol': ProtocolTypeEnumG,
            'exchange_specification_version': str,
            'operating_mode': OperatingModeEnumG,
            'update_method': UpdateMethodEnumG,
            'non_coded_exchange_protocol': str,
            'supplier_or_cis_requester': Agent,
            'client_or_cis_provider': List[Agent],
            'subscription': Subscription,
            'exchange_context_extension_g': Dict[str, object]
        }

        self.attribute_map = {
            'coded_exchange_protocol': 'codedExchangeProtocol',
            'exchange_specification_version': 'exchangeSpecificationVersion',
            'operating_mode': 'operatingMode',
            'update_method': 'updateMethod',
            'non_coded_exchange_protocol': 'nonCodedExchangeProtocol',
            'supplier_or_cis_requester': 'supplierOrCisRequester',
            'client_or_cis_provider': 'clientOrCisProvider',
            'subscription': 'subscription',
            'exchange_context_extension_g': 'exchangeContextExtensionG'
        }

        self._coded_exchange_protocol = coded_exchange_protocol
        self._exchange_specification_version = exchange_specification_version
        self._operating_mode = operating_mode
        self._update_method = update_method
        self._non_coded_exchange_protocol = non_coded_exchange_protocol
        self._supplier_or_cis_requester = supplier_or_cis_requester
        self._client_or_cis_provider = client_or_cis_provider
        self._subscription = subscription
        self._exchange_context_extension_g = exchange_context_extension_g

    @classmethod
    def from_dict(cls, dikt) -> 'ExchangeContext':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ExchangeContext of this ExchangeContext.  # noqa: E501
        :rtype: ExchangeContext
        """
        return util.deserialize_model(dikt, cls)

    @property
    def coded_exchange_protocol(self) -> ProtocolTypeEnumG:
        """Gets the coded_exchange_protocol of this ExchangeContext.


        :return: The coded_exchange_protocol of this ExchangeContext.
        :rtype: ProtocolTypeEnumG
        """
        return self._coded_exchange_protocol

    @coded_exchange_protocol.setter
    def coded_exchange_protocol(self, coded_exchange_protocol: ProtocolTypeEnumG):
        """Sets the coded_exchange_protocol of this ExchangeContext.


        :param coded_exchange_protocol: The coded_exchange_protocol of this ExchangeContext.
        :type coded_exchange_protocol: ProtocolTypeEnumG
        """
        if coded_exchange_protocol is None:
            raise ValueError("Invalid value for `coded_exchange_protocol`, must not be `None`")  # noqa: E501

        self._coded_exchange_protocol = coded_exchange_protocol

    @property
    def exchange_specification_version(self) -> str:
        """Gets the exchange_specification_version of this ExchangeContext.


        :return: The exchange_specification_version of this ExchangeContext.
        :rtype: str
        """
        return self._exchange_specification_version

    @exchange_specification_version.setter
    def exchange_specification_version(self, exchange_specification_version: str):
        """Sets the exchange_specification_version of this ExchangeContext.


        :param exchange_specification_version: The exchange_specification_version of this ExchangeContext.
        :type exchange_specification_version: str
        """
        if exchange_specification_version is None:
            raise ValueError("Invalid value for `exchange_specification_version`, must not be `None`")  # noqa: E501
        if exchange_specification_version is not None and len(exchange_specification_version) > 1024:
            raise ValueError("Invalid value for `exchange_specification_version`, length must be less than or equal to `1024`")  # noqa: E501

        self._exchange_specification_version = exchange_specification_version

    @property
    def operating_mode(self) -> OperatingModeEnumG:
        """Gets the operating_mode of this ExchangeContext.


        :return: The operating_mode of this ExchangeContext.
        :rtype: OperatingModeEnumG
        """
        return self._operating_mode

    @operating_mode.setter
    def operating_mode(self, operating_mode: OperatingModeEnumG):
        """Sets the operating_mode of this ExchangeContext.


        :param operating_mode: The operating_mode of this ExchangeContext.
        :type operating_mode: OperatingModeEnumG
        """

        self._operating_mode = operating_mode

    @property
    def update_method(self) -> UpdateMethodEnumG:
        """Gets the update_method of this ExchangeContext.


        :return: The update_method of this ExchangeContext.
        :rtype: UpdateMethodEnumG
        """
        return self._update_method

    @update_method.setter
    def update_method(self, update_method: UpdateMethodEnumG):
        """Sets the update_method of this ExchangeContext.


        :param update_method: The update_method of this ExchangeContext.
        :type update_method: UpdateMethodEnumG
        """

        self._update_method = update_method

    @property
    def non_coded_exchange_protocol(self) -> str:
        """Gets the non_coded_exchange_protocol of this ExchangeContext.


        :return: The non_coded_exchange_protocol of this ExchangeContext.
        :rtype: str
        """
        return self._non_coded_exchange_protocol

    @non_coded_exchange_protocol.setter
    def non_coded_exchange_protocol(self, non_coded_exchange_protocol: str):
        """Sets the non_coded_exchange_protocol of this ExchangeContext.


        :param non_coded_exchange_protocol: The non_coded_exchange_protocol of this ExchangeContext.
        :type non_coded_exchange_protocol: str
        """
        if non_coded_exchange_protocol is not None and len(non_coded_exchange_protocol) > 1024:
            raise ValueError("Invalid value for `non_coded_exchange_protocol`, length must be less than or equal to `1024`")  # noqa: E501

        self._non_coded_exchange_protocol = non_coded_exchange_protocol

    @property
    def supplier_or_cis_requester(self) -> Agent:
        """Gets the supplier_or_cis_requester of this ExchangeContext.


        :return: The supplier_or_cis_requester of this ExchangeContext.
        :rtype: Agent
        """
        return self._supplier_or_cis_requester

    @supplier_or_cis_requester.setter
    def supplier_or_cis_requester(self, supplier_or_cis_requester: Agent):
        """Sets the supplier_or_cis_requester of this ExchangeContext.


        :param supplier_or_cis_requester: The supplier_or_cis_requester of this ExchangeContext.
        :type supplier_or_cis_requester: Agent
        """
        if supplier_or_cis_requester is None:
            raise ValueError("Invalid value for `supplier_or_cis_requester`, must not be `None`")  # noqa: E501

        self._supplier_or_cis_requester = supplier_or_cis_requester

    @property
    def client_or_cis_provider(self) -> List[Agent]:
        """Gets the client_or_cis_provider of this ExchangeContext.


        :return: The client_or_cis_provider of this ExchangeContext.
        :rtype: List[Agent]
        """
        return self._client_or_cis_provider

    @client_or_cis_provider.setter
    def client_or_cis_provider(self, client_or_cis_provider: List[Agent]):
        """Sets the client_or_cis_provider of this ExchangeContext.


        :param client_or_cis_provider: The client_or_cis_provider of this ExchangeContext.
        :type client_or_cis_provider: List[Agent]
        """
        if client_or_cis_provider is not None and len(client_or_cis_provider) < 0:
            raise ValueError("Invalid value for `client_or_cis_provider`, number of items must be greater than or equal to `0`")  # noqa: E501

        self._client_or_cis_provider = client_or_cis_provider

    @property
    def subscription(self) -> Subscription:
        """Gets the subscription of this ExchangeContext.


        :return: The subscription of this ExchangeContext.
        :rtype: Subscription
        """
        return self._subscription

    @subscription.setter
    def subscription(self, subscription: Subscription):
        """Sets the subscription of this ExchangeContext.


        :param subscription: The subscription of this ExchangeContext.
        :type subscription: Subscription
        """

        self._subscription = subscription

    @property
    def exchange_context_extension_g(self) -> Dict[str, object]:
        """Gets the exchange_context_extension_g of this ExchangeContext.


        :return: The exchange_context_extension_g of this ExchangeContext.
        :rtype: Dict[str, object]
        """
        return self._exchange_context_extension_g

    @exchange_context_extension_g.setter
    def exchange_context_extension_g(self, exchange_context_extension_g: Dict[str, object]):
        """Sets the exchange_context_extension_g of this ExchangeContext.


        :param exchange_context_extension_g: The exchange_context_extension_g of this ExchangeContext.
        :type exchange_context_extension_g: Dict[str, object]
        """

        self._exchange_context_extension_g = exchange_context_extension_g
