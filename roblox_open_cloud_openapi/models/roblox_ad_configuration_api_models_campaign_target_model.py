from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.roblox_ad_configuration_api_models_campaign_target_model_campaign_target_type import (
    RobloxAdConfigurationApiModelsCampaignTargetModelCampaignTargetType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxAdConfigurationApiModelsCampaignTargetModel")


@_attrs_define
class RobloxAdConfigurationApiModelsCampaignTargetModel:
    """Represents a sponsored ad campaign target

    Attributes:
        campaign_target_type (RobloxAdConfigurationApiModelsCampaignTargetModelCampaignTargetType | Unset): The campaign
            target type ['Undefined' = 0, 'Universe' = 1, 'Asset' = 2, 'ImmersiveAd' = 3]
        campaign_target_id (int | Unset): The ID of the campaign target
        name (str | Unset): The name of the campaign target (i.e. the asset name, universe name, group name, etc.)
    """

    campaign_target_type: RobloxAdConfigurationApiModelsCampaignTargetModelCampaignTargetType | Unset = UNSET
    campaign_target_id: int | Unset = UNSET
    name: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        campaign_target_type: int | Unset = UNSET
        if not isinstance(self.campaign_target_type, Unset):
            campaign_target_type = self.campaign_target_type.value

        campaign_target_id = self.campaign_target_id

        name = self.name

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if campaign_target_type is not UNSET:
            field_dict["campaignTargetType"] = campaign_target_type
        if campaign_target_id is not UNSET:
            field_dict["campaignTargetId"] = campaign_target_id
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        _campaign_target_type = d.pop("campaignTargetType", UNSET)
        campaign_target_type: RobloxAdConfigurationApiModelsCampaignTargetModelCampaignTargetType | Unset
        if isinstance(_campaign_target_type, Unset):
            campaign_target_type = UNSET
        else:
            campaign_target_type = RobloxAdConfigurationApiModelsCampaignTargetModelCampaignTargetType(
                _campaign_target_type
            )

        campaign_target_id = d.pop("campaignTargetId", UNSET)

        name = d.pop("name", UNSET)

        roblox_ad_configuration_api_models_campaign_target_model = cls(
            campaign_target_type=campaign_target_type,
            campaign_target_id=campaign_target_id,
            name=name,
        )

        return roblox_ad_configuration_api_models_campaign_target_model
