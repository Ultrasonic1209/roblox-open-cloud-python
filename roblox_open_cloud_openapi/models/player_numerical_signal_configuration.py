from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.matchmaking_numerical_attribute_comparison_type import MatchmakingNumericalAttributeComparisonType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.matchmaking_attribute_aggregation import MatchmakingAttributeAggregation
    from ..models.matchmaking_attribute_reference import MatchmakingAttributeReference


T = TypeVar("T", bound="PlayerNumericalSignalConfiguration")


@_attrs_define
class PlayerNumericalSignalConfiguration:
    """The player numerical signal configuration.

    Attributes:
        player_attribute (MatchmakingAttributeReference | Unset): Matchmaking attribute reference object for matchmaking
            rules.
        aggregation (MatchmakingAttributeAggregation | Unset): Matchmaking attribute aggregation object for matchmaking
            rules.
        comparison_type (MatchmakingNumericalAttributeComparisonType | Unset): The numerical attribute comparison type
            for matchmaking.
        max_relevant_difference (float | None | Unset): The maximum relevant difference for this signal.
        constant_value (float | None | Unset): The constant value for this signal to be compared to.
    """

    player_attribute: MatchmakingAttributeReference | Unset = UNSET
    aggregation: MatchmakingAttributeAggregation | Unset = UNSET
    comparison_type: MatchmakingNumericalAttributeComparisonType | Unset = UNSET
    max_relevant_difference: float | None | Unset = UNSET
    constant_value: float | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        player_attribute: dict[str, Any] | Unset = UNSET
        if not isinstance(self.player_attribute, Unset):
            player_attribute = self.player_attribute.to_dict()

        aggregation: dict[str, Any] | Unset = UNSET
        if not isinstance(self.aggregation, Unset):
            aggregation = self.aggregation.to_dict()

        comparison_type: str | Unset = UNSET
        if not isinstance(self.comparison_type, Unset):
            comparison_type = self.comparison_type.value

        max_relevant_difference: float | None | Unset
        if isinstance(self.max_relevant_difference, Unset):
            max_relevant_difference = UNSET
        else:
            max_relevant_difference = self.max_relevant_difference

        constant_value: float | None | Unset
        if isinstance(self.constant_value, Unset):
            constant_value = UNSET
        else:
            constant_value = self.constant_value

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if player_attribute is not UNSET:
            field_dict["playerAttribute"] = player_attribute
        if aggregation is not UNSET:
            field_dict["aggregation"] = aggregation
        if comparison_type is not UNSET:
            field_dict["comparisonType"] = comparison_type
        if max_relevant_difference is not UNSET:
            field_dict["maxRelevantDifference"] = max_relevant_difference
        if constant_value is not UNSET:
            field_dict["constantValue"] = constant_value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.matchmaking_attribute_aggregation import MatchmakingAttributeAggregation
        from ..models.matchmaking_attribute_reference import MatchmakingAttributeReference

        d = dict(src_dict)
        _player_attribute = d.pop("playerAttribute", UNSET)
        player_attribute: MatchmakingAttributeReference | Unset
        if isinstance(_player_attribute, Unset):
            player_attribute = UNSET
        else:
            player_attribute = MatchmakingAttributeReference.from_dict(_player_attribute)

        _aggregation = d.pop("aggregation", UNSET)
        aggregation: MatchmakingAttributeAggregation | Unset
        if isinstance(_aggregation, Unset):
            aggregation = UNSET
        else:
            aggregation = MatchmakingAttributeAggregation.from_dict(_aggregation)

        _comparison_type = d.pop("comparisonType", UNSET)
        comparison_type: MatchmakingNumericalAttributeComparisonType | Unset
        if isinstance(_comparison_type, Unset):
            comparison_type = UNSET
        else:
            comparison_type = MatchmakingNumericalAttributeComparisonType(_comparison_type)

        def _parse_max_relevant_difference(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        max_relevant_difference = _parse_max_relevant_difference(d.pop("maxRelevantDifference", UNSET))

        def _parse_constant_value(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        constant_value = _parse_constant_value(d.pop("constantValue", UNSET))

        player_numerical_signal_configuration = cls(
            player_attribute=player_attribute,
            aggregation=aggregation,
            comparison_type=comparison_type,
            max_relevant_difference=max_relevant_difference,
            constant_value=constant_value,
        )

        return player_numerical_signal_configuration
