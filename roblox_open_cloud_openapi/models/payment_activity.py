from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.payment_activity_ad_credit_transaction_type import PaymentActivityAdCreditTransactionType
from ..models.payment_activity_state import PaymentActivityState
from ..models.payment_activity_type import PaymentActivityType
from ..types import UNSET, Unset

T = TypeVar("T", bound="PaymentActivity")


@_attrs_define
class PaymentActivity:
    """
    Attributes:
        amount_micros (str): Amount actually charged, refunded, granted, or spent, in micro-USD.
        create_time (datetime.datetime): Creation timestamp as an RFC 3339 UTC string.
        state (PaymentActivityState): The settlement state (`PENDING`, `SUCCEEDED`, `FAILED`, or `REVERSED`).
        type_ (PaymentActivityType): The activity type (`CHARGE`, `REFUND`, `AD_CREDIT_GRANT`, `AD_CREDIT_SPEND`, or
            `ROBUX_CONVERSION`).
        actor_user_id (str | Unset): Roblox user who initiated the AD_CREDIT transaction, when available, for user and
            group accounts.
        ad_credit_transaction_type (PaymentActivityAdCreditTransactionType | Unset): Source transaction type for
            AD_CREDIT rows. The broader type remains available.
        campaign_id (str | Unset): Associated campaign ID, when applicable.
        campaign_name (str | Unset): Associated campaign name, present when campaignId is set.
        card_last_four_digits (str | Unset): Last four digits of the card used (`CHARGE` and `REFUND` only).
        charge_time (datetime.datetime | Unset): Latest associated card charge settlement timestamp as an RFC 3339 UTC
            string, when available (`CHARGE` only).
        currency_code (str | Unset): ISO 4217 currency of the card charge (`CHARGE` and `REFUND` only).
        description (str | Unset): Optional human-readable description.
        id (str | Unset): Stable payment identifier, when available. Absent for requests without a payment identifier.
        o_18_robux_amount (str | Unset): Portion of robuxAmount debited from 18+ eligible Robux (`ROBUX_CONVERSION`
            only).
        request_amount_micros (str | Unset): Amount originally requested, in micro-USD (`CHARGE` and `REFUND` only).
        robux_amount (str | Unset): Total Robux debited (`ROBUX_CONVERSION` only).
    """

    amount_micros: str
    create_time: datetime.datetime
    state: PaymentActivityState
    type_: PaymentActivityType
    actor_user_id: str | Unset = UNSET
    ad_credit_transaction_type: PaymentActivityAdCreditTransactionType | Unset = UNSET
    campaign_id: str | Unset = UNSET
    campaign_name: str | Unset = UNSET
    card_last_four_digits: str | Unset = UNSET
    charge_time: datetime.datetime | Unset = UNSET
    currency_code: str | Unset = UNSET
    description: str | Unset = UNSET
    id: str | Unset = UNSET
    o_18_robux_amount: str | Unset = UNSET
    request_amount_micros: str | Unset = UNSET
    robux_amount: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        amount_micros = self.amount_micros

        create_time = self.create_time.isoformat()

        state = self.state.value

        type_ = self.type_.value

        actor_user_id = self.actor_user_id

        ad_credit_transaction_type: str | Unset = UNSET
        if not isinstance(self.ad_credit_transaction_type, Unset):
            ad_credit_transaction_type = self.ad_credit_transaction_type.value

        campaign_id = self.campaign_id

        campaign_name = self.campaign_name

        card_last_four_digits = self.card_last_four_digits

        charge_time: str | Unset = UNSET
        if not isinstance(self.charge_time, Unset):
            charge_time = self.charge_time.isoformat()

        currency_code = self.currency_code

        description = self.description

        id = self.id

        o_18_robux_amount = self.o_18_robux_amount

        request_amount_micros = self.request_amount_micros

        robux_amount = self.robux_amount

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "amountMicros": amount_micros,
                "createTime": create_time,
                "state": state,
                "type": type_,
            }
        )
        if actor_user_id is not UNSET:
            field_dict["actorUserId"] = actor_user_id
        if ad_credit_transaction_type is not UNSET:
            field_dict["adCreditTransactionType"] = ad_credit_transaction_type
        if campaign_id is not UNSET:
            field_dict["campaignId"] = campaign_id
        if campaign_name is not UNSET:
            field_dict["campaignName"] = campaign_name
        if card_last_four_digits is not UNSET:
            field_dict["cardLastFourDigits"] = card_last_four_digits
        if charge_time is not UNSET:
            field_dict["chargeTime"] = charge_time
        if currency_code is not UNSET:
            field_dict["currencyCode"] = currency_code
        if description is not UNSET:
            field_dict["description"] = description
        if id is not UNSET:
            field_dict["id"] = id
        if o_18_robux_amount is not UNSET:
            field_dict["o18RobuxAmount"] = o_18_robux_amount
        if request_amount_micros is not UNSET:
            field_dict["requestAmountMicros"] = request_amount_micros
        if robux_amount is not UNSET:
            field_dict["robuxAmount"] = robux_amount

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        amount_micros = d.pop("amountMicros")

        create_time = datetime.datetime.fromisoformat(d.pop("createTime"))

        state = PaymentActivityState(d.pop("state"))

        type_ = PaymentActivityType(d.pop("type"))

        actor_user_id = d.pop("actorUserId", UNSET)

        _ad_credit_transaction_type = d.pop("adCreditTransactionType", UNSET)
        ad_credit_transaction_type: PaymentActivityAdCreditTransactionType | Unset
        if isinstance(_ad_credit_transaction_type, Unset):
            ad_credit_transaction_type = UNSET
        else:
            ad_credit_transaction_type = PaymentActivityAdCreditTransactionType(_ad_credit_transaction_type)

        campaign_id = d.pop("campaignId", UNSET)

        campaign_name = d.pop("campaignName", UNSET)

        card_last_four_digits = d.pop("cardLastFourDigits", UNSET)

        _charge_time = d.pop("chargeTime", UNSET)
        charge_time: datetime.datetime | Unset
        if isinstance(_charge_time, Unset):
            charge_time = UNSET
        else:
            charge_time = datetime.datetime.fromisoformat(_charge_time)

        currency_code = d.pop("currencyCode", UNSET)

        description = d.pop("description", UNSET)

        id = d.pop("id", UNSET)

        o_18_robux_amount = d.pop("o18RobuxAmount", UNSET)

        request_amount_micros = d.pop("requestAmountMicros", UNSET)

        robux_amount = d.pop("robuxAmount", UNSET)

        payment_activity = cls(
            amount_micros=amount_micros,
            create_time=create_time,
            state=state,
            type_=type_,
            actor_user_id=actor_user_id,
            ad_credit_transaction_type=ad_credit_transaction_type,
            campaign_id=campaign_id,
            campaign_name=campaign_name,
            card_last_four_digits=card_last_four_digits,
            charge_time=charge_time,
            currency_code=currency_code,
            description=description,
            id=id,
            o_18_robux_amount=o_18_robux_amount,
            request_amount_micros=request_amount_micros,
            robux_amount=robux_amount,
        )

        payment_activity.additional_properties = d
        return payment_activity

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
