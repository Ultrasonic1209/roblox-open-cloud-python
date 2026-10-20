from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.roblox_authentication_api_models_username_validation_response_code import (
    RobloxAuthenticationApiModelsUsernameValidationResponseCode,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxAuthenticationApiModelsUsernameValidationResponse")


@_attrs_define
class RobloxAuthenticationApiModelsUsernameValidationResponse:
    """
    Attributes:
        code (RobloxAuthenticationApiModelsUsernameValidationResponseCode | Unset):  ['ValidUsername' = 0,
            'AlreadyInUseError' = 1, 'ModerationError' = 2, 'InvalidLengthError' = 3, 'StartsOrEndsWithUnderscoreError' = 4,
            'TooManyUnderscoresError' = 5, 'ContainsSpacesError' = 6, 'InvalidCharactersError' = 7, 'ContainsPiiError' = 10,
            'ContainsReservedUsernameError' = 12]
        message (str | Unset):
    """

    code: RobloxAuthenticationApiModelsUsernameValidationResponseCode | Unset = UNSET
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
        d = dict(src_dict)
        _code = d.pop("code", UNSET)
        code: RobloxAuthenticationApiModelsUsernameValidationResponseCode | Unset
        if isinstance(_code, Unset):
            code = UNSET
        else:
            code = RobloxAuthenticationApiModelsUsernameValidationResponseCode(_code)

        message = d.pop("message", UNSET)

        roblox_authentication_api_models_username_validation_response = cls(
            code=code,
            message=message,
        )

        return roblox_authentication_api_models_username_validation_response
