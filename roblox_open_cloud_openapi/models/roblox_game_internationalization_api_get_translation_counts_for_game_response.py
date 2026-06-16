from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_game_internationalization_api_translation_count_language_or_locale_response import (
        RobloxGameInternationalizationApiTranslationCountLanguageOrLocaleResponse,
    )


T = TypeVar("T", bound="RobloxGameInternationalizationApiGetTranslationCountsForGameResponse")


@_attrs_define
class RobloxGameInternationalizationApiGetTranslationCountsForGameResponse:
    """A response model that contains game info for getting a translation count.

    Attributes:
        game_id (int | Unset): The game id.
        languages_or_locales (list[RobloxGameInternationalizationApiTranslationCountLanguageOrLocaleResponse] | Unset):
            The list of languages/locales of the game.
    """

    game_id: int | Unset = UNSET
    languages_or_locales: list[RobloxGameInternationalizationApiTranslationCountLanguageOrLocaleResponse] | Unset = (
        UNSET
    )

    def to_dict(self) -> dict[str, Any]:
        game_id = self.game_id

        languages_or_locales: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.languages_or_locales, Unset):
            languages_or_locales = []
            for languages_or_locales_item_data in self.languages_or_locales:
                languages_or_locales_item = languages_or_locales_item_data.to_dict()
                languages_or_locales.append(languages_or_locales_item)

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if game_id is not UNSET:
            field_dict["gameId"] = game_id
        if languages_or_locales is not UNSET:
            field_dict["languagesOrLocales"] = languages_or_locales

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_game_internationalization_api_translation_count_language_or_locale_response import (
            RobloxGameInternationalizationApiTranslationCountLanguageOrLocaleResponse,
        )

        d = dict(src_dict)
        game_id = d.pop("gameId", UNSET)

        _languages_or_locales = d.pop("languagesOrLocales", UNSET)
        languages_or_locales: (
            list[RobloxGameInternationalizationApiTranslationCountLanguageOrLocaleResponse] | Unset
        ) = UNSET
        if _languages_or_locales is not UNSET:
            languages_or_locales = []
            for languages_or_locales_item_data in _languages_or_locales:
                languages_or_locales_item = (
                    RobloxGameInternationalizationApiTranslationCountLanguageOrLocaleResponse.from_dict(
                        languages_or_locales_item_data
                    )
                )

                languages_or_locales.append(languages_or_locales_item)

        roblox_game_internationalization_api_get_translation_counts_for_game_response = cls(
            game_id=game_id,
            languages_or_locales=languages_or_locales,
        )

        return roblox_game_internationalization_api_get_translation_counts_for_game_response
