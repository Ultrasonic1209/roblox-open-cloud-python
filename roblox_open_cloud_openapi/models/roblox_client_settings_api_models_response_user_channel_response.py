from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..models.roblox_client_settings_api_models_response_user_channel_response_channel_assignment_type import (
    RobloxClientSettingsApiModelsResponseUserChannelResponseChannelAssignmentType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_client_settings_api_models_response_beta_program_info import (
        RobloxClientSettingsApiModelsResponseBetaProgramInfo,
    )


T = TypeVar("T", bound="RobloxClientSettingsApiModelsResponseUserChannelResponse")


@_attrs_define
class RobloxClientSettingsApiModelsResponseUserChannelResponse:
    """Response data object for getting a user's channel information.

    Attributes:
        channel_name (str | Unset): Name of the channel.
        channel_assignment_type (RobloxClientSettingsApiModelsResponseUserChannelResponseChannelAssignmentType | Unset):
            How the user was bound to the channel. If the user is not assigned to any channel, this is omitted. ['None' = 0,
            'PerMille' = 1, 'BoundToPrivateChannel' = 2, 'BoundToPublicChannel' = 3,
            'OptedInToBetaProgramWithPrivateChannel' = 4, 'OptedInToBetaProgramWithPublicChannel' = 5]
        token (str | Unset): JWT token. If the channel is not private, this is omitted.
        program (RobloxClientSettingsApiModelsResponseBetaProgramInfo | Unset): Beta program information included in the
            user channel response.
        is_flag_only (bool | Unset): Whether the channel is flag-only. A flag-only channel uses production binaries.
            If the channel is not flag-only, this is omitted.
    """

    channel_name: str | Unset = UNSET
    channel_assignment_type: RobloxClientSettingsApiModelsResponseUserChannelResponseChannelAssignmentType | Unset = (
        UNSET
    )
    token: str | Unset = UNSET
    program: RobloxClientSettingsApiModelsResponseBetaProgramInfo | Unset = UNSET
    is_flag_only: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        channel_name = self.channel_name

        channel_assignment_type: int | Unset = UNSET
        if not isinstance(self.channel_assignment_type, Unset):
            channel_assignment_type = self.channel_assignment_type.value

        token = self.token

        program: dict[str, Any] | Unset = UNSET
        if not isinstance(self.program, Unset):
            program = self.program.to_dict()

        is_flag_only = self.is_flag_only

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if channel_name is not UNSET:
            field_dict["channelName"] = channel_name
        if channel_assignment_type is not UNSET:
            field_dict["channelAssignmentType"] = channel_assignment_type
        if token is not UNSET:
            field_dict["token"] = token
        if program is not UNSET:
            field_dict["program"] = program
        if is_flag_only is not UNSET:
            field_dict["isFlagOnly"] = is_flag_only

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_client_settings_api_models_response_beta_program_info import (
            RobloxClientSettingsApiModelsResponseBetaProgramInfo,
        )

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        channel_name = d.pop("channelName", UNSET)

        _channel_assignment_type = d.pop("channelAssignmentType", UNSET)
        channel_assignment_type: RobloxClientSettingsApiModelsResponseUserChannelResponseChannelAssignmentType | Unset
        if isinstance(_channel_assignment_type, Unset):
            channel_assignment_type = UNSET
        else:
            channel_assignment_type = RobloxClientSettingsApiModelsResponseUserChannelResponseChannelAssignmentType(
                _channel_assignment_type
            )

        token = d.pop("token", UNSET)

        _program = d.pop("program", UNSET)
        program: RobloxClientSettingsApiModelsResponseBetaProgramInfo | Unset
        if isinstance(_program, Unset):
            program = UNSET
        else:
            program = RobloxClientSettingsApiModelsResponseBetaProgramInfo.from_dict(_program)

        is_flag_only = d.pop("isFlagOnly", UNSET)

        roblox_client_settings_api_models_response_user_channel_response = cls(
            channel_name=channel_name,
            channel_assignment_type=channel_assignment_type,
            token=token,
            program=program,
            is_flag_only=is_flag_only,
        )

        return roblox_client_settings_api_models_response_user_channel_response
