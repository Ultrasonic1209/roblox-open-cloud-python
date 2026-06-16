from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxGameInternationalizationApiModelsResponseGetPlayerChoiceUniverseSettingsResponse")


@_attrs_define
class RobloxGameInternationalizationApiModelsResponseGetPlayerChoiceUniverseSettingsResponse:
    """
    Attributes:
        is_player_choice_enabled (bool | Unset): Checks whether player choice warning should be displayed to users.
    """

    is_player_choice_enabled: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        is_player_choice_enabled = self.is_player_choice_enabled

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if is_player_choice_enabled is not UNSET:
            field_dict["IsPlayerChoiceEnabled"] = is_player_choice_enabled

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        is_player_choice_enabled = d.pop("IsPlayerChoiceEnabled", UNSET)

        roblox_game_internationalization_api_models_response_get_player_choice_universe_settings_response = cls(
            is_player_choice_enabled=is_player_choice_enabled,
        )

        return roblox_game_internationalization_api_models_response_get_player_choice_universe_settings_response
