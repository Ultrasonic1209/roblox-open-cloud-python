from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..models.matchmaking_server_attribute_default_value_source_case import (
    MatchmakingServerAttributeDefaultValueSourceCase,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.matchmaking_attribute_reference import MatchmakingAttributeReference
    from ..models.matchmaking_attribute_value import MatchmakingAttributeValue


T = TypeVar("T", bound="MatchmakingServerAttributeDefaultValue")


@_attrs_define
class MatchmakingServerAttributeDefaultValue:
    """Describes how the server attribute value should be derived

    Attributes:
        source_case (MatchmakingServerAttributeDefaultValueSourceCase | Unset): The storage solution used for this
            MatchmakingPlayerAttributeDefinition.
        constant (MatchmakingAttributeValue | Unset): Matchmaking attribute value object for matchmaking rules.
        player_attribute_reference (MatchmakingAttributeReference | Unset): Matchmaking attribute reference object for
            matchmaking rules.
    """

    source_case: MatchmakingServerAttributeDefaultValueSourceCase | Unset = UNSET
    constant: MatchmakingAttributeValue | Unset = UNSET
    player_attribute_reference: MatchmakingAttributeReference | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        source_case: str | Unset = UNSET
        if not isinstance(self.source_case, Unset):
            source_case = self.source_case.value

        constant: dict[str, Any] | Unset = UNSET
        if not isinstance(self.constant, Unset):
            constant = self.constant.to_dict()

        player_attribute_reference: dict[str, Any] | Unset = UNSET
        if not isinstance(self.player_attribute_reference, Unset):
            player_attribute_reference = self.player_attribute_reference.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if source_case is not UNSET:
            field_dict["sourceCase"] = source_case
        if constant is not UNSET:
            field_dict["constant"] = constant
        if player_attribute_reference is not UNSET:
            field_dict["playerAttributeReference"] = player_attribute_reference

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.matchmaking_attribute_reference import MatchmakingAttributeReference
        from ..models.matchmaking_attribute_value import MatchmakingAttributeValue

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        _source_case = d.pop("sourceCase", UNSET)
        source_case: MatchmakingServerAttributeDefaultValueSourceCase | Unset
        if isinstance(_source_case, Unset):
            source_case = UNSET
        else:
            source_case = MatchmakingServerAttributeDefaultValueSourceCase(_source_case)

        _constant = d.pop("constant", UNSET)
        constant: MatchmakingAttributeValue | Unset
        if isinstance(_constant, Unset):
            constant = UNSET
        else:
            constant = MatchmakingAttributeValue.from_dict(_constant)

        _player_attribute_reference = d.pop("playerAttributeReference", UNSET)
        player_attribute_reference: MatchmakingAttributeReference | Unset
        if isinstance(_player_attribute_reference, Unset):
            player_attribute_reference = UNSET
        else:
            player_attribute_reference = MatchmakingAttributeReference.from_dict(_player_attribute_reference)

        matchmaking_server_attribute_default_value = cls(
            source_case=source_case,
            constant=constant,
            player_attribute_reference=player_attribute_reference,
        )

        return matchmaking_server_attribute_default_value
