from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxTwoStepVerificationApiRegenerateRecoveryCodesRequest")


@_attrs_define
class RobloxTwoStepVerificationApiRegenerateRecoveryCodesRequest:
    """Request information needed to regenerate recovery codes.

    Attributes:
        password (str | Unset): The user's password.
    """

    password: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        password = self.password

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if password is not UNSET:
            field_dict["password"] = password

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        password = d.pop("password", UNSET)

        roblox_two_step_verification_api_regenerate_recovery_codes_request = cls(
            password=password,
        )

        return roblox_two_step_verification_api_regenerate_recovery_codes_request
