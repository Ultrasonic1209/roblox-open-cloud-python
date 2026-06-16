from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.roblox_account_settings_api_trade_value_request_trade_value import (
    RobloxAccountSettingsApiTradeValueRequestTradeValue,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxAccountSettingsApiTradeValueRequest")


@_attrs_define
class RobloxAccountSettingsApiTradeValueRequest:
    """Request model for trade value setting update

    Attributes:
        trade_value (RobloxAccountSettingsApiTradeValueRequestTradeValue | Unset): The desired trade value setting for
            the active user ['Undefined' = 0, 'None' = 1, 'Low' = 2, 'Medium' = 3, 'High' = 4]
    """

    trade_value: RobloxAccountSettingsApiTradeValueRequestTradeValue | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        trade_value: int | Unset = UNSET
        if not isinstance(self.trade_value, Unset):
            trade_value = self.trade_value.value

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if trade_value is not UNSET:
            field_dict["tradeValue"] = trade_value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _trade_value = d.pop("tradeValue", UNSET)
        trade_value: RobloxAccountSettingsApiTradeValueRequestTradeValue | Unset
        if isinstance(_trade_value, Unset):
            trade_value = UNSET
        else:
            trade_value = RobloxAccountSettingsApiTradeValueRequestTradeValue(_trade_value)

        roblox_account_settings_api_trade_value_request = cls(
            trade_value=trade_value,
        )

        return roblox_account_settings_api_trade_value_request
