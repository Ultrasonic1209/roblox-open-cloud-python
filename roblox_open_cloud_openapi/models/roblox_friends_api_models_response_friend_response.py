from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxFriendsApiModelsResponseFriendResponse")


@_attrs_define
class RobloxFriendsApiModelsResponseFriendResponse:
    """A response model representing friend information

    Attributes:
        id (int | Unset): The friend's userId
        has_verified_badge (bool | Unset): The friend's verified badge status.
    """

    id: int | Unset = UNSET
    has_verified_badge: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        has_verified_badge = self.has_verified_badge

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if has_verified_badge is not UNSET:
            field_dict["hasVerifiedBadge"] = has_verified_badge

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        id = d.pop("id", UNSET)

        has_verified_badge = d.pop("hasVerifiedBadge", UNSET)

        roblox_friends_api_models_response_friend_response = cls(
            id=id,
            has_verified_badge=has_verified_badge,
        )

        return roblox_friends_api_models_response_friend_response
