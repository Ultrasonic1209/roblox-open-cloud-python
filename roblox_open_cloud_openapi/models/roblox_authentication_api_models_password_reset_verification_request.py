from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.roblox_authentication_api_models_password_reset_verification_request_target_type import (
    RobloxAuthenticationApiModelsPasswordResetVerificationRequestTargetType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxAuthenticationApiModelsPasswordResetVerificationRequest")


@_attrs_define
class RobloxAuthenticationApiModelsPasswordResetVerificationRequest:
    """
    Attributes:
        target_type (RobloxAuthenticationApiModelsPasswordResetVerificationRequestTargetType | Unset):  ['Email' = 0,
            'PhoneNumber' = 1, 'RecoverySessionID' = 2]
        nonce (str | Unset):
        code (str | Unset):
    """

    target_type: RobloxAuthenticationApiModelsPasswordResetVerificationRequestTargetType | Unset = UNSET
    nonce: str | Unset = UNSET
    code: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        target_type: int | Unset = UNSET
        if not isinstance(self.target_type, Unset):
            target_type = self.target_type.value

        nonce = self.nonce

        code = self.code

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if target_type is not UNSET:
            field_dict["targetType"] = target_type
        if nonce is not UNSET:
            field_dict["nonce"] = nonce
        if code is not UNSET:
            field_dict["code"] = code

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _target_type = d.pop("targetType", UNSET)
        target_type: RobloxAuthenticationApiModelsPasswordResetVerificationRequestTargetType | Unset
        if isinstance(_target_type, Unset):
            target_type = UNSET
        else:
            target_type = RobloxAuthenticationApiModelsPasswordResetVerificationRequestTargetType(_target_type)

        nonce = d.pop("nonce", UNSET)

        code = d.pop("code", UNSET)

        roblox_authentication_api_models_password_reset_verification_request = cls(
            target_type=target_type,
            nonce=nonce,
            code=code,
        )

        return roblox_authentication_api_models_password_reset_verification_request
