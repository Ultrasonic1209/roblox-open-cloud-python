from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxFriendsApiModelsResponseNewFriendRequestsCountResponse")


@_attrs_define
class RobloxFriendsApiModelsResponseNewFriendRequestsCountResponse:
    """The friendship status response model.

    Attributes:
        count (int | Unset): Count of new friend requests.
    """

    count: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        count = self.count

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if count is not UNSET:
            field_dict["count"] = count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        count = d.pop("count", UNSET)

        roblox_friends_api_models_response_new_friend_requests_count_response = cls(
            count=count,
        )

        return roblox_friends_api_models_response_new_friend_requests_count_response
