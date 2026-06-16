from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..models.roblox_game_internationalization_api_get_translation_counts_for_language_or_locale_response_language_or_locale_type import (
    RobloxGameInternationalizationApiGetTranslationCountsForLanguageOrLocaleResponseLanguageOrLocaleType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_game_internationalization_api_translation_count_game_info_response import (
        RobloxGameInternationalizationApiTranslationCountGameInfoResponse,
    )


T = TypeVar("T", bound="RobloxGameInternationalizationApiGetTranslationCountsForLanguageOrLocaleResponse")


@_attrs_define
class RobloxGameInternationalizationApiGetTranslationCountsForLanguageOrLocaleResponse:
    """A response model for getting translation counts for a language or locale.

    Attributes:
        language_or_locale_code (str | Unset): The code of the language or locale.
        language_or_locale_type
            (RobloxGameInternationalizationApiGetTranslationCountsForLanguageOrLocaleResponseLanguageOrLocaleType | Unset):
            An indicator that says whether the passed in language/locale code represents a language or locale. ['Language' =
            0, 'Locale' = 1]
        games (list[RobloxGameInternationalizationApiTranslationCountGameInfoResponse] | Unset): Info for the requested
            games, including their translation counts for the specified language or locale.
    """

    language_or_locale_code: str | Unset = UNSET
    language_or_locale_type: (
        RobloxGameInternationalizationApiGetTranslationCountsForLanguageOrLocaleResponseLanguageOrLocaleType | Unset
    ) = UNSET
    games: list[RobloxGameInternationalizationApiTranslationCountGameInfoResponse] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        language_or_locale_code = self.language_or_locale_code

        language_or_locale_type: str | Unset = UNSET
        if not isinstance(self.language_or_locale_type, Unset):
            language_or_locale_type = self.language_or_locale_type.value

        games: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.games, Unset):
            games = []
            for games_item_data in self.games:
                games_item = games_item_data.to_dict()
                games.append(games_item)

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if language_or_locale_code is not UNSET:
            field_dict["languageOrLocaleCode"] = language_or_locale_code
        if language_or_locale_type is not UNSET:
            field_dict["languageOrLocaleType"] = language_or_locale_type
        if games is not UNSET:
            field_dict["games"] = games

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_game_internationalization_api_translation_count_game_info_response import (
            RobloxGameInternationalizationApiTranslationCountGameInfoResponse,
        )

        d = dict(src_dict)
        language_or_locale_code = d.pop("languageOrLocaleCode", UNSET)

        _language_or_locale_type = d.pop("languageOrLocaleType", UNSET)
        language_or_locale_type: (
            RobloxGameInternationalizationApiGetTranslationCountsForLanguageOrLocaleResponseLanguageOrLocaleType | Unset
        )
        if isinstance(_language_or_locale_type, Unset):
            language_or_locale_type = UNSET
        else:
            language_or_locale_type = (
                RobloxGameInternationalizationApiGetTranslationCountsForLanguageOrLocaleResponseLanguageOrLocaleType(
                    _language_or_locale_type
                )
            )

        _games = d.pop("games", UNSET)
        games: list[RobloxGameInternationalizationApiTranslationCountGameInfoResponse] | Unset = UNSET
        if _games is not UNSET:
            games = []
            for games_item_data in _games:
                games_item = RobloxGameInternationalizationApiTranslationCountGameInfoResponse.from_dict(
                    games_item_data
                )

                games.append(games_item)

        roblox_game_internationalization_api_get_translation_counts_for_language_or_locale_response = cls(
            language_or_locale_code=language_or_locale_code,
            language_or_locale_type=language_or_locale_type,
            games=games,
        )

        return roblox_game_internationalization_api_get_translation_counts_for_language_or_locale_response
