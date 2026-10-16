from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="PublicRecurringPayoutRequestModel")


@_attrs_define
class PublicRecurringPayoutRequestModel:
    """A numeric-ID recurring payout split in the public groups API contract.

    Attributes:
        user_id (int): The payout recipient user ID.
        percentage (int): The recipient's payout percentage.
    """

    user_id: int
    percentage: int

    def to_dict(self) -> dict[str, Any]:
        user_id = self.user_id

        percentage = self.percentage

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "userId": user_id,
                "percentage": percentage,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        user_id = d.pop("userId")

        percentage = d.pop("percentage")

        public_recurring_payout_request_model = cls(
            user_id=user_id,
            percentage=percentage,
        )

        return public_recurring_payout_request_model
