from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxAdsApiModelsResponseCreateSponsoredItemCampaignResponse")


@_attrs_define
class RobloxAdsApiModelsResponseCreateSponsoredItemCampaignResponse:
    """The response model for serving a sponsored game.

    Attributes:
        creator_target_id (int | Unset): Id of the universe that is being sponsored.
        creator_type (str | Unset): Type of the creator.
        creator_name (str | Unset): Name of the creator.
    """

    creator_target_id: int | Unset = UNSET
    creator_type: str | Unset = UNSET
    creator_name: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        creator_target_id = self.creator_target_id

        creator_type = self.creator_type

        creator_name = self.creator_name

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if creator_target_id is not UNSET:
            field_dict["creatorTargetId"] = creator_target_id
        if creator_type is not UNSET:
            field_dict["creatorType"] = creator_type
        if creator_name is not UNSET:
            field_dict["creatorName"] = creator_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        creator_target_id = d.pop("creatorTargetId", UNSET)

        creator_type = d.pop("creatorType", UNSET)

        creator_name = d.pop("creatorName", UNSET)

        roblox_ads_api_models_response_create_sponsored_item_campaign_response = cls(
            creator_target_id=creator_target_id,
            creator_type=creator_type,
            creator_name=creator_name,
        )

        return roblox_ads_api_models_response_create_sponsored_item_campaign_response
