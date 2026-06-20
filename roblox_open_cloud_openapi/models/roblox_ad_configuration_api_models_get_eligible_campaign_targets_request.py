from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.roblox_ad_configuration_api_models_get_eligible_campaign_targets_request_campaign_target_types_item import (
    RobloxAdConfigurationApiModelsGetEligibleCampaignTargetsRequestCampaignTargetTypesItem,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxAdConfigurationApiModelsGetEligibleCampaignTargetsRequest")


@_attrs_define
class RobloxAdConfigurationApiModelsGetEligibleCampaignTargetsRequest:
    """A model represents a request to stop a sponsored campaign / ad.

    Attributes:
        campaign_target_types
            (list[RobloxAdConfigurationApiModelsGetEligibleCampaignTargetsRequestCampaignTargetTypesItem] | Unset): The list
            of campaign types we want to include in the results
        group_id (int | Unset): The group id, if applicable.
    """

    campaign_target_types: (
        list[RobloxAdConfigurationApiModelsGetEligibleCampaignTargetsRequestCampaignTargetTypesItem] | Unset
    ) = UNSET
    group_id: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        campaign_target_types: list[int] | Unset = UNSET
        if not isinstance(self.campaign_target_types, Unset):
            campaign_target_types = []
            for campaign_target_types_item_data in self.campaign_target_types:
                campaign_target_types_item = campaign_target_types_item_data.value
                campaign_target_types.append(campaign_target_types_item)

        group_id = self.group_id

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if campaign_target_types is not UNSET:
            field_dict["campaignTargetTypes"] = campaign_target_types
        if group_id is not UNSET:
            field_dict["groupId"] = group_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        _campaign_target_types = d.pop("campaignTargetTypes", UNSET)
        campaign_target_types: (
            list[RobloxAdConfigurationApiModelsGetEligibleCampaignTargetsRequestCampaignTargetTypesItem] | Unset
        ) = UNSET
        if _campaign_target_types is not UNSET:
            campaign_target_types = []
            for campaign_target_types_item_data in _campaign_target_types:
                campaign_target_types_item = (
                    RobloxAdConfigurationApiModelsGetEligibleCampaignTargetsRequestCampaignTargetTypesItem(
                        campaign_target_types_item_data
                    )
                )

                campaign_target_types.append(campaign_target_types_item)

        group_id = d.pop("groupId", UNSET)

        roblox_ad_configuration_api_models_get_eligible_campaign_targets_request = cls(
            campaign_target_types=campaign_target_types,
            group_id=group_id,
        )

        return roblox_ad_configuration_api_models_get_eligible_campaign_targets_request
