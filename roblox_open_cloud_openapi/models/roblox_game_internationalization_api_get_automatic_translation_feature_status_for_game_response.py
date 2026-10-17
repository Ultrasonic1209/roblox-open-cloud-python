from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxGameInternationalizationApiGetAutomaticTranslationFeatureStatusForGameResponse")


@_attrs_define
class RobloxGameInternationalizationApiGetAutomaticTranslationFeatureStatusForGameResponse:
    """A response model for getting the automatic translation allowed status of a game.

    Attributes:
        game_id (int | Unset): The game id.
        is_automatic_translation_allowed (bool | Unset): Indicates whether or not automatic translation is allowed for
            the game.
        is_automatic_translation_switches_ui_enabled (bool | Unset): Indicates whether or not automatic translation
            switches are enabled for the game.
    """

    game_id: int | Unset = UNSET
    is_automatic_translation_allowed: bool | Unset = UNSET
    is_automatic_translation_switches_ui_enabled: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        game_id = self.game_id

        is_automatic_translation_allowed = self.is_automatic_translation_allowed

        is_automatic_translation_switches_ui_enabled = self.is_automatic_translation_switches_ui_enabled

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if game_id is not UNSET:
            field_dict["gameId"] = game_id
        if is_automatic_translation_allowed is not UNSET:
            field_dict["isAutomaticTranslationAllowed"] = is_automatic_translation_allowed
        if is_automatic_translation_switches_ui_enabled is not UNSET:
            field_dict["isAutomaticTranslationSwitchesUIEnabled"] = is_automatic_translation_switches_ui_enabled

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        game_id = d.pop("gameId", UNSET)

        is_automatic_translation_allowed = d.pop("isAutomaticTranslationAllowed", UNSET)

        is_automatic_translation_switches_ui_enabled = d.pop("isAutomaticTranslationSwitchesUIEnabled", UNSET)

        roblox_game_internationalization_api_get_automatic_translation_feature_status_for_game_response = cls(
            game_id=game_id,
            is_automatic_translation_allowed=is_automatic_translation_allowed,
            is_automatic_translation_switches_ui_enabled=is_automatic_translation_switches_ui_enabled,
        )

        return roblox_game_internationalization_api_get_automatic_translation_feature_status_for_game_response
