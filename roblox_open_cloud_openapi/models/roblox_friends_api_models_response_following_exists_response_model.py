from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_friends_api_models_response_following_exists_response import (
        RobloxFriendsApiModelsResponseFollowingExistsResponse,
    )


T = TypeVar("T", bound="RobloxFriendsApiModelsResponseFollowingExistsResponseModel")


@_attrs_define
class RobloxFriendsApiModelsResponseFollowingExistsResponseModel:
    """Response model for FollowingExists endpoint.

    Attributes:
        followings (list[RobloxFriendsApiModelsResponseFollowingExistsResponse] | Unset): A list of userIds and whether
            or not the given user is following them.
    """

    followings: list[RobloxFriendsApiModelsResponseFollowingExistsResponse] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        followings: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.followings, Unset):
            followings = []
            for followings_item_data in self.followings:
                followings_item = followings_item_data.to_dict()
                followings.append(followings_item)

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if followings is not UNSET:
            field_dict["followings"] = followings

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_friends_api_models_response_following_exists_response import (
            RobloxFriendsApiModelsResponseFollowingExistsResponse,
        )

        d = dict(src_dict)
        _followings = d.pop("followings", UNSET)
        followings: list[RobloxFriendsApiModelsResponseFollowingExistsResponse] | Unset = UNSET
        if _followings is not UNSET:
            followings = []
            for followings_item_data in _followings:
                followings_item = RobloxFriendsApiModelsResponseFollowingExistsResponse.from_dict(followings_item_data)

                followings.append(followings_item)

        roblox_friends_api_models_response_following_exists_response_model = cls(
            followings=followings,
        )

        return roblox_friends_api_models_response_following_exists_response_model
