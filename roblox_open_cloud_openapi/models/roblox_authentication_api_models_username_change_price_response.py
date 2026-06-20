from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxAuthenticationApiModelsUsernameChangePriceResponse")


@_attrs_define
class RobloxAuthenticationApiModelsUsernameChangePriceResponse:
    """
    Attributes:
        price_in_robux (int | Unset):
        base_price_in_robux (int | Unset):
    """

    price_in_robux: int | Unset = UNSET
    base_price_in_robux: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        price_in_robux = self.price_in_robux

        base_price_in_robux = self.base_price_in_robux

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if price_in_robux is not UNSET:
            field_dict["priceInRobux"] = price_in_robux
        if base_price_in_robux is not UNSET:
            field_dict["basePriceInRobux"] = base_price_in_robux

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        price_in_robux = d.pop("priceInRobux", UNSET)

        base_price_in_robux = d.pop("basePriceInRobux", UNSET)

        roblox_authentication_api_models_username_change_price_response = cls(
            price_in_robux=price_in_robux,
            base_price_in_robux=base_price_in_robux,
        )

        return roblox_authentication_api_models_username_change_price_response
