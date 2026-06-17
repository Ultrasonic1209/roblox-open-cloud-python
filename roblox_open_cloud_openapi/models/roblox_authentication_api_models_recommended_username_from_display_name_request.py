from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxAuthenticationApiModelsRecommendedUsernameFromDisplayNameRequest")


@_attrs_define
class RobloxAuthenticationApiModelsRecommendedUsernameFromDisplayNameRequest:
    """
    Attributes:
        display_name (str | Unset):
        birthday (datetime.datetime | Unset):
    """

    display_name: str | Unset = UNSET
    birthday: datetime.datetime | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        display_name = self.display_name

        birthday: str | Unset = UNSET
        if not isinstance(self.birthday, Unset):
            birthday = self.birthday.isoformat()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if birthday is not UNSET:
            field_dict["birthday"] = birthday

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        display_name = d.pop("displayName", UNSET)

        _birthday = d.pop("birthday", UNSET)
        birthday: datetime.datetime | Unset
        if isinstance(_birthday, Unset):
            birthday = UNSET
        else:
            birthday = datetime.datetime.fromisoformat(_birthday)

        roblox_authentication_api_models_recommended_username_from_display_name_request = cls(
            display_name=display_name,
            birthday=birthday,
        )

        return roblox_authentication_api_models_recommended_username_from_display_name_request
