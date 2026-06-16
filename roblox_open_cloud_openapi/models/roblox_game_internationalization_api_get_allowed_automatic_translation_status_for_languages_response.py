from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_game_internationalization_api_automatic_translation_status_target_language import (
        RobloxGameInternationalizationApiAutomaticTranslationStatusTargetLanguage,
    )


T = TypeVar("T", bound="RobloxGameInternationalizationApiGetAllowedAutomaticTranslationStatusForLanguagesResponse")


@_attrs_define
class RobloxGameInternationalizationApiGetAllowedAutomaticTranslationStatusForLanguagesResponse:
    """A response model for getting the automatic translation allowed status of target languages.

    Attributes:
        source_language (str | Unset): The source language.
        target_languages (list[RobloxGameInternationalizationApiAutomaticTranslationStatusTargetLanguage] | Unset): The
            target languages with the automatic translation allowed status.
            The status basically says if automatic translation can be enabled for the source and target.
    """

    source_language: str | Unset = UNSET
    target_languages: list[RobloxGameInternationalizationApiAutomaticTranslationStatusTargetLanguage] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        source_language = self.source_language

        target_languages: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.target_languages, Unset):
            target_languages = []
            for target_languages_item_data in self.target_languages:
                target_languages_item = target_languages_item_data.to_dict()
                target_languages.append(target_languages_item)

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if source_language is not UNSET:
            field_dict["sourceLanguage"] = source_language
        if target_languages is not UNSET:
            field_dict["targetLanguages"] = target_languages

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_game_internationalization_api_automatic_translation_status_target_language import (
            RobloxGameInternationalizationApiAutomaticTranslationStatusTargetLanguage,
        )

        d = dict(src_dict)
        source_language = d.pop("sourceLanguage", UNSET)

        _target_languages = d.pop("targetLanguages", UNSET)
        target_languages: list[RobloxGameInternationalizationApiAutomaticTranslationStatusTargetLanguage] | Unset = (
            UNSET
        )
        if _target_languages is not UNSET:
            target_languages = []
            for target_languages_item_data in _target_languages:
                target_languages_item = (
                    RobloxGameInternationalizationApiAutomaticTranslationStatusTargetLanguage.from_dict(
                        target_languages_item_data
                    )
                )

                target_languages.append(target_languages_item)

        roblox_game_internationalization_api_get_allowed_automatic_translation_status_for_languages_response = cls(
            source_language=source_language,
            target_languages=target_languages,
        )

        return roblox_game_internationalization_api_get_allowed_automatic_translation_status_for_languages_response
