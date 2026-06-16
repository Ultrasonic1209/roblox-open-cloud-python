from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.matchmaking_categorical_attribute_comparison_type import MatchmakingCategoricalAttributeComparisonType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.matchmaking_attribute_reference import MatchmakingAttributeReference


T = TypeVar("T", bound="ServerCategoricalSignalConfiguration")


@_attrs_define
class ServerCategoricalSignalConfiguration:
    """The server categorical signal configuration.

    Attributes:
        server_attribute (MatchmakingAttributeReference | Unset): Matchmaking attribute reference object for matchmaking
            rules.
        comparison_type (MatchmakingCategoricalAttributeComparisonType | Unset): The categorical attribute comparison
            type for matchmaking.
        player_attribute (MatchmakingAttributeReference | Unset): Matchmaking attribute reference object for matchmaking
            rules.
        constant_value (None | str | Unset): The constant value for this signal to be compared to.
    """

    server_attribute: MatchmakingAttributeReference | Unset = UNSET
    comparison_type: MatchmakingCategoricalAttributeComparisonType | Unset = UNSET
    player_attribute: MatchmakingAttributeReference | Unset = UNSET
    constant_value: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        server_attribute: dict[str, Any] | Unset = UNSET
        if not isinstance(self.server_attribute, Unset):
            server_attribute = self.server_attribute.to_dict()

        comparison_type: str | Unset = UNSET
        if not isinstance(self.comparison_type, Unset):
            comparison_type = self.comparison_type.value

        player_attribute: dict[str, Any] | Unset = UNSET
        if not isinstance(self.player_attribute, Unset):
            player_attribute = self.player_attribute.to_dict()

        constant_value: None | str | Unset
        if isinstance(self.constant_value, Unset):
            constant_value = UNSET
        else:
            constant_value = self.constant_value

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if server_attribute is not UNSET:
            field_dict["serverAttribute"] = server_attribute
        if comparison_type is not UNSET:
            field_dict["comparisonType"] = comparison_type
        if player_attribute is not UNSET:
            field_dict["playerAttribute"] = player_attribute
        if constant_value is not UNSET:
            field_dict["constantValue"] = constant_value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.matchmaking_attribute_reference import MatchmakingAttributeReference

        d = dict(src_dict)
        _server_attribute = d.pop("serverAttribute", UNSET)
        server_attribute: MatchmakingAttributeReference | Unset
        if isinstance(_server_attribute, Unset):
            server_attribute = UNSET
        else:
            server_attribute = MatchmakingAttributeReference.from_dict(_server_attribute)

        _comparison_type = d.pop("comparisonType", UNSET)
        comparison_type: MatchmakingCategoricalAttributeComparisonType | Unset
        if isinstance(_comparison_type, Unset):
            comparison_type = UNSET
        else:
            comparison_type = MatchmakingCategoricalAttributeComparisonType(_comparison_type)

        _player_attribute = d.pop("playerAttribute", UNSET)
        player_attribute: MatchmakingAttributeReference | Unset
        if isinstance(_player_attribute, Unset):
            player_attribute = UNSET
        else:
            player_attribute = MatchmakingAttributeReference.from_dict(_player_attribute)

        def _parse_constant_value(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        constant_value = _parse_constant_value(d.pop("constantValue", UNSET))

        server_categorical_signal_configuration = cls(
            server_attribute=server_attribute,
            comparison_type=comparison_type,
            player_attribute=player_attribute,
            constant_value=constant_value,
        )

        return server_categorical_signal_configuration
