from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="RobloxItemConfigurationApiCancelScheduledSaleStatusResponse")


@_attrs_define
class RobloxItemConfigurationApiCancelScheduledSaleStatusResponse:
    """Defines the response model for the DELETE M:Roblox.ItemConfiguration.Api.CollectiblesController.CancelScheduledSaleS
    tatusAsync(System.String,System.Threading.CancellationToken).

    """

    def to_dict(self) -> dict[str, Any]:

        field_dict: dict[str, Any] = {}

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        roblox_item_configuration_api_cancel_scheduled_sale_status_response = cls()

        return roblox_item_configuration_api_cancel_scheduled_sale_status_response
