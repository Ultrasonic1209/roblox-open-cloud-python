from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.budget_type import BudgetType
from ..types import UNSET, Unset

T = TypeVar("T", bound="Budget")


@_attrs_define
class Budget:
    """
    Attributes:
        amount_micros (str): The budget amount in micro-USD, as a decimal string (for example, `5000000` =
            $5.00). Money is sent and returned as a string so large values keep full
            precision in every client. On a request it must be a numeric string of micro-USD.
            For ADS_CREDIT, the daily budget must not exceed the available ad credit balance
            after unbilled spend. For LIFETIME, compare amountMicros divided by the number of
            campaign days with that balance. maximumDailyBudgetMicros does not limit
            ADS_CREDIT or INVOICE campaigns.
        type_ (BudgetType): The budget cadence. Fixed when the campaign is created. Can be `DAILY` or `LIFETIME`.
        scheduled_amount_micros (str | Unset): The queued lower budget for a pending decrease, in micro-USD as a decimal
            string
            (same format as amountMicros). A budget increase takes effect immediately, but a
            decrease on a running campaign is applied at the next midnight in the account's
            time zone; until then the campaign keeps serving on amountMicros (the current,
            higher budget). Omitted when no decrease is pending.
        scheduled_effective_time (datetime.datetime | Unset): The time a pending budget decrease takes effect, as an RFC
            3339 UTC timestamp.
            Omitted when no decrease is pending.
    """

    amount_micros: str
    type_: BudgetType
    scheduled_amount_micros: str | Unset = UNSET
    scheduled_effective_time: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        amount_micros = self.amount_micros

        type_ = self.type_.value

        scheduled_amount_micros = self.scheduled_amount_micros

        scheduled_effective_time: str | Unset = UNSET
        if not isinstance(self.scheduled_effective_time, Unset):
            scheduled_effective_time = self.scheduled_effective_time.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "amountMicros": amount_micros,
                "type": type_,
            }
        )
        if scheduled_amount_micros is not UNSET:
            field_dict["scheduledAmountMicros"] = scheduled_amount_micros
        if scheduled_effective_time is not UNSET:
            field_dict["scheduledEffectiveTime"] = scheduled_effective_time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        amount_micros = d.pop("amountMicros")

        type_ = BudgetType(d.pop("type"))

        scheduled_amount_micros = d.pop("scheduledAmountMicros", UNSET)

        _scheduled_effective_time = d.pop("scheduledEffectiveTime", UNSET)
        scheduled_effective_time: datetime.datetime | Unset
        if isinstance(_scheduled_effective_time, Unset):
            scheduled_effective_time = UNSET
        else:
            scheduled_effective_time = datetime.datetime.fromisoformat(_scheduled_effective_time)

        budget = cls(
            amount_micros=amount_micros,
            type_=type_,
            scheduled_amount_micros=scheduled_amount_micros,
            scheduled_effective_time=scheduled_effective_time,
        )

        budget.additional_properties = d
        return budget

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
