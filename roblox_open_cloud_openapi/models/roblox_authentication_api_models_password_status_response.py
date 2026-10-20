from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxAuthenticationApiModelsPasswordStatusResponse")


@_attrs_define
class RobloxAuthenticationApiModelsPasswordStatusResponse:
    """
    Attributes:
        valid (bool | Unset):
    """

    valid: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        valid = self.valid

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if valid is not UNSET:
            field_dict["valid"] = valid

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        valid = d.pop("valid", UNSET)

        roblox_authentication_api_models_password_status_response = cls(
            valid=valid,
        )

        return roblox_authentication_api_models_password_status_response
