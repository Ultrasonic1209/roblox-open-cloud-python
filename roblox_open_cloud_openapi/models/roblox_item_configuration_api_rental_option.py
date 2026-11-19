from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxItemConfigurationApiRentalOption")


@_attrs_define
class RobloxItemConfigurationApiRentalOption:
    """Rental options for a collectible item.

    Attributes:
        rental_days (int | Unset): The duration of the rental in days. null is the permanent purchase price.
        price_in_robux (int | Unset): The price of the rental in Robux.
    """

    rental_days: int | Unset = UNSET
    price_in_robux: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        rental_days = self.rental_days

        price_in_robux = self.price_in_robux

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if rental_days is not UNSET:
            field_dict["rentalDays"] = rental_days
        if price_in_robux is not UNSET:
            field_dict["priceInRobux"] = price_in_robux

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        rental_days = d.pop("rentalDays", UNSET)

        price_in_robux = d.pop("priceInRobux", UNSET)

        roblox_item_configuration_api_rental_option = cls(
            rental_days=rental_days,
            price_in_robux=price_in_robux,
        )

        return roblox_item_configuration_api_rental_option
