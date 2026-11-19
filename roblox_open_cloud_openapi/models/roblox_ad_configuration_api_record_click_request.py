from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.roblox_ad_configuration_api_record_click_request_campaign_target_type import (
    RobloxAdConfigurationApiRecordClickRequestCampaignTargetType,
)
from ..models.roblox_ad_configuration_api_record_click_request_placement_location import (
    RobloxAdConfigurationApiRecordClickRequestPlacementLocation,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxAdConfigurationApiRecordClickRequest")


@_attrs_define
class RobloxAdConfigurationApiRecordClickRequest:
    """A request model for an ad click.

    Attributes:
        encrypted_ad_tracking_data (str | Unset): The encrypted tracking data. IsRequired will be set to false
            temporarily until AdTrackingData is removed.
        campaign_target_type (RobloxAdConfigurationApiRecordClickRequestCampaignTargetType | Unset): The campaign target
            type ['Undefined' = 0, 'Universe' = 1, 'Asset' = 2, 'ImmersiveAd' = 3]
        placement_location (RobloxAdConfigurationApiRecordClickRequestPlacementLocation | Unset): The placement location
            ['Undefined' = 1, 'GameSort' = 2, 'AvatarShop' = 4, 'ItemDetails' = 8, 'HomePage' = 16, 'Billboard300x250' = 32,
            'Billboard600x300' = 64, 'Billboard300x600' = 128]
        ad_tracking_data (str | Unset): DO NOT USE. This field is temporary. Will be removed.
    """

    encrypted_ad_tracking_data: str | Unset = UNSET
    campaign_target_type: RobloxAdConfigurationApiRecordClickRequestCampaignTargetType | Unset = UNSET
    placement_location: RobloxAdConfigurationApiRecordClickRequestPlacementLocation | Unset = UNSET
    ad_tracking_data: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        encrypted_ad_tracking_data = self.encrypted_ad_tracking_data

        campaign_target_type: int | Unset = UNSET
        if not isinstance(self.campaign_target_type, Unset):
            campaign_target_type = self.campaign_target_type.value

        placement_location: int | Unset = UNSET
        if not isinstance(self.placement_location, Unset):
            placement_location = self.placement_location.value

        ad_tracking_data = self.ad_tracking_data

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if encrypted_ad_tracking_data is not UNSET:
            field_dict["encryptedAdTrackingData"] = encrypted_ad_tracking_data
        if campaign_target_type is not UNSET:
            field_dict["campaignTargetType"] = campaign_target_type
        if placement_location is not UNSET:
            field_dict["placementLocation"] = placement_location
        if ad_tracking_data is not UNSET:
            field_dict["adTrackingData"] = ad_tracking_data

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        encrypted_ad_tracking_data = d.pop("encryptedAdTrackingData", UNSET)

        _campaign_target_type = d.pop("campaignTargetType", UNSET)
        campaign_target_type: RobloxAdConfigurationApiRecordClickRequestCampaignTargetType | Unset
        if isinstance(_campaign_target_type, Unset):
            campaign_target_type = UNSET
        else:
            campaign_target_type = RobloxAdConfigurationApiRecordClickRequestCampaignTargetType(_campaign_target_type)

        _placement_location = d.pop("placementLocation", UNSET)
        placement_location: RobloxAdConfigurationApiRecordClickRequestPlacementLocation | Unset
        if isinstance(_placement_location, Unset):
            placement_location = UNSET
        else:
            placement_location = RobloxAdConfigurationApiRecordClickRequestPlacementLocation(_placement_location)

        ad_tracking_data = d.pop("adTrackingData", UNSET)

        roblox_ad_configuration_api_record_click_request = cls(
            encrypted_ad_tracking_data=encrypted_ad_tracking_data,
            campaign_target_type=campaign_target_type,
            placement_location=placement_location,
            ad_tracking_data=ad_tracking_data,
        )

        return roblox_ad_configuration_api_record_click_request
