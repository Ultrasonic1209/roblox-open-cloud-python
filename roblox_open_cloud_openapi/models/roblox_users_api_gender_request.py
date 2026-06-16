from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.roblox_users_api_gender_request_gender import RobloxUsersApiGenderRequestGender
from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxUsersApiGenderRequest")


@_attrs_define
class RobloxUsersApiGenderRequest:
    """The gender request

    Attributes:
        gender (RobloxUsersApiGenderRequestGender | Unset): The gender ['Unknown' = 1, 'Male' = 2, 'Female' = 3]
    """

    gender: RobloxUsersApiGenderRequestGender | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        gender: int | Unset = UNSET
        if not isinstance(self.gender, Unset):
            gender = self.gender.value

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if gender is not UNSET:
            field_dict["gender"] = gender

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _gender = d.pop("gender", UNSET)
        gender: RobloxUsersApiGenderRequestGender | Unset
        if isinstance(_gender, Unset):
            gender = UNSET
        else:
            gender = RobloxUsersApiGenderRequestGender(_gender)

        roblox_users_api_gender_request = cls(
            gender=gender,
        )

        return roblox_users_api_gender_request
