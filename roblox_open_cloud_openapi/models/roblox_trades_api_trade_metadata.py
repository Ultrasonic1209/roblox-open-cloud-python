from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxTradesApiTradeMetadata")


@_attrs_define
class RobloxTradesApiTradeMetadata:
    """
    Attributes:
        max_items_per_side (int | Unset):
        min_value_ratio (float | Unset):
        trade_system_max_robux_percent (float | Unset):
        trade_system_robux_fee (float | Unset):
    """

    max_items_per_side: int | Unset = UNSET
    min_value_ratio: float | Unset = UNSET
    trade_system_max_robux_percent: float | Unset = UNSET
    trade_system_robux_fee: float | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        max_items_per_side = self.max_items_per_side

        min_value_ratio = self.min_value_ratio

        trade_system_max_robux_percent = self.trade_system_max_robux_percent

        trade_system_robux_fee = self.trade_system_robux_fee

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if max_items_per_side is not UNSET:
            field_dict["maxItemsPerSide"] = max_items_per_side
        if min_value_ratio is not UNSET:
            field_dict["minValueRatio"] = min_value_ratio
        if trade_system_max_robux_percent is not UNSET:
            field_dict["tradeSystemMaxRobuxPercent"] = trade_system_max_robux_percent
        if trade_system_robux_fee is not UNSET:
            field_dict["tradeSystemRobuxFee"] = trade_system_robux_fee

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        max_items_per_side = d.pop("maxItemsPerSide", UNSET)

        min_value_ratio = d.pop("minValueRatio", UNSET)

        trade_system_max_robux_percent = d.pop("tradeSystemMaxRobuxPercent", UNSET)

        trade_system_robux_fee = d.pop("tradeSystemRobuxFee", UNSET)

        roblox_trades_api_trade_metadata = cls(
            max_items_per_side=max_items_per_side,
            min_value_ratio=min_value_ratio,
            trade_system_max_robux_percent=trade_system_max_robux_percent,
            trade_system_robux_fee=trade_system_robux_fee,
        )

        return roblox_trades_api_trade_metadata
