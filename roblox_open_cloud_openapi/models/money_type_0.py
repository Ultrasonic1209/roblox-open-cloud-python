from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.decimal_type_0 import DecimalType0


T = TypeVar("T", bound="MoneyType0")


@_attrs_define
class MoneyType0:
    """
    Attributes:
        currency_code (None | str | Unset):
        quantity (DecimalType0 | None | Unset):
    """

    currency_code: None | str | Unset = UNSET
    quantity: DecimalType0 | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.decimal_type_0 import DecimalType0  # noqa: PLC0415

        currency_code: None | str | Unset
        if isinstance(self.currency_code, Unset):
            currency_code = UNSET
        else:
            currency_code = self.currency_code

        quantity: dict[str, Any] | None | Unset
        if isinstance(self.quantity, Unset):
            quantity = UNSET
        elif isinstance(self.quantity, DecimalType0):
            quantity = self.quantity.to_dict()
        else:
            quantity = self.quantity

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if currency_code is not UNSET:
            field_dict["currencyCode"] = currency_code
        if quantity is not UNSET:
            field_dict["quantity"] = quantity

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.decimal_type_0 import DecimalType0  # noqa: PLC0415

        d = dict(src_dict)

        def _parse_currency_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        currency_code = _parse_currency_code(d.pop("currencyCode", UNSET))

        def _parse_quantity(data: object) -> DecimalType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_decimal_type_0 = DecimalType0.from_dict(data)

                return componentsschemas_decimal_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DecimalType0 | None | Unset, data)

        quantity = _parse_quantity(d.pop("quantity", UNSET))

        money_type_0 = cls(
            currency_code=currency_code,
            quantity=quantity,
        )

        return money_type_0
