from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.matchmaking_player_attribute_definition import MatchmakingPlayerAttributeDefinition


T = TypeVar("T", bound="ListMatchmakingPlayerAttributeDefinitionsResponse")


@_attrs_define
class ListMatchmakingPlayerAttributeDefinitionsResponse:
    """The response for listing matchmaking player attribute definitions.

    Attributes:
        player_attribute_schema (list[MatchmakingPlayerAttributeDefinition] | None | Unset): All
            PlayerAttributeDefinitions for a universe.
    """

    player_attribute_schema: list[MatchmakingPlayerAttributeDefinition] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        player_attribute_schema: list[dict[str, Any]] | None | Unset
        if isinstance(self.player_attribute_schema, Unset):
            player_attribute_schema = UNSET
        elif isinstance(self.player_attribute_schema, list):
            player_attribute_schema = []
            for player_attribute_schema_type_0_item_data in self.player_attribute_schema:
                player_attribute_schema_type_0_item = player_attribute_schema_type_0_item_data.to_dict()
                player_attribute_schema.append(player_attribute_schema_type_0_item)

        else:
            player_attribute_schema = self.player_attribute_schema

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if player_attribute_schema is not UNSET:
            field_dict["playerAttributeSchema"] = player_attribute_schema

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.matchmaking_player_attribute_definition import MatchmakingPlayerAttributeDefinition

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}

        def _parse_player_attribute_schema(data: object) -> list[MatchmakingPlayerAttributeDefinition] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                player_attribute_schema_type_0 = []
                _player_attribute_schema_type_0 = data
                for player_attribute_schema_type_0_item_data in _player_attribute_schema_type_0:
                    player_attribute_schema_type_0_item = MatchmakingPlayerAttributeDefinition.from_dict(
                        player_attribute_schema_type_0_item_data
                    )

                    player_attribute_schema_type_0.append(player_attribute_schema_type_0_item)

                return player_attribute_schema_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[MatchmakingPlayerAttributeDefinition] | None | Unset, data)

        player_attribute_schema = _parse_player_attribute_schema(d.pop("playerAttributeSchema", UNSET))

        list_matchmaking_player_attribute_definitions_response = cls(
            player_attribute_schema=player_attribute_schema,
        )

        return list_matchmaking_player_attribute_definitions_response
