from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxTradesApiTradeOfferRequest")


@_attrs_define
class RobloxTradesApiTradeOfferRequest:
    """
    Attributes:
        user_id (int | Unset):
        user_asset_ids (list[int] | Unset):
        robux (int | Unset):
    """

    user_id: int | Unset = UNSET
    user_asset_ids: list[int] | Unset = UNSET
    robux: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        user_id = self.user_id

        user_asset_ids: list[int] | Unset = UNSET
        if not isinstance(self.user_asset_ids, Unset):
            user_asset_ids = self.user_asset_ids

        robux = self.robux

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if user_id is not UNSET:
            field_dict["userId"] = user_id
        if user_asset_ids is not UNSET:
            field_dict["userAssetIds"] = user_asset_ids
        if robux is not UNSET:
            field_dict["robux"] = robux

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        user_id = d.pop("userId", UNSET)

        user_asset_ids = cast(list[int], d.pop("userAssetIds", UNSET))

        robux = d.pop("robux", UNSET)

        roblox_trades_api_trade_offer_request = cls(
            user_id=user_id,
            user_asset_ids=user_asset_ids,
            robux=robux,
        )

        return roblox_trades_api_trade_offer_request
