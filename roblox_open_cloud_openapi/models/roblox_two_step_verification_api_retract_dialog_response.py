from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="RobloxTwoStepVerificationApiRetractDialogResponse")


@_attrs_define
class RobloxTwoStepVerificationApiRetractDialogResponse:
    """Result for a successful attempt to retract a Cross Device state from ACTIVE to PENDING."""

    def to_dict(self) -> dict[str, Any]:

        field_dict: dict[str, Any] = {}

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        roblox_two_step_verification_api_retract_dialog_response = cls()

        return roblox_two_step_verification_api_retract_dialog_response
