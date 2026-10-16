from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.roblox_publish_api_upload_audio_request_asset_privacy import (
    RobloxPublishApiUploadAudioRequestAssetPrivacy,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxPublishApiUploadAudioRequest")


@_attrs_define
class RobloxPublishApiUploadAudioRequest:
    """A request model for uploading an audio file.

    Attributes:
        name (str | Unset): Name for the audio file.
        file (str | Unset): File to be uploaded. Formatted as a base64 string.
        group_id (int | Unset): Id of the group you are publishing the audio asset for. Null if not publishing under a
            group.
        payment_source (str | Unset): The source of funds for payment.
              User: Use personal funds of authenticated user.
              Group: Use group funds from Roblox.Publish.Api.UploadAudioRequest.GroupId.
              Null/Empty: Will default to authenticated user funds.
        estimated_file_size (int | Unset): Estimated file size of the audio file in bytes.
        estimated_duration (float | Unset): Estimated duration of the audio file in seconds.
        asset_privacy (RobloxPublishApiUploadAudioRequestAssetPrivacy | Unset): The asset privacy of the audio asset.
    """

    name: str | Unset = UNSET
    file: str | Unset = UNSET
    group_id: int | Unset = UNSET
    payment_source: str | Unset = UNSET
    estimated_file_size: int | Unset = UNSET
    estimated_duration: float | Unset = UNSET
    asset_privacy: RobloxPublishApiUploadAudioRequestAssetPrivacy | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        file = self.file

        group_id = self.group_id

        payment_source = self.payment_source

        estimated_file_size = self.estimated_file_size

        estimated_duration = self.estimated_duration

        asset_privacy: int | Unset = UNSET
        if not isinstance(self.asset_privacy, Unset):
            asset_privacy = self.asset_privacy.value

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if file is not UNSET:
            field_dict["file"] = file
        if group_id is not UNSET:
            field_dict["groupId"] = group_id
        if payment_source is not UNSET:
            field_dict["paymentSource"] = payment_source
        if estimated_file_size is not UNSET:
            field_dict["estimatedFileSize"] = estimated_file_size
        if estimated_duration is not UNSET:
            field_dict["estimatedDuration"] = estimated_duration
        if asset_privacy is not UNSET:
            field_dict["assetPrivacy"] = asset_privacy

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        name = d.pop("name", UNSET)

        file = d.pop("file", UNSET)

        group_id = d.pop("groupId", UNSET)

        payment_source = d.pop("paymentSource", UNSET)

        estimated_file_size = d.pop("estimatedFileSize", UNSET)

        estimated_duration = d.pop("estimatedDuration", UNSET)

        _asset_privacy = d.pop("assetPrivacy", UNSET)
        asset_privacy: RobloxPublishApiUploadAudioRequestAssetPrivacy | Unset
        if isinstance(_asset_privacy, Unset):
            asset_privacy = UNSET
        else:
            asset_privacy = RobloxPublishApiUploadAudioRequestAssetPrivacy(_asset_privacy)

        roblox_publish_api_upload_audio_request = cls(
            name=name,
            file=file,
            group_id=group_id,
            payment_source=payment_source,
            estimated_file_size=estimated_file_size,
            estimated_duration=estimated_duration,
            asset_privacy=asset_privacy,
        )

        return roblox_publish_api_upload_audio_request
