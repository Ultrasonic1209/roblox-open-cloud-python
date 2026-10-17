from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.roblox_friends_api_friend_status_response_status import RobloxFriendsApiFriendStatusResponseStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxFriendsApiFriendStatusResponse")


@_attrs_define
class RobloxFriendsApiFriendStatusResponse:
    """The friendship status response model.

    Attributes:
        id (int | Unset): The user Id of the friend.
        status (RobloxFriendsApiFriendStatusResponseStatus | Unset): The friendship status. ['NotFriends' = 0, 'Friends'
            = 1, 'RequestSent' = 2, 'RequestReceived' = 3]
    """

    id: int | Unset = UNSET
    status: RobloxFriendsApiFriendStatusResponseStatus | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        status: int | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        _status = d.pop("status", UNSET)
        status: RobloxFriendsApiFriendStatusResponseStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = RobloxFriendsApiFriendStatusResponseStatus(_status)

        roblox_friends_api_friend_status_response = cls(
            id=id,
            status=status,
        )

        return roblox_friends_api_friend_status_response
