from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxPublishApiVerifyAudioResponse")


@_attrs_define
class RobloxPublishApiVerifyAudioResponse:
    """Response model for verify audio endpoint.

    Attributes:
        name (str | Unset): Name of the audio file.
        price (int | Unset): Price in robux to publish the audio file.
        balance (int | Unset): User's current Robux balance.
        can_afford (bool | Unset): Boolean, true if the user can afford to purchase the publishing of the audio file.
    """

    name: str | Unset = UNSET
    price: int | Unset = UNSET
    balance: int | Unset = UNSET
    can_afford: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        price = self.price

        balance = self.balance

        can_afford = self.can_afford

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if price is not UNSET:
            field_dict["price"] = price
        if balance is not UNSET:
            field_dict["balance"] = balance
        if can_afford is not UNSET:
            field_dict["canAfford"] = can_afford

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        price = d.pop("price", UNSET)

        balance = d.pop("balance", UNSET)

        can_afford = d.pop("canAfford", UNSET)

        roblox_publish_api_verify_audio_response = cls(
            name=name,
            price=price,
            balance=balance,
            can_afford=can_afford,
        )

        return roblox_publish_api_verify_audio_response
