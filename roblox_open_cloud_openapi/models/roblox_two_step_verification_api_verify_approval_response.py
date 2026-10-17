from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxTwoStepVerificationApiVerifyApprovalResponse")


@_attrs_define
class RobloxTwoStepVerificationApiVerifyApprovalResponse:
    """Result for a successful Cross Device approval verification.

    Attributes:
        verification_token (str | Unset): The verification token.
    """

    verification_token: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        verification_token = self.verification_token

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if verification_token is not UNSET:
            field_dict["verificationToken"] = verification_token

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        verification_token = d.pop("verificationToken", UNSET)

        roblox_two_step_verification_api_verify_approval_response = cls(
            verification_token=verification_token,
        )

        return roblox_two_step_verification_api_verify_approval_response
