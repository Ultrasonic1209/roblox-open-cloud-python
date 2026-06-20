from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_groups_api_group_feature_response import RobloxGroupsApiGroupFeatureResponse


T = TypeVar("T", bound="RobloxGroupsApiGetGroupFeaturesResponse")


@_attrs_define
class RobloxGroupsApiGetGroupFeaturesResponse:
    """Response model for the group features endpoint.

    Attributes:
        is_locked (bool | Unset): Whether the group is currently locked.
        features (list[RobloxGroupsApiGroupFeatureResponse] | Unset): The freeze status of each feature for the group.
    """

    is_locked: bool | Unset = UNSET
    features: list[RobloxGroupsApiGroupFeatureResponse] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        is_locked = self.is_locked

        features: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.features, Unset):
            features = []
            for features_item_data in self.features:
                features_item = features_item_data.to_dict()
                features.append(features_item)

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if is_locked is not UNSET:
            field_dict["isLocked"] = is_locked
        if features is not UNSET:
            field_dict["features"] = features

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_groups_api_group_feature_response import RobloxGroupsApiGroupFeatureResponse

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        is_locked = d.pop("isLocked", UNSET)

        _features = d.pop("features", UNSET)
        features: list[RobloxGroupsApiGroupFeatureResponse] | Unset = UNSET
        if _features is not UNSET:
            features = []
            for features_item_data in _features:
                features_item = RobloxGroupsApiGroupFeatureResponse.from_dict(features_item_data)

                features.append(features_item)

        roblox_groups_api_get_group_features_response = cls(
            is_locked=is_locked,
            features=features,
        )

        return roblox_groups_api_get_group_features_response
