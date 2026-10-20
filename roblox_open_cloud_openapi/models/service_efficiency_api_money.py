from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="ServiceEfficiencyApiMoney")


@_attrs_define
class ServiceEfficiencyApiMoney:
    """Temporary until https://roblox.atlassian.net/browse/ICSC-1360 is done.
    Will be replaced by google.type.Money

        Attributes:
            currency_code (None | str | Unset): The three-letter currency code defined in ISO 4217.
            units (int | Unset): The whole units of the amount.
                For example if `currencyCode` is `"USD"`, then 1 unit is one US dollar.
            nanos (int | Unset): Number of nano (10^-9) units of the amount.
                The value must be between -999,999,999 and +999,999,999 inclusive.
                If `units` is positive, `nanos` must be positive or zero.
                If `units` is zero, `nanos` can be positive, zero, or negative.
                If `units` is negative, `nanos` must be negative or zero.
                For example $-1.75 is represented as `units`=-1 and `nanos`=-750,000,000.
    """

    currency_code: None | str | Unset = UNSET
    units: int | Unset = UNSET
    nanos: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        currency_code: None | str | Unset
        if isinstance(self.currency_code, Unset):
            currency_code = UNSET
        else:
            currency_code = self.currency_code

        units = self.units

        nanos = self.nanos

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if currency_code is not UNSET:
            field_dict["currencyCode"] = currency_code
        if units is not UNSET:
            field_dict["units"] = units
        if nanos is not UNSET:
            field_dict["nanos"] = nanos

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_currency_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        currency_code = _parse_currency_code(d.pop("currencyCode", UNSET))

        units = d.pop("units", UNSET)

        nanos = d.pop("nanos", UNSET)

        service_efficiency_api_money = cls(
            currency_code=currency_code,
            units=units,
            nanos=nanos,
        )

        return service_efficiency_api_money
