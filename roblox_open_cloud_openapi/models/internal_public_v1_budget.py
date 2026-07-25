from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.internal_public_v1_budget_type import InternalPublicV1BudgetType
from ..types import UNSET, Unset

T = TypeVar("T", bound="InternalPublicV1Budget")


@_attrs_define
class InternalPublicV1Budget:
    """
    Attributes:
        amount_micros (str | Unset): The budget amount in micro-USD, as a decimal string (for example, `5000000` =
            $5.00). Money is sent and returned as a string so large values keep full
            precision in every client. On a request it must be a numeric string of micro-USD.
        scheduled_amount_micros (str | Unset): The queued lower budget for a pending decrease, in micro-USD as a decimal
            string
            (same format as amountMicros). A budget increase takes effect immediately, but a
            decrease on a running campaign is applied at the next midnight in the account's
            time zone; until then the campaign keeps serving on amountMicros (the current,
            higher budget). Omitted when no decrease is pending.
        scheduled_effective_time (str | Unset): The time a pending budget decrease takes effect, as an RFC 3339 UTC
            timestamp.
            Omitted when no decrease is pending.
        type_ (InternalPublicV1BudgetType | Unset): The budget cadence. Fixed when the campaign is created. Can be
            `DAILY` or `LIFETIME`.
    """

    amount_micros: str | Unset = UNSET
    scheduled_amount_micros: str | Unset = UNSET
    scheduled_effective_time: str | Unset = UNSET
    type_: InternalPublicV1BudgetType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        amount_micros = self.amount_micros

        scheduled_amount_micros = self.scheduled_amount_micros

        scheduled_effective_time = self.scheduled_effective_time

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if amount_micros is not UNSET:
            field_dict["amountMicros"] = amount_micros
        if scheduled_amount_micros is not UNSET:
            field_dict["scheduledAmountMicros"] = scheduled_amount_micros
        if scheduled_effective_time is not UNSET:
            field_dict["scheduledEffectiveTime"] = scheduled_effective_time
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        amount_micros = d.pop("amountMicros", UNSET)

        scheduled_amount_micros = d.pop("scheduledAmountMicros", UNSET)

        scheduled_effective_time = d.pop("scheduledEffectiveTime", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: InternalPublicV1BudgetType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = InternalPublicV1BudgetType(_type_)

        internal_public_v1_budget = cls(
            amount_micros=amount_micros,
            scheduled_amount_micros=scheduled_amount_micros,
            scheduled_effective_time=scheduled_effective_time,
            type_=type_,
        )

        internal_public_v1_budget.additional_properties = d
        return internal_public_v1_budget

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
