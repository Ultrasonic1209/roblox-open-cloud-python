from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.matchmaking_server_attribute_definition import MatchmakingServerAttributeDefinition


T = TypeVar("T", bound="UpdateMatchmakingServerAttributeDefinitionResponse")


@_attrs_define
class UpdateMatchmakingServerAttributeDefinitionResponse:
    """The response for updating a matchmaking server attribute definition.

    Attributes:
        player_attribute_definition (MatchmakingServerAttributeDefinition | Unset): Describes a player attribute
            definition for matchmaking.
    """

    player_attribute_definition: MatchmakingServerAttributeDefinition | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        player_attribute_definition: dict[str, Any] | Unset = UNSET
        if not isinstance(self.player_attribute_definition, Unset):
            player_attribute_definition = self.player_attribute_definition.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if player_attribute_definition is not UNSET:
            field_dict["playerAttributeDefinition"] = player_attribute_definition

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.matchmaking_server_attribute_definition import MatchmakingServerAttributeDefinition

        d = dict(src_dict)
        _player_attribute_definition = d.pop("playerAttributeDefinition", UNSET)
        player_attribute_definition: MatchmakingServerAttributeDefinition | Unset
        if isinstance(_player_attribute_definition, Unset):
            player_attribute_definition = UNSET
        else:
            player_attribute_definition = MatchmakingServerAttributeDefinition.from_dict(_player_attribute_definition)

        update_matchmaking_server_attribute_definition_response = cls(
            player_attribute_definition=player_attribute_definition,
        )

        return update_matchmaking_server_attribute_definition_response
