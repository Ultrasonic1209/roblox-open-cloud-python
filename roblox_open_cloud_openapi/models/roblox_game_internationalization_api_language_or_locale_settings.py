from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.roblox_game_internationalization_api_language_or_locale_settings_language_code_type import (
    RobloxGameInternationalizationApiLanguageOrLocaleSettingsLanguageCodeType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxGameInternationalizationApiLanguageOrLocaleSettings")


@_attrs_define
class RobloxGameInternationalizationApiLanguageOrLocaleSettings:
    """
    Attributes:
        language_code_type (RobloxGameInternationalizationApiLanguageOrLocaleSettingsLanguageCodeType | Unset): The
            language code type. ['Language' = 0, 'Locale' = 1]
        language_code (str | Unset): The language code.
        is_automatic_translation_enabled (bool | Unset): Indicates whether or not automatic translation is currently
            enabled for the game and language.
        is_image_translation_enabled (bool | Unset): Indicates whether image translation is currently enabled for the
            game and language.
    """

    language_code_type: RobloxGameInternationalizationApiLanguageOrLocaleSettingsLanguageCodeType | Unset = UNSET
    language_code: str | Unset = UNSET
    is_automatic_translation_enabled: bool | Unset = UNSET
    is_image_translation_enabled: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        language_code_type: str | Unset = UNSET
        if not isinstance(self.language_code_type, Unset):
            language_code_type = self.language_code_type.value

        language_code = self.language_code

        is_automatic_translation_enabled = self.is_automatic_translation_enabled

        is_image_translation_enabled = self.is_image_translation_enabled

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if language_code_type is not UNSET:
            field_dict["languageCodeType"] = language_code_type
        if language_code is not UNSET:
            field_dict["languageCode"] = language_code
        if is_automatic_translation_enabled is not UNSET:
            field_dict["isAutomaticTranslationEnabled"] = is_automatic_translation_enabled
        if is_image_translation_enabled is not UNSET:
            field_dict["isImageTranslationEnabled"] = is_image_translation_enabled

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _language_code_type = d.pop("languageCodeType", UNSET)
        language_code_type: RobloxGameInternationalizationApiLanguageOrLocaleSettingsLanguageCodeType | Unset
        if isinstance(_language_code_type, Unset):
            language_code_type = UNSET
        else:
            language_code_type = RobloxGameInternationalizationApiLanguageOrLocaleSettingsLanguageCodeType(
                _language_code_type
            )

        language_code = d.pop("languageCode", UNSET)

        is_automatic_translation_enabled = d.pop("isAutomaticTranslationEnabled", UNSET)

        is_image_translation_enabled = d.pop("isImageTranslationEnabled", UNSET)

        roblox_game_internationalization_api_language_or_locale_settings = cls(
            language_code_type=language_code_type,
            language_code=language_code,
            is_automatic_translation_enabled=is_automatic_translation_enabled,
            is_image_translation_enabled=is_image_translation_enabled,
        )

        return roblox_game_internationalization_api_language_or_locale_settings
