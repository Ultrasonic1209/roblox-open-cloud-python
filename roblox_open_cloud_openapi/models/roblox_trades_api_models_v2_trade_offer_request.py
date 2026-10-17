from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxTradesApiModelsV2TradeOfferRequest")


@_attrs_define
class RobloxTradesApiModelsV2TradeOfferRequest:
    """Represents a trade offer.

    Attributes:
        user_id (int | Unset): The user ID of the offer.
        robux (int | Unset): The amount of Robux in the trade offer.
        collectible_item_instance_ids (list[str] | Unset): List of items in the trade offer.
    """

    user_id: int | Unset = UNSET
    robux: int | Unset = UNSET
    collectible_item_instance_ids: list[str] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        user_id = self.user_id

        robux = self.robux

        collectible_item_instance_ids: list[str] | Unset = UNSET
        if not isinstance(self.collectible_item_instance_ids, Unset):
            collectible_item_instance_ids = self.collectible_item_instance_ids

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if user_id is not UNSET:
            field_dict["userId"] = user_id
        if robux is not UNSET:
            field_dict["robux"] = robux
        if collectible_item_instance_ids is not UNSET:
            field_dict["collectibleItemInstanceIds"] = collectible_item_instance_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        user_id = d.pop("userId", UNSET)

        robux = d.pop("robux", UNSET)

        collectible_item_instance_ids = cast(list[str], d.pop("collectibleItemInstanceIds", UNSET))

        roblox_trades_api_models_v2_trade_offer_request = cls(
            user_id=user_id,
            robux=robux,
            collectible_item_instance_ids=collectible_item_instance_ids,
        )

        return roblox_trades_api_models_v2_trade_offer_request
