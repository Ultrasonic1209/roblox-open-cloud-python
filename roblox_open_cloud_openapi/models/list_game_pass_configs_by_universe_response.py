from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.game_pass_config_v2 import GamePassConfigV2


T = TypeVar("T", bound="ListGamePassConfigsByUniverseResponse")


@_attrs_define
class ListGamePassConfigsByUniverseResponse:
    """Response for listing game pass configuration details by universe

    Attributes:
        game_passes (list[GamePassConfigV2]): The list of game passes with their corresponding configuration details.
        next_page_token (None | str): The next page token.
    """

    game_passes: list[GamePassConfigV2]
    next_page_token: None | str

    def to_dict(self) -> dict[str, Any]:
        game_passes = []
        for game_passes_item_data in self.game_passes:
            game_passes_item = game_passes_item_data.to_dict()
            game_passes.append(game_passes_item)

        next_page_token: None | str
        next_page_token = self.next_page_token

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "gamePasses": game_passes,
                "nextPageToken": next_page_token,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.game_pass_config_v2 import GamePassConfigV2

        d = dict(src_dict)
        game_passes = []
        _game_passes = d.pop("gamePasses")
        for game_passes_item_data in _game_passes:
            game_passes_item = GamePassConfigV2.from_dict(game_passes_item_data)

            game_passes.append(game_passes_item)

        def _parse_next_page_token(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        next_page_token = _parse_next_page_token(d.pop("nextPageToken"))

        list_game_pass_configs_by_universe_response = cls(
            game_passes=game_passes,
            next_page_token=next_page_token,
        )

        return list_game_pass_configs_by_universe_response
