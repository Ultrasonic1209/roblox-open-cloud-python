from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxFollowingsApiModelsUserFollowingUniverseStatusResponse")


@_attrs_define
class RobloxFollowingsApiModelsUserFollowingUniverseStatusResponse:
    """Model for a user following a universe  state controller responses

    Attributes:
        universe_id (int | Unset): The id of the universe.
        user_id (int | Unset): The id of the user.
        can_follow (bool | Unset): If the user can follow the universe.
        is_following (bool | Unset): If the user is currently following the universe.
        following_count_by_type (int | Unset): The number of followings between this user and a universe.
        following_limit_by_type (int | Unset): The limit to the number of followings between a user and a universe for a
            specific user.
    """

    universe_id: int | Unset = UNSET
    user_id: int | Unset = UNSET
    can_follow: bool | Unset = UNSET
    is_following: bool | Unset = UNSET
    following_count_by_type: int | Unset = UNSET
    following_limit_by_type: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        universe_id = self.universe_id

        user_id = self.user_id

        can_follow = self.can_follow

        is_following = self.is_following

        following_count_by_type = self.following_count_by_type

        following_limit_by_type = self.following_limit_by_type

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if universe_id is not UNSET:
            field_dict["UniverseId"] = universe_id
        if user_id is not UNSET:
            field_dict["UserId"] = user_id
        if can_follow is not UNSET:
            field_dict["CanFollow"] = can_follow
        if is_following is not UNSET:
            field_dict["IsFollowing"] = is_following
        if following_count_by_type is not UNSET:
            field_dict["FollowingCountByType"] = following_count_by_type
        if following_limit_by_type is not UNSET:
            field_dict["FollowingLimitByType"] = following_limit_by_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        universe_id = d.pop("UniverseId", UNSET)

        user_id = d.pop("UserId", UNSET)

        can_follow = d.pop("CanFollow", UNSET)

        is_following = d.pop("IsFollowing", UNSET)

        following_count_by_type = d.pop("FollowingCountByType", UNSET)

        following_limit_by_type = d.pop("FollowingLimitByType", UNSET)

        roblox_followings_api_models_user_following_universe_status_response = cls(
            universe_id=universe_id,
            user_id=user_id,
            can_follow=can_follow,
            is_following=is_following,
            following_count_by_type=following_count_by_type,
            following_limit_by_type=following_limit_by_type,
        )

        return roblox_followings_api_models_user_following_universe_status_response
