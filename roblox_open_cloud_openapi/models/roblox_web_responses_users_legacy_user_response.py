from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxWebResponsesUsersLegacyUserResponse")


@_attrs_define
class RobloxWebResponsesUsersLegacyUserResponse:
    """
    Attributes:
        user_id (int | Unset):
        username (str | Unset):
        display_name (str | Unset):
    """

    user_id: int | Unset = UNSET
    username: str | Unset = UNSET
    display_name: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        user_id = self.user_id

        username = self.username

        display_name = self.display_name

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if user_id is not UNSET:
            field_dict["userId"] = user_id
        if username is not UNSET:
            field_dict["username"] = username
        if display_name is not UNSET:
            field_dict["displayName"] = display_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        user_id = d.pop("userId", UNSET)

        username = d.pop("username", UNSET)

        display_name = d.pop("displayName", UNSET)

        roblox_web_responses_users_legacy_user_response = cls(
            user_id=user_id,
            username=username,
            display_name=display_name,
        )

        return roblox_web_responses_users_legacy_user_response
