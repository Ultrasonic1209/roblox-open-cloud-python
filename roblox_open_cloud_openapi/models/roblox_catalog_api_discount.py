from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxCatalogApiDiscount")


@_attrs_define
class RobloxCatalogApiDiscount:
    """
    Attributes:
        robux_discount_amount (int | Unset):
        robux_discount_percentage (float | Unset):
        discount_campaign (str | Unset):
        localized_discount_attribution (str | Unset):
    """

    robux_discount_amount: int | Unset = UNSET
    robux_discount_percentage: float | Unset = UNSET
    discount_campaign: str | Unset = UNSET
    localized_discount_attribution: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        robux_discount_amount = self.robux_discount_amount

        robux_discount_percentage = self.robux_discount_percentage

        discount_campaign = self.discount_campaign

        localized_discount_attribution = self.localized_discount_attribution

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if robux_discount_amount is not UNSET:
            field_dict["robuxDiscountAmount"] = robux_discount_amount
        if robux_discount_percentage is not UNSET:
            field_dict["robuxDiscountPercentage"] = robux_discount_percentage
        if discount_campaign is not UNSET:
            field_dict["discountCampaign"] = discount_campaign
        if localized_discount_attribution is not UNSET:
            field_dict["localizedDiscountAttribution"] = localized_discount_attribution

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        robux_discount_amount = d.pop("robuxDiscountAmount", UNSET)

        robux_discount_percentage = d.pop("robuxDiscountPercentage", UNSET)

        discount_campaign = d.pop("discountCampaign", UNSET)

        localized_discount_attribution = d.pop("localizedDiscountAttribution", UNSET)

        roblox_catalog_api_discount = cls(
            robux_discount_amount=robux_discount_amount,
            robux_discount_percentage=robux_discount_percentage,
            discount_campaign=discount_campaign,
            localized_discount_attribution=localized_discount_attribution,
        )

        return roblox_catalog_api_discount
