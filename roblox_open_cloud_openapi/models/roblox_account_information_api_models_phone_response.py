from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxAccountInformationApiModelsPhoneResponse")


@_attrs_define
class RobloxAccountInformationApiModelsPhoneResponse:
    """The phone response

    Attributes:
        country_code (str | Unset): The country Code
        prefix (str | Unset): The Phone Prefix
        phone (str | Unset): The Phone number
        is_verified (bool | Unset): Is the phone verified
        verification_code_length (int | Unset): Verification Code Length
        can_bypass_password_for_phone_update (bool | Unset): Whether user needs to provide password to update their
            phone numbers
    """

    country_code: str | Unset = UNSET
    prefix: str | Unset = UNSET
    phone: str | Unset = UNSET
    is_verified: bool | Unset = UNSET
    verification_code_length: int | Unset = UNSET
    can_bypass_password_for_phone_update: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        country_code = self.country_code

        prefix = self.prefix

        phone = self.phone

        is_verified = self.is_verified

        verification_code_length = self.verification_code_length

        can_bypass_password_for_phone_update = self.can_bypass_password_for_phone_update

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if country_code is not UNSET:
            field_dict["countryCode"] = country_code
        if prefix is not UNSET:
            field_dict["prefix"] = prefix
        if phone is not UNSET:
            field_dict["phone"] = phone
        if is_verified is not UNSET:
            field_dict["isVerified"] = is_verified
        if verification_code_length is not UNSET:
            field_dict["verificationCodeLength"] = verification_code_length
        if can_bypass_password_for_phone_update is not UNSET:
            field_dict["canBypassPasswordForPhoneUpdate"] = can_bypass_password_for_phone_update

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        country_code = d.pop("countryCode", UNSET)

        prefix = d.pop("prefix", UNSET)

        phone = d.pop("phone", UNSET)

        is_verified = d.pop("isVerified", UNSET)

        verification_code_length = d.pop("verificationCodeLength", UNSET)

        can_bypass_password_for_phone_update = d.pop("canBypassPasswordForPhoneUpdate", UNSET)

        roblox_account_information_api_models_phone_response = cls(
            country_code=country_code,
            prefix=prefix,
            phone=phone,
            is_verified=is_verified,
            verification_code_length=verification_code_length,
            can_bypass_password_for_phone_update=can_bypass_password_for_phone_update,
        )

        return roblox_account_information_api_models_phone_response
