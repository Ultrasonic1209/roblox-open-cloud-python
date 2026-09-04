from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxAuthenticationApiModelsEmailValidationResponse")


@_attrs_define
class RobloxAuthenticationApiModelsEmailValidationResponse:
    """
    Attributes:
        is_email_valid (bool | Unset):
    """

    is_email_valid: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        is_email_valid = self.is_email_valid

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if is_email_valid is not UNSET:
            field_dict["isEmailValid"] = is_email_valid

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        is_email_valid = d.pop("isEmailValid", UNSET)

        roblox_authentication_api_models_email_validation_response = cls(
            is_email_valid=is_email_valid,
        )

        return roblox_authentication_api_models_email_validation_response
