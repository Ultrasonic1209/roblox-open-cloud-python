from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxGameInternationalizationApiEditAutomaticTranslationStatusForGameAndLanguageResponse")


@_attrs_define
class RobloxGameInternationalizationApiEditAutomaticTranslationStatusForGameAndLanguageResponse:
    """
    Attributes:
        game_id (int | Unset): The game id.
        language_code (str | Unset): The language code.
        is_automatic_translation_enabled (bool | Unset): Indicates whether or not automatic translation is currently
            enabled for the game and language.
    """

    game_id: int | Unset = UNSET
    language_code: str | Unset = UNSET
    is_automatic_translation_enabled: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        game_id = self.game_id

        language_code = self.language_code

        is_automatic_translation_enabled = self.is_automatic_translation_enabled

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if game_id is not UNSET:
            field_dict["gameId"] = game_id
        if language_code is not UNSET:
            field_dict["languageCode"] = language_code
        if is_automatic_translation_enabled is not UNSET:
            field_dict["isAutomaticTranslationEnabled"] = is_automatic_translation_enabled

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        game_id = d.pop("gameId", UNSET)

        language_code = d.pop("languageCode", UNSET)

        is_automatic_translation_enabled = d.pop("isAutomaticTranslationEnabled", UNSET)

        roblox_game_internationalization_api_edit_automatic_translation_status_for_game_and_language_response = cls(
            game_id=game_id,
            language_code=language_code,
            is_automatic_translation_enabled=is_automatic_translation_enabled,
        )

        return roblox_game_internationalization_api_edit_automatic_translation_status_for_game_and_language_response
