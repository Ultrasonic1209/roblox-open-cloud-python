from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxFriendsApiMultigetAreFriendsResponse")


@_attrs_define
class RobloxFriendsApiMultigetAreFriendsResponse:
    """Response model for MultigetAreFriendsResponse

    Attributes:
        friends_id (list[int] | Unset): friends id list
    """

    friends_id: list[int] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        friends_id: list[int] | Unset = UNSET
        if not isinstance(self.friends_id, Unset):
            friends_id = self.friends_id

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if friends_id is not UNSET:
            field_dict["friendsId"] = friends_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        friends_id = cast(list[int], d.pop("friendsId", UNSET))

        roblox_friends_api_multiget_are_friends_response = cls(
            friends_id=friends_id,
        )

        return roblox_friends_api_multiget_are_friends_response
