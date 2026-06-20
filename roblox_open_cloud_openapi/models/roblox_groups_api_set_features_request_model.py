from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.roblox_groups_api_set_features_request_model_features import (
        RobloxGroupsApiSetFeaturesRequestModelFeatures,
    )


T = TypeVar("T", bound="RobloxGroupsApiSetFeaturesRequestModel")


@_attrs_define
class RobloxGroupsApiSetFeaturesRequestModel:
    """Request model for setting the desired status of group features.

    Attributes:
        features (RobloxGroupsApiSetFeaturesRequestModelFeatures): Dictionary of features and their desired status.
    """

    features: RobloxGroupsApiSetFeaturesRequestModelFeatures

    def to_dict(self) -> dict[str, Any]:
        features = self.features.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "Features": features,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_groups_api_set_features_request_model_features import (
            RobloxGroupsApiSetFeaturesRequestModelFeatures,
        )

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        features = RobloxGroupsApiSetFeaturesRequestModelFeatures.from_dict(d.pop("Features"))

        roblox_groups_api_set_features_request_model = cls(
            features=features,
        )

        return roblox_groups_api_set_features_request_model
