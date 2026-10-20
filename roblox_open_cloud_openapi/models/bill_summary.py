from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.bill_status import BillStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.service_efficiency_api_money import ServiceEfficiencyApiMoney


T = TypeVar("T", bound="BillSummary")


@_attrs_define
class BillSummary:
    """Summary of a bill.

    Attributes:
        timestamp (int): Gets or sets the year of this bill.
        bill_status (BillStatus): Bill Status Type
        total_amount (ServiceEfficiencyApiMoney): Temporary until https://roblox.atlassian.net/browse/ICSC-1360 is done.
            Will be replaced by google.type.Money
        bill_id (None | str | Unset): Gets or sets string ID of the bill.
    """

    timestamp: int
    bill_status: BillStatus
    total_amount: ServiceEfficiencyApiMoney
    bill_id: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        timestamp = self.timestamp

        bill_status = self.bill_status.value

        total_amount = self.total_amount.to_dict()

        bill_id: None | str | Unset
        if isinstance(self.bill_id, Unset):
            bill_id = UNSET
        else:
            bill_id = self.bill_id

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "timestamp": timestamp,
                "billStatus": bill_status,
                "totalAmount": total_amount,
            }
        )
        if bill_id is not UNSET:
            field_dict["billId"] = bill_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.service_efficiency_api_money import ServiceEfficiencyApiMoney  # noqa: PLC0415

        d = dict(src_dict)
        timestamp = d.pop("timestamp")

        bill_status = BillStatus(d.pop("billStatus"))

        total_amount = ServiceEfficiencyApiMoney.from_dict(d.pop("totalAmount"))

        def _parse_bill_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        bill_id = _parse_bill_id(d.pop("billId", UNSET))

        bill_summary = cls(
            timestamp=timestamp,
            bill_status=bill_status,
            total_amount=total_amount,
            bill_id=bill_id,
        )

        return bill_summary
