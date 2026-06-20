from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..models.roblox_api_notifications_models_notification_stream_entries_model_notification_source_type import (
    RobloxApiNotificationsModelsNotificationStreamEntriesModelNotificationSourceType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxApiNotificationsModelsNotificationStreamEntriesModel")


@_attrs_define
class RobloxApiNotificationsModelsNotificationStreamEntriesModel:
    """
    Attributes:
        id (UUID | Unset): Id of the notification stream entry
        notification_source_type (RobloxApiNotificationsModelsNotificationStreamEntriesModelNotificationSourceType |
            Unset): Type of the notification source ['Test' = 0, 'FriendRequestReceived' = 1, 'FriendRequestAccepted' = 2,
            'PartyInviteReceived' = 3, 'PartyMemberJoined' = 4, 'ChatNewMessage' = 5, 'PrivateMessageReceived' = 6,
            'UserAddedToPrivateServerWhiteList' = 7, 'ConversationUniverseChanged' = 8, 'TeamCreateInvite' = 9, 'GameUpdate'
            = 10, 'DeveloperMetricsAvailable' = 11, 'GroupJoinRequestAccepted' = 12, 'Sendr' = 13, 'ExperienceInvitation' =
            14]
        event_date (datetime.datetime | Unset): Datetime when the notification stream entry event had occured
        timestamp (str | Unset): Relative timestamp for sendr notification stream entry
        is_interacted (bool | Unset): Has the user interacted with the notification stream entry
        metadata_collection (list[Any] | Unset): List of metadata objects showing more details related to the
            notification stream entry
        event_count (int | Unset): Count of events corresponding to the group of notification stream entry
        content (Any | Unset): Content object for sendr notification stream entry
    """

    id: UUID | Unset = UNSET
    notification_source_type: (
        RobloxApiNotificationsModelsNotificationStreamEntriesModelNotificationSourceType | Unset
    ) = UNSET
    event_date: datetime.datetime | Unset = UNSET
    timestamp: str | Unset = UNSET
    is_interacted: bool | Unset = UNSET
    metadata_collection: list[Any] | Unset = UNSET
    event_count: int | Unset = UNSET
    content: Any | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        notification_source_type: str | Unset = UNSET
        if not isinstance(self.notification_source_type, Unset):
            notification_source_type = self.notification_source_type.value

        event_date: str | Unset = UNSET
        if not isinstance(self.event_date, Unset):
            event_date = self.event_date.isoformat()

        timestamp = self.timestamp

        is_interacted = self.is_interacted

        metadata_collection: list[Any] | Unset = UNSET
        if not isinstance(self.metadata_collection, Unset):
            metadata_collection = self.metadata_collection

        event_count = self.event_count

        content = self.content

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if notification_source_type is not UNSET:
            field_dict["notificationSourceType"] = notification_source_type
        if event_date is not UNSET:
            field_dict["eventDate"] = event_date
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp
        if is_interacted is not UNSET:
            field_dict["isInteracted"] = is_interacted
        if metadata_collection is not UNSET:
            field_dict["metadataCollection"] = metadata_collection
        if event_count is not UNSET:
            field_dict["eventCount"] = event_count
        if content is not UNSET:
            field_dict["content"] = content

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = UUID(_id)

        _notification_source_type = d.pop("notificationSourceType", UNSET)
        notification_source_type: (
            RobloxApiNotificationsModelsNotificationStreamEntriesModelNotificationSourceType | Unset
        )
        if isinstance(_notification_source_type, Unset):
            notification_source_type = UNSET
        else:
            notification_source_type = RobloxApiNotificationsModelsNotificationStreamEntriesModelNotificationSourceType(
                _notification_source_type
            )

        _event_date = d.pop("eventDate", UNSET)
        event_date: datetime.datetime | Unset
        if isinstance(_event_date, Unset):
            event_date = UNSET
        else:
            event_date = datetime.datetime.fromisoformat(_event_date)

        timestamp = d.pop("timestamp", UNSET)

        is_interacted = d.pop("isInteracted", UNSET)

        metadata_collection = cast(list[Any], d.pop("metadataCollection", UNSET))

        event_count = d.pop("eventCount", UNSET)

        content = d.pop("content", UNSET)

        roblox_api_notifications_models_notification_stream_entries_model = cls(
            id=id,
            notification_source_type=notification_source_type,
            event_date=event_date,
            timestamp=timestamp,
            is_interacted=is_interacted,
            metadata_collection=metadata_collection,
            event_count=event_count,
            content=content,
        )

        return roblox_api_notifications_models_notification_stream_entries_model
