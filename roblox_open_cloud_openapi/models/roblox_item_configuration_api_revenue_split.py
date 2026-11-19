from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxItemConfigurationApiRevenueSplit")


@_attrs_define
class RobloxItemConfigurationApiRevenueSplit:
    """Revenue split model.

    Attributes:
        creator_split_percentage (int | Unset): Creator split percentage.
        seller_split_percentage (int | Unset): Seller split percentage.
        marketplace_split_percentage (int | Unset): Marketplace split percentage.
        reseller_split_percentage (int | Unset): Reseller split percentage.
        ip_holder_split_percentage (int | Unset): IP-holder split percentage. Non-zero only when the request carries a
            LicenseId with a royalty;
            rounded up and subtracted from Roblox.ItemConfiguration.Api.RevenueSplit.CreatorSplitPercentage. Defaults to 0.
    """

    creator_split_percentage: int | Unset = UNSET
    seller_split_percentage: int | Unset = UNSET
    marketplace_split_percentage: int | Unset = UNSET
    reseller_split_percentage: int | Unset = UNSET
    ip_holder_split_percentage: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        creator_split_percentage = self.creator_split_percentage

        seller_split_percentage = self.seller_split_percentage

        marketplace_split_percentage = self.marketplace_split_percentage

        reseller_split_percentage = self.reseller_split_percentage

        ip_holder_split_percentage = self.ip_holder_split_percentage

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if creator_split_percentage is not UNSET:
            field_dict["creatorSplitPercentage"] = creator_split_percentage
        if seller_split_percentage is not UNSET:
            field_dict["sellerSplitPercentage"] = seller_split_percentage
        if marketplace_split_percentage is not UNSET:
            field_dict["marketplaceSplitPercentage"] = marketplace_split_percentage
        if reseller_split_percentage is not UNSET:
            field_dict["resellerSplitPercentage"] = reseller_split_percentage
        if ip_holder_split_percentage is not UNSET:
            field_dict["ipHolderSplitPercentage"] = ip_holder_split_percentage

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        creator_split_percentage = d.pop("creatorSplitPercentage", UNSET)

        seller_split_percentage = d.pop("sellerSplitPercentage", UNSET)

        marketplace_split_percentage = d.pop("marketplaceSplitPercentage", UNSET)

        reseller_split_percentage = d.pop("resellerSplitPercentage", UNSET)

        ip_holder_split_percentage = d.pop("ipHolderSplitPercentage", UNSET)

        roblox_item_configuration_api_revenue_split = cls(
            creator_split_percentage=creator_split_percentage,
            seller_split_percentage=seller_split_percentage,
            marketplace_split_percentage=marketplace_split_percentage,
            reseller_split_percentage=reseller_split_percentage,
            ip_holder_split_percentage=ip_holder_split_percentage,
        )

        return roblox_item_configuration_api_revenue_split
