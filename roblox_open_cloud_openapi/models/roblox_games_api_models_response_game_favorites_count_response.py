from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxGamesApiModelsResponseGameFavoritesCountResponse")


@_attrs_define
class RobloxGamesApiModelsResponseGameFavoritesCountResponse:
    """Response model for favorited game count.

    Attributes:
        favorites_count (int | Unset): Favorites count.
    """

    favorites_count: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        favorites_count = self.favorites_count

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if favorites_count is not UNSET:
            field_dict["favoritesCount"] = favorites_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        favorites_count = d.pop("favoritesCount", UNSET)

        roblox_games_api_models_response_game_favorites_count_response = cls(
            favorites_count=favorites_count,
        )

        return roblox_games_api_models_response_game_favorites_count_response
