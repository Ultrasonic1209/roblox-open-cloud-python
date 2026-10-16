from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxAccountSettingsApiTradePrivacyResponse")


@_attrs_define
class RobloxAccountSettingsApiTradePrivacyResponse:
    """Response model for getting the user's trade privacy settings

    Attributes:
        trade_privacy (str | Unset): The current trade privacy setting for the current user
    """

    trade_privacy: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        trade_privacy = self.trade_privacy

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if trade_privacy is not UNSET:
            field_dict["tradePrivacy"] = trade_privacy

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        trade_privacy = d.pop("tradePrivacy", UNSET)

        roblox_account_settings_api_trade_privacy_response = cls(
            trade_privacy=trade_privacy,
        )

        return roblox_account_settings_api_trade_privacy_response
