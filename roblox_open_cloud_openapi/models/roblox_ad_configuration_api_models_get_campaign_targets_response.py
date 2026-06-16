from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_ad_configuration_api_models_campaign_target_model import (
        RobloxAdConfigurationApiModelsCampaignTargetModel,
    )


T = TypeVar("T", bound="RobloxAdConfigurationApiModelsGetCampaignTargetsResponse")


@_attrs_define
class RobloxAdConfigurationApiModelsGetCampaignTargetsResponse:
    """The response model which returns a collection of Roblox.AdConfiguration.Api.Models.CampaignTargetModel

    Attributes:
        campaign_target_models (list[RobloxAdConfigurationApiModelsCampaignTargetModel] | Unset): Gets or sets a
            collection of Roblox.AdConfiguration.Api.Models.CampaignTargetModel
    """

    campaign_target_models: list[RobloxAdConfigurationApiModelsCampaignTargetModel] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        campaign_target_models: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.campaign_target_models, Unset):
            campaign_target_models = []
            for campaign_target_models_item_data in self.campaign_target_models:
                campaign_target_models_item = campaign_target_models_item_data.to_dict()
                campaign_target_models.append(campaign_target_models_item)

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if campaign_target_models is not UNSET:
            field_dict["campaignTargetModels"] = campaign_target_models

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_ad_configuration_api_models_campaign_target_model import (
            RobloxAdConfigurationApiModelsCampaignTargetModel,
        )

        d = dict(src_dict)
        _campaign_target_models = d.pop("campaignTargetModels", UNSET)
        campaign_target_models: list[RobloxAdConfigurationApiModelsCampaignTargetModel] | Unset = UNSET
        if _campaign_target_models is not UNSET:
            campaign_target_models = []
            for campaign_target_models_item_data in _campaign_target_models:
                campaign_target_models_item = RobloxAdConfigurationApiModelsCampaignTargetModel.from_dict(
                    campaign_target_models_item_data
                )

                campaign_target_models.append(campaign_target_models_item)

        roblox_ad_configuration_api_models_get_campaign_targets_response = cls(
            campaign_target_models=campaign_target_models,
        )

        return roblox_ad_configuration_api_models_get_campaign_targets_response
