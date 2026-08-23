from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.roblox_trades_api_models_v2_free_trades_allowance_response_window import (
    RobloxTradesApiModelsV2FreeTradesAllowanceResponseWindow,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxTradesApiModelsV2FreeTradesAllowanceResponse")


@_attrs_define
class RobloxTradesApiModelsV2FreeTradesAllowanceResponse:
    """
    Attributes:
        limit (int | Unset):
        remaining (int | Unset):
        window (RobloxTradesApiModelsV2FreeTradesAllowanceResponseWindow | Unset):  ['Day' = 1, 'Week' = 2, 'Month' = 3,
            'Year' = 4, 'Lifetime' = 5]
    """

    limit: int | Unset = UNSET
    remaining: int | Unset = UNSET
    window: RobloxTradesApiModelsV2FreeTradesAllowanceResponseWindow | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        limit = self.limit

        remaining = self.remaining

        window: str | Unset = UNSET
        if not isinstance(self.window, Unset):
            window = self.window.value

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if limit is not UNSET:
            field_dict["limit"] = limit
        if remaining is not UNSET:
            field_dict["remaining"] = remaining
        if window is not UNSET:
            field_dict["window"] = window

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        limit = d.pop("limit", UNSET)

        remaining = d.pop("remaining", UNSET)

        _window = d.pop("window", UNSET)
        window: RobloxTradesApiModelsV2FreeTradesAllowanceResponseWindow | Unset
        if isinstance(_window, Unset):
            window = UNSET
        else:
            window = RobloxTradesApiModelsV2FreeTradesAllowanceResponseWindow(_window)

        roblox_trades_api_models_v2_free_trades_allowance_response = cls(
            limit=limit,
            remaining=remaining,
            window=window,
        )

        return roblox_trades_api_models_v2_free_trades_allowance_response
