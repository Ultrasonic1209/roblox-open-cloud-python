from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxPublishApiVerifyAudioRequest")


@_attrs_define
class RobloxPublishApiVerifyAudioRequest:
    """Request model to publish an audio asset.

    Attributes:
        name (str | Unset): Gets or sets the name of the audio asset.
        file (str | Unset): File to be uploaded. Formatted as a base64 string.
        group_id (int | Unset): Gets or sets the ID of the group if applicable. Optional.
        payment_source (str | Unset): Gets or sets the payment source. 'User' or 'Group'. Required if Group ID is set.
        file_size (int | Unset): Gets or sets the size of the audio file in bytes.
        duration (float | Unset): Gets or sets the duration of the audio in seconds.
    """

    name: str | Unset = UNSET
    file: str | Unset = UNSET
    group_id: int | Unset = UNSET
    payment_source: str | Unset = UNSET
    file_size: int | Unset = UNSET
    duration: float | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        file = self.file

        group_id = self.group_id

        payment_source = self.payment_source

        file_size = self.file_size

        duration = self.duration

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
        if file_size is not UNSET:
            field_dict["fileSize"] = file_size
        if duration is not UNSET:
            field_dict["duration"] = duration

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        name = d.pop("name", UNSET)

        file = d.pop("file", UNSET)

        group_id = d.pop("groupId", UNSET)

        payment_source = d.pop("paymentSource", UNSET)

        file_size = d.pop("fileSize", UNSET)

        duration = d.pop("duration", UNSET)

        roblox_publish_api_verify_audio_request = cls(
            name=name,
            file=file,
            group_id=group_id,
            payment_source=payment_source,
            file_size=file_size,
            duration=duration,
        )

        return roblox_publish_api_verify_audio_request
