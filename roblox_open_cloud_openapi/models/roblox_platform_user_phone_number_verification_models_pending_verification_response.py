from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxPlatformUserPhoneNumberVerificationModelsPendingVerificationResponse")


@_attrs_define
class RobloxPlatformUserPhoneNumberVerificationModelsPendingVerificationResponse:
    """
    Attributes:
        verification_channel (str | Unset):
        data (str | Unset):
    """

    verification_channel: str | Unset = UNSET
    data: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        verification_channel = self.verification_channel

        data = self.data

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if verification_channel is not UNSET:
            field_dict["verificationChannel"] = verification_channel
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        verification_channel = d.pop("verificationChannel", UNSET)

        data = d.pop("data", UNSET)

        roblox_platform_user_phone_number_verification_models_pending_verification_response = cls(
            verification_channel=verification_channel,
            data=data,
        )

        return roblox_platform_user_phone_number_verification_models_pending_verification_response
