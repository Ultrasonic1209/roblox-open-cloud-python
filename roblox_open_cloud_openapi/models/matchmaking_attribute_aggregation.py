from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.attribute_aggregation_function import AttributeAggregationFunction
from ..types import UNSET, Unset

T = TypeVar("T", bound="MatchmakingAttributeAggregation")


@_attrs_define
class MatchmakingAttributeAggregation:
    """Matchmaking attribute aggregation object for matchmaking rules.

    Attributes:
        aggregation_function (AttributeAggregationFunction | Unset): Matchmaking attribute aggregation function type.
    """

    aggregation_function: AttributeAggregationFunction | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        aggregation_function: str | Unset = UNSET
        if not isinstance(self.aggregation_function, Unset):
            aggregation_function = self.aggregation_function.value

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if aggregation_function is not UNSET:
            field_dict["aggregationFunction"] = aggregation_function

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        _aggregation_function = d.pop("aggregationFunction", UNSET)
        aggregation_function: AttributeAggregationFunction | Unset
        if isinstance(_aggregation_function, Unset):
            aggregation_function = UNSET
        else:
            aggregation_function = AttributeAggregationFunction(_aggregation_function)

        matchmaking_attribute_aggregation = cls(
            aggregation_function=aggregation_function,
        )

        return matchmaking_attribute_aggregation
