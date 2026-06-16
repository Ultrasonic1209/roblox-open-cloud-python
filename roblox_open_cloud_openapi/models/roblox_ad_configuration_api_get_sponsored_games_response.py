from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_ad_configuration_api_sponsored_game_v2_model import (
        RobloxAdConfigurationApiSponsoredGameV2Model,
    )


T = TypeVar("T", bound="RobloxAdConfigurationApiGetSponsoredGamesResponse")


@_attrs_define
class RobloxAdConfigurationApiGetSponsoredGamesResponse:
    """A response model for retrieving a page of Roblox.AdConfiguration.Api.SponsoredGameV2Model.

    Attributes:
        sponsored_games (list[RobloxAdConfigurationApiSponsoredGameV2Model] | Unset): A collection of
            Roblox.AdConfiguration.Api.SponsoredGameV2Model.
        previous_page_cursor (str | Unset): The cursor for retrieving the previous page, if present.
        next_page_cursor (str | Unset): The cursor for retrieving the next page, if present.
    """

    sponsored_games: list[RobloxAdConfigurationApiSponsoredGameV2Model] | Unset = UNSET
    previous_page_cursor: str | Unset = UNSET
    next_page_cursor: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        sponsored_games: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.sponsored_games, Unset):
            sponsored_games = []
            for sponsored_games_item_data in self.sponsored_games:
                sponsored_games_item = sponsored_games_item_data.to_dict()
                sponsored_games.append(sponsored_games_item)

        previous_page_cursor = self.previous_page_cursor

        next_page_cursor = self.next_page_cursor

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if sponsored_games is not UNSET:
            field_dict["sponsoredGames"] = sponsored_games
        if previous_page_cursor is not UNSET:
            field_dict["previousPageCursor"] = previous_page_cursor
        if next_page_cursor is not UNSET:
            field_dict["nextPageCursor"] = next_page_cursor

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_ad_configuration_api_sponsored_game_v2_model import (
            RobloxAdConfigurationApiSponsoredGameV2Model,
        )

        d = dict(src_dict)
        _sponsored_games = d.pop("sponsoredGames", UNSET)
        sponsored_games: list[RobloxAdConfigurationApiSponsoredGameV2Model] | Unset = UNSET
        if _sponsored_games is not UNSET:
            sponsored_games = []
            for sponsored_games_item_data in _sponsored_games:
                sponsored_games_item = RobloxAdConfigurationApiSponsoredGameV2Model.from_dict(sponsored_games_item_data)

                sponsored_games.append(sponsored_games_item)

        previous_page_cursor = d.pop("previousPageCursor", UNSET)

        next_page_cursor = d.pop("nextPageCursor", UNSET)

        roblox_ad_configuration_api_get_sponsored_games_response = cls(
            sponsored_games=sponsored_games,
            previous_page_cursor=previous_page_cursor,
            next_page_cursor=next_page_cursor,
        )

        return roblox_ad_configuration_api_get_sponsored_games_response
