from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxUsersApiMultiGetByUserIdRequest")


@_attrs_define
class RobloxUsersApiMultiGetByUserIdRequest:
    """Request model for getting users by ids.

    Attributes:
        user_ids (list[int] | Unset): The user ids.
        exclude_banned_users (bool | Unset): Whether the response should exclude banned users
    """

    user_ids: list[int] | Unset = UNSET
    exclude_banned_users: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        user_ids: list[int] | Unset = UNSET
        if not isinstance(self.user_ids, Unset):
            user_ids = self.user_ids

        exclude_banned_users = self.exclude_banned_users

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if user_ids is not UNSET:
            field_dict["userIds"] = user_ids
        if exclude_banned_users is not UNSET:
            field_dict["excludeBannedUsers"] = exclude_banned_users

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        user_ids = cast(list[int], d.pop("userIds", UNSET))

        exclude_banned_users = d.pop("excludeBannedUsers", UNSET)

        roblox_users_api_multi_get_by_user_id_request = cls(
            user_ids=user_ids,
            exclude_banned_users=exclude_banned_users,
        )

        return roblox_users_api_multi_get_by_user_id_request
