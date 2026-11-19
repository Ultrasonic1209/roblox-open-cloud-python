from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxItemConfigurationApiGetItemUploadFeeResponse")


@_attrs_define
class RobloxItemConfigurationApiGetItemUploadFeeResponse:
    """Defines the response model for the GET v1/items/upload-fee endpoint.

    Attributes:
        can_afford (bool | Unset): Whether the user can afford the upload fee with their current balance.
        price (int | Unset): The upload fee.
        balance (int | Unset): The user's current robux balance.
    """

    can_afford: bool | Unset = UNSET
    price: int | Unset = UNSET
    balance: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        can_afford = self.can_afford

        price = self.price

        balance = self.balance

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if can_afford is not UNSET:
            field_dict["canAfford"] = can_afford
        if price is not UNSET:
            field_dict["price"] = price
        if balance is not UNSET:
            field_dict["balance"] = balance

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        can_afford = d.pop("canAfford", UNSET)

        price = d.pop("price", UNSET)

        balance = d.pop("balance", UNSET)

        roblox_item_configuration_api_get_item_upload_fee_response = cls(
            can_afford=can_afford,
            price=price,
            balance=balance,
        )

        return roblox_item_configuration_api_get_item_upload_fee_response
