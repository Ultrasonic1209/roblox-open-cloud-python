from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.decimal import Decimal


T = TypeVar("T", bound="Money")


@_attrs_define
class Money:
    """Represents an amount of money with its currency type.

    Examples:
     - Five US dollars === `{currency_code: "USD" quantity: {significand: 5}}`

        Attributes:
            currency_code (str | Unset): A currency code.

                This may be a three-letter currency code defined in ISO 4217.

                APIs may define additional currency codes that are not included in the ISO
                4217 standard (for example, virtual currencies or cryptocurrencies). These
                must start with `X-`, in order to distinguish them from potential future
                ISO 4217 codes. For example, `"USD"` is the ISO 4217 code for United States
                dollar.
            quantity (Decimal | Unset): Represents a decimal number in a form similar to scientific notation.

                Examples:
                 - 17            === `{significand: 17   exponent: 0} (or just {significand:
                   17})`
                 - -0.005        === `{significand: -5   exponent: -3}`
                 - 33.5 million  === `{significand: 335  exponent: 5}`
                 - 11/8 (1.375)  === `{significand: 1375 exponent: -3}`

                Note that the range of a Decimal exceeds that of a JSON `number` (double), as
                well as that of a `decimal64`.
    """

    currency_code: str | Unset = UNSET
    quantity: Decimal | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        currency_code = self.currency_code

        quantity: dict[str, Any] | Unset = UNSET
        if not isinstance(self.quantity, Unset):
            quantity = self.quantity.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if currency_code is not UNSET:
            field_dict["currencyCode"] = currency_code
        if quantity is not UNSET:
            field_dict["quantity"] = quantity

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.decimal import Decimal

        d = dict(src_dict)
        currency_code = d.pop("currencyCode", UNSET)

        _quantity = d.pop("quantity", UNSET)
        quantity: Decimal | Unset
        if isinstance(_quantity, Unset):
            quantity = UNSET
        else:
            quantity = Decimal.from_dict(_quantity)

        money = cls(
            currency_code=currency_code,
            quantity=quantity,
        )

        money.additional_properties = d
        return money

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
