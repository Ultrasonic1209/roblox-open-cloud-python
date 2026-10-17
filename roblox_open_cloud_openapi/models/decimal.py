from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Decimal")


@_attrs_define
class Decimal:
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
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        significand = self.significand

        exponent = self.exponent

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
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

        decimal = cls(
            significand=significand,
            exponent=exponent,
        )

        decimal.additional_properties = d
        return decimal

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
