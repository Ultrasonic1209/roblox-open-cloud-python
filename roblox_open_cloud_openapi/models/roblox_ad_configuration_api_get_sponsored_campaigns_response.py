from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_ad_configuration_api_sponsored_campaign_model import (
        RobloxAdConfigurationApiSponsoredCampaignModel,
    )


T = TypeVar("T", bound="RobloxAdConfigurationApiGetSponsoredCampaignsResponse")


@_attrs_define
class RobloxAdConfigurationApiGetSponsoredCampaignsResponse:
    """A response model for retrieving a page of Roblox.AdConfiguration.Api.SponsoredCampaignModel.

    Attributes:
        sponsored_campaigns (list[RobloxAdConfigurationApiSponsoredCampaignModel] | Unset): A collection of
            Roblox.AdConfiguration.Api.SponsoredCampaignModel.
        previous_page_cursor (str | Unset): The cursor for retrieving the previous page, if present.
        next_page_cursor (str | Unset): The cursor for retrieving the next page, if present.
    """

    sponsored_campaigns: list[RobloxAdConfigurationApiSponsoredCampaignModel] | Unset = UNSET
    previous_page_cursor: str | Unset = UNSET
    next_page_cursor: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        sponsored_campaigns: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.sponsored_campaigns, Unset):
            sponsored_campaigns = []
            for sponsored_campaigns_item_data in self.sponsored_campaigns:
                sponsored_campaigns_item = sponsored_campaigns_item_data.to_dict()
                sponsored_campaigns.append(sponsored_campaigns_item)

        previous_page_cursor = self.previous_page_cursor

        next_page_cursor = self.next_page_cursor

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if sponsored_campaigns is not UNSET:
            field_dict["sponsoredCampaigns"] = sponsored_campaigns
        if previous_page_cursor is not UNSET:
            field_dict["previousPageCursor"] = previous_page_cursor
        if next_page_cursor is not UNSET:
            field_dict["nextPageCursor"] = next_page_cursor

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_ad_configuration_api_sponsored_campaign_model import (
            RobloxAdConfigurationApiSponsoredCampaignModel,
        )

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        _sponsored_campaigns = d.pop("sponsoredCampaigns", UNSET)
        sponsored_campaigns: list[RobloxAdConfigurationApiSponsoredCampaignModel] | Unset = UNSET
        if _sponsored_campaigns is not UNSET:
            sponsored_campaigns = []
            for sponsored_campaigns_item_data in _sponsored_campaigns:
                sponsored_campaigns_item = RobloxAdConfigurationApiSponsoredCampaignModel.from_dict(
                    sponsored_campaigns_item_data
                )

                sponsored_campaigns.append(sponsored_campaigns_item)

        previous_page_cursor = d.pop("previousPageCursor", UNSET)

        next_page_cursor = d.pop("nextPageCursor", UNSET)

        roblox_ad_configuration_api_get_sponsored_campaigns_response = cls(
            sponsored_campaigns=sponsored_campaigns,
            previous_page_cursor=previous_page_cursor,
            next_page_cursor=next_page_cursor,
        )

        return roblox_ad_configuration_api_get_sponsored_campaigns_response
