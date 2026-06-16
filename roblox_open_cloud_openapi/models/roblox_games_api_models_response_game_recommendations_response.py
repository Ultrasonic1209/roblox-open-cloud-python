from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_games_api_models_response_game_response_model import (
        RobloxGamesApiModelsResponseGameResponseModel,
    )


T = TypeVar("T", bound="RobloxGamesApiModelsResponseGameRecommendationsResponse")


@_attrs_define
class RobloxGamesApiModelsResponseGameRecommendationsResponse:
    """Game recommendations response model.

    Attributes:
        games (list[RobloxGamesApiModelsResponseGameResponseModel] | Unset): The recommended games.
        next_pagination_key (str | Unset): The pagination key for next page query.
            It will be null if there is no more data.
    """

    games: list[RobloxGamesApiModelsResponseGameResponseModel] | Unset = UNSET
    next_pagination_key: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        games: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.games, Unset):
            games = []
            for games_item_data in self.games:
                games_item = games_item_data.to_dict()
                games.append(games_item)

        next_pagination_key = self.next_pagination_key

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if games is not UNSET:
            field_dict["games"] = games
        if next_pagination_key is not UNSET:
            field_dict["nextPaginationKey"] = next_pagination_key

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_games_api_models_response_game_response_model import (
            RobloxGamesApiModelsResponseGameResponseModel,
        )

        d = dict(src_dict)
        _games = d.pop("games", UNSET)
        games: list[RobloxGamesApiModelsResponseGameResponseModel] | Unset = UNSET
        if _games is not UNSET:
            games = []
            for games_item_data in _games:
                games_item = RobloxGamesApiModelsResponseGameResponseModel.from_dict(games_item_data)

                games.append(games_item)

        next_pagination_key = d.pop("nextPaginationKey", UNSET)

        roblox_games_api_models_response_game_recommendations_response = cls(
            games=games,
            next_pagination_key=next_pagination_key,
        )

        return roblox_games_api_models_response_game_recommendations_response
