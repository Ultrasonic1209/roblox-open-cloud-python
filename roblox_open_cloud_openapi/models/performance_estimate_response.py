from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.performance_estimate_response_predicted import PerformanceEstimateResponsePredicted
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.performance_estimate_budget import PerformanceEstimateBudget
    from ..models.performance_estimate_derived_metrics import PerformanceEstimateDerivedMetrics
    from ..models.performance_estimate_outcome import PerformanceEstimateOutcome


T = TypeVar("T", bound="PerformanceEstimateResponse")


@_attrs_define
class PerformanceEstimateResponse:
    """
    Attributes:
        budget (PerformanceEstimateBudget | Unset):
        derived_metrics (PerformanceEstimateDerivedMetrics | Unset):
        outcome (PerformanceEstimateOutcome | Unset):
        predicted (PerformanceEstimateResponsePredicted | Unset): Which side was calculated: OUTCOME from a budget, or
            BUDGET from a target outcome.
    """

    budget: PerformanceEstimateBudget | Unset = UNSET
    derived_metrics: PerformanceEstimateDerivedMetrics | Unset = UNSET
    outcome: PerformanceEstimateOutcome | Unset = UNSET
    predicted: PerformanceEstimateResponsePredicted | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        budget: dict[str, Any] | Unset = UNSET
        if not isinstance(self.budget, Unset):
            budget = self.budget.to_dict()

        derived_metrics: dict[str, Any] | Unset = UNSET
        if not isinstance(self.derived_metrics, Unset):
            derived_metrics = self.derived_metrics.to_dict()

        outcome: dict[str, Any] | Unset = UNSET
        if not isinstance(self.outcome, Unset):
            outcome = self.outcome.to_dict()

        predicted: str | Unset = UNSET
        if not isinstance(self.predicted, Unset):
            predicted = self.predicted.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if budget is not UNSET:
            field_dict["budget"] = budget
        if derived_metrics is not UNSET:
            field_dict["derivedMetrics"] = derived_metrics
        if outcome is not UNSET:
            field_dict["outcome"] = outcome
        if predicted is not UNSET:
            field_dict["predicted"] = predicted

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.performance_estimate_budget import PerformanceEstimateBudget  # noqa: PLC0415
        from ..models.performance_estimate_derived_metrics import PerformanceEstimateDerivedMetrics  # noqa: PLC0415
        from ..models.performance_estimate_outcome import PerformanceEstimateOutcome  # noqa: PLC0415

        d = dict(src_dict)
        _budget = d.pop("budget", UNSET)
        budget: PerformanceEstimateBudget | Unset
        if isinstance(_budget, Unset):
            budget = UNSET
        else:
            budget = PerformanceEstimateBudget.from_dict(_budget)

        _derived_metrics = d.pop("derivedMetrics", UNSET)
        derived_metrics: PerformanceEstimateDerivedMetrics | Unset
        if isinstance(_derived_metrics, Unset):
            derived_metrics = UNSET
        else:
            derived_metrics = PerformanceEstimateDerivedMetrics.from_dict(_derived_metrics)

        _outcome = d.pop("outcome", UNSET)
        outcome: PerformanceEstimateOutcome | Unset
        if isinstance(_outcome, Unset):
            outcome = UNSET
        else:
            outcome = PerformanceEstimateOutcome.from_dict(_outcome)

        _predicted = d.pop("predicted", UNSET)
        predicted: PerformanceEstimateResponsePredicted | Unset
        if isinstance(_predicted, Unset):
            predicted = UNSET
        else:
            predicted = PerformanceEstimateResponsePredicted(_predicted)

        performance_estimate_response = cls(
            budget=budget,
            derived_metrics=derived_metrics,
            outcome=outcome,
            predicted=predicted,
        )

        performance_estimate_response.additional_properties = d
        return performance_estimate_response

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
