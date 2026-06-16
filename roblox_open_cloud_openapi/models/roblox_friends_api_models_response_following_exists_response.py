from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxFriendsApiModelsResponseFollowingExistsResponse")


@_attrs_define
class RobloxFriendsApiModelsResponseFollowingExistsResponse:
    """Response contained in list for FollowingExists endpoint. Corresponds to a single userId.

    Attributes:
        is_following (bool | Unset): Whether or not a user is following userId in FriendsController.FollowingExists
        is_followed (bool | Unset): Whether or not a user is followed by userId in FriendsController.FollowingExists
        user_id (int | Unset): The userId being potentially followed
    """

    is_following: bool | Unset = UNSET
    is_followed: bool | Unset = UNSET
    user_id: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        is_following = self.is_following

        is_followed = self.is_followed

        user_id = self.user_id

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if is_following is not UNSET:
            field_dict["isFollowing"] = is_following
        if is_followed is not UNSET:
            field_dict["isFollowed"] = is_followed
        if user_id is not UNSET:
            field_dict["userId"] = user_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        is_following = d.pop("isFollowing", UNSET)

        is_followed = d.pop("isFollowed", UNSET)

        user_id = d.pop("userId", UNSET)

        roblox_friends_api_models_response_following_exists_response = cls(
            is_following=is_following,
            is_followed=is_followed,
            user_id=user_id,
        )

        return roblox_friends_api_models_response_following_exists_response
