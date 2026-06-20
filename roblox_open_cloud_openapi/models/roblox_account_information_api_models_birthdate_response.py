from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxAccountInformationApiModelsBirthdateResponse")


@_attrs_define
class RobloxAccountInformationApiModelsBirthdateResponse:
    """The birthdate response

    Attributes:
        birth_month (int | Unset): The birth month
        birth_day (int | Unset): The birth day
        birth_year (int | Unset): The birth year
    """

    birth_month: int | Unset = UNSET
    birth_day: int | Unset = UNSET
    birth_year: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        birth_month = self.birth_month

        birth_day = self.birth_day

        birth_year = self.birth_year

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if birth_month is not UNSET:
            field_dict["birthMonth"] = birth_month
        if birth_day is not UNSET:
            field_dict["birthDay"] = birth_day
        if birth_year is not UNSET:
            field_dict["birthYear"] = birth_year

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        birth_month = d.pop("birthMonth", UNSET)

        birth_day = d.pop("birthDay", UNSET)

        birth_year = d.pop("birthYear", UNSET)

        roblox_account_information_api_models_birthdate_response = cls(
            birth_month=birth_month,
            birth_day=birth_day,
            birth_year=birth_year,
        )

        return roblox_account_information_api_models_birthdate_response
