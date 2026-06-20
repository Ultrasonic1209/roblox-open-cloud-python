from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxGameInternationalizationApiAutomaticTranslationStatusTargetLanguage")


@_attrs_define
class RobloxGameInternationalizationApiAutomaticTranslationStatusTargetLanguage:
    """
    Attributes:
        language_code (str | Unset): The language code.
        is_automatic_translation_allowed (bool | Unset): Indicates whether or not automatic translation is allowed for
            the target language.
    """

    language_code: str | Unset = UNSET
    is_automatic_translation_allowed: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        language_code = self.language_code

        is_automatic_translation_allowed = self.is_automatic_translation_allowed

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if language_code is not UNSET:
            field_dict["languageCode"] = language_code
        if is_automatic_translation_allowed is not UNSET:
            field_dict["isAutomaticTranslationAllowed"] = is_automatic_translation_allowed

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        language_code = d.pop("languageCode", UNSET)

        is_automatic_translation_allowed = d.pop("isAutomaticTranslationAllowed", UNSET)

        roblox_game_internationalization_api_automatic_translation_status_target_language = cls(
            language_code=language_code,
            is_automatic_translation_allowed=is_automatic_translation_allowed,
        )

        return roblox_game_internationalization_api_automatic_translation_status_target_language
