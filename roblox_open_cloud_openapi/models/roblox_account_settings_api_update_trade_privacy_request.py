from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.roblox_account_settings_api_update_trade_privacy_request_trade_privacy import (
    RobloxAccountSettingsApiUpdateTradePrivacyRequestTradePrivacy,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxAccountSettingsApiUpdateTradePrivacyRequest")


@_attrs_define
class RobloxAccountSettingsApiUpdateTradePrivacyRequest:
    """Request model for trade privacy setting update

    Attributes:
        trade_privacy (RobloxAccountSettingsApiUpdateTradePrivacyRequestTradePrivacy | Unset): The desired trade privacy
            setting for the active user ['Undefined' = 0, 'Disabled' = 1, 'NoOne' = 2, 'Friends' = 3, 'TopFriends' = 4,
            'Following' = 5, 'Followers' = 6, 'All' = 7]
    """

    trade_privacy: RobloxAccountSettingsApiUpdateTradePrivacyRequestTradePrivacy | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        trade_privacy: int | Unset = UNSET
        if not isinstance(self.trade_privacy, Unset):
            trade_privacy = self.trade_privacy.value

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if trade_privacy is not UNSET:
            field_dict["tradePrivacy"] = trade_privacy

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        _trade_privacy = d.pop("tradePrivacy", UNSET)
        trade_privacy: RobloxAccountSettingsApiUpdateTradePrivacyRequestTradePrivacy | Unset
        if isinstance(_trade_privacy, Unset):
            trade_privacy = UNSET
        else:
            trade_privacy = RobloxAccountSettingsApiUpdateTradePrivacyRequestTradePrivacy(_trade_privacy)

        roblox_account_settings_api_update_trade_privacy_request = cls(
            trade_privacy=trade_privacy,
        )

        return roblox_account_settings_api_update_trade_privacy_request
