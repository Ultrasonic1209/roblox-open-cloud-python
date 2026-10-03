from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="PublicOneTimePayout")


@_attrs_define
class PublicOneTimePayout:
    """One-time payout details in the public groups API contract.

    Attributes:
        amount (int | Unset):
        created_at (datetime.datetime | Unset):
    """

    amount: int | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        amount = self.amount

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if amount is not UNSET:
            field_dict["amount"] = amount
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        amount = d.pop("amount", UNSET)

        _created_at = d.pop("createdAt", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = datetime.datetime.fromisoformat(_created_at)

        public_one_time_payout = cls(
            amount=amount,
            created_at=created_at,
        )

        return public_one_time_payout
