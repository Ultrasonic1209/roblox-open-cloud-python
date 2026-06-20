from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxApiNotificationsModelsRegisterAndroidRequestModel")


@_attrs_define
class RobloxApiNotificationsModelsRegisterAndroidRequestModel:
    """
    Attributes:
        notification_token (str | Unset): Token for notification
        authorize_for_user (bool | Unset): Is this call authorized for user
        old_notification_token (str | Unset): Old notification token
        device_name (str | Unset): Name of the requesting device
    """

    notification_token: str | Unset = UNSET
    authorize_for_user: bool | Unset = UNSET
    old_notification_token: str | Unset = UNSET
    device_name: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        notification_token = self.notification_token

        authorize_for_user = self.authorize_for_user

        old_notification_token = self.old_notification_token

        device_name = self.device_name

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if notification_token is not UNSET:
            field_dict["notificationToken"] = notification_token
        if authorize_for_user is not UNSET:
            field_dict["authorizeForUser"] = authorize_for_user
        if old_notification_token is not UNSET:
            field_dict["oldNotificationToken"] = old_notification_token
        if device_name is not UNSET:
            field_dict["deviceName"] = device_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        notification_token = d.pop("notificationToken", UNSET)

        authorize_for_user = d.pop("authorizeForUser", UNSET)

        old_notification_token = d.pop("oldNotificationToken", UNSET)

        device_name = d.pop("deviceName", UNSET)

        roblox_api_notifications_models_register_android_request_model = cls(
            notification_token=notification_token,
            authorize_for_user=authorize_for_user,
            old_notification_token=old_notification_token,
            device_name=device_name,
        )

        return roblox_api_notifications_models_register_android_request_model
