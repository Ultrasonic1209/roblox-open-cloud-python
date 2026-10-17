from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxApiNotificationsModelsUnreadStreamNotificationsModel")


@_attrs_define
class RobloxApiNotificationsModelsUnreadStreamNotificationsModel:
    """
    Attributes:
        unread_notifications (int | Unset): Count of unread notifications in the stream
        status_message (str | Unset): Message for the success response
    """

    unread_notifications: int | Unset = UNSET
    status_message: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        unread_notifications = self.unread_notifications

        status_message = self.status_message

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if unread_notifications is not UNSET:
            field_dict["unreadNotifications"] = unread_notifications
        if status_message is not UNSET:
            field_dict["statusMessage"] = status_message

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        unread_notifications = d.pop("unreadNotifications", UNSET)

        status_message = d.pop("statusMessage", UNSET)

        roblox_api_notifications_models_unread_stream_notifications_model = cls(
            unread_notifications=unread_notifications,
            status_message=status_message,
        )

        return roblox_api_notifications_models_unread_stream_notifications_model
