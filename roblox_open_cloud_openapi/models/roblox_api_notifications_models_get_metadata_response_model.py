from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_api_notifications_models_push_notification_client_metadata import (
        RobloxApiNotificationsModelsPushNotificationClientMetadata,
    )


T = TypeVar("T", bound="RobloxApiNotificationsModelsGetMetadataResponseModel")


@_attrs_define
class RobloxApiNotificationsModelsGetMetadataResponseModel:
    """
    Attributes:
        metadata (RobloxApiNotificationsModelsPushNotificationClientMetadata | Unset):
        status_message (str | Unset): Message for the success response
    """

    metadata: RobloxApiNotificationsModelsPushNotificationClientMetadata | Unset = UNSET
    status_message: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        status_message = self.status_message

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if status_message is not UNSET:
            field_dict["statusMessage"] = status_message

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_api_notifications_models_push_notification_client_metadata import (
            RobloxApiNotificationsModelsPushNotificationClientMetadata,
        )

        d = dict(src_dict)
        _metadata = d.pop("metadata", UNSET)
        metadata: RobloxApiNotificationsModelsPushNotificationClientMetadata | Unset
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = RobloxApiNotificationsModelsPushNotificationClientMetadata.from_dict(_metadata)

        status_message = d.pop("statusMessage", UNSET)

        roblox_api_notifications_models_get_metadata_response_model = cls(
            metadata=metadata,
            status_message=status_message,
        )

        return roblox_api_notifications_models_get_metadata_response_model
