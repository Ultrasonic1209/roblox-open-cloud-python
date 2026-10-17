from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxApiNotificationsModelsResponseModelsNotificationStreamMetadataResponse")


@_attrs_define
class RobloxApiNotificationsModelsResponseModelsNotificationStreamMetadataResponse:
    """
    Attributes:
        banner_dismiss_time_span (int | Unset):
        signal_r_disconnection_response_in_milliseconds (int | Unset):
        can_launch_game_from_game_update (bool | Unset):
    """

    banner_dismiss_time_span: int | Unset = UNSET
    signal_r_disconnection_response_in_milliseconds: int | Unset = UNSET
    can_launch_game_from_game_update: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        banner_dismiss_time_span = self.banner_dismiss_time_span

        signal_r_disconnection_response_in_milliseconds = self.signal_r_disconnection_response_in_milliseconds

        can_launch_game_from_game_update = self.can_launch_game_from_game_update

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if banner_dismiss_time_span is not UNSET:
            field_dict["bannerDismissTimeSpan"] = banner_dismiss_time_span
        if signal_r_disconnection_response_in_milliseconds is not UNSET:
            field_dict["signalRDisconnectionResponseInMilliseconds"] = signal_r_disconnection_response_in_milliseconds
        if can_launch_game_from_game_update is not UNSET:
            field_dict["canLaunchGameFromGameUpdate"] = can_launch_game_from_game_update

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        banner_dismiss_time_span = d.pop("bannerDismissTimeSpan", UNSET)

        signal_r_disconnection_response_in_milliseconds = d.pop("signalRDisconnectionResponseInMilliseconds", UNSET)

        can_launch_game_from_game_update = d.pop("canLaunchGameFromGameUpdate", UNSET)

        roblox_api_notifications_models_response_models_notification_stream_metadata_response = cls(
            banner_dismiss_time_span=banner_dismiss_time_span,
            signal_r_disconnection_response_in_milliseconds=signal_r_disconnection_response_in_milliseconds,
            can_launch_game_from_game_update=can_launch_game_from_game_update,
        )

        return roblox_api_notifications_models_response_models_notification_stream_metadata_response
