from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxAccountSettingsApiCurrentEmailsResponse")


@_attrs_define
class RobloxAccountSettingsApiCurrentEmailsResponse:
    """Response model for getting the user's verified and pending email addresses

    Attributes:
        verified_email (str | Unset): The user's most recent verified email address (masked)
        pending_email (str | Unset): The user's pending (unverified) email address if one exists (masked)
    """

    verified_email: str | Unset = UNSET
    pending_email: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        verified_email = self.verified_email

        pending_email = self.pending_email

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if verified_email is not UNSET:
            field_dict["verifiedEmail"] = verified_email
        if pending_email is not UNSET:
            field_dict["pendingEmail"] = pending_email

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        verified_email = d.pop("verifiedEmail", UNSET)

        pending_email = d.pop("pendingEmail", UNSET)

        roblox_account_settings_api_current_emails_response = cls(
            verified_email=verified_email,
            pending_email=pending_email,
        )

        return roblox_account_settings_api_current_emails_response
