from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GenerateSpeechAssetRequestGeneratedSpeechStyle")


@_attrs_define
class GenerateSpeechAssetRequestGeneratedSpeechStyle:
    """Information about the style of generated speech.

    Attributes:
        voice_id (str | Unset): An ID corresponding to the voice type specified. A mapping of voice type
            to
            ID number is available in the documentation. Example: 1.
        pitch (float | Unset): The pitch of the generated speech.
        speed (float | Unset): The speed of the generated speech.
    """

    voice_id: str | Unset = UNSET
    pitch: float | Unset = UNSET
    speed: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        voice_id = self.voice_id

        pitch = self.pitch

        speed = self.speed

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if voice_id is not UNSET:
            field_dict["voiceId"] = voice_id
        if pitch is not UNSET:
            field_dict["pitch"] = pitch
        if speed is not UNSET:
            field_dict["speed"] = speed

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        voice_id = d.pop("voiceId", UNSET)

        pitch = d.pop("pitch", UNSET)

        speed = d.pop("speed", UNSET)

        generate_speech_asset_request_generated_speech_style = cls(
            voice_id=voice_id,
            pitch=pitch,
            speed=speed,
        )

        generate_speech_asset_request_generated_speech_style.additional_properties = d
        return generate_speech_asset_request_generated_speech_style

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
