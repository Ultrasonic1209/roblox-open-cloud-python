from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.billing_account_payment_status import BillingAccountPaymentStatus
from ..models.billing_account_payment_status_reason import BillingAccountPaymentStatusReason
from ..models.billing_account_status import BillingAccountStatus
from ..models.billing_account_supported_payment_types_item import BillingAccountSupportedPaymentTypesItem
from ..models.billing_account_type import BillingAccountType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ads_management_api_creator import AdsManagementApiCreator
    from ..models.billing_account_limits import BillingAccountLimits
    from ..models.payment_method import PaymentMethod


T = TypeVar("T", bound="BillingAccount")


@_attrs_define
class BillingAccount:
    """
    Attributes:
        ad_credit_balance_micros (str | Unset): Available ad credit balance in micro-USD, as a decimal string.
        create_time (datetime.datetime | Unset): The time the account was created, as an RFC 3339 UTC timestamp.
        creator (AdsManagementApiCreator | Unset):
        display_name (str | Unset): The human-readable name of the account.
        failed_payment_balance_micros (str | Unset): Total of failed credit card charges in micro-USD, as a decimal
            string.
        id (str | Unset): The unique identifier of the billing account. Use it as the {id} path parameter.
        limits (BillingAccountLimits | Unset):
        organization_id (str | Unset): The identifier of the organization that owns the account.
        outstanding_balance_micros (str | Unset): Unbilled credit card spend in micro-USD, as a decimal string.
        payment_methods (list[PaymentMethod] | Unset): Masked payment methods on file. Read-only; cards are added and
            updated in Ads Manager.
        payment_setup_url (str | Unset): Ads Manager page to add a payment method, buy ad credit, or resolve a failed
            payment. On a READY account
            it is informational: offer it, but do not stop for it. When paymentStatus is ACTION_REQUIRED or PAST_DUE,
            show it to the user and check again after they say they are done. Omitted when no setup applies and for
            disabled accounts. Never collect payment details through the API or in chat.
        payment_status (BillingAccountPaymentStatus | Unset): Whether the account can fund a new campaign. Can be
            `READY`, `ACTION_REQUIRED`, `PAST_DUE`, or `DISABLED`.
            READY means at least one payment type in supportedPaymentTypes can fund a campaign. ACTION_REQUIRED
            means no payment type can. PAST_DUE means a card payment failed or a failed charge is unpaid; create
            succeeds only with a payment type listed in supportedPaymentTypes, which can be empty. DISABLED accounts
            list no payment types.
        payment_status_reason (BillingAccountPaymentStatusReason | Unset): Machine-readable reason for a paymentStatus
            other than READY. NO_PAYMENT_METHOD means that no payment type
            can fund a campaign: no usable card and no usable ad credit. A group's account can pay only with ad credit,
            so for a group it means the ad credit balance is below the minimum daily budget; buy ad credit with
            paymentSetupUrl. PROFILE_NOT_VERIFIED means the same, but a card exists and needs verification.
        status (BillingAccountStatus | Unset): The current state of the account. Can be `ACTIVE`, `DISABLED`, or
            `ARCHIVED`.
        supported_payment_types (list[BillingAccountSupportedPaymentTypesItem] | Unset): Campaign payment types that can
            fund a new campaign now. CREDIT_CARD needs a verified card and a daily
            spend limit (limits.maximumDailyBudgetMicros) of at least the minimum daily budget. ADS_CREDIT
            needs activated ad credit with a balance of at least the minimum daily budget. Create also checks that
            the ad credit balance covers the campaign's daily budget. Group accounts can use only ADS_CREDIT.
        time_zone (str | Unset): The IANA time zone the account's reporting dates and budget schedules are
            interpreted in. Example: `America/Los_Angeles`.
        type_ (BillingAccountType | Unset): The account category. External advertisers are always SELF_SERVICE; MANAGED
            and
            INTERNAL are Roblox-operated accounts. Can be `SELF_SERVICE`, `MANAGED`, or `INTERNAL`.
        update_time (datetime.datetime | Unset): The time the account was last updated, as an RFC 3339 UTC timestamp.
    """

    ad_credit_balance_micros: str | Unset = UNSET
    create_time: datetime.datetime | Unset = UNSET
    creator: AdsManagementApiCreator | Unset = UNSET
    display_name: str | Unset = UNSET
    failed_payment_balance_micros: str | Unset = UNSET
    id: str | Unset = UNSET
    limits: BillingAccountLimits | Unset = UNSET
    organization_id: str | Unset = UNSET
    outstanding_balance_micros: str | Unset = UNSET
    payment_methods: list[PaymentMethod] | Unset = UNSET
    payment_setup_url: str | Unset = UNSET
    payment_status: BillingAccountPaymentStatus | Unset = UNSET
    payment_status_reason: BillingAccountPaymentStatusReason | Unset = UNSET
    status: BillingAccountStatus | Unset = UNSET
    supported_payment_types: list[BillingAccountSupportedPaymentTypesItem] | Unset = UNSET
    time_zone: str | Unset = UNSET
    type_: BillingAccountType | Unset = UNSET
    update_time: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ad_credit_balance_micros = self.ad_credit_balance_micros

        create_time: str | Unset = UNSET
        if not isinstance(self.create_time, Unset):
            create_time = self.create_time.isoformat()

        creator: dict[str, Any] | Unset = UNSET
        if not isinstance(self.creator, Unset):
            creator = self.creator.to_dict()

        display_name = self.display_name

        failed_payment_balance_micros = self.failed_payment_balance_micros

        id = self.id

        limits: dict[str, Any] | Unset = UNSET
        if not isinstance(self.limits, Unset):
            limits = self.limits.to_dict()

        organization_id = self.organization_id

        outstanding_balance_micros = self.outstanding_balance_micros

        payment_methods: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.payment_methods, Unset):
            payment_methods = []
            for payment_methods_item_data in self.payment_methods:
                payment_methods_item = payment_methods_item_data.to_dict()
                payment_methods.append(payment_methods_item)

        payment_setup_url = self.payment_setup_url

        payment_status: str | Unset = UNSET
        if not isinstance(self.payment_status, Unset):
            payment_status = self.payment_status.value

        payment_status_reason: str | Unset = UNSET
        if not isinstance(self.payment_status_reason, Unset):
            payment_status_reason = self.payment_status_reason.value

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        supported_payment_types: list[str] | Unset = UNSET
        if not isinstance(self.supported_payment_types, Unset):
            supported_payment_types = []
            for supported_payment_types_item_data in self.supported_payment_types:
                supported_payment_types_item = supported_payment_types_item_data.value
                supported_payment_types.append(supported_payment_types_item)

        time_zone = self.time_zone

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        update_time: str | Unset = UNSET
        if not isinstance(self.update_time, Unset):
            update_time = self.update_time.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ad_credit_balance_micros is not UNSET:
            field_dict["adCreditBalanceMicros"] = ad_credit_balance_micros
        if create_time is not UNSET:
            field_dict["createTime"] = create_time
        if creator is not UNSET:
            field_dict["creator"] = creator
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if failed_payment_balance_micros is not UNSET:
            field_dict["failedPaymentBalanceMicros"] = failed_payment_balance_micros
        if id is not UNSET:
            field_dict["id"] = id
        if limits is not UNSET:
            field_dict["limits"] = limits
        if organization_id is not UNSET:
            field_dict["organizationId"] = organization_id
        if outstanding_balance_micros is not UNSET:
            field_dict["outstandingBalanceMicros"] = outstanding_balance_micros
        if payment_methods is not UNSET:
            field_dict["paymentMethods"] = payment_methods
        if payment_setup_url is not UNSET:
            field_dict["paymentSetupUrl"] = payment_setup_url
        if payment_status is not UNSET:
            field_dict["paymentStatus"] = payment_status
        if payment_status_reason is not UNSET:
            field_dict["paymentStatusReason"] = payment_status_reason
        if status is not UNSET:
            field_dict["status"] = status
        if supported_payment_types is not UNSET:
            field_dict["supportedPaymentTypes"] = supported_payment_types
        if time_zone is not UNSET:
            field_dict["timeZone"] = time_zone
        if type_ is not UNSET:
            field_dict["type"] = type_
        if update_time is not UNSET:
            field_dict["updateTime"] = update_time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ads_management_api_creator import AdsManagementApiCreator  # noqa: PLC0415
        from ..models.billing_account_limits import BillingAccountLimits  # noqa: PLC0415
        from ..models.payment_method import PaymentMethod  # noqa: PLC0415

        d = dict(src_dict)
        ad_credit_balance_micros = d.pop("adCreditBalanceMicros", UNSET)

        _create_time = d.pop("createTime", UNSET)
        create_time: datetime.datetime | Unset
        if isinstance(_create_time, Unset):
            create_time = UNSET
        else:
            create_time = datetime.datetime.fromisoformat(_create_time)

        _creator = d.pop("creator", UNSET)
        creator: AdsManagementApiCreator | Unset
        if isinstance(_creator, Unset):
            creator = UNSET
        else:
            creator = AdsManagementApiCreator.from_dict(_creator)

        display_name = d.pop("displayName", UNSET)

        failed_payment_balance_micros = d.pop("failedPaymentBalanceMicros", UNSET)

        id = d.pop("id", UNSET)

        _limits = d.pop("limits", UNSET)
        limits: BillingAccountLimits | Unset
        if isinstance(_limits, Unset):
            limits = UNSET
        else:
            limits = BillingAccountLimits.from_dict(_limits)

        organization_id = d.pop("organizationId", UNSET)

        outstanding_balance_micros = d.pop("outstandingBalanceMicros", UNSET)

        _payment_methods = d.pop("paymentMethods", UNSET)
        payment_methods: list[PaymentMethod] | Unset = UNSET
        if _payment_methods is not UNSET:
            payment_methods = []
            for payment_methods_item_data in _payment_methods:
                payment_methods_item = PaymentMethod.from_dict(payment_methods_item_data)

                payment_methods.append(payment_methods_item)

        payment_setup_url = d.pop("paymentSetupUrl", UNSET)

        _payment_status = d.pop("paymentStatus", UNSET)
        payment_status: BillingAccountPaymentStatus | Unset
        if isinstance(_payment_status, Unset):
            payment_status = UNSET
        else:
            payment_status = BillingAccountPaymentStatus(_payment_status)

        _payment_status_reason = d.pop("paymentStatusReason", UNSET)
        payment_status_reason: BillingAccountPaymentStatusReason | Unset
        if isinstance(_payment_status_reason, Unset):
            payment_status_reason = UNSET
        else:
            payment_status_reason = BillingAccountPaymentStatusReason(_payment_status_reason)

        _status = d.pop("status", UNSET)
        status: BillingAccountStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = BillingAccountStatus(_status)

        _supported_payment_types = d.pop("supportedPaymentTypes", UNSET)
        supported_payment_types: list[BillingAccountSupportedPaymentTypesItem] | Unset = UNSET
        if _supported_payment_types is not UNSET:
            supported_payment_types = []
            for supported_payment_types_item_data in _supported_payment_types:
                supported_payment_types_item = BillingAccountSupportedPaymentTypesItem(
                    supported_payment_types_item_data
                )

                supported_payment_types.append(supported_payment_types_item)

        time_zone = d.pop("timeZone", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: BillingAccountType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = BillingAccountType(_type_)

        _update_time = d.pop("updateTime", UNSET)
        update_time: datetime.datetime | Unset
        if isinstance(_update_time, Unset):
            update_time = UNSET
        else:
            update_time = datetime.datetime.fromisoformat(_update_time)

        billing_account = cls(
            ad_credit_balance_micros=ad_credit_balance_micros,
            create_time=create_time,
            creator=creator,
            display_name=display_name,
            failed_payment_balance_micros=failed_payment_balance_micros,
            id=id,
            limits=limits,
            organization_id=organization_id,
            outstanding_balance_micros=outstanding_balance_micros,
            payment_methods=payment_methods,
            payment_setup_url=payment_setup_url,
            payment_status=payment_status,
            payment_status_reason=payment_status_reason,
            status=status,
            supported_payment_types=supported_payment_types,
            time_zone=time_zone,
            type_=type_,
            update_time=update_time,
        )

        billing_account.additional_properties = d
        return billing_account

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
