from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.payment_method_card_brand import PaymentMethodCardBrand
from ..models.payment_method_status import PaymentMethodStatus
from ..models.payment_method_type import PaymentMethodType
from ..models.payment_method_verification_state import PaymentMethodVerificationState
from ..types import UNSET, Unset

T = TypeVar("T", bound="PaymentMethod")


@_attrs_define
class PaymentMethod:
    """
    Attributes:
        display_label (str): Masked human-readable label (for example, `Visa ending in 4242`).
        id (str): The payment method ID.
        status (PaymentMethodStatus): The current status of the payment method. Can be `ACTIVE`, `ACTION_REQUIRED`,
            `EXPIRED`, or `DISABLED`.
        type_ (PaymentMethodType): The payment method category. Can be `CARD` or `INVOICE`.
        card_brand (PaymentMethodCardBrand | Unset):
        expiration_month (int | Unset): Card expiration month (1-12).
        expiration_year (int | Unset): Card expiration year (four-digit year).
        last_four_digits (str | Unset): Last four digits of the card.
        verification_state (PaymentMethodVerificationState | Unset): Card verification state, independent of expiration.
    """

    display_label: str
    id: str
    status: PaymentMethodStatus
    type_: PaymentMethodType
    card_brand: PaymentMethodCardBrand | Unset = UNSET
    expiration_month: int | Unset = UNSET
    expiration_year: int | Unset = UNSET
    last_four_digits: str | Unset = UNSET
    verification_state: PaymentMethodVerificationState | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        display_label = self.display_label

        id = self.id

        status = self.status.value

        type_ = self.type_.value

        card_brand: str | Unset = UNSET
        if not isinstance(self.card_brand, Unset):
            card_brand = self.card_brand.value

        expiration_month = self.expiration_month

        expiration_year = self.expiration_year

        last_four_digits = self.last_four_digits

        verification_state: str | Unset = UNSET
        if not isinstance(self.verification_state, Unset):
            verification_state = self.verification_state.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "displayLabel": display_label,
                "id": id,
                "status": status,
                "type": type_,
            }
        )
        if card_brand is not UNSET:
            field_dict["cardBrand"] = card_brand
        if expiration_month is not UNSET:
            field_dict["expirationMonth"] = expiration_month
        if expiration_year is not UNSET:
            field_dict["expirationYear"] = expiration_year
        if last_four_digits is not UNSET:
            field_dict["lastFourDigits"] = last_four_digits
        if verification_state is not UNSET:
            field_dict["verificationState"] = verification_state

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        display_label = d.pop("displayLabel")

        id = d.pop("id")

        status = PaymentMethodStatus(d.pop("status"))

        type_ = PaymentMethodType(d.pop("type"))

        _card_brand = d.pop("cardBrand", UNSET)
        card_brand: PaymentMethodCardBrand | Unset
        if isinstance(_card_brand, Unset):
            card_brand = UNSET
        else:
            card_brand = PaymentMethodCardBrand(_card_brand)

        expiration_month = d.pop("expirationMonth", UNSET)

        expiration_year = d.pop("expirationYear", UNSET)

        last_four_digits = d.pop("lastFourDigits", UNSET)

        _verification_state = d.pop("verificationState", UNSET)
        verification_state: PaymentMethodVerificationState | Unset
        if isinstance(_verification_state, Unset):
            verification_state = UNSET
        else:
            verification_state = PaymentMethodVerificationState(_verification_state)

        payment_method = cls(
            display_label=display_label,
            id=id,
            status=status,
            type_=type_,
            card_brand=card_brand,
            expiration_month=expiration_month,
            expiration_year=expiration_year,
            last_four_digits=last_four_digits,
            verification_state=verification_state,
        )

        payment_method.additional_properties = d
        return payment_method

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
