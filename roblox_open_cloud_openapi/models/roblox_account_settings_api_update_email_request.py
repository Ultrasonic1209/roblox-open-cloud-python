from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxAccountSettingsApiUpdateEmailRequest")


@_attrs_define
class RobloxAccountSettingsApiUpdateEmailRequest:
    """Request model for updating an email

    Attributes:
        password (str | Unset): The user's password.
        email_address (str | Unset): The new email address to set.
        skip_verification_email (bool | Unset): Should the email controller skip sending the verification email.
        is_ads_account (bool | Unset): Whether the request is coming from ads site.
    """

    password: str | Unset = UNSET
    email_address: str | Unset = UNSET
    skip_verification_email: bool | Unset = UNSET
    is_ads_account: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        password = self.password

        email_address = self.email_address

        skip_verification_email = self.skip_verification_email

        is_ads_account = self.is_ads_account

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if password is not UNSET:
            field_dict["password"] = password
        if email_address is not UNSET:
            field_dict["emailAddress"] = email_address
        if skip_verification_email is not UNSET:
            field_dict["skipVerificationEmail"] = skip_verification_email
        if is_ads_account is not UNSET:
            field_dict["isAdsAccount"] = is_ads_account

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        password = d.pop("password", UNSET)

        email_address = d.pop("emailAddress", UNSET)

        skip_verification_email = d.pop("skipVerificationEmail", UNSET)

        is_ads_account = d.pop("isAdsAccount", UNSET)

        roblox_account_settings_api_update_email_request = cls(
            password=password,
            email_address=email_address,
            skip_verification_email=skip_verification_email,
            is_ads_account=is_ads_account,
        )

        return roblox_account_settings_api_update_email_request
