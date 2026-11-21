from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.performance_estimate_outcome_outcome_type import PerformanceEstimateOutcomeOutcomeType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.performance_estimate_value_range import PerformanceEstimateValueRange


T = TypeVar("T", bound="PerformanceEstimateOutcome")


@_attrs_define
class PerformanceEstimateOutcome:
    """
    Attributes:
        daily_value (int | Unset): Supplied daily outcome. Omitted when predicting an outcome.
        daily_value_range (PerformanceEstimateValueRange | Unset):
        lifetime_value (int | Unset): Supplied lifetime outcome. Omitted for a daily budget or when predicting an
            outcome.
        lifetime_value_range (PerformanceEstimateValueRange | Unset):
        outcome_type (PerformanceEstimateOutcomeOutcomeType | Unset): The outcome measured. Always PLAYS.
    """

    daily_value: int | Unset = UNSET
    daily_value_range: PerformanceEstimateValueRange | Unset = UNSET
    lifetime_value: int | Unset = UNSET
    lifetime_value_range: PerformanceEstimateValueRange | Unset = UNSET
    outcome_type: PerformanceEstimateOutcomeOutcomeType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        daily_value = self.daily_value

        daily_value_range: dict[str, Any] | Unset = UNSET
        if not isinstance(self.daily_value_range, Unset):
            daily_value_range = self.daily_value_range.to_dict()

        lifetime_value = self.lifetime_value

        lifetime_value_range: dict[str, Any] | Unset = UNSET
        if not isinstance(self.lifetime_value_range, Unset):
            lifetime_value_range = self.lifetime_value_range.to_dict()

        outcome_type: str | Unset = UNSET
        if not isinstance(self.outcome_type, Unset):
            outcome_type = self.outcome_type.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if daily_value is not UNSET:
            field_dict["dailyValue"] = daily_value
        if daily_value_range is not UNSET:
            field_dict["dailyValueRange"] = daily_value_range
        if lifetime_value is not UNSET:
            field_dict["lifetimeValue"] = lifetime_value
        if lifetime_value_range is not UNSET:
            field_dict["lifetimeValueRange"] = lifetime_value_range
        if outcome_type is not UNSET:
            field_dict["outcomeType"] = outcome_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.performance_estimate_value_range import PerformanceEstimateValueRange  # noqa: PLC0415

        d = dict(src_dict)
        daily_value = d.pop("dailyValue", UNSET)

        _daily_value_range = d.pop("dailyValueRange", UNSET)
        daily_value_range: PerformanceEstimateValueRange | Unset
        if isinstance(_daily_value_range, Unset):
            daily_value_range = UNSET
        else:
            daily_value_range = PerformanceEstimateValueRange.from_dict(_daily_value_range)

        lifetime_value = d.pop("lifetimeValue", UNSET)

        _lifetime_value_range = d.pop("lifetimeValueRange", UNSET)
        lifetime_value_range: PerformanceEstimateValueRange | Unset
        if isinstance(_lifetime_value_range, Unset):
            lifetime_value_range = UNSET
        else:
            lifetime_value_range = PerformanceEstimateValueRange.from_dict(_lifetime_value_range)

        _outcome_type = d.pop("outcomeType", UNSET)
        outcome_type: PerformanceEstimateOutcomeOutcomeType | Unset
        if isinstance(_outcome_type, Unset):
            outcome_type = UNSET
        else:
            outcome_type = PerformanceEstimateOutcomeOutcomeType(_outcome_type)

        performance_estimate_outcome = cls(
            daily_value=daily_value,
            daily_value_range=daily_value_range,
            lifetime_value=lifetime_value,
            lifetime_value_range=lifetime_value_range,
            outcome_type=outcome_type,
        )

        performance_estimate_outcome.additional_properties = d
        return performance_estimate_outcome

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
