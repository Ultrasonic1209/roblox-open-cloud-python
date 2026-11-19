from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.marketplace_fiat_service_decimal import MarketplaceFiatServiceDecimal


T = TypeVar("T", bound="MarketplaceFiatServiceMoney")


@_attrs_define
class MarketplaceFiatServiceMoney:
    """Represents an amount of money with its currency type.

    Examples:
     - Five US dollars === `{currency_code: "USD" quantity: {significand: 5}}`

        Attributes:
            currency_code (None | str | Unset): A currency code.

                This may be a three-letter currency code defined in ISO 4217.

                APIs may define additional currency codes that are not included in the ISO
                4217 standard (for example, virtual currencies or cryptocurrencies). These
                must start with `X-`, in order to distinguish them from potential future
                ISO 4217 codes. For example, `"USD"` is the ISO 4217 code for United States
                dollar.
            quantity (MarketplaceFiatServiceDecimal | Unset): Represents a decimal number in a form similar to scientific
                notation.

                Examples:
                 - 17            === `{significand: 17   exponent: 0} (or just {significand:
                   17})`
                 - -0.005        === `{significand: -5   exponent: -3}`
                 - 33.5 million  === `{significand: 335  exponent: 5}`
                 - 11/8 (1.375)  === `{significand: 1375 exponent: -3}`

                Note that the range of a Decimal exceeds that of a JSON `number` (double), as
                well as that of a `decimal64`.
    """

    currency_code: None | str | Unset = UNSET
    quantity: MarketplaceFiatServiceDecimal | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        currency_code: None | str | Unset
        if isinstance(self.currency_code, Unset):
            currency_code = UNSET
        else:
            currency_code = self.currency_code

        quantity: dict[str, Any] | Unset = UNSET
        if not isinstance(self.quantity, Unset):
            quantity = self.quantity.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if currency_code is not UNSET:
            field_dict["currencyCode"] = currency_code
        if quantity is not UNSET:
            field_dict["quantity"] = quantity

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.marketplace_fiat_service_decimal import MarketplaceFiatServiceDecimal  # noqa: PLC0415

        d = dict(src_dict)

        def _parse_currency_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        currency_code = _parse_currency_code(d.pop("currencyCode", UNSET))

        _quantity = d.pop("quantity", UNSET)
        quantity: MarketplaceFiatServiceDecimal | Unset
        if isinstance(_quantity, Unset):
            quantity = UNSET
        else:
            quantity = MarketplaceFiatServiceDecimal.from_dict(_quantity)

        marketplace_fiat_service_money = cls(
            currency_code=currency_code,
            quantity=quantity,
        )

        return marketplace_fiat_service_money
