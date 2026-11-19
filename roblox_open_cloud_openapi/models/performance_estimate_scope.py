from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.performance_estimate_scope_budget_type import PerformanceEstimateScopeBudgetType
from ..types import UNSET, Unset

T = TypeVar("T", bound="PerformanceEstimateScope")


@_attrs_define
class PerformanceEstimateScope:
    """
    Attributes:
        budget_type (PerformanceEstimateScopeBudgetType): DAILY or LIFETIME.
        duration_in_days (int | Unset): Required and positive for LIFETIME. Must be 0 for DAILY.
    """

    budget_type: PerformanceEstimateScopeBudgetType
    duration_in_days: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        budget_type = self.budget_type.value

        duration_in_days = self.duration_in_days

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "budgetType": budget_type,
            }
        )
        if duration_in_days is not UNSET:
            field_dict["durationInDays"] = duration_in_days

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        budget_type = PerformanceEstimateScopeBudgetType(d.pop("budgetType"))

        duration_in_days = d.pop("durationInDays", UNSET)

        performance_estimate_scope = cls(
            budget_type=budget_type,
            duration_in_days=duration_in_days,
        )

        performance_estimate_scope.additional_properties = d
        return performance_estimate_scope

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
