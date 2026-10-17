from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxGroupsApiCommunityFeatureFreezeStatus")


@_attrs_define
class RobloxGroupsApiCommunityFeatureFreezeStatus:
    """Response model representing the freeze status of a community feature.

    Attributes:
        feature (str | Unset): The community feature.
        is_disabled (bool | Unset): Whether the feature is currently disabled.
    """

    feature: str | Unset = UNSET
    is_disabled: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        feature = self.feature

        is_disabled = self.is_disabled

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if feature is not UNSET:
            field_dict["feature"] = feature
        if is_disabled is not UNSET:
            field_dict["isDisabled"] = is_disabled

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        feature = d.pop("feature", UNSET)

        is_disabled = d.pop("isDisabled", UNSET)

        roblox_groups_api_community_feature_freeze_status = cls(
            feature=feature,
            is_disabled=is_disabled,
        )

        return roblox_groups_api_community_feature_freeze_status
