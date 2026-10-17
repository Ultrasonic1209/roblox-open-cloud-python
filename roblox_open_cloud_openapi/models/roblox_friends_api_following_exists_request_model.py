from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxFriendsApiFollowingExistsRequestModel")


@_attrs_define
class RobloxFriendsApiFollowingExistsRequestModel:
    """Request model for FollowingExists endpoint

    Attributes:
        target_user_ids (list[int] | Unset): The userIds which the user may or may not be following.
    """

    target_user_ids: list[int] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        target_user_ids: list[int] | Unset = UNSET
        if not isinstance(self.target_user_ids, Unset):
            target_user_ids = self.target_user_ids

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if target_user_ids is not UNSET:
            field_dict["targetUserIds"] = target_user_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        target_user_ids = cast(list[int], d.pop("targetUserIds", UNSET))

        roblox_friends_api_following_exists_request_model = cls(
            target_user_ids=target_user_ids,
        )

        return roblox_friends_api_following_exists_request_model
