from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxAccountSettingsApiSendVerifyEmailRequest")


@_attrs_define
class RobloxAccountSettingsApiSendVerifyEmailRequest:
    """Request model for sending a verify email request

    Attributes:
        free_item (bool | Unset): Whether the user will see messaging that they received a free item after verifying
            their email
        is_ads_account (bool | Unset): Whether the request is coming from ads site
    """

    free_item: bool | Unset = UNSET
    is_ads_account: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        free_item = self.free_item

        is_ads_account = self.is_ads_account

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if free_item is not UNSET:
            field_dict["freeItem"] = free_item
        if is_ads_account is not UNSET:
            field_dict["isAdsAccount"] = is_ads_account

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        free_item = d.pop("freeItem", UNSET)

        is_ads_account = d.pop("isAdsAccount", UNSET)

        roblox_account_settings_api_send_verify_email_request = cls(
            free_item=free_item,
            is_ads_account=is_ads_account,
        )

        return roblox_account_settings_api_send_verify_email_request
