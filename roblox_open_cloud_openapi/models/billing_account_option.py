from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.billing_account_option_payment_status import BillingAccountOptionPaymentStatus
from ..models.billing_account_option_payment_status_reason import BillingAccountOptionPaymentStatusReason
from ..models.billing_account_option_payment_types_item import BillingAccountOptionPaymentTypesItem
from ..models.billing_account_option_status import BillingAccountOptionStatus
from ..models.billing_account_option_type import BillingAccountOptionType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ads_management_api_creator import AdsManagementApiCreator


T = TypeVar("T", bound="BillingAccountOption")


@_attrs_define
class BillingAccountOption:
    """
    Attributes:
        creator (AdsManagementApiCreator):
        display_name (str): The human-readable name of the account.
        id (str): The billing account ID. Pass it as billingAccountId when creating a campaign.
        payment_types (list[BillingAccountOptionPaymentTypesItem]): The payment types that can fund a new campaign in
            this account now. This
            matches supportedPaymentTypes on GET /billing-accounts/{id}: CREDIT_CARD needs a
            verified card and a daily spend limit of at least the minimum daily budget, ADS_CREDIT needs activated ad credit
            with at least the minimum daily
            budget, and a group's account can use only ADS_CREDIT. `INVOICE` is for a managed account.
        status (BillingAccountOptionStatus): The current state of the account. Can be `ACTIVE`, `DISABLED`, or
            `ARCHIVED`.
        type_ (BillingAccountOptionType): The account category. Can be `SELF_SERVICE`, `MANAGED`, or `INTERNAL`.
        maximum_daily_budget_micros (str | Unset): The maximum daily budget for CREDIT_CARD campaigns in this account,
            in micro-USD.
            A non-positive value means no positive CREDIT_CARD budget is allowed.
            For LIFETIME, multiply by the schedule's number of days.
            Omitted when no verified card bills the account. Returned even when it is too low
            for CREDIT_CARD to be usable. Does not limit ADS_CREDIT or INVOICE campaigns.
        payment_setup_url (str | Unset): Ads Manager page to add a payment method, buy ad credit, or resolve a failed
            payment. Informational on a READY account.
            Same as on GET /billing-accounts/{id}. Never collect payment details in chat.
        payment_status (BillingAccountOptionPaymentStatus | Unset): Whether the account can fund a new campaign: READY,
            ACTION_REQUIRED, PAST_DUE, or DISABLED. Same as on GET /billing-accounts/{id}.
        payment_status_reason (BillingAccountOptionPaymentStatusReason | Unset): Reason for a paymentStatus other than
            READY. Same as on GET /billing-accounts/{id}. For a group's account,
            NO_PAYMENT_METHOD means that its ad credit balance is too low, not that a payment method is missing.
    """

    creator: AdsManagementApiCreator
    display_name: str
    id: str
    payment_types: list[BillingAccountOptionPaymentTypesItem]
    status: BillingAccountOptionStatus
    type_: BillingAccountOptionType
    maximum_daily_budget_micros: str | Unset = UNSET
    payment_setup_url: str | Unset = UNSET
    payment_status: BillingAccountOptionPaymentStatus | Unset = UNSET
    payment_status_reason: BillingAccountOptionPaymentStatusReason | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        creator = self.creator.to_dict()

        display_name = self.display_name

        id = self.id

        payment_types = []
        for payment_types_item_data in self.payment_types:
            payment_types_item = payment_types_item_data.value
            payment_types.append(payment_types_item)

        status = self.status.value

        type_ = self.type_.value

        maximum_daily_budget_micros = self.maximum_daily_budget_micros

        payment_setup_url = self.payment_setup_url

        payment_status: str | Unset = UNSET
        if not isinstance(self.payment_status, Unset):
            payment_status = self.payment_status.value

        payment_status_reason: str | Unset = UNSET
        if not isinstance(self.payment_status_reason, Unset):
            payment_status_reason = self.payment_status_reason.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "creator": creator,
                "displayName": display_name,
                "id": id,
                "paymentTypes": payment_types,
                "status": status,
                "type": type_,
            }
        )
        if maximum_daily_budget_micros is not UNSET:
            field_dict["maximumDailyBudgetMicros"] = maximum_daily_budget_micros
        if payment_setup_url is not UNSET:
            field_dict["paymentSetupUrl"] = payment_setup_url
        if payment_status is not UNSET:
            field_dict["paymentStatus"] = payment_status
        if payment_status_reason is not UNSET:
            field_dict["paymentStatusReason"] = payment_status_reason

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ads_management_api_creator import AdsManagementApiCreator  # noqa: PLC0415

        d = dict(src_dict)
        creator = AdsManagementApiCreator.from_dict(d.pop("creator"))

        display_name = d.pop("displayName")

        id = d.pop("id")

        payment_types = []
        _payment_types = d.pop("paymentTypes")
        for payment_types_item_data in _payment_types:
            payment_types_item = BillingAccountOptionPaymentTypesItem(payment_types_item_data)

            payment_types.append(payment_types_item)

        status = BillingAccountOptionStatus(d.pop("status"))

        type_ = BillingAccountOptionType(d.pop("type"))

        maximum_daily_budget_micros = d.pop("maximumDailyBudgetMicros", UNSET)

        payment_setup_url = d.pop("paymentSetupUrl", UNSET)

        _payment_status = d.pop("paymentStatus", UNSET)
        payment_status: BillingAccountOptionPaymentStatus | Unset
        if isinstance(_payment_status, Unset):
            payment_status = UNSET
        else:
            payment_status = BillingAccountOptionPaymentStatus(_payment_status)

        _payment_status_reason = d.pop("paymentStatusReason", UNSET)
        payment_status_reason: BillingAccountOptionPaymentStatusReason | Unset
        if isinstance(_payment_status_reason, Unset):
            payment_status_reason = UNSET
        else:
            payment_status_reason = BillingAccountOptionPaymentStatusReason(_payment_status_reason)

        billing_account_option = cls(
            creator=creator,
            display_name=display_name,
            id=id,
            payment_types=payment_types,
            status=status,
            type_=type_,
            maximum_daily_budget_micros=maximum_daily_budget_micros,
            payment_setup_url=payment_setup_url,
            payment_status=payment_status,
            payment_status_reason=payment_status_reason,
        )

        billing_account_option.additional_properties = d
        return billing_account_option

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
