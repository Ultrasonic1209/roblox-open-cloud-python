from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..models.roblox_api_notifications_models_user_push_destination_platform import (
    RobloxApiNotificationsModelsUserPushDestinationPlatform,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_api_notifications_models_notification_user import RobloxApiNotificationsModelsNotificationUser


T = TypeVar("T", bound="RobloxApiNotificationsModelsUserPushDestination")


@_attrs_define
class RobloxApiNotificationsModelsUserPushDestination:
    """
    Attributes:
        user (RobloxApiNotificationsModelsNotificationUser | Unset):
        name (str | Unset): Name of the destination
        notification_token (str | Unset): Token for the corresponding notification
        supports_update_notifications (bool | Unset): Is Update notification feature supported
        user_push_notification_destination_id (int | Unset): Destination Id for the push notification
        application (str | Unset): application for the corresponding notification
            Example : "Roblox"
        platform (RobloxApiNotificationsModelsUserPushDestinationPlatform | Unset): Platform for the corresponding
            notification ['ChromeOnDesktop' = 0, 'AndroidNative' = 1, 'FirefoxOnDesktop' = 2, 'IOSNative' = 3,
            'AndroidAmazon' = 4, 'IOSTencent' = 5, 'AndroidTencentService' = 6, 'IOSPushKit' = 7]
    """

    user: RobloxApiNotificationsModelsNotificationUser | Unset = UNSET
    name: str | Unset = UNSET
    notification_token: str | Unset = UNSET
    supports_update_notifications: bool | Unset = UNSET
    user_push_notification_destination_id: int | Unset = UNSET
    application: str | Unset = UNSET
    platform: RobloxApiNotificationsModelsUserPushDestinationPlatform | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        user: dict[str, Any] | Unset = UNSET
        if not isinstance(self.user, Unset):
            user = self.user.to_dict()

        name = self.name

        notification_token = self.notification_token

        supports_update_notifications = self.supports_update_notifications

        user_push_notification_destination_id = self.user_push_notification_destination_id

        application = self.application

        platform: str | Unset = UNSET
        if not isinstance(self.platform, Unset):
            platform = self.platform.value

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if user is not UNSET:
            field_dict["user"] = user
        if name is not UNSET:
            field_dict["name"] = name
        if notification_token is not UNSET:
            field_dict["notificationToken"] = notification_token
        if supports_update_notifications is not UNSET:
            field_dict["supportsUpdateNotifications"] = supports_update_notifications
        if user_push_notification_destination_id is not UNSET:
            field_dict["userPushNotificationDestinationId"] = user_push_notification_destination_id
        if application is not UNSET:
            field_dict["application"] = application
        if platform is not UNSET:
            field_dict["platform"] = platform

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_api_notifications_models_notification_user import (
            RobloxApiNotificationsModelsNotificationUser,
        )

        d = dict(src_dict)
        _user = d.pop("user", UNSET)
        user: RobloxApiNotificationsModelsNotificationUser | Unset
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = RobloxApiNotificationsModelsNotificationUser.from_dict(_user)

        name = d.pop("name", UNSET)

        notification_token = d.pop("notificationToken", UNSET)

        supports_update_notifications = d.pop("supportsUpdateNotifications", UNSET)

        user_push_notification_destination_id = d.pop("userPushNotificationDestinationId", UNSET)

        application = d.pop("application", UNSET)

        _platform = d.pop("platform", UNSET)
        platform: RobloxApiNotificationsModelsUserPushDestinationPlatform | Unset
        if isinstance(_platform, Unset):
            platform = UNSET
        else:
            platform = RobloxApiNotificationsModelsUserPushDestinationPlatform(_platform)

        roblox_api_notifications_models_user_push_destination = cls(
            user=user,
            name=name,
            notification_token=notification_token,
            supports_update_notifications=supports_update_notifications,
            user_push_notification_destination_id=user_push_notification_destination_id,
            application=application,
            platform=platform,
        )

        return roblox_api_notifications_models_user_push_destination
