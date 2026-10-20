from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.roblox_ads_api_record_click_request_campaign_target_type import (
    RobloxAdsApiRecordClickRequestCampaignTargetType,
)
from ..models.roblox_ads_api_record_click_request_placement_location import (
    RobloxAdsApiRecordClickRequestPlacementLocation,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxAdsApiRecordClickRequest")


@_attrs_define
class RobloxAdsApiRecordClickRequest:
    """A request model for an ad click.

    Attributes:
        encrypted_ad_tracking_data (str | Unset): The encrypted tracking data
        campaign_target_type (RobloxAdsApiRecordClickRequestCampaignTargetType | Unset): The campaign target type
            ['Undefined' = 0, 'Universe' = 1, 'Asset' = 2, 'ImmersiveAd' = 3]
        placement_location (RobloxAdsApiRecordClickRequestPlacementLocation | Unset): The placement location
            ['Undefined' = 1, 'GameSort' = 2, 'AvatarShop' = 4, 'ItemDetails' = 8, 'HomePage' = 16, 'Billboard300x250' = 32,
            'Billboard600x300' = 64, 'Billboard300x600' = 128]
    """

    encrypted_ad_tracking_data: str | Unset = UNSET
    campaign_target_type: RobloxAdsApiRecordClickRequestCampaignTargetType | Unset = UNSET
    placement_location: RobloxAdsApiRecordClickRequestPlacementLocation | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        encrypted_ad_tracking_data = self.encrypted_ad_tracking_data

        campaign_target_type: int | Unset = UNSET
        if not isinstance(self.campaign_target_type, Unset):
            campaign_target_type = self.campaign_target_type.value

        placement_location: int | Unset = UNSET
        if not isinstance(self.placement_location, Unset):
            placement_location = self.placement_location.value

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if encrypted_ad_tracking_data is not UNSET:
            field_dict["encryptedAdTrackingData"] = encrypted_ad_tracking_data
        if campaign_target_type is not UNSET:
            field_dict["campaignTargetType"] = campaign_target_type
        if placement_location is not UNSET:
            field_dict["placementLocation"] = placement_location

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        encrypted_ad_tracking_data = d.pop("encryptedAdTrackingData", UNSET)

        _campaign_target_type = d.pop("campaignTargetType", UNSET)
        campaign_target_type: RobloxAdsApiRecordClickRequestCampaignTargetType | Unset
        if isinstance(_campaign_target_type, Unset):
            campaign_target_type = UNSET
        else:
            campaign_target_type = RobloxAdsApiRecordClickRequestCampaignTargetType(_campaign_target_type)

        _placement_location = d.pop("placementLocation", UNSET)
        placement_location: RobloxAdsApiRecordClickRequestPlacementLocation | Unset
        if isinstance(_placement_location, Unset):
            placement_location = UNSET
        else:
            placement_location = RobloxAdsApiRecordClickRequestPlacementLocation(_placement_location)

        roblox_ads_api_record_click_request = cls(
            encrypted_ad_tracking_data=encrypted_ad_tracking_data,
            campaign_target_type=campaign_target_type,
            placement_location=placement_location,
        )

        return roblox_ads_api_record_click_request
