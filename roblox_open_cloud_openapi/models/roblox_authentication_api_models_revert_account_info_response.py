from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxAuthenticationApiModelsRevertAccountInfoResponse")


@_attrs_define
class RobloxAuthenticationApiModelsRevertAccountInfoResponse:
    """
    Attributes:
        is_two_step_verification_enabled (bool | Unset):
        is_email_verified (bool | Unset):
        is_email_changed (bool | Unset):
        is_phone_verified (bool | Unset):
        user_id (int | Unset):
        username (str | Unset):
        ticket (str | Unset):
    """

    is_two_step_verification_enabled: bool | Unset = UNSET
    is_email_verified: bool | Unset = UNSET
    is_email_changed: bool | Unset = UNSET
    is_phone_verified: bool | Unset = UNSET
    user_id: int | Unset = UNSET
    username: str | Unset = UNSET
    ticket: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        is_two_step_verification_enabled = self.is_two_step_verification_enabled

        is_email_verified = self.is_email_verified

        is_email_changed = self.is_email_changed

        is_phone_verified = self.is_phone_verified

        user_id = self.user_id

        username = self.username

        ticket = self.ticket

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if is_two_step_verification_enabled is not UNSET:
            field_dict["isTwoStepVerificationEnabled"] = is_two_step_verification_enabled
        if is_email_verified is not UNSET:
            field_dict["isEmailVerified"] = is_email_verified
        if is_email_changed is not UNSET:
            field_dict["isEmailChanged"] = is_email_changed
        if is_phone_verified is not UNSET:
            field_dict["isPhoneVerified"] = is_phone_verified
        if user_id is not UNSET:
            field_dict["userId"] = user_id
        if username is not UNSET:
            field_dict["username"] = username
        if ticket is not UNSET:
            field_dict["ticket"] = ticket

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        is_two_step_verification_enabled = d.pop("isTwoStepVerificationEnabled", UNSET)

        is_email_verified = d.pop("isEmailVerified", UNSET)

        is_email_changed = d.pop("isEmailChanged", UNSET)

        is_phone_verified = d.pop("isPhoneVerified", UNSET)

        user_id = d.pop("userId", UNSET)

        username = d.pop("username", UNSET)

        ticket = d.pop("ticket", UNSET)

        roblox_authentication_api_models_revert_account_info_response = cls(
            is_two_step_verification_enabled=is_two_step_verification_enabled,
            is_email_verified=is_email_verified,
            is_email_changed=is_email_changed,
            is_phone_verified=is_phone_verified,
            user_id=user_id,
            username=username,
            ticket=ticket,
        )

        return roblox_authentication_api_models_revert_account_info_response
