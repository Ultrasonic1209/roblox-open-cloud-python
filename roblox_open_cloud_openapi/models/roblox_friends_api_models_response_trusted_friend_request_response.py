from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxFriendsApiModelsResponseTrustedFriendRequestResponse")


@_attrs_define
class RobloxFriendsApiModelsResponseTrustedFriendRequestResponse:
    """A response model representing a friend request.

    Attributes:
        sent_at (datetime.datetime | Unset): When the TF request was sent.
        sender_id (int | Unset): The sender user Id.
        is_unseen (bool | Unset): Whether this trusted friend request is unseen by the recipient.
    """

    sent_at: datetime.datetime | Unset = UNSET
    sender_id: int | Unset = UNSET
    is_unseen: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        sent_at: str | Unset = UNSET
        if not isinstance(self.sent_at, Unset):
            sent_at = self.sent_at.isoformat()

        sender_id = self.sender_id

        is_unseen = self.is_unseen

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if sent_at is not UNSET:
            field_dict["sentAt"] = sent_at
        if sender_id is not UNSET:
            field_dict["senderId"] = sender_id
        if is_unseen is not UNSET:
            field_dict["isUnseen"] = is_unseen

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

        is_unseen = d.pop("isUnseen", UNSET)

        roblox_friends_api_models_response_trusted_friend_request_response = cls(
            sent_at=sent_at,
            sender_id=sender_id,
            is_unseen=is_unseen,
        )

        return roblox_friends_api_models_response_trusted_friend_request_response
