from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxApiNotificationsModelsPushNotificationClientMetadata")


@_attrs_define
class RobloxApiNotificationsModelsPushNotificationClientMetadata:
    """
    Attributes:
        notification_id (UUID | Unset): Id for the push client notification
        type_ (str | Unset): Type of the push client notification
        detail (Any | Unset): Details corresponding to the notification
        fallback_delivered (bool | Unset): Is fallback delivered for the notification metadata
    """

    notification_id: UUID | Unset = UNSET
    type_: str | Unset = UNSET
    detail: Any | Unset = UNSET
    fallback_delivered: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        notification_id: str | Unset = UNSET
        if not isinstance(self.notification_id, Unset):
            notification_id = str(self.notification_id)

        type_ = self.type_

        detail = self.detail

        fallback_delivered = self.fallback_delivered

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if notification_id is not UNSET:
            field_dict["notificationId"] = notification_id
        if type_ is not UNSET:
            field_dict["type"] = type_
        if detail is not UNSET:
            field_dict["detail"] = detail
        if fallback_delivered is not UNSET:
            field_dict["fallbackDelivered"] = fallback_delivered

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _notification_id = d.pop("notificationId", UNSET)
        notification_id: UUID | Unset
        if isinstance(_notification_id, Unset):
            notification_id = UNSET
        else:
            notification_id = UUID(_notification_id)

        type_ = d.pop("type", UNSET)

        detail = d.pop("detail", UNSET)

        fallback_delivered = d.pop("fallbackDelivered", UNSET)

        roblox_api_notifications_models_push_notification_client_metadata = cls(
            notification_id=notification_id,
            type_=type_,
            detail=detail,
            fallback_delivered=fallback_delivered,
        )

        return roblox_api_notifications_models_push_notification_client_metadata
