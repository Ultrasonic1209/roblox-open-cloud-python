from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxGameInternationalizationApiUniverseDisplayInfoAutomaticTranslationSettings")


@_attrs_define
class RobloxGameInternationalizationApiUniverseDisplayInfoAutomaticTranslationSettings:
    """
    Attributes:
        language_code (str | Unset): The language code.
        is_universe_display_info_automatic_translation_enabled (bool | Unset): Indicates whether or not automatic
            translation is currently enabled for Game and Place Information for a game and language.
    """

    language_code: str | Unset = UNSET
    is_universe_display_info_automatic_translation_enabled: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        language_code = self.language_code

        is_universe_display_info_automatic_translation_enabled = (
            self.is_universe_display_info_automatic_translation_enabled
        )

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if language_code is not UNSET:
            field_dict["languageCode"] = language_code
        if is_universe_display_info_automatic_translation_enabled is not UNSET:
            field_dict["isUniverseDisplayInfoAutomaticTranslationEnabled"] = (
                is_universe_display_info_automatic_translation_enabled
            )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        language_code = d.pop("languageCode", UNSET)

        is_universe_display_info_automatic_translation_enabled = d.pop(
            "isUniverseDisplayInfoAutomaticTranslationEnabled", UNSET
        )

        roblox_game_internationalization_api_universe_display_info_automatic_translation_settings = cls(
            language_code=language_code,
            is_universe_display_info_automatic_translation_enabled=is_universe_display_info_automatic_translation_enabled,
        )

        return roblox_game_internationalization_api_universe_display_info_automatic_translation_settings
