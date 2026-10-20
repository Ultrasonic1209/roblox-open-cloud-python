from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.bill_status import BillStatus
from ..models.response_account_state import ResponseAccountState
from ..models.tax_id_type import TaxIdType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.address import Address
    from ..models.consumer_usage import ConsumerUsage
    from ..models.payment import Payment
    from ..models.service_efficiency_api_money import ServiceEfficiencyApiMoney


T = TypeVar("T", bound="BillDetailsResponse")


@_attrs_define
class BillDetailsResponse:
    """Response object for a billing statement.

    Attributes:
        bill_status (BillStatus): Bill Status Type
        usage_amount (ServiceEfficiencyApiMoney): Temporary until https://roblox.atlassian.net/browse/ICSC-1360 is done.
            Will be replaced by google.type.Money
        tax_amount (ServiceEfficiencyApiMoney): Temporary until https://roblox.atlassian.net/browse/ICSC-1360 is done.
            Will be replaced by google.type.Money
        total_amount (ServiceEfficiencyApiMoney): Temporary until https://roblox.atlassian.net/browse/ICSC-1360 is done.
            Will be replaced by google.type.Money
        usages (list[ConsumerUsage]): Gets or sets the list of consumer usages.
        billing_address (Address): Represents an address.
        roblox_address (Address): Represents an address.
        payments (list[Payment]): Gets or sets the payments associated with this bill.
        account_state (ResponseAccountState | Unset): Account State in the HTTP response.
        bill_id (None | str | Unset): Gets or sets the ID of the bill.
        tax_id (None | str | Unset): Gets or sets the tax id used for this bill.
        tax_id_type (None | TaxIdType | Unset): Gets or sets the type of the tax id used for this bill.
        conversion_rate (float | None | Unset): Gets or sets the USD-to-local-currency conversion rate at bill creation
            time, provided for reference only.
            Null if the payment method is in the US, the bill predates this feature, or for pending bills.
            -1 if the currency converter lookup failed.
    """

    bill_status: BillStatus
    usage_amount: ServiceEfficiencyApiMoney
    tax_amount: ServiceEfficiencyApiMoney
    total_amount: ServiceEfficiencyApiMoney
    usages: list[ConsumerUsage]
    billing_address: Address
    roblox_address: Address
    payments: list[Payment]
    account_state: ResponseAccountState | Unset = UNSET
    bill_id: None | str | Unset = UNSET
    tax_id: None | str | Unset = UNSET
    tax_id_type: None | TaxIdType | Unset = UNSET
    conversion_rate: float | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        bill_status = self.bill_status.value

        usage_amount = self.usage_amount.to_dict()

        tax_amount = self.tax_amount.to_dict()

        total_amount = self.total_amount.to_dict()

        usages = []
        for usages_item_data in self.usages:
            usages_item = usages_item_data.to_dict()
            usages.append(usages_item)

        billing_address = self.billing_address.to_dict()

        roblox_address = self.roblox_address.to_dict()

        payments = []
        for payments_item_data in self.payments:
            payments_item = payments_item_data.to_dict()
            payments.append(payments_item)

        account_state: str | Unset = UNSET
        if not isinstance(self.account_state, Unset):
            account_state = self.account_state.value

        bill_id: None | str | Unset
        if isinstance(self.bill_id, Unset):
            bill_id = UNSET
        else:
            bill_id = self.bill_id

        tax_id: None | str | Unset
        if isinstance(self.tax_id, Unset):
            tax_id = UNSET
        else:
            tax_id = self.tax_id

        tax_id_type: None | str | Unset
        if isinstance(self.tax_id_type, Unset):
            tax_id_type = UNSET
        elif isinstance(self.tax_id_type, TaxIdType):
            tax_id_type = self.tax_id_type.value
        else:
            tax_id_type = self.tax_id_type

        conversion_rate: float | None | Unset
        if isinstance(self.conversion_rate, Unset):
            conversion_rate = UNSET
        else:
            conversion_rate = self.conversion_rate

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "billStatus": bill_status,
                "usageAmount": usage_amount,
                "taxAmount": tax_amount,
                "totalAmount": total_amount,
                "usages": usages,
                "billingAddress": billing_address,
                "robloxAddress": roblox_address,
                "payments": payments,
            }
        )
        if account_state is not UNSET:
            field_dict["accountState"] = account_state
        if bill_id is not UNSET:
            field_dict["billId"] = bill_id
        if tax_id is not UNSET:
            field_dict["taxId"] = tax_id
        if tax_id_type is not UNSET:
            field_dict["taxIdType"] = tax_id_type
        if conversion_rate is not UNSET:
            field_dict["conversionRate"] = conversion_rate

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.address import Address  # noqa: PLC0415
        from ..models.consumer_usage import ConsumerUsage  # noqa: PLC0415
        from ..models.payment import Payment  # noqa: PLC0415
        from ..models.service_efficiency_api_money import ServiceEfficiencyApiMoney  # noqa: PLC0415

        d = dict(src_dict)
        bill_status = BillStatus(d.pop("billStatus"))

        usage_amount = ServiceEfficiencyApiMoney.from_dict(d.pop("usageAmount"))

        tax_amount = ServiceEfficiencyApiMoney.from_dict(d.pop("taxAmount"))

        total_amount = ServiceEfficiencyApiMoney.from_dict(d.pop("totalAmount"))

        usages = []
        _usages = d.pop("usages")
        for usages_item_data in _usages:
            usages_item = ConsumerUsage.from_dict(usages_item_data)

            usages.append(usages_item)

        billing_address = Address.from_dict(d.pop("billingAddress"))

        roblox_address = Address.from_dict(d.pop("robloxAddress"))

        payments = []
        _payments = d.pop("payments")
        for payments_item_data in _payments:
            payments_item = Payment.from_dict(payments_item_data)

            payments.append(payments_item)

        _account_state = d.pop("accountState", UNSET)
        account_state: ResponseAccountState | Unset
        if isinstance(_account_state, Unset):
            account_state = UNSET
        else:
            account_state = ResponseAccountState(_account_state)

        def _parse_bill_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        bill_id = _parse_bill_id(d.pop("billId", UNSET))

        def _parse_tax_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tax_id = _parse_tax_id(d.pop("taxId", UNSET))

        def _parse_tax_id_type(data: object) -> None | TaxIdType | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                tax_id_type_type_1 = TaxIdType(data)

                return tax_id_type_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | TaxIdType | Unset, data)

        tax_id_type = _parse_tax_id_type(d.pop("taxIdType", UNSET))

        def _parse_conversion_rate(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        conversion_rate = _parse_conversion_rate(d.pop("conversionRate", UNSET))

        bill_details_response = cls(
            bill_status=bill_status,
            usage_amount=usage_amount,
            tax_amount=tax_amount,
            total_amount=total_amount,
            usages=usages,
            billing_address=billing_address,
            roblox_address=roblox_address,
            payments=payments,
            account_state=account_state,
            bill_id=bill_id,
            tax_id=tax_id,
            tax_id_type=tax_id_type,
            conversion_rate=conversion_rate,
        )

        return bill_details_response
