from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.roblox_groups_api_update_group_notification_preference_request_type import (
    RobloxGroupsApiUpdateGroupNotificationPreferenceRequestType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxGroupsApiUpdateGroupNotificationPreferenceRequest")


@_attrs_define
class RobloxGroupsApiUpdateGroupNotificationPreferenceRequest:
    """A request model for updating a group's notification preference.

    Attributes:
        notifications_enabled (bool | Unset): Whether the user wants to receive notifications from the group.
        type_ (RobloxGroupsApiUpdateGroupNotificationPreferenceRequestType | Unset):  ['AnnouncementCreatedNotification'
            = 0, 'ForumPostCreatedNotification' = 1, 'ForumCommentCreatedNotification' = 2,
            'ForumCommentReplyCreatedNotification' = 3, 'ForumSubscriberNotification' = 4]
    """

    notifications_enabled: bool | Unset = UNSET
    type_: RobloxGroupsApiUpdateGroupNotificationPreferenceRequestType | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        notifications_enabled = self.notifications_enabled

        type_: int | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if notifications_enabled is not UNSET:
            field_dict["notificationsEnabled"] = notifications_enabled
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        notifications_enabled = d.pop("notificationsEnabled", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: RobloxGroupsApiUpdateGroupNotificationPreferenceRequestType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = RobloxGroupsApiUpdateGroupNotificationPreferenceRequestType(_type_)

        roblox_groups_api_update_group_notification_preference_request = cls(
            notifications_enabled=notifications_enabled,
            type_=type_,
        )

        return roblox_groups_api_update_group_notification_preference_request
