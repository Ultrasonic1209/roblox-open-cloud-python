from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxTradesApiModelsV2NewTradeResponse")


@_attrs_define
class RobloxTradesApiModelsV2NewTradeResponse:
    """Represents a newly created trade.

    Attributes:
        trade_id (int | Unset): The ID of the trade.
    """

    trade_id: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        trade_id = self.trade_id

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if trade_id is not UNSET:
            field_dict["tradeId"] = trade_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        trade_id = d.pop("tradeId", UNSET)

        roblox_trades_api_models_v2_new_trade_response = cls(
            trade_id=trade_id,
        )

        return roblox_trades_api_models_v2_new_trade_response
