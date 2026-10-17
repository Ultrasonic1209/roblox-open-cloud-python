from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxAccountInformationApiModelsGenderRequest")


@_attrs_define
class RobloxAccountInformationApiModelsGenderRequest:
    """The gender request

    Attributes:
        gender (str | Unset): The gender
    """

    gender: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        gender = self.gender

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if gender is not UNSET:
            field_dict["gender"] = gender

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        gender = d.pop("gender", UNSET)

        roblox_account_information_api_models_gender_request = cls(
            gender=gender,
        )

        return roblox_account_information_api_models_gender_request
