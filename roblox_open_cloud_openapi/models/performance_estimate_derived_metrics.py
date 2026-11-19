from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.performance_estimate_money_range import PerformanceEstimateMoneyRange


T = TypeVar("T", bound="PerformanceEstimateDerivedMetrics")


@_attrs_define
class PerformanceEstimateDerivedMetrics:
    """
    Attributes:
        cost_per_outcome_micro_usd (str | Unset): Cost per outcome in micro-USD, as a decimal string.
        cost_per_outcome_micro_usd_range (PerformanceEstimateMoneyRange | Unset):
    """

    cost_per_outcome_micro_usd: str | Unset = UNSET
    cost_per_outcome_micro_usd_range: PerformanceEstimateMoneyRange | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cost_per_outcome_micro_usd = self.cost_per_outcome_micro_usd

        cost_per_outcome_micro_usd_range: dict[str, Any] | Unset = UNSET
        if not isinstance(self.cost_per_outcome_micro_usd_range, Unset):
            cost_per_outcome_micro_usd_range = self.cost_per_outcome_micro_usd_range.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cost_per_outcome_micro_usd is not UNSET:
            field_dict["costPerOutcomeMicroUsd"] = cost_per_outcome_micro_usd
        if cost_per_outcome_micro_usd_range is not UNSET:
            field_dict["costPerOutcomeMicroUsdRange"] = cost_per_outcome_micro_usd_range

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.performance_estimate_money_range import PerformanceEstimateMoneyRange  # noqa: PLC0415

        d = dict(src_dict)
        cost_per_outcome_micro_usd = d.pop("costPerOutcomeMicroUsd", UNSET)

        _cost_per_outcome_micro_usd_range = d.pop("costPerOutcomeMicroUsdRange", UNSET)
        cost_per_outcome_micro_usd_range: PerformanceEstimateMoneyRange | Unset
        if isinstance(_cost_per_outcome_micro_usd_range, Unset):
            cost_per_outcome_micro_usd_range = UNSET
        else:
            cost_per_outcome_micro_usd_range = PerformanceEstimateMoneyRange.from_dict(
                _cost_per_outcome_micro_usd_range
            )

        performance_estimate_derived_metrics = cls(
            cost_per_outcome_micro_usd=cost_per_outcome_micro_usd,
            cost_per_outcome_micro_usd_range=cost_per_outcome_micro_usd_range,
        )

        performance_estimate_derived_metrics.additional_properties = d
        return performance_estimate_derived_metrics

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
