from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.roblox_api_notifications_models_push_notification_registration_platform import (
    RobloxApiNotificationsModelsPushNotificationRegistrationPlatform,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxApiNotificationsModelsPushNotificationRegistration")


@_attrs_define
class RobloxApiNotificationsModelsPushNotificationRegistration:
    """
    Attributes:
        user_push_notification_destination_id (int | Unset): Id of the push notification destination
        name (str | Unset): Name of the push Notification destination
        notification_token (str | Unset): Notification token
        application (str | Unset): Notification application
            Example : "Roblox"
        platform (RobloxApiNotificationsModelsPushNotificationRegistrationPlatform | Unset): Notification platform
            ['ChromeOnDesktop' = 0, 'AndroidNative' = 1, 'FirefoxOnDesktop' = 2, 'IOSNative' = 3, 'AndroidAmazon' = 4,
            'IOSTencent' = 5, 'AndroidTencentService' = 6, 'IOSPushKit' = 7]
    """

    user_push_notification_destination_id: int | Unset = UNSET
    name: str | Unset = UNSET
    notification_token: str | Unset = UNSET
    application: str | Unset = UNSET
    platform: RobloxApiNotificationsModelsPushNotificationRegistrationPlatform | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        user_push_notification_destination_id = self.user_push_notification_destination_id

        name = self.name

        notification_token = self.notification_token

        application = self.application

        platform: str | Unset = UNSET
        if not isinstance(self.platform, Unset):
            platform = self.platform.value

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if user_push_notification_destination_id is not UNSET:
            field_dict["userPushNotificationDestinationId"] = user_push_notification_destination_id
        if name is not UNSET:
            field_dict["name"] = name
        if notification_token is not UNSET:
            field_dict["notificationToken"] = notification_token
        if application is not UNSET:
            field_dict["application"] = application
        if platform is not UNSET:
            field_dict["platform"] = platform

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        user_push_notification_destination_id = d.pop("userPushNotificationDestinationId", UNSET)

        name = d.pop("name", UNSET)

        notification_token = d.pop("notificationToken", UNSET)

        application = d.pop("application", UNSET)

        _platform = d.pop("platform", UNSET)
        platform: RobloxApiNotificationsModelsPushNotificationRegistrationPlatform | Unset
        if isinstance(_platform, Unset):
            platform = UNSET
        else:
            platform = RobloxApiNotificationsModelsPushNotificationRegistrationPlatform(_platform)

        roblox_api_notifications_models_push_notification_registration = cls(
            user_push_notification_destination_id=user_push_notification_destination_id,
            name=name,
            notification_token=notification_token,
            application=application,
            platform=platform,
        )

        return roblox_api_notifications_models_push_notification_registration
