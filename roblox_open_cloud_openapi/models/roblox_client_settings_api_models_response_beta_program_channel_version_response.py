from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="RobloxClientSettingsApiModelsResponseBetaProgramChannelVersionResponse")


@_attrs_define
class RobloxClientSettingsApiModelsResponseBetaProgramChannelVersionResponse:
    """The channel of a beta program and its current version guid.

    Attributes:
        channel_name (str): Name of the channel.
        is_flag_only (bool): Whether the channel is flag-only, i.e. uses production binaries.
        client_version_upload (str): The channel's current client version upload. For flag-only channels, this is
            production's.
    """

    channel_name: str
    is_flag_only: bool
    client_version_upload: str

    def to_dict(self) -> dict[str, Any]:
        channel_name = self.channel_name

        is_flag_only = self.is_flag_only

        client_version_upload = self.client_version_upload

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "channelName": channel_name,
                "isFlagOnly": is_flag_only,
                "clientVersionUpload": client_version_upload,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        channel_name = d.pop("channelName")

        is_flag_only = d.pop("isFlagOnly")

        client_version_upload = d.pop("clientVersionUpload")

        roblox_client_settings_api_models_response_beta_program_channel_version_response = cls(
            channel_name=channel_name,
            is_flag_only=is_flag_only,
            client_version_upload=client_version_upload,
        )

        return roblox_client_settings_api_models_response_beta_program_channel_version_response
