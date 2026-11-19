from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PerformanceEstimateBudgetInput")


@_attrs_define
class PerformanceEstimateBudgetInput:
    """
    Attributes:
        amount_micro_usd (str | Unset): Daily or lifetime total, matching forecastScope.budgetType, in micro-USD as a
            decimal string.
    """

    amount_micro_usd: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        amount_micro_usd = self.amount_micro_usd

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if amount_micro_usd is not UNSET:
            field_dict["amountMicroUsd"] = amount_micro_usd

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        amount_micro_usd = d.pop("amountMicroUsd", UNSET)

        performance_estimate_budget_input = cls(
            amount_micro_usd=amount_micro_usd,
        )

        performance_estimate_budget_input.additional_properties = d
        return performance_estimate_budget_input

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
