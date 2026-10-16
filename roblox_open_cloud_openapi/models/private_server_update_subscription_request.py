from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="PrivateServerUpdateSubscriptionRequest")


@_attrs_define
class PrivateServerUpdateSubscriptionRequest:
    """
    Attributes:
        active (bool | None | Unset):
        price (int | None | Unset):
    """

    active: bool | None | Unset = UNSET
    price: int | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        active: bool | None | Unset
        if isinstance(self.active, Unset):
            active = UNSET
        else:
            active = self.active

        price: int | None | Unset
        if isinstance(self.price, Unset):
            price = UNSET
        else:
            price = self.price

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if active is not UNSET:
            field_dict["active"] = active
        if price is not UNSET:
            field_dict["price"] = price

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}

        def _parse_active(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        active = _parse_active(d.pop("active", UNSET))

        def _parse_price(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        price = _parse_price(d.pop("price", UNSET))

        private_server_update_subscription_request = cls(
            active=active,
            price=price,
        )

        return private_server_update_subscription_request
