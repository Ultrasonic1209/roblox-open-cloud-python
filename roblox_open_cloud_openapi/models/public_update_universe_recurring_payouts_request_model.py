from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.public_recurring_payout_request_model import PublicRecurringPayoutRequestModel


T = TypeVar("T", bound="PublicUpdateUniverseRecurringPayoutsRequestModel")


@_attrs_define
class PublicUpdateUniverseRecurringPayoutsRequestModel:
    """Request for updating recurring payouts through the public groups API.

    Attributes:
        payouts (list[PublicRecurringPayoutRequestModel]): The recurring payout splits to apply.
    """

    payouts: list[PublicRecurringPayoutRequestModel]

    def to_dict(self) -> dict[str, Any]:
        payouts = []
        for payouts_item_data in self.payouts:
            payouts_item = payouts_item_data.to_dict()
            payouts.append(payouts_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "payouts": payouts,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.public_recurring_payout_request_model import PublicRecurringPayoutRequestModel

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        payouts = []
        _payouts = d.pop("payouts")
        for payouts_item_data in _payouts:
            payouts_item = PublicRecurringPayoutRequestModel.from_dict(payouts_item_data)

            payouts.append(payouts_item)

        public_update_universe_recurring_payouts_request_model = cls(
            payouts=payouts,
        )

        return public_update_universe_recurring_payouts_request_model
