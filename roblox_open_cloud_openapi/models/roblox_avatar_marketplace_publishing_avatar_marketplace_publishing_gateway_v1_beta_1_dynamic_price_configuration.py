from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar(
    "T", bound="RobloxAvatarMarketplacePublishingAvatarMarketplacePublishingGatewayV1Beta1DynamicPriceConfiguration"
)


@_attrs_define
class RobloxAvatarMarketplacePublishingAvatarMarketplacePublishingGatewayV1Beta1DynamicPriceConfiguration:
    """
    Attributes:
        minimum_price (int | Unset):
        price_offset (int | Unset):
        is_opt_out_regional_pricing (bool | Unset):
    """

    minimum_price: int | Unset = UNSET
    price_offset: int | Unset = UNSET
    is_opt_out_regional_pricing: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        minimum_price = self.minimum_price

        price_offset = self.price_offset

        is_opt_out_regional_pricing = self.is_opt_out_regional_pricing

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if minimum_price is not UNSET:
            field_dict["MinimumPrice"] = minimum_price
        if price_offset is not UNSET:
            field_dict["PriceOffset"] = price_offset
        if is_opt_out_regional_pricing is not UNSET:
            field_dict["IsOptOutRegionalPricing"] = is_opt_out_regional_pricing

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        minimum_price = d.pop("MinimumPrice", UNSET)

        price_offset = d.pop("PriceOffset", UNSET)

        is_opt_out_regional_pricing = d.pop("IsOptOutRegionalPricing", UNSET)

        roblox_avatar_marketplace_publishing_avatar_marketplace_publishing_gateway_v1_beta_1_dynamic_price_configuration = cls(
            minimum_price=minimum_price,
            price_offset=price_offset,
            is_opt_out_regional_pricing=is_opt_out_regional_pricing,
        )

        return roblox_avatar_marketplace_publishing_avatar_marketplace_publishing_gateway_v1_beta_1_dynamic_price_configuration
