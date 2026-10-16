from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.roblox_account_settings_api_trade_privacy_update_response_inventory_privacy import (
    RobloxAccountSettingsApiTradePrivacyUpdateResponseInventoryPrivacy,
)
from ..models.roblox_account_settings_api_trade_privacy_update_response_privacy_setting_response import (
    RobloxAccountSettingsApiTradePrivacyUpdateResponsePrivacySettingResponse,
)
from ..models.roblox_account_settings_api_trade_privacy_update_response_trade_privacy import (
    RobloxAccountSettingsApiTradePrivacyUpdateResponseTradePrivacy,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxAccountSettingsApiTradePrivacyUpdateResponse")


@_attrs_define
class RobloxAccountSettingsApiTradePrivacyUpdateResponse:
    """Response model for updating the user's trade privacy settings

    Attributes:
        trade_privacy (RobloxAccountSettingsApiTradePrivacyUpdateResponseTradePrivacy | Unset): The trade privacy
            setting after updating ['Undefined' = 0, 'Disabled' = 1, 'NoOne' = 2, 'Friends' = 3, 'TopFriends' = 4,
            'Following' = 5, 'Followers' = 6, 'All' = 7]
        inventory_privacy (RobloxAccountSettingsApiTradePrivacyUpdateResponseInventoryPrivacy | Unset): The inventory
            privacy setting after updating ['NoOne' = 1, 'Friends' = 2, 'FriendsAndFollowing' = 3,
            'FriendsFollowingAndFollowers' = 4, 'AllAuthenticatedUsers' = 5, 'AllUsers' = 6]
        privacy_setting_response (RobloxAccountSettingsApiTradePrivacyUpdateResponsePrivacySettingResponse | Unset): The
            response state after updating trade privacy ['Success' = 0, 'Conflict' = 1]
    """

    trade_privacy: RobloxAccountSettingsApiTradePrivacyUpdateResponseTradePrivacy | Unset = UNSET
    inventory_privacy: RobloxAccountSettingsApiTradePrivacyUpdateResponseInventoryPrivacy | Unset = UNSET
    privacy_setting_response: RobloxAccountSettingsApiTradePrivacyUpdateResponsePrivacySettingResponse | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        trade_privacy: int | Unset = UNSET
        if not isinstance(self.trade_privacy, Unset):
            trade_privacy = self.trade_privacy.value

        inventory_privacy: int | Unset = UNSET
        if not isinstance(self.inventory_privacy, Unset):
            inventory_privacy = self.inventory_privacy.value

        privacy_setting_response: int | Unset = UNSET
        if not isinstance(self.privacy_setting_response, Unset):
            privacy_setting_response = self.privacy_setting_response.value

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if trade_privacy is not UNSET:
            field_dict["tradePrivacy"] = trade_privacy
        if inventory_privacy is not UNSET:
            field_dict["inventoryPrivacy"] = inventory_privacy
        if privacy_setting_response is not UNSET:
            field_dict["privacySettingResponse"] = privacy_setting_response

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        _trade_privacy = d.pop("tradePrivacy", UNSET)
        trade_privacy: RobloxAccountSettingsApiTradePrivacyUpdateResponseTradePrivacy | Unset
        if isinstance(_trade_privacy, Unset):
            trade_privacy = UNSET
        else:
            trade_privacy = RobloxAccountSettingsApiTradePrivacyUpdateResponseTradePrivacy(_trade_privacy)

        _inventory_privacy = d.pop("inventoryPrivacy", UNSET)
        inventory_privacy: RobloxAccountSettingsApiTradePrivacyUpdateResponseInventoryPrivacy | Unset
        if isinstance(_inventory_privacy, Unset):
            inventory_privacy = UNSET
        else:
            inventory_privacy = RobloxAccountSettingsApiTradePrivacyUpdateResponseInventoryPrivacy(_inventory_privacy)

        _privacy_setting_response = d.pop("privacySettingResponse", UNSET)
        privacy_setting_response: RobloxAccountSettingsApiTradePrivacyUpdateResponsePrivacySettingResponse | Unset
        if isinstance(_privacy_setting_response, Unset):
            privacy_setting_response = UNSET
        else:
            privacy_setting_response = RobloxAccountSettingsApiTradePrivacyUpdateResponsePrivacySettingResponse(
                _privacy_setting_response
            )

        roblox_account_settings_api_trade_privacy_update_response = cls(
            trade_privacy=trade_privacy,
            inventory_privacy=inventory_privacy,
            privacy_setting_response=privacy_setting_response,
        )

        return roblox_account_settings_api_trade_privacy_update_response
