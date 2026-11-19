from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.performance_estimate_budget_input import PerformanceEstimateBudgetInput
    from ..models.performance_estimate_target_outcome import PerformanceEstimateTargetOutcome


T = TypeVar("T", bound="PerformanceEstimateForecastInput")


@_attrs_define
class PerformanceEstimateForecastInput:
    """
    Attributes:
        budget (PerformanceEstimateBudgetInput | Unset):
        target_outcome (PerformanceEstimateTargetOutcome | Unset):
    """

    budget: PerformanceEstimateBudgetInput | Unset = UNSET
    target_outcome: PerformanceEstimateTargetOutcome | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        budget: dict[str, Any] | Unset = UNSET
        if not isinstance(self.budget, Unset):
            budget = self.budget.to_dict()

        target_outcome: dict[str, Any] | Unset = UNSET
        if not isinstance(self.target_outcome, Unset):
            target_outcome = self.target_outcome.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if budget is not UNSET:
            field_dict["budget"] = budget
        if target_outcome is not UNSET:
            field_dict["targetOutcome"] = target_outcome

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.performance_estimate_budget_input import PerformanceEstimateBudgetInput  # noqa: PLC0415
        from ..models.performance_estimate_target_outcome import PerformanceEstimateTargetOutcome  # noqa: PLC0415

        d = dict(src_dict)
        _budget = d.pop("budget", UNSET)
        budget: PerformanceEstimateBudgetInput | Unset
        if isinstance(_budget, Unset):
            budget = UNSET
        else:
            budget = PerformanceEstimateBudgetInput.from_dict(_budget)

        _target_outcome = d.pop("targetOutcome", UNSET)
        target_outcome: PerformanceEstimateTargetOutcome | Unset
        if isinstance(_target_outcome, Unset):
            target_outcome = UNSET
        else:
            target_outcome = PerformanceEstimateTargetOutcome.from_dict(_target_outcome)

        performance_estimate_forecast_input = cls(
            budget=budget,
            target_outcome=target_outcome,
        )

        performance_estimate_forecast_input.additional_properties = d
        return performance_estimate_forecast_input

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
