from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxCatalogApiPremiumPricingModel")


@_attrs_define
class RobloxCatalogApiPremiumPricingModel:
    """Defines the Premium pricing for a catalog item.

    Attributes:
        premium_discount_percentage (int | Unset): The Premium discount percentage for a catalog item.
        premium_price_in_robux (int | Unset): The Premium price for a catalog item.
    """

    premium_discount_percentage: int | Unset = UNSET
    premium_price_in_robux: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        premium_discount_percentage = self.premium_discount_percentage

        premium_price_in_robux = self.premium_price_in_robux

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if premium_discount_percentage is not UNSET:
            field_dict["premiumDiscountPercentage"] = premium_discount_percentage
        if premium_price_in_robux is not UNSET:
            field_dict["premiumPriceInRobux"] = premium_price_in_robux

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        premium_discount_percentage = d.pop("premiumDiscountPercentage", UNSET)

        premium_price_in_robux = d.pop("premiumPriceInRobux", UNSET)

        roblox_catalog_api_premium_pricing_model = cls(
            premium_discount_percentage=premium_discount_percentage,
            premium_price_in_robux=premium_price_in_robux,
        )

        return roblox_catalog_api_premium_pricing_model
