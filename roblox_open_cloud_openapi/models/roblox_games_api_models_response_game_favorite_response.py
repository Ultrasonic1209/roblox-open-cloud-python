from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxGamesApiModelsResponseGameFavoriteResponse")


@_attrs_define
class RobloxGamesApiModelsResponseGameFavoriteResponse:
    """Game favorite response model.

    Attributes:
        is_favorited (bool | Unset): Is it a favorite game.
    """

    is_favorited: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        is_favorited = self.is_favorited

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if is_favorited is not UNSET:
            field_dict["isFavorited"] = is_favorited

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        is_favorited = d.pop("isFavorited", UNSET)

        roblox_games_api_models_response_game_favorite_response = cls(
            is_favorited=is_favorited,
        )

        return roblox_games_api_models_response_game_favorite_response
