from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_api_notifications_models_user_push_destination import (
        RobloxApiNotificationsModelsUserPushDestination,
    )


T = TypeVar("T", bound="RobloxApiNotificationsModelsGetPushDestinationsResponseModel")


@_attrs_define
class RobloxApiNotificationsModelsGetPushDestinationsResponseModel:
    """
    Attributes:
        destinations (list[RobloxApiNotificationsModelsUserPushDestination] | Unset): List of destinations for the user
            push notification
        status_message (str | Unset): Message for the success response
    """

    destinations: list[RobloxApiNotificationsModelsUserPushDestination] | Unset = UNSET
    status_message: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        destinations: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.destinations, Unset):
            destinations = []
            for destinations_item_data in self.destinations:
                destinations_item = destinations_item_data.to_dict()
                destinations.append(destinations_item)

        status_message = self.status_message

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if destinations is not UNSET:
            field_dict["destinations"] = destinations
        if status_message is not UNSET:
            field_dict["statusMessage"] = status_message

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_api_notifications_models_user_push_destination import (
            RobloxApiNotificationsModelsUserPushDestination,
        )

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        _destinations = d.pop("destinations", UNSET)
        destinations: list[RobloxApiNotificationsModelsUserPushDestination] | Unset = UNSET
        if _destinations is not UNSET:
            destinations = []
            for destinations_item_data in _destinations:
                destinations_item = RobloxApiNotificationsModelsUserPushDestination.from_dict(destinations_item_data)

                destinations.append(destinations_item)

        status_message = d.pop("statusMessage", UNSET)

        roblox_api_notifications_models_get_push_destinations_response_model = cls(
            destinations=destinations,
            status_message=status_message,
        )

        return roblox_api_notifications_models_get_push_destinations_response_model
