from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_catalog_api_premium_pricing_model import RobloxCatalogApiPremiumPricingModel


T = TypeVar("T", bound="RobloxCatalogApiBundleProductModel")


@_attrs_define
class RobloxCatalogApiBundleProductModel:
    """
    Attributes:
        id (int | Unset):
        type_ (str | Unset):
        is_public_domain (bool | Unset):
        is_for_sale (bool | Unset):
        price_in_robux (int | Unset):
        is_free (bool | Unset):
        no_price_text (str | Unset):
        premium_pricing (RobloxCatalogApiPremiumPricingModel | Unset): Defines the Premium pricing for a catalog item.
    """

    id: int | Unset = UNSET
    type_: str | Unset = UNSET
    is_public_domain: bool | Unset = UNSET
    is_for_sale: bool | Unset = UNSET
    price_in_robux: int | Unset = UNSET
    is_free: bool | Unset = UNSET
    no_price_text: str | Unset = UNSET
    premium_pricing: RobloxCatalogApiPremiumPricingModel | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        type_ = self.type_

        is_public_domain = self.is_public_domain

        is_for_sale = self.is_for_sale

        price_in_robux = self.price_in_robux

        is_free = self.is_free

        no_price_text = self.no_price_text

        premium_pricing: dict[str, Any] | Unset = UNSET
        if not isinstance(self.premium_pricing, Unset):
            premium_pricing = self.premium_pricing.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if type_ is not UNSET:
            field_dict["type"] = type_
        if is_public_domain is not UNSET:
            field_dict["isPublicDomain"] = is_public_domain
        if is_for_sale is not UNSET:
            field_dict["isForSale"] = is_for_sale
        if price_in_robux is not UNSET:
            field_dict["priceInRobux"] = price_in_robux
        if is_free is not UNSET:
            field_dict["isFree"] = is_free
        if no_price_text is not UNSET:
            field_dict["noPriceText"] = no_price_text
        if premium_pricing is not UNSET:
            field_dict["premiumPricing"] = premium_pricing

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_catalog_api_premium_pricing_model import RobloxCatalogApiPremiumPricingModel

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        id = d.pop("id", UNSET)

        type_ = d.pop("type", UNSET)

        is_public_domain = d.pop("isPublicDomain", UNSET)

        is_for_sale = d.pop("isForSale", UNSET)

        price_in_robux = d.pop("priceInRobux", UNSET)

        is_free = d.pop("isFree", UNSET)

        no_price_text = d.pop("noPriceText", UNSET)

        _premium_pricing = d.pop("premiumPricing", UNSET)
        premium_pricing: RobloxCatalogApiPremiumPricingModel | Unset
        if isinstance(_premium_pricing, Unset):
            premium_pricing = UNSET
        else:
            premium_pricing = RobloxCatalogApiPremiumPricingModel.from_dict(_premium_pricing)

        roblox_catalog_api_bundle_product_model = cls(
            id=id,
            type_=type_,
            is_public_domain=is_public_domain,
            is_for_sale=is_for_sale,
            price_in_robux=price_in_robux,
            is_free=is_free,
            no_price_text=no_price_text,
            premium_pricing=premium_pricing,
        )

        return roblox_catalog_api_bundle_product_model
