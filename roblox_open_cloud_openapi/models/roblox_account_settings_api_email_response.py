from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxAccountSettingsApiEmailResponse")


@_attrs_define
class RobloxAccountSettingsApiEmailResponse:
    """Response model for getting the user's email address and verified status

    Attributes:
        email_address (str | Unset): The masked and formatted email address
        verified (bool | Unset): The verified status of the email
        can_bypass_password_for_email_update (bool | Unset): Whether password is required for updating email
    """

    email_address: str | Unset = UNSET
    verified: bool | Unset = UNSET
    can_bypass_password_for_email_update: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        email_address = self.email_address

        verified = self.verified

        can_bypass_password_for_email_update = self.can_bypass_password_for_email_update

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if email_address is not UNSET:
            field_dict["emailAddress"] = email_address
        if verified is not UNSET:
            field_dict["verified"] = verified
        if can_bypass_password_for_email_update is not UNSET:
            field_dict["canBypassPasswordForEmailUpdate"] = can_bypass_password_for_email_update

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        email_address = d.pop("emailAddress", UNSET)

        verified = d.pop("verified", UNSET)

        can_bypass_password_for_email_update = d.pop("canBypassPasswordForEmailUpdate", UNSET)

        roblox_account_settings_api_email_response = cls(
            email_address=email_address,
            verified=verified,
            can_bypass_password_for_email_update=can_bypass_password_for_email_update,
        )

        return roblox_account_settings_api_email_response
