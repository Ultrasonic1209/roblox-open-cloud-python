from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.user_notification_payload import UserNotificationPayload
    from ..models.user_notification_source import UserNotificationSource


T = TypeVar("T", bound="UserNotification")


@_attrs_define
class UserNotification:
    """Represents a notification sent to a user.

    Attributes:
        path (str | Unset): The resource path of the user notification.

            Format: `users/{user_id}/notifications/{user_notification_id}` Example:
            users/123/notifications/01234567-ABCD-1234-ABCD-0123456789AB.
        id (str | Unset): A unique UUID of the user notification. Example: a6746f2e-2cc6-11ee-be56-0242ac120002.
        source (UserNotificationSource | Unset): The source of the notification.
        payload (UserNotificationPayload | Unset): Details about the notification.
    """

    path: str | Unset = UNSET
    id: str | Unset = UNSET
    source: UserNotificationSource | Unset = UNSET
    payload: UserNotificationPayload | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        path = self.path

        id = self.id

        source: dict[str, Any] | Unset = UNSET
        if not isinstance(self.source, Unset):
            source = self.source.to_dict()

        payload: dict[str, Any] | Unset = UNSET
        if not isinstance(self.payload, Unset):
            payload = self.payload.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if path is not UNSET:
            field_dict["path"] = path
        if id is not UNSET:
            field_dict["id"] = id
        if source is not UNSET:
            field_dict["source"] = source
        if payload is not UNSET:
            field_dict["payload"] = payload

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.user_notification_payload import UserNotificationPayload
        from ..models.user_notification_source import UserNotificationSource

        d = dict(src_dict)
        path = d.pop("path", UNSET)

        id = d.pop("id", UNSET)

        _source = d.pop("source", UNSET)
        source: UserNotificationSource | Unset
        if isinstance(_source, Unset):
            source = UNSET
        else:
            source = UserNotificationSource.from_dict(_source)

        _payload = d.pop("payload", UNSET)
        payload: UserNotificationPayload | Unset
        if isinstance(_payload, Unset):
            payload = UNSET
        else:
            payload = UserNotificationPayload.from_dict(_payload)

        user_notification = cls(
            path=path,
            id=id,
            source=source,
            payload=payload,
        )

        user_notification.additional_properties = d
        return user_notification

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
