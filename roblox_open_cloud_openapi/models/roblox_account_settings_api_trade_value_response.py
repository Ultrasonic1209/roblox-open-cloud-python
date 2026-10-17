from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxAccountSettingsApiTradeValueResponse")


@_attrs_define
class RobloxAccountSettingsApiTradeValueResponse:
    """Response model for getting the user's trade value settings

    Attributes:
        trade_value (str | Unset): The current trade value setting for the current user
    """

    trade_value: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        trade_value = self.trade_value

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if trade_value is not UNSET:
            field_dict["tradeValue"] = trade_value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        trade_value = d.pop("tradeValue", UNSET)

        roblox_account_settings_api_trade_value_response = cls(
            trade_value=trade_value,
        )

        return roblox_account_settings_api_trade_value_response
