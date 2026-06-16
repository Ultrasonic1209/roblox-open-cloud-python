from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_groups_api_community_feature_freeze_status import RobloxGroupsApiCommunityFeatureFreezeStatus


T = TypeVar("T", bound="RobloxGroupsApiGetCommunityFeatureFreezesResponse")


@_attrs_define
class RobloxGroupsApiGetCommunityFeatureFreezesResponse:
    """Response model for the community feature freezes endpoint.

    Attributes:
        features (list[RobloxGroupsApiCommunityFeatureFreezeStatus] | Unset): The freeze status of each community
            feature.
    """

    features: list[RobloxGroupsApiCommunityFeatureFreezeStatus] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        features: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.features, Unset):
            features = []
            for features_item_data in self.features:
                features_item = features_item_data.to_dict()
                features.append(features_item)

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if features is not UNSET:
            field_dict["features"] = features

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_groups_api_community_feature_freeze_status import (
            RobloxGroupsApiCommunityFeatureFreezeStatus,
        )

        d = dict(src_dict)
        _features = d.pop("features", UNSET)
        features: list[RobloxGroupsApiCommunityFeatureFreezeStatus] | Unset = UNSET
        if _features is not UNSET:
            features = []
            for features_item_data in _features:
                features_item = RobloxGroupsApiCommunityFeatureFreezeStatus.from_dict(features_item_data)

                features.append(features_item)

        roblox_groups_api_get_community_feature_freezes_response = cls(
            features=features,
        )

        return roblox_groups_api_get_community_feature_freezes_response
