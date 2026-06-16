from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="RobloxTwoStepVerificationApiRetryApprovalResponse")


@_attrs_define
class RobloxTwoStepVerificationApiRetryApprovalResponse:
    """Result for a successful Cross Device approval retry, an empty JSON."""

    def to_dict(self) -> dict[str, Any]:

        field_dict: dict[str, Any] = {}

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        roblox_two_step_verification_api_retry_approval_response = cls()

        return roblox_two_step_verification_api_retry_approval_response
