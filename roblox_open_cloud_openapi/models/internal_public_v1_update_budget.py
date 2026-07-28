from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="InternalPublicV1UpdateBudget")


@_attrs_define
class InternalPublicV1UpdateBudget:
    """
    Attributes:
        amount_micros (str | Unset): The new budget amount in micro-USD, as a decimal string (for example,
            `5000000` = $5.00). Money is sent as a string so large values keep full
            precision in every client. Must be a numeric string of micro-USD.
    """

    amount_micros: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        amount_micros = self.amount_micros

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if amount_micros is not UNSET:
            field_dict["amountMicros"] = amount_micros

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        amount_micros = d.pop("amountMicros", UNSET)

        internal_public_v1_update_budget = cls(
            amount_micros=amount_micros,
        )

        internal_public_v1_update_budget.additional_properties = d
        return internal_public_v1_update_budget

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
