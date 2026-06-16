from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxTwoStepVerificationApiRegenerateRecoveryCodesResponse")


@_attrs_define
class RobloxTwoStepVerificationApiRegenerateRecoveryCodesResponse:
    """The response for regenerating recovery codes.

    Attributes:
        recovery_codes (list[str] | Unset): The collection of generated recovery codes.
    """

    recovery_codes: list[str] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        recovery_codes: list[str] | Unset = UNSET
        if not isinstance(self.recovery_codes, Unset):
            recovery_codes = self.recovery_codes

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if recovery_codes is not UNSET:
            field_dict["recoveryCodes"] = recovery_codes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        recovery_codes = cast(list[str], d.pop("recoveryCodes", UNSET))

        roblox_two_step_verification_api_regenerate_recovery_codes_response = cls(
            recovery_codes=recovery_codes,
        )

        return roblox_two_step_verification_api_regenerate_recovery_codes_response
