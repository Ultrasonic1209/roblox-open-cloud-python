from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxItemConfigurationApiGetCommissionRatesResponse")


@_attrs_define
class RobloxItemConfigurationApiGetCommissionRatesResponse:
    """Defines the response model for the v1/collectibles/commission-rates.

    Attributes:
        creator_fees_percentage (int | Unset): Creator fees percentage.
        marketplace_fees_percentage (int | Unset): Marketplace fees percentage.
        reseller_fees_percentage (int | Unset): Reseller fees percentage.
        seller_fees_percentage (int | Unset): Seller fees percentage.
    """

    creator_fees_percentage: int | Unset = UNSET
    marketplace_fees_percentage: int | Unset = UNSET
    reseller_fees_percentage: int | Unset = UNSET
    seller_fees_percentage: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        creator_fees_percentage = self.creator_fees_percentage

        marketplace_fees_percentage = self.marketplace_fees_percentage

        reseller_fees_percentage = self.reseller_fees_percentage

        seller_fees_percentage = self.seller_fees_percentage

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if creator_fees_percentage is not UNSET:
            field_dict["creatorFeesPercentage"] = creator_fees_percentage
        if marketplace_fees_percentage is not UNSET:
            field_dict["marketplaceFeesPercentage"] = marketplace_fees_percentage
        if reseller_fees_percentage is not UNSET:
            field_dict["resellerFeesPercentage"] = reseller_fees_percentage
        if seller_fees_percentage is not UNSET:
            field_dict["sellerFeesPercentage"] = seller_fees_percentage

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        creator_fees_percentage = d.pop("creatorFeesPercentage", UNSET)

        marketplace_fees_percentage = d.pop("marketplaceFeesPercentage", UNSET)

        reseller_fees_percentage = d.pop("resellerFeesPercentage", UNSET)

        seller_fees_percentage = d.pop("sellerFeesPercentage", UNSET)

        roblox_item_configuration_api_get_commission_rates_response = cls(
            creator_fees_percentage=creator_fees_percentage,
            marketplace_fees_percentage=marketplace_fees_percentage,
            reseller_fees_percentage=reseller_fees_percentage,
            seller_fees_percentage=seller_fees_percentage,
        )

        return roblox_item_configuration_api_get_commission_rates_response
