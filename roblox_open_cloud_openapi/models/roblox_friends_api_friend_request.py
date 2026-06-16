from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.roblox_friends_api_friend_request_origin_source_type import RobloxFriendsApiFriendRequestOriginSourceType
from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxFriendsApiFriendRequest")


@_attrs_define
class RobloxFriendsApiFriendRequest:
    """A response model representing a friend request.

    Attributes:
        sent_at (datetime.datetime | Unset): When the friend request was sent.
        sender_id (int | Unset): The sender user Id.
        source_universe_id (int | Unset): The source universe Id which the request was sent in.
        origin_source_type (RobloxFriendsApiFriendRequestOriginSourceType | Unset): The origin source type associated
            with the friend request. ['Unknown' = 0, 'PlayerSearch' = 1, 'QrCode' = 2, 'InGame' = 3, 'UserProfile' = 4,
            'QqContactImporter' = 5, 'WeChatContactImporter' = 6, 'ProfileShare' = 7, 'PhoneContactImporter' = 8,
            'FriendRecommendations' = 9, 'UserCommunities' = 10]
        contact_name (str | Unset): The contact name associated with the friend request.
        sender_nickname (str | Unset): The nickname associated with the friend request.
    """

    sent_at: datetime.datetime | Unset = UNSET
    sender_id: int | Unset = UNSET
    source_universe_id: int | Unset = UNSET
    origin_source_type: RobloxFriendsApiFriendRequestOriginSourceType | Unset = UNSET
    contact_name: str | Unset = UNSET
    sender_nickname: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        sent_at: str | Unset = UNSET
        if not isinstance(self.sent_at, Unset):
            sent_at = self.sent_at.isoformat()

        sender_id = self.sender_id

        source_universe_id = self.source_universe_id

        origin_source_type: int | Unset = UNSET
        if not isinstance(self.origin_source_type, Unset):
            origin_source_type = self.origin_source_type.value

        contact_name = self.contact_name

        sender_nickname = self.sender_nickname

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if sent_at is not UNSET:
            field_dict["sentAt"] = sent_at
        if sender_id is not UNSET:
            field_dict["senderId"] = sender_id
        if source_universe_id is not UNSET:
            field_dict["sourceUniverseId"] = source_universe_id
        if origin_source_type is not UNSET:
            field_dict["originSourceType"] = origin_source_type
        if contact_name is not UNSET:
            field_dict["contactName"] = contact_name
        if sender_nickname is not UNSET:
            field_dict["senderNickname"] = sender_nickname

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _sent_at = d.pop("sentAt", UNSET)
        sent_at: datetime.datetime | Unset
        if isinstance(_sent_at, Unset):
            sent_at = UNSET
        else:
            sent_at = datetime.datetime.fromisoformat(_sent_at)

        sender_id = d.pop("senderId", UNSET)

        source_universe_id = d.pop("sourceUniverseId", UNSET)

        _origin_source_type = d.pop("originSourceType", UNSET)
        origin_source_type: RobloxFriendsApiFriendRequestOriginSourceType | Unset
        if isinstance(_origin_source_type, Unset):
            origin_source_type = UNSET
        else:
            origin_source_type = RobloxFriendsApiFriendRequestOriginSourceType(_origin_source_type)

        contact_name = d.pop("contactName", UNSET)

        sender_nickname = d.pop("senderNickname", UNSET)

        roblox_friends_api_friend_request = cls(
            sent_at=sent_at,
            sender_id=sender_id,
            source_universe_id=source_universe_id,
            origin_source_type=origin_source_type,
            contact_name=contact_name,
            sender_nickname=sender_nickname,
        )

        return roblox_friends_api_friend_request
