from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.matchmaking_player_attribute_definition import MatchmakingPlayerAttributeDefinition


T = TypeVar("T", bound="CreateMatchmakingPlayerAttributeDefinitionResponse")


@_attrs_define
class CreateMatchmakingPlayerAttributeDefinitionResponse:
    """The response for creating a matchmaking player attribute definition.

    Attributes:
        player_attribute_definition (MatchmakingPlayerAttributeDefinition): Describes a player attribute definition for
            matchmaking.
    """

    player_attribute_definition: MatchmakingPlayerAttributeDefinition

    def to_dict(self) -> dict[str, Any]:
        player_attribute_definition = self.player_attribute_definition.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "playerAttributeDefinition": player_attribute_definition,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.matchmaking_player_attribute_definition import MatchmakingPlayerAttributeDefinition  # noqa: PLC0415

        d = dict(src_dict)
        player_attribute_definition = MatchmakingPlayerAttributeDefinition.from_dict(d.pop("playerAttributeDefinition"))

        create_matchmaking_player_attribute_definition_response = cls(
            player_attribute_definition=player_attribute_definition,
        )

        return create_matchmaking_player_attribute_definition_response
