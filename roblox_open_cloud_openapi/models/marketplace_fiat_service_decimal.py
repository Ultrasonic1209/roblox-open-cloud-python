from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="MarketplaceFiatServiceDecimal")


@_attrs_define
class MarketplaceFiatServiceDecimal:
    """Represents a decimal number in a form similar to scientific notation.

    Examples:
     - 17            === `{significand: 17   exponent: 0} (or just {significand:
       17})`
     - -0.005        === `{significand: -5   exponent: -3}`
     - 33.5 million  === `{significand: 335  exponent: 5}`
     - 11/8 (1.375)  === `{significand: 1375 exponent: -3}`

    Note that the range of a Decimal exceeds that of a JSON `number` (double), as
    well as that of a `decimal64`.

        Attributes:
            significand (int | Unset): The significant digits of the number.
            exponent (int | Unset): Represents the position of the decimal point within the significand.

                When the exponent is 0, the value of the Decimal is simply the value of
                `significand`.

                When the exponent is greater than 0, represents the number of trailing
                zeroes after the significant digits.

                When the exponent is less than 0, represents how many of the significant
                digits (and implicit leading zeroes, as needed) come after the decmial
                point.
    """

    significand: int | Unset = UNSET
    exponent: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        significand = self.significand

        exponent = self.exponent

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if significand is not UNSET:
            field_dict["significand"] = significand
        if exponent is not UNSET:
            field_dict["exponent"] = exponent

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        significand = d.pop("significand", UNSET)

        exponent = d.pop("exponent", UNSET)

        marketplace_fiat_service_decimal = cls(
            significand=significand,
            exponent=exponent,
        )

        return marketplace_fiat_service_decimal
