from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_api_notifications_models_user_push_destination import (
        RobloxApiNotificationsModelsUserPushDestination,
    )


T = TypeVar("T", bound="RobloxApiNotificationsModelsGetCurrentPushDestinationResponseModel")


@_attrs_define
class RobloxApiNotificationsModelsGetCurrentPushDestinationResponseModel:
    """
    Attributes:
        destination (RobloxApiNotificationsModelsUserPushDestination | Unset):
        status_message (str | Unset): Message for the success response
    """

    destination: RobloxApiNotificationsModelsUserPushDestination | Unset = UNSET
    status_message: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        destination: dict[str, Any] | Unset = UNSET
        if not isinstance(self.destination, Unset):
            destination = self.destination.to_dict()

        status_message = self.status_message

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if destination is not UNSET:
            field_dict["destination"] = destination
        if status_message is not UNSET:
            field_dict["statusMessage"] = status_message

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_api_notifications_models_user_push_destination import (
            RobloxApiNotificationsModelsUserPushDestination,
        )

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        _destination = d.pop("destination", UNSET)
        destination: RobloxApiNotificationsModelsUserPushDestination | Unset
        if isinstance(_destination, Unset):
            destination = UNSET
        else:
            destination = RobloxApiNotificationsModelsUserPushDestination.from_dict(_destination)

        status_message = d.pop("statusMessage", UNSET)

        roblox_api_notifications_models_get_current_push_destination_response_model = cls(
            destination=destination,
            status_message=status_message,
        )

        return roblox_api_notifications_models_get_current_push_destination_response_model
