from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_api_notifications_models_push_notification_registration import (
        RobloxApiNotificationsModelsPushNotificationRegistration,
    )


T = TypeVar("T", bound="RobloxApiNotificationsModelsRegistrationResponseModel")


@_attrs_define
class RobloxApiNotificationsModelsRegistrationResponseModel:
    """
    Attributes:
        registration (RobloxApiNotificationsModelsPushNotificationRegistration | Unset):
        status_message (str | Unset): Message for the success response
    """

    registration: RobloxApiNotificationsModelsPushNotificationRegistration | Unset = UNSET
    status_message: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        registration: dict[str, Any] | Unset = UNSET
        if not isinstance(self.registration, Unset):
            registration = self.registration.to_dict()

        status_message = self.status_message

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if registration is not UNSET:
            field_dict["registration"] = registration
        if status_message is not UNSET:
            field_dict["statusMessage"] = status_message

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_api_notifications_models_push_notification_registration import (
            RobloxApiNotificationsModelsPushNotificationRegistration,
        )

        d = dict(src_dict)
        _registration = d.pop("registration", UNSET)
        registration: RobloxApiNotificationsModelsPushNotificationRegistration | Unset
        if isinstance(_registration, Unset):
            registration = UNSET
        else:
            registration = RobloxApiNotificationsModelsPushNotificationRegistration.from_dict(_registration)

        status_message = d.pop("statusMessage", UNSET)

        roblox_api_notifications_models_registration_response_model = cls(
            registration=registration,
            status_message=status_message,
        )

        return roblox_api_notifications_models_registration_response_model
