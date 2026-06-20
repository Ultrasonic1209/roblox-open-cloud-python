from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.roblox_authentication_api_models_send_reset_password_request_target_type import (
    RobloxAuthenticationApiModelsSendResetPasswordRequestTargetType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxAuthenticationApiModelsSendResetPasswordRequest")


@_attrs_define
class RobloxAuthenticationApiModelsSendResetPasswordRequest:
    """
    Attributes:
        target_type (RobloxAuthenticationApiModelsSendResetPasswordRequestTargetType | Unset):  ['Email' = 0,
            'PhoneNumber' = 1, 'RecoverySessionID' = 2]
        target (str | Unset):
        captcha_id (str | Unset):
        captcha_token (str | Unset):
        captcha_provider (str | Unset):
        challenge_id (str | Unset):
    """

    target_type: RobloxAuthenticationApiModelsSendResetPasswordRequestTargetType | Unset = UNSET
    target: str | Unset = UNSET
    captcha_id: str | Unset = UNSET
    captcha_token: str | Unset = UNSET
    captcha_provider: str | Unset = UNSET
    challenge_id: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        target_type: int | Unset = UNSET
        if not isinstance(self.target_type, Unset):
            target_type = self.target_type.value

        target = self.target

        captcha_id = self.captcha_id

        captcha_token = self.captcha_token

        captcha_provider = self.captcha_provider

        challenge_id = self.challenge_id

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if target_type is not UNSET:
            field_dict["targetType"] = target_type
        if target is not UNSET:
            field_dict["target"] = target
        if captcha_id is not UNSET:
            field_dict["captchaId"] = captcha_id
        if captcha_token is not UNSET:
            field_dict["captchaToken"] = captcha_token
        if captcha_provider is not UNSET:
            field_dict["captchaProvider"] = captcha_provider
        if challenge_id is not UNSET:
            field_dict["challengeId"] = challenge_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _target_type = d.pop("targetType", UNSET)
        target_type: RobloxAuthenticationApiModelsSendResetPasswordRequestTargetType | Unset
        if isinstance(_target_type, Unset):
            target_type = UNSET
        else:
            target_type = RobloxAuthenticationApiModelsSendResetPasswordRequestTargetType(_target_type)

        target = d.pop("target", UNSET)

        captcha_id = d.pop("captchaId", UNSET)

        captcha_token = d.pop("captchaToken", UNSET)

        captcha_provider = d.pop("captchaProvider", UNSET)

        challenge_id = d.pop("challengeId", UNSET)

        roblox_authentication_api_models_send_reset_password_request = cls(
            target_type=target_type,
            target=target,
            captcha_id=captcha_id,
            captcha_token=captcha_token,
            captcha_provider=captcha_provider,
            challenge_id=challenge_id,
        )

        return roblox_authentication_api_models_send_reset_password_request
