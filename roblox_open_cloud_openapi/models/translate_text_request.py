from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TranslateTextRequest")


@_attrs_define
class TranslateTextRequest:
    """Contains the text to be translated, the source language (optional), and a
    list of target languages for translation.

        Attributes:
            text (str): The text to be translated. Example: Hello.
            source_language_code (str | Unset): The IETF BCP-47 language code representing the language of the
                input text.

                If not provided, the system automatically detects the
                source language.

                Supported language codes include:

                - English (en-us)
                - French (fr-fr)
                - Vietnamese (vi-vn)
                - Thai (th-th)
                - Turkish (tr-tr)
                - Russian (ru-ru)
                - Spanish (es-es)
                - Portuguese (pt-br)
                - Korean (ko-kr)
                - Japanese (ja-jp)
                - Chinese Simplified (zh-cn)
                - Chinese Traditional (zh-tw)
                - German (de-de)
                - Polish (pl-pl)
                - Italian (it-it)
                - Indonesian (id-id) Example: en-us.
            target_language_codes (list[str] | Unset): A list of target language codes in IETF BCP-47 format for
                translation.

                Supported language codes include:

                - English (en-us)
                - French (fr-fr)
                - Vietnamese (vi-vn)
                - Thai (th-th)
                - Turkish (tr-tr)
                - Russian (ru-ru)
                - Spanish (es-es)
                - Portuguese (pt-br)
                - Korean (ko-kr)
                - Japanese (ja-jp)
                - Chinese Simplified (zh-cn)
                - Chinese Traditional (zh-tw)
                - German (de-de)
                - Polish (pl-pl)
                - Italian (it-it)
                - Indonesian (id-id) Example: fr-fr, vi-vn, ja-jp.
    """

    text: str
    source_language_code: str | Unset = UNSET
    target_language_codes: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        text = self.text

        source_language_code = self.source_language_code

        target_language_codes: list[str] | Unset = UNSET
        if not isinstance(self.target_language_codes, Unset):
            target_language_codes = self.target_language_codes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "text": text,
            }
        )
        if source_language_code is not UNSET:
            field_dict["sourceLanguageCode"] = source_language_code
        if target_language_codes is not UNSET:
            field_dict["targetLanguageCodes"] = target_language_codes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        text = d.pop("text")

        source_language_code = d.pop("sourceLanguageCode", UNSET)

        target_language_codes = cast(list[str], d.pop("targetLanguageCodes", UNSET))

        translate_text_request = cls(
            text=text,
            source_language_code=source_language_code,
            target_language_codes=target_language_codes,
        )

        translate_text_request.additional_properties = d
        return translate_text_request

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
