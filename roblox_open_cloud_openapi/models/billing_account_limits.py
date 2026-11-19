from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BillingAccountLimits")


@_attrs_define
class BillingAccountLimits:
    """
    Attributes:
        billing_threshold_micros (str | Unset): Card billing threshold in micro-USD: when outstandingBalanceMicros
            reaches this
            amount, accrued charges are billed to the card on file. Applies only to CREDIT_CARD
            spend: ADS_CREDIT spends from the balance, and INVOICE accounts are billed monthly.
            Can be present before a card is on file. Omitted when the account has no threshold.
        maximum_daily_budget_micros (str | Unset): The maximum daily budget for CREDIT_CARD campaigns in this account,
            in micro-USD.
            A non-positive value means no positive CREDIT_CARD budget is allowed.
            For LIFETIME, multiply by the schedule's number of days.
            Omitted when no verified card bills the account. Returned even when it is too low
            for CREDIT_CARD to be usable. Does not limit ADS_CREDIT or INVOICE campaigns.
    """

    billing_threshold_micros: str | Unset = UNSET
    maximum_daily_budget_micros: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        billing_threshold_micros = self.billing_threshold_micros

        maximum_daily_budget_micros = self.maximum_daily_budget_micros

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if billing_threshold_micros is not UNSET:
            field_dict["billingThresholdMicros"] = billing_threshold_micros
        if maximum_daily_budget_micros is not UNSET:
            field_dict["maximumDailyBudgetMicros"] = maximum_daily_budget_micros

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        billing_threshold_micros = d.pop("billingThresholdMicros", UNSET)

        maximum_daily_budget_micros = d.pop("maximumDailyBudgetMicros", UNSET)

        billing_account_limits = cls(
            billing_threshold_micros=billing_threshold_micros,
            maximum_daily_budget_micros=maximum_daily_budget_micros,
        )

        billing_account_limits.additional_properties = d
        return billing_account_limits

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
