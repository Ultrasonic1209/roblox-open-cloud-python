from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..models.service_efficiency_api_transaction_status import ServiceEfficiencyApiTransactionStatus

if TYPE_CHECKING:
    from ..models.service_efficiency_api_money import ServiceEfficiencyApiMoney


T = TypeVar("T", bound="Payment")


@_attrs_define
class Payment:
    """Service Efficiency API representation of a payment.

    Attributes:
        timestamp (int): Gets or sets the time of this payment, in unix milliseconds.
        amount (ServiceEfficiencyApiMoney): Temporary until https://roblox.atlassian.net/browse/ICSC-1360 is done.
            Will be replaced by google.type.Money
        status (ServiceEfficiencyApiTransactionStatus): Transaction Status for HTTP responses.
    """

    timestamp: int
    amount: ServiceEfficiencyApiMoney
    status: ServiceEfficiencyApiTransactionStatus

    def to_dict(self) -> dict[str, Any]:
        timestamp = self.timestamp

        amount = self.amount.to_dict()

        status = self.status.value

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "timestamp": timestamp,
                "amount": amount,
                "status": status,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.service_efficiency_api_money import ServiceEfficiencyApiMoney

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        timestamp = d.pop("timestamp")

        amount = ServiceEfficiencyApiMoney.from_dict(d.pop("amount"))

        status = ServiceEfficiencyApiTransactionStatus(d.pop("status"))

        payment = cls(
            timestamp=timestamp,
            amount=amount,
            status=status,
        )

        return payment
