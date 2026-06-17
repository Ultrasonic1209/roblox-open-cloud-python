from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxAuthenticationApiModelsRequestFinishARPreAuthPasskeyRegistrationRequest")


@_attrs_define
class RobloxAuthenticationApiModelsRequestFinishARPreAuthPasskeyRegistrationRequest:
    """
    Attributes:
        recovery_session (str | Unset):
        passkey_session_id (str | Unset):
        passkey_registration_response (str | Unset):
        user_id (int | Unset):
        is_post_recovery (bool | Unset):
    """

    recovery_session: str | Unset = UNSET
    passkey_session_id: str | Unset = UNSET
    passkey_registration_response: str | Unset = UNSET
    user_id: int | Unset = UNSET
    is_post_recovery: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        recovery_session = self.recovery_session

        passkey_session_id = self.passkey_session_id

        passkey_registration_response = self.passkey_registration_response

        user_id = self.user_id

        is_post_recovery = self.is_post_recovery

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if recovery_session is not UNSET:
            field_dict["recoverySession"] = recovery_session
        if passkey_session_id is not UNSET:
            field_dict["passkeySessionId"] = passkey_session_id
        if passkey_registration_response is not UNSET:
            field_dict["passkeyRegistrationResponse"] = passkey_registration_response
        if user_id is not UNSET:
            field_dict["userId"] = user_id
        if is_post_recovery is not UNSET:
            field_dict["isPostRecovery"] = is_post_recovery

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        recovery_session = d.pop("recoverySession", UNSET)

        passkey_session_id = d.pop("passkeySessionId", UNSET)

        passkey_registration_response = d.pop("passkeyRegistrationResponse", UNSET)

        user_id = d.pop("userId", UNSET)

        is_post_recovery = d.pop("isPostRecovery", UNSET)

        roblox_authentication_api_models_request_finish_ar_pre_auth_passkey_registration_request = cls(
            recovery_session=recovery_session,
            passkey_session_id=passkey_session_id,
            passkey_registration_response=passkey_registration_response,
            user_id=user_id,
            is_post_recovery=is_post_recovery,
        )

        return roblox_authentication_api_models_request_finish_ar_pre_auth_passkey_registration_request
