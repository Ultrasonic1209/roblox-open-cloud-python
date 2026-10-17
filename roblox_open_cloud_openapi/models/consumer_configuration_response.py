from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..models.response_account_state import ResponseAccountState
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.service_configuration import ServiceConfiguration


T = TypeVar("T", bound="ConsumerConfigurationResponse")


@_attrs_define
class ConsumerConfigurationResponse:
    """Response object for consumer configuration.

    Attributes:
        service_configurations (list[ServiceConfiguration]): Gets or sets the service configuration lists.
        account_state (ResponseAccountState | Unset): Account State in the HTTP response.
        account_info_complete (bool | Unset): Gets or sets a value indicating whether account information is complete.
    """

    service_configurations: list[ServiceConfiguration]
    account_state: ResponseAccountState | Unset = UNSET
    account_info_complete: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        service_configurations = []
        for service_configurations_item_data in self.service_configurations:
            service_configurations_item = service_configurations_item_data.to_dict()
            service_configurations.append(service_configurations_item)

        account_state: str | Unset = UNSET
        if not isinstance(self.account_state, Unset):
            account_state = self.account_state.value

        account_info_complete = self.account_info_complete

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "serviceConfigurations": service_configurations,
            }
        )
        if account_state is not UNSET:
            field_dict["accountState"] = account_state
        if account_info_complete is not UNSET:
            field_dict["accountInfoComplete"] = account_info_complete

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.service_configuration import ServiceConfiguration

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        service_configurations = []
        _service_configurations = d.pop("serviceConfigurations")
        for service_configurations_item_data in _service_configurations:
            service_configurations_item = ServiceConfiguration.from_dict(service_configurations_item_data)

            service_configurations.append(service_configurations_item)

        _account_state = d.pop("accountState", UNSET)
        account_state: ResponseAccountState | Unset
        if isinstance(_account_state, Unset):
            account_state = UNSET
        else:
            account_state = ResponseAccountState(_account_state)

        account_info_complete = d.pop("accountInfoComplete", UNSET)

        consumer_configuration_response = cls(
            service_configurations=service_configurations,
            account_state=account_state,
            account_info_complete=account_info_complete,
        )

        return consumer_configuration_response
