from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.response_account_state import ResponseAccountState
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bill_summary import BillSummary
    from ..models.service_efficiency_api_money import ServiceEfficiencyApiMoney


T = TypeVar("T", bound="BillingActivitiesResponse")


@_attrs_define
class BillingActivitiesResponse:
    """Response object for Billing Activities request.

    Attributes:
        current_balance (ServiceEfficiencyApiMoney): Temporary until https://roblox.atlassian.net/browse/ICSC-1360 is
            done.
            Will be replaced by google.type.Money
        month_to_date_balance (ServiceEfficiencyApiMoney): Temporary until https://roblox.atlassian.net/browse/ICSC-1360
            is done.
            Will be replaced by google.type.Money
        charging_threshold (ServiceEfficiencyApiMoney): Temporary until https://roblox.atlassian.net/browse/ICSC-1360 is
            done.
            Will be replaced by google.type.Money
        account_state (ResponseAccountState | Unset): Account State in the HTTP response.
        bill_summaries (list[BillSummary] | None | Unset): Gets or sets the list of account bill summaries.
    """

    current_balance: ServiceEfficiencyApiMoney
    month_to_date_balance: ServiceEfficiencyApiMoney
    charging_threshold: ServiceEfficiencyApiMoney
    account_state: ResponseAccountState | Unset = UNSET
    bill_summaries: list[BillSummary] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        current_balance = self.current_balance.to_dict()

        month_to_date_balance = self.month_to_date_balance.to_dict()

        charging_threshold = self.charging_threshold.to_dict()

        account_state: str | Unset = UNSET
        if not isinstance(self.account_state, Unset):
            account_state = self.account_state.value

        bill_summaries: list[dict[str, Any]] | None | Unset
        if isinstance(self.bill_summaries, Unset):
            bill_summaries = UNSET
        elif isinstance(self.bill_summaries, list):
            bill_summaries = []
            for bill_summaries_type_0_item_data in self.bill_summaries:
                bill_summaries_type_0_item = bill_summaries_type_0_item_data.to_dict()
                bill_summaries.append(bill_summaries_type_0_item)

        else:
            bill_summaries = self.bill_summaries

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "currentBalance": current_balance,
                "monthToDateBalance": month_to_date_balance,
                "chargingThreshold": charging_threshold,
            }
        )
        if account_state is not UNSET:
            field_dict["accountState"] = account_state
        if bill_summaries is not UNSET:
            field_dict["billSummaries"] = bill_summaries

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bill_summary import BillSummary  # noqa: PLC0415
        from ..models.service_efficiency_api_money import ServiceEfficiencyApiMoney  # noqa: PLC0415

        d = dict(src_dict)
        current_balance = ServiceEfficiencyApiMoney.from_dict(d.pop("currentBalance"))

        month_to_date_balance = ServiceEfficiencyApiMoney.from_dict(d.pop("monthToDateBalance"))

        charging_threshold = ServiceEfficiencyApiMoney.from_dict(d.pop("chargingThreshold"))

        _account_state = d.pop("accountState", UNSET)
        account_state: ResponseAccountState | Unset
        if isinstance(_account_state, Unset):
            account_state = UNSET
        else:
            account_state = ResponseAccountState(_account_state)

        def _parse_bill_summaries(data: object) -> list[BillSummary] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                bill_summaries_type_0 = []
                _bill_summaries_type_0 = data
                for bill_summaries_type_0_item_data in _bill_summaries_type_0:
                    bill_summaries_type_0_item = BillSummary.from_dict(bill_summaries_type_0_item_data)

                    bill_summaries_type_0.append(bill_summaries_type_0_item)

                return bill_summaries_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[BillSummary] | None | Unset, data)

        bill_summaries = _parse_bill_summaries(d.pop("billSummaries", UNSET))

        billing_activities_response = cls(
            current_balance=current_balance,
            month_to_date_balance=month_to_date_balance,
            charging_threshold=charging_threshold,
            account_state=account_state,
            bill_summaries=bill_summaries,
        )

        return billing_activities_response
