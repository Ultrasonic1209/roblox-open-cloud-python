from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxUsersApiMultiGetByUsernameRequest")


@_attrs_define
class RobloxUsersApiMultiGetByUsernameRequest:
    """Request model for getting users by usernames.

    Attributes:
        usernames (list[str] | Unset): The usernames.
        exclude_banned_users (bool | Unset): Whether the response should exclude banned users
    """

    usernames: list[str] | Unset = UNSET
    exclude_banned_users: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        usernames: list[str] | Unset = UNSET
        if not isinstance(self.usernames, Unset):
            usernames = self.usernames

        exclude_banned_users = self.exclude_banned_users

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if usernames is not UNSET:
            field_dict["usernames"] = usernames
        if exclude_banned_users is not UNSET:
            field_dict["excludeBannedUsers"] = exclude_banned_users

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        usernames = cast(list[str], d.pop("usernames", UNSET))

        exclude_banned_users = d.pop("excludeBannedUsers", UNSET)

        roblox_users_api_multi_get_by_username_request = cls(
            usernames=usernames,
            exclude_banned_users=exclude_banned_users,
        )

        return roblox_users_api_multi_get_by_username_request
