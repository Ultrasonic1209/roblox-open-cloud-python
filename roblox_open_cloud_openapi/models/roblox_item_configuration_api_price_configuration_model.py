from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxItemConfigurationApiPriceConfigurationModel")


@_attrs_define
class RobloxItemConfigurationApiPriceConfigurationModel:
    """Defines the configuration options for an items price.

    Attributes:
        price_in_robux (int | Unset): Gets or sets the standard price of the item in Robux.
        premium_discount_percentage (int | Unset): Gets or sets the discount rate on the price of the item that is given
            to premium users
            Should not be used while applying a PremiumPriceInRobux.
        premium_price_in_robux (int | Unset): Gets or sets the price of the item in Robux that applies only to premium
            users
            Should not be used while applying a PremiumDiscountPercentage.
        price_offset (int | Unset): Gets or sets the price offset of the item in Robux above the price floor.
    """

    price_in_robux: int | Unset = UNSET
    premium_discount_percentage: int | Unset = UNSET
    premium_price_in_robux: int | Unset = UNSET
    price_offset: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        price_in_robux = self.price_in_robux

        premium_discount_percentage = self.premium_discount_percentage

        premium_price_in_robux = self.premium_price_in_robux

        price_offset = self.price_offset

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if price_in_robux is not UNSET:
            field_dict["priceInRobux"] = price_in_robux
        if premium_discount_percentage is not UNSET:
            field_dict["premiumDiscountPercentage"] = premium_discount_percentage
        if premium_price_in_robux is not UNSET:
            field_dict["premiumPriceInRobux"] = premium_price_in_robux
        if price_offset is not UNSET:
            field_dict["priceOffset"] = price_offset

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        price_in_robux = d.pop("priceInRobux", UNSET)

        premium_discount_percentage = d.pop("premiumDiscountPercentage", UNSET)

        premium_price_in_robux = d.pop("premiumPriceInRobux", UNSET)

        price_offset = d.pop("priceOffset", UNSET)

        roblox_item_configuration_api_price_configuration_model = cls(
            price_in_robux=price_in_robux,
            premium_discount_percentage=premium_discount_percentage,
            premium_price_in_robux=premium_price_in_robux,
            price_offset=price_offset,
        )

        return roblox_item_configuration_api_price_configuration_model
