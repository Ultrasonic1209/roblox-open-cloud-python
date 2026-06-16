from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..models.roblox_ad_configuration_api_models_create_sponsored_campaign_request_campaign_target_type import (
    RobloxAdConfigurationApiModelsCreateSponsoredCampaignRequestCampaignTargetType,
)
from ..models.roblox_ad_configuration_api_models_create_sponsored_campaign_request_placement_location import (
    RobloxAdConfigurationApiModelsCreateSponsoredCampaignRequestPlacementLocation,
)
from ..models.roblox_ad_configuration_api_models_create_sponsored_campaign_request_target_age_bracket import (
    RobloxAdConfigurationApiModelsCreateSponsoredCampaignRequestTargetAgeBracket,
)
from ..models.roblox_ad_configuration_api_models_create_sponsored_campaign_request_target_device_type import (
    RobloxAdConfigurationApiModelsCreateSponsoredCampaignRequestTargetDeviceType,
)
from ..models.roblox_ad_configuration_api_models_create_sponsored_campaign_request_target_gender import (
    RobloxAdConfigurationApiModelsCreateSponsoredCampaignRequestTargetGender,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_ad_configuration_api_creative_model import RobloxAdConfigurationApiCreativeModel


T = TypeVar("T", bound="RobloxAdConfigurationApiModelsCreateSponsoredCampaignRequest")


@_attrs_define
class RobloxAdConfigurationApiModelsCreateSponsoredCampaignRequest:
    """A request model for creating a sponsored game

    Attributes:
        campaign_target_id (int | Unset): The ID of the campaign target Example: 1.
        campaign_target_type (RobloxAdConfigurationApiModelsCreateSponsoredCampaignRequestCampaignTargetType | Unset):
            The type of the campaign target ['Undefined' = 0, 'Universe' = 1, 'Asset' = 2, 'ImmersiveAd' = 3] Example: 2.
        target_gender (RobloxAdConfigurationApiModelsCreateSponsoredCampaignRequestTargetGender | Unset): Targeting
            gender(s) of the ad set ['Undefined' = 1, 'Male' = 2, 'Female' = 4] Example: 4.
        target_age_bracket (RobloxAdConfigurationApiModelsCreateSponsoredCampaignRequestTargetAgeBracket | Unset):
            Targeting age bracket(s) of the ad set ['Undefined' = 1, 'AgeUnder13' = 2, 'Age13OrOver' = 4, 'Age13To16' = 8,
            'Age17OrOver' = 16] Example: 4.
        start_date (datetime.datetime | Unset): The start date of the ad set
        end_date (datetime.datetime | Unset): The end date of the ad set
        target_device_type (RobloxAdConfigurationApiModelsCreateSponsoredCampaignRequestTargetDeviceType | Unset):
            Targeting device type(s) of the ad set ['Undefined' = 1, 'Computer' = 2, 'Phone' = 4, 'Tablet' = 8, 'Console' =
            16, 'VR' = 32] Example: 2.
        campaign_name (str | Unset): The name of the Campaign / Ad
        daily_bid_amount_in_robux (int | Unset): The daily bid amount for the campaign / ad, in Robux Example: 101.
        placement_location (RobloxAdConfigurationApiModelsCreateSponsoredCampaignRequestPlacementLocation | Unset): The
            location to place the campaign ['Undefined' = 1, 'GameSort' = 2, 'AvatarShop' = 4, 'ItemDetails' = 8, 'HomePage'
            = 16, 'Billboard300x250' = 32, 'Billboard600x300' = 64, 'Billboard300x600' = 128] Example: 4.
        creative_model (RobloxAdConfigurationApiCreativeModel | Unset): A model representing an Ad Creative (for
            example, an ad thumbnail).
    """

    campaign_target_id: int | Unset = UNSET
    campaign_target_type: RobloxAdConfigurationApiModelsCreateSponsoredCampaignRequestCampaignTargetType | Unset = UNSET
    target_gender: RobloxAdConfigurationApiModelsCreateSponsoredCampaignRequestTargetGender | Unset = UNSET
    target_age_bracket: RobloxAdConfigurationApiModelsCreateSponsoredCampaignRequestTargetAgeBracket | Unset = UNSET
    start_date: datetime.datetime | Unset = UNSET
    end_date: datetime.datetime | Unset = UNSET
    target_device_type: RobloxAdConfigurationApiModelsCreateSponsoredCampaignRequestTargetDeviceType | Unset = UNSET
    campaign_name: str | Unset = UNSET
    daily_bid_amount_in_robux: int | Unset = UNSET
    placement_location: RobloxAdConfigurationApiModelsCreateSponsoredCampaignRequestPlacementLocation | Unset = UNSET
    creative_model: RobloxAdConfigurationApiCreativeModel | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        campaign_target_id = self.campaign_target_id

        campaign_target_type: int | Unset = UNSET
        if not isinstance(self.campaign_target_type, Unset):
            campaign_target_type = self.campaign_target_type.value

        target_gender: int | Unset = UNSET
        if not isinstance(self.target_gender, Unset):
            target_gender = self.target_gender.value

        target_age_bracket: int | Unset = UNSET
        if not isinstance(self.target_age_bracket, Unset):
            target_age_bracket = self.target_age_bracket.value

        start_date: str | Unset = UNSET
        if not isinstance(self.start_date, Unset):
            start_date = self.start_date.isoformat()

        end_date: str | Unset = UNSET
        if not isinstance(self.end_date, Unset):
            end_date = self.end_date.isoformat()

        target_device_type: int | Unset = UNSET
        if not isinstance(self.target_device_type, Unset):
            target_device_type = self.target_device_type.value

        campaign_name = self.campaign_name

        daily_bid_amount_in_robux = self.daily_bid_amount_in_robux

        placement_location: int | Unset = UNSET
        if not isinstance(self.placement_location, Unset):
            placement_location = self.placement_location.value

        creative_model: dict[str, Any] | Unset = UNSET
        if not isinstance(self.creative_model, Unset):
            creative_model = self.creative_model.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if campaign_target_id is not UNSET:
            field_dict["campaignTargetId"] = campaign_target_id
        if campaign_target_type is not UNSET:
            field_dict["campaignTargetType"] = campaign_target_type
        if target_gender is not UNSET:
            field_dict["targetGender"] = target_gender
        if target_age_bracket is not UNSET:
            field_dict["targetAgeBracket"] = target_age_bracket
        if start_date is not UNSET:
            field_dict["startDate"] = start_date
        if end_date is not UNSET:
            field_dict["endDate"] = end_date
        if target_device_type is not UNSET:
            field_dict["targetDeviceType"] = target_device_type
        if campaign_name is not UNSET:
            field_dict["campaignName"] = campaign_name
        if daily_bid_amount_in_robux is not UNSET:
            field_dict["dailyBidAmountInRobux"] = daily_bid_amount_in_robux
        if placement_location is not UNSET:
            field_dict["placementLocation"] = placement_location
        if creative_model is not UNSET:
            field_dict["creativeModel"] = creative_model

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_ad_configuration_api_creative_model import RobloxAdConfigurationApiCreativeModel

        d = dict(src_dict)
        campaign_target_id = d.pop("campaignTargetId", UNSET)

        _campaign_target_type = d.pop("campaignTargetType", UNSET)
        campaign_target_type: RobloxAdConfigurationApiModelsCreateSponsoredCampaignRequestCampaignTargetType | Unset
        if isinstance(_campaign_target_type, Unset):
            campaign_target_type = UNSET
        else:
            campaign_target_type = RobloxAdConfigurationApiModelsCreateSponsoredCampaignRequestCampaignTargetType(
                _campaign_target_type
            )

        _target_gender = d.pop("targetGender", UNSET)
        target_gender: RobloxAdConfigurationApiModelsCreateSponsoredCampaignRequestTargetGender | Unset
        if isinstance(_target_gender, Unset):
            target_gender = UNSET
        else:
            target_gender = RobloxAdConfigurationApiModelsCreateSponsoredCampaignRequestTargetGender(_target_gender)

        _target_age_bracket = d.pop("targetAgeBracket", UNSET)
        target_age_bracket: RobloxAdConfigurationApiModelsCreateSponsoredCampaignRequestTargetAgeBracket | Unset
        if isinstance(_target_age_bracket, Unset):
            target_age_bracket = UNSET
        else:
            target_age_bracket = RobloxAdConfigurationApiModelsCreateSponsoredCampaignRequestTargetAgeBracket(
                _target_age_bracket
            )

        _start_date = d.pop("startDate", UNSET)
        start_date: datetime.datetime | Unset
        if isinstance(_start_date, Unset):
            start_date = UNSET
        else:
            start_date = datetime.datetime.fromisoformat(_start_date)

        _end_date = d.pop("endDate", UNSET)
        end_date: datetime.datetime | Unset
        if isinstance(_end_date, Unset):
            end_date = UNSET
        else:
            end_date = datetime.datetime.fromisoformat(_end_date)

        _target_device_type = d.pop("targetDeviceType", UNSET)
        target_device_type: RobloxAdConfigurationApiModelsCreateSponsoredCampaignRequestTargetDeviceType | Unset
        if isinstance(_target_device_type, Unset):
            target_device_type = UNSET
        else:
            target_device_type = RobloxAdConfigurationApiModelsCreateSponsoredCampaignRequestTargetDeviceType(
                _target_device_type
            )

        campaign_name = d.pop("campaignName", UNSET)

        daily_bid_amount_in_robux = d.pop("dailyBidAmountInRobux", UNSET)

        _placement_location = d.pop("placementLocation", UNSET)
        placement_location: RobloxAdConfigurationApiModelsCreateSponsoredCampaignRequestPlacementLocation | Unset
        if isinstance(_placement_location, Unset):
            placement_location = UNSET
        else:
            placement_location = RobloxAdConfigurationApiModelsCreateSponsoredCampaignRequestPlacementLocation(
                _placement_location
            )

        _creative_model = d.pop("creativeModel", UNSET)
        creative_model: RobloxAdConfigurationApiCreativeModel | Unset
        if isinstance(_creative_model, Unset):
            creative_model = UNSET
        else:
            creative_model = RobloxAdConfigurationApiCreativeModel.from_dict(_creative_model)

        roblox_ad_configuration_api_models_create_sponsored_campaign_request = cls(
            campaign_target_id=campaign_target_id,
            campaign_target_type=campaign_target_type,
            target_gender=target_gender,
            target_age_bracket=target_age_bracket,
            start_date=start_date,
            end_date=end_date,
            target_device_type=target_device_type,
            campaign_name=campaign_name,
            daily_bid_amount_in_robux=daily_bid_amount_in_robux,
            placement_location=placement_location,
            creative_model=creative_model,
        )

        return roblox_ad_configuration_api_models_create_sponsored_campaign_request
