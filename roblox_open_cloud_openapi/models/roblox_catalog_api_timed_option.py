from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_catalog_api_discount_information import RobloxCatalogApiDiscountInformation


T = TypeVar("T", bound="RobloxCatalogApiTimedOption")


@_attrs_define
class RobloxCatalogApiTimedOption:
    """Defines a timed option for a catalog item.

    Attributes:
        days (int | Unset): The days for the timed option.
        price (int | Unset): The price for the timed option.
        discount_information (RobloxCatalogApiDiscountInformation | Unset):
        selected (bool | Unset): To indicate if this option is selected by the client.
    """

    days: int | Unset = UNSET
    price: int | Unset = UNSET
    discount_information: RobloxCatalogApiDiscountInformation | Unset = UNSET
    selected: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        days = self.days

        price = self.price

        discount_information: dict[str, Any] | Unset = UNSET
        if not isinstance(self.discount_information, Unset):
            discount_information = self.discount_information.to_dict()

        selected = self.selected

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if days is not UNSET:
            field_dict["days"] = days
        if price is not UNSET:
            field_dict["price"] = price
        if discount_information is not UNSET:
            field_dict["discountInformation"] = discount_information
        if selected is not UNSET:
            field_dict["selected"] = selected

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_catalog_api_discount_information import RobloxCatalogApiDiscountInformation

        d = dict(src_dict)
        days = d.pop("days", UNSET)

        price = d.pop("price", UNSET)

        _discount_information = d.pop("discountInformation", UNSET)
        discount_information: RobloxCatalogApiDiscountInformation | Unset
        if isinstance(_discount_information, Unset):
            discount_information = UNSET
        else:
            discount_information = RobloxCatalogApiDiscountInformation.from_dict(_discount_information)

        selected = d.pop("selected", UNSET)

        roblox_catalog_api_timed_option = cls(
            days=days,
            price=price,
            discount_information=discount_information,
            selected=selected,
        )

        return roblox_catalog_api_timed_option
