from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxTwoStepVerificationApiDisableTwoStepVerificationRequest")


@_attrs_define
class RobloxTwoStepVerificationApiDisableTwoStepVerificationRequest:
    """Request information needed to disable two step verification.

    Attributes:
        password (str | Unset): The user's password.
        reauthentication_token (str | Unset): A re-authentication token redeemable for any password check.
    """

    password: str | Unset = UNSET
    reauthentication_token: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        password = self.password

        reauthentication_token = self.reauthentication_token

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if password is not UNSET:
            field_dict["password"] = password
        if reauthentication_token is not UNSET:
            field_dict["reauthenticationToken"] = reauthentication_token

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        password = d.pop("password", UNSET)

        reauthentication_token = d.pop("reauthenticationToken", UNSET)

        roblox_two_step_verification_api_disable_two_step_verification_request = cls(
            password=password,
            reauthentication_token=reauthentication_token,
        )

        return roblox_two_step_verification_api_disable_two_step_verification_request
