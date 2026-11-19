from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxItemConfigurationApiRegionalPrice")


@_attrs_define
class RobloxItemConfigurationApiRegionalPrice:
    """Defines a country and its regional price.

    Attributes:
        price_in_robux (int | Unset): The price in the country in robux.
        country_iso_2_code (str | Unset): The ISO2 code of the country.
    """

    price_in_robux: int | Unset = UNSET
    country_iso_2_code: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        price_in_robux = self.price_in_robux

        country_iso_2_code = self.country_iso_2_code

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if price_in_robux is not UNSET:
            field_dict["priceInRobux"] = price_in_robux
        if country_iso_2_code is not UNSET:
            field_dict["countryIso2Code"] = country_iso_2_code

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        price_in_robux = d.pop("priceInRobux", UNSET)

        country_iso_2_code = d.pop("countryIso2Code", UNSET)

        roblox_item_configuration_api_regional_price = cls(
            price_in_robux=price_in_robux,
            country_iso_2_code=country_iso_2_code,
        )

        return roblox_item_configuration_api_regional_price
