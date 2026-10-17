from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.roblox_groups_api_group_notification_preference_data_type import (
    RobloxGroupsApiGroupNotificationPreferenceDataType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxGroupsApiGroupNotificationPreferenceData")


@_attrs_define
class RobloxGroupsApiGroupNotificationPreferenceData:
    """
    Attributes:
        type_ (RobloxGroupsApiGroupNotificationPreferenceDataType | Unset):  ['AnnouncementCreatedNotification' = 0,
            'ForumPostCreatedNotification' = 1, 'ForumCommentCreatedNotification' = 2,
            'ForumCommentReplyCreatedNotification' = 3, 'ForumSubscriberNotification' = 4]
        enabled (bool | Unset):
        name (str | Unset):
        description (str | Unset):
    """

    type_: RobloxGroupsApiGroupNotificationPreferenceDataType | Unset = UNSET
    enabled: bool | Unset = UNSET
    name: str | Unset = UNSET
    description: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        type_: int | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        enabled = self.enabled

        name = self.name

        description = self.description

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _type_ = d.pop("type", UNSET)
        type_: RobloxGroupsApiGroupNotificationPreferenceDataType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = RobloxGroupsApiGroupNotificationPreferenceDataType(_type_)

        enabled = d.pop("enabled", UNSET)

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        roblox_groups_api_group_notification_preference_data = cls(
            type_=type_,
            enabled=enabled,
            name=name,
            description=description,
        )

        return roblox_groups_api_group_notification_preference_data
