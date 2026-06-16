from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.translate_text_response_translations import TranslateTextResponseTranslations


T = TypeVar("T", bound="TranslateTextResponse")


@_attrs_define
class TranslateTextResponse:
    """Contains the detected or specified source language code and a map of
    requested translations, where each key is a language code and the value is
    the translated text.

        Attributes:
            source_language_code (str | Unset): The IETF BCP-47 language code representing the detected or user-specified
                language of the source text.
            translations (TranslateTextResponseTranslations | Unset): A map containing the requested translations. The key
                is the IETF BCP-47
                language code, and the value is the translated text for that language.
                The map contains all requested translations.
    """

    source_language_code: str | Unset = UNSET
    translations: TranslateTextResponseTranslations | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        source_language_code = self.source_language_code

        translations: dict[str, Any] | Unset = UNSET
        if not isinstance(self.translations, Unset):
            translations = self.translations.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if source_language_code is not UNSET:
            field_dict["sourceLanguageCode"] = source_language_code
        if translations is not UNSET:
            field_dict["translations"] = translations

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.translate_text_response_translations import TranslateTextResponseTranslations

        d = dict(src_dict)
        source_language_code = d.pop("sourceLanguageCode", UNSET)

        _translations = d.pop("translations", UNSET)
        translations: TranslateTextResponseTranslations | Unset
        if isinstance(_translations, Unset):
            translations = UNSET
        else:
            translations = TranslateTextResponseTranslations.from_dict(_translations)

        translate_text_response = cls(
            source_language_code=source_language_code,
            translations=translations,
        )

        translate_text_response.additional_properties = d
        return translate_text_response

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
