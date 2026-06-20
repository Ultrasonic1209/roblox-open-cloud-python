from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.roblox_authentication_api_models_password_validation_response_code import (
    RobloxAuthenticationApiModelsPasswordValidationResponseCode,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxAuthenticationApiModelsPasswordValidationResponse")


@_attrs_define
class RobloxAuthenticationApiModelsPasswordValidationResponse:
    """
    Attributes:
        code (RobloxAuthenticationApiModelsPasswordValidationResponseCode | Unset):  ['ValidPassword' = 0,
            'WeakPasswordError' = 1, 'PasswordLengthError' = 2, 'PasswordSameAsUsernameError' = 3, 'ForbiddenPasswordError'
            = 4, 'DumbStringsError' = 5]
        message (str | Unset):
    """

    code: RobloxAuthenticationApiModelsPasswordValidationResponseCode | Unset = UNSET
    message: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        code: int | Unset = UNSET
        if not isinstance(self.code, Unset):
            code = self.code.value

        message = self.message

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if code is not UNSET:
            field_dict["code"] = code
        if message is not UNSET:
            field_dict["message"] = message

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        _code = d.pop("code", UNSET)
        code: RobloxAuthenticationApiModelsPasswordValidationResponseCode | Unset
        if isinstance(_code, Unset):
            code = UNSET
        else:
            code = RobloxAuthenticationApiModelsPasswordValidationResponseCode(_code)

        message = d.pop("message", UNSET)

        roblox_authentication_api_models_password_validation_response = cls(
            code=code,
            message=message,
        )

        return roblox_authentication_api_models_password_validation_response
