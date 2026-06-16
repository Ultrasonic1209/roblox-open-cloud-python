from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_catalog_api_discount import RobloxCatalogApiDiscount


T = TypeVar("T", bound="RobloxCatalogApiDiscountInformation")


@_attrs_define
class RobloxCatalogApiDiscountInformation:
    """
    Attributes:
        original_price (int | Unset):
        total_discount_percentage (float | Unset):
        total_discount_amount (int | Unset):
        discounts (list[RobloxCatalogApiDiscount] | Unset):
    """

    original_price: int | Unset = UNSET
    total_discount_percentage: float | Unset = UNSET
    total_discount_amount: int | Unset = UNSET
    discounts: list[RobloxCatalogApiDiscount] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        original_price = self.original_price

        total_discount_percentage = self.total_discount_percentage

        total_discount_amount = self.total_discount_amount

        discounts: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.discounts, Unset):
            discounts = []
            for discounts_item_data in self.discounts:
                discounts_item = discounts_item_data.to_dict()
                discounts.append(discounts_item)

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if original_price is not UNSET:
            field_dict["originalPrice"] = original_price
        if total_discount_percentage is not UNSET:
            field_dict["totalDiscountPercentage"] = total_discount_percentage
        if total_discount_amount is not UNSET:
            field_dict["totalDiscountAmount"] = total_discount_amount
        if discounts is not UNSET:
            field_dict["discounts"] = discounts

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_catalog_api_discount import RobloxCatalogApiDiscount

        d = dict(src_dict)
        original_price = d.pop("originalPrice", UNSET)

        total_discount_percentage = d.pop("totalDiscountPercentage", UNSET)

        total_discount_amount = d.pop("totalDiscountAmount", UNSET)

        _discounts = d.pop("discounts", UNSET)
        discounts: list[RobloxCatalogApiDiscount] | Unset = UNSET
        if _discounts is not UNSET:
            discounts = []
            for discounts_item_data in _discounts:
                discounts_item = RobloxCatalogApiDiscount.from_dict(discounts_item_data)

                discounts.append(discounts_item)

        roblox_catalog_api_discount_information = cls(
            original_price=original_price,
            total_discount_percentage=total_discount_percentage,
            total_discount_amount=total_discount_amount,
            discounts=discounts,
        )

        return roblox_catalog_api_discount_information
