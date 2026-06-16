from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.roblox_game_internationalization_api_language_or_locale_language_code_type import (
    RobloxGameInternationalizationApiLanguageOrLocaleLanguageCodeType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxGameInternationalizationApiLanguageOrLocale")


@_attrs_define
class RobloxGameInternationalizationApiLanguageOrLocale:
    """
    Attributes:
        name (str | Unset):
        language_code_type (RobloxGameInternationalizationApiLanguageOrLocaleLanguageCodeType | Unset): An enum to
            distinguish between locale codes and language codes. ['Language' = 0, 'Locale' = 1]
        language_code (str | Unset):
    """

    name: str | Unset = UNSET
    language_code_type: RobloxGameInternationalizationApiLanguageOrLocaleLanguageCodeType | Unset = UNSET
    language_code: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        language_code_type: str | Unset = UNSET
        if not isinstance(self.language_code_type, Unset):
            language_code_type = self.language_code_type.value

        language_code = self.language_code

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if language_code_type is not UNSET:
            field_dict["languageCodeType"] = language_code_type
        if language_code is not UNSET:
            field_dict["languageCode"] = language_code

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        _language_code_type = d.pop("languageCodeType", UNSET)
        language_code_type: RobloxGameInternationalizationApiLanguageOrLocaleLanguageCodeType | Unset
        if isinstance(_language_code_type, Unset):
            language_code_type = UNSET
        else:
            language_code_type = RobloxGameInternationalizationApiLanguageOrLocaleLanguageCodeType(_language_code_type)

        language_code = d.pop("languageCode", UNSET)

        roblox_game_internationalization_api_language_or_locale = cls(
            name=name,
            language_code_type=language_code_type,
            language_code=language_code,
        )

        return roblox_game_internationalization_api_language_or_locale
