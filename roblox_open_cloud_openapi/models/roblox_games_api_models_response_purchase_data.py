from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxGamesApiModelsResponsePurchaseData")


@_attrs_define
class RobloxGamesApiModelsResponsePurchaseData:
    """
    Attributes:
        localized_fiat_price (str | Unset): Fiat purchase price in a localized string for display on client.
        base_price_id (str | Unset): ID of base price, needed by clients to prepare purchase url.
    """

    localized_fiat_price: str | Unset = UNSET
    base_price_id: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        localized_fiat_price = self.localized_fiat_price

        base_price_id = self.base_price_id

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if localized_fiat_price is not UNSET:
            field_dict["localizedFiatPrice"] = localized_fiat_price
        if base_price_id is not UNSET:
            field_dict["basePriceId"] = base_price_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        localized_fiat_price = d.pop("localizedFiatPrice", UNSET)

        base_price_id = d.pop("basePriceId", UNSET)

        roblox_games_api_models_response_purchase_data = cls(
            localized_fiat_price=localized_fiat_price,
            base_price_id=base_price_id,
        )

        return roblox_games_api_models_response_purchase_data
