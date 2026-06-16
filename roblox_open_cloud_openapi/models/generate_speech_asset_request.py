from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.generate_speech_asset_request_generated_speech_style import (
        GenerateSpeechAssetRequestGeneratedSpeechStyle,
    )


T = TypeVar("T", bound="GenerateSpeechAssetRequest")


@_attrs_define
class GenerateSpeechAssetRequest:
    """Specifies the text from which to generate speech and the voice style.

    Attributes:
        text (str): The text to be translated. Example: Hello.
        speech_style (GenerateSpeechAssetRequestGeneratedSpeechStyle | Unset): Information about the style of generated
            speech.
    """

    text: str
    speech_style: GenerateSpeechAssetRequestGeneratedSpeechStyle | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        text = self.text

        speech_style: dict[str, Any] | Unset = UNSET
        if not isinstance(self.speech_style, Unset):
            speech_style = self.speech_style.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "text": text,
            }
        )
        if speech_style is not UNSET:
            field_dict["speechStyle"] = speech_style

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.generate_speech_asset_request_generated_speech_style import (
            GenerateSpeechAssetRequestGeneratedSpeechStyle,
        )

        d = dict(src_dict)
        text = d.pop("text")

        _speech_style = d.pop("speechStyle", UNSET)
        speech_style: GenerateSpeechAssetRequestGeneratedSpeechStyle | Unset
        if isinstance(_speech_style, Unset):
            speech_style = UNSET
        else:
            speech_style = GenerateSpeechAssetRequestGeneratedSpeechStyle.from_dict(_speech_style)

        generate_speech_asset_request = cls(
            text=text,
            speech_style=speech_style,
        )

        generate_speech_asset_request.additional_properties = d
        return generate_speech_asset_request

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
