from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="PaymentProfile")


@_attrs_define
class PaymentProfile:
    """Service Efficiency representation of a Payment Profile.

    Attributes:
        payment_profile_id (None | str | Unset): Gets or sets the payment profile id.
        payment_profile_owner_type (None | str | Unset): Gets or sets the payment profile owner type. GROUP or USER.
        card_network (None | str | Unset): Gets or sets the card network.
        last_4_digits (None | str | Unset): Gets or sets the last four digits of the card.
        exp_month (int | None | Unset): Gets or sets the expiry month of the card.
        exp_year (int | None | Unset): Gets or sets the expiry year of the card.
    """

    payment_profile_id: None | str | Unset = UNSET
    payment_profile_owner_type: None | str | Unset = UNSET
    card_network: None | str | Unset = UNSET
    last_4_digits: None | str | Unset = UNSET
    exp_month: int | None | Unset = UNSET
    exp_year: int | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        payment_profile_id: None | str | Unset
        if isinstance(self.payment_profile_id, Unset):
            payment_profile_id = UNSET
        else:
            payment_profile_id = self.payment_profile_id

        payment_profile_owner_type: None | str | Unset
        if isinstance(self.payment_profile_owner_type, Unset):
            payment_profile_owner_type = UNSET
        else:
            payment_profile_owner_type = self.payment_profile_owner_type

        card_network: None | str | Unset
        if isinstance(self.card_network, Unset):
            card_network = UNSET
        else:
            card_network = self.card_network

        last_4_digits: None | str | Unset
        if isinstance(self.last_4_digits, Unset):
            last_4_digits = UNSET
        else:
            last_4_digits = self.last_4_digits

        exp_month: int | None | Unset
        if isinstance(self.exp_month, Unset):
            exp_month = UNSET
        else:
            exp_month = self.exp_month

        exp_year: int | None | Unset
        if isinstance(self.exp_year, Unset):
            exp_year = UNSET
        else:
            exp_year = self.exp_year

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if payment_profile_id is not UNSET:
            field_dict["paymentProfileId"] = payment_profile_id
        if payment_profile_owner_type is not UNSET:
            field_dict["paymentProfileOwnerType"] = payment_profile_owner_type
        if card_network is not UNSET:
            field_dict["cardNetwork"] = card_network
        if last_4_digits is not UNSET:
            field_dict["last4Digits"] = last_4_digits
        if exp_month is not UNSET:
            field_dict["expMonth"] = exp_month
        if exp_year is not UNSET:
            field_dict["expYear"] = exp_year

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}

        def _parse_payment_profile_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        payment_profile_id = _parse_payment_profile_id(d.pop("paymentProfileId", UNSET))

        def _parse_payment_profile_owner_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        payment_profile_owner_type = _parse_payment_profile_owner_type(d.pop("paymentProfileOwnerType", UNSET))

        def _parse_card_network(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        card_network = _parse_card_network(d.pop("cardNetwork", UNSET))

        def _parse_last_4_digits(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        last_4_digits = _parse_last_4_digits(d.pop("last4Digits", UNSET))

        def _parse_exp_month(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        exp_month = _parse_exp_month(d.pop("expMonth", UNSET))

        def _parse_exp_year(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        exp_year = _parse_exp_year(d.pop("expYear", UNSET))

        payment_profile = cls(
            payment_profile_id=payment_profile_id,
            payment_profile_owner_type=payment_profile_owner_type,
            card_network=card_network,
            last_4_digits=last_4_digits,
            exp_month=exp_month,
            exp_year=exp_year,
        )

        return payment_profile
