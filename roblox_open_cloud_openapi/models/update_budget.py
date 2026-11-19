from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="UpdateBudget")


@_attrs_define
class UpdateBudget:
    """
    Attributes:
        amount_micros (str): The new budget amount in micro-USD, as a decimal string (for example,
            `5000000` = $5.00). Money is sent as a string so large values keep full
            precision in every client. Must be a numeric string of micro-USD.
            Uses the same payment-specific limits as Budget.amountMicros: ADS_CREDIT budgets
            are checked against the available ad credit balance after unbilled spend.
            maximumDailyBudgetMicros does not limit ADS_CREDIT or INVOICE campaigns.
    """

    amount_micros: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        amount_micros = self.amount_micros

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "amountMicros": amount_micros,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        amount_micros = d.pop("amountMicros")

        update_budget = cls(
            amount_micros=amount_micros,
        )

        update_budget.additional_properties = d
        return update_budget

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
