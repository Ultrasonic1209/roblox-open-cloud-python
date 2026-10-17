from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.service_efficiency_api_money import ServiceEfficiencyApiMoney


T = TypeVar("T", bound="SubmitManualPaymentRequest")


@_attrs_define
class SubmitManualPaymentRequest:
    """Request object to be set as the body of submit manual payment endpoint requests.

    Attributes:
        amount (None | ServiceEfficiencyApiMoney | Unset): Gets or sets the amount of money to charge in the manual
            payment.
        bill_id (None | str | Unset): Gets or sets the id of the bill to make the manual payment on.
    """

    amount: None | ServiceEfficiencyApiMoney | Unset = UNSET
    bill_id: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.service_efficiency_api_money import ServiceEfficiencyApiMoney

        amount: dict[str, Any] | None | Unset
        if isinstance(self.amount, Unset):
            amount = UNSET
        elif isinstance(self.amount, ServiceEfficiencyApiMoney):
            amount = self.amount.to_dict()
        else:
            amount = self.amount

        bill_id: None | str | Unset
        if isinstance(self.bill_id, Unset):
            bill_id = UNSET
        else:
            bill_id = self.bill_id

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if amount is not UNSET:
            field_dict["amount"] = amount
        if bill_id is not UNSET:
            field_dict["billId"] = bill_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.service_efficiency_api_money import ServiceEfficiencyApiMoney

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}

        def _parse_amount(data: object) -> None | ServiceEfficiencyApiMoney | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                amount_type_1 = ServiceEfficiencyApiMoney.from_dict(data)

                return amount_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ServiceEfficiencyApiMoney | Unset, data)

        amount = _parse_amount(d.pop("amount", UNSET))

        def _parse_bill_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        bill_id = _parse_bill_id(d.pop("billId", UNSET))

        submit_manual_payment_request = cls(
            amount=amount,
            bill_id=bill_id,
        )

        return submit_manual_payment_request
