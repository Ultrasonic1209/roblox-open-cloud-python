from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.budget_constraint_budget_type import BudgetConstraintBudgetType
from ..types import UNSET, Unset

T = TypeVar("T", bound="BudgetConstraint")


@_attrs_define
class BudgetConstraint:
    """
    Attributes:
        budget_type (BudgetConstraintBudgetType): The budget type. Values can be `DAILY` or `LIFETIME`.
        minimum_amount_micros (str): The minimum budget in micro-USD, as a decimal string. For `LIFETIME`, this is
            the minimum per day of the schedule.
        maximum_amount_micros (str | Unset): The personal account's maximum DAILY budget for CREDIT_CARD,
            in micro-USD. Omitted for other payment types and when universeId is supplied.
        maximum_duration_in_days (int | Unset): The longest schedule allowed, in days.
    """

    budget_type: BudgetConstraintBudgetType
    minimum_amount_micros: str
    maximum_amount_micros: str | Unset = UNSET
    maximum_duration_in_days: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        budget_type = self.budget_type.value

        minimum_amount_micros = self.minimum_amount_micros

        maximum_amount_micros = self.maximum_amount_micros

        maximum_duration_in_days = self.maximum_duration_in_days

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "budgetType": budget_type,
                "minimumAmountMicros": minimum_amount_micros,
            }
        )
        if maximum_amount_micros is not UNSET:
            field_dict["maximumAmountMicros"] = maximum_amount_micros
        if maximum_duration_in_days is not UNSET:
            field_dict["maximumDurationInDays"] = maximum_duration_in_days

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        budget_type = BudgetConstraintBudgetType(d.pop("budgetType"))

        minimum_amount_micros = d.pop("minimumAmountMicros")

        maximum_amount_micros = d.pop("maximumAmountMicros", UNSET)

        maximum_duration_in_days = d.pop("maximumDurationInDays", UNSET)

        budget_constraint = cls(
            budget_type=budget_type,
            minimum_amount_micros=minimum_amount_micros,
            maximum_amount_micros=maximum_amount_micros,
            maximum_duration_in_days=maximum_duration_in_days,
        )

        budget_constraint.additional_properties = d
        return budget_constraint

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
