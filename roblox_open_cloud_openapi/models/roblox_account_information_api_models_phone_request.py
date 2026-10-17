from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxAccountInformationApiModelsPhoneRequest")


@_attrs_define
class RobloxAccountInformationApiModelsPhoneRequest:
    """The phone request

    Attributes:
        country_code (str | Unset): The country Code
        prefix (str | Unset): The Phone Prefix
        phone (str | Unset): The Phone number
        password (str | Unset): Password
        verification_channel (str | Unset): Verification Channel
    """

    country_code: str | Unset = UNSET
    prefix: str | Unset = UNSET
    phone: str | Unset = UNSET
    password: str | Unset = UNSET
    verification_channel: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        country_code = self.country_code

        prefix = self.prefix

        phone = self.phone

        password = self.password

        verification_channel = self.verification_channel

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if country_code is not UNSET:
            field_dict["countryCode"] = country_code
        if prefix is not UNSET:
            field_dict["prefix"] = prefix
        if phone is not UNSET:
            field_dict["phone"] = phone
        if password is not UNSET:
            field_dict["password"] = password
        if verification_channel is not UNSET:
            field_dict["verificationChannel"] = verification_channel

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        country_code = d.pop("countryCode", UNSET)

        prefix = d.pop("prefix", UNSET)

        phone = d.pop("phone", UNSET)

        password = d.pop("password", UNSET)

        verification_channel = d.pop("verificationChannel", UNSET)

        roblox_account_information_api_models_phone_request = cls(
            country_code=country_code,
            prefix=prefix,
            phone=phone,
            password=password,
            verification_channel=verification_channel,
        )

        return roblox_account_information_api_models_phone_request
