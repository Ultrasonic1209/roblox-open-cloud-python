from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxApiDevelopModelsPrivateServerDetailsResponse")


@_attrs_define
class RobloxApiDevelopModelsPrivateServerDetailsResponse:
    """Model for private server details responses from the UniverseSettings controller.

    Attributes:
        is_enabled (bool | Unset): Whether or not VIP servers are enabled on this universe.
        price (int | Unset): The price of the VIP server.
        active_servers_count (int | Unset): The number of active VIP servers for this universe. A negative value
            indicates at least this many exist (i.e. -100 means 100+ active private servers).
        active_subscriptions_count (int | Unset): The number of active VIP server subscriptions. A negative value
            indicates at least this many exist (i.e. -100 means 100+ active subscriptions).
    """

    is_enabled: bool | Unset = UNSET
    price: int | Unset = UNSET
    active_servers_count: int | Unset = UNSET
    active_subscriptions_count: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        is_enabled = self.is_enabled

        price = self.price

        active_servers_count = self.active_servers_count

        active_subscriptions_count = self.active_subscriptions_count

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if is_enabled is not UNSET:
            field_dict["isEnabled"] = is_enabled
        if price is not UNSET:
            field_dict["price"] = price
        if active_servers_count is not UNSET:
            field_dict["activeServersCount"] = active_servers_count
        if active_subscriptions_count is not UNSET:
            field_dict["activeSubscriptionsCount"] = active_subscriptions_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        is_enabled = d.pop("isEnabled", UNSET)

        price = d.pop("price", UNSET)

        active_servers_count = d.pop("activeServersCount", UNSET)

        active_subscriptions_count = d.pop("activeSubscriptionsCount", UNSET)

        roblox_api_develop_models_private_server_details_response = cls(
            is_enabled=is_enabled,
            price=price,
            active_servers_count=active_servers_count,
            active_subscriptions_count=active_subscriptions_count,
        )

        return roblox_api_develop_models_private_server_details_response
