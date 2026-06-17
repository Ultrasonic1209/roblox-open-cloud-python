from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxAuthenticationApiModelsRecommendedUsernameRequest")


@_attrs_define
class RobloxAuthenticationApiModelsRecommendedUsernameRequest:
    """
    Attributes:
        username (str | Unset):
        birthday (datetime.datetime | Unset):
    """

    username: str | Unset = UNSET
    birthday: datetime.datetime | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        username = self.username

        birthday: str | Unset = UNSET
        if not isinstance(self.birthday, Unset):
            birthday = self.birthday.isoformat()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if username is not UNSET:
            field_dict["username"] = username
        if birthday is not UNSET:
            field_dict["birthday"] = birthday

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        username = d.pop("username", UNSET)

        _birthday = d.pop("birthday", UNSET)
        birthday: datetime.datetime | Unset
        if isinstance(_birthday, Unset):
            birthday = UNSET
        else:
            birthday = datetime.datetime.fromisoformat(_birthday)

        roblox_authentication_api_models_recommended_username_request = cls(
            username=username,
            birthday=birthday,
        )

        return roblox_authentication_api_models_recommended_username_request
