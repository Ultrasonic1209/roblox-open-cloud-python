from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.roblox_groups_api_group_feature_response_feature import RobloxGroupsApiGroupFeatureResponseFeature
from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxGroupsApiGroupFeatureResponse")


@_attrs_define
class RobloxGroupsApiGroupFeatureResponse:
    """Response model representing the freeze status of a group feature.

    Attributes:
        feature (RobloxGroupsApiGroupFeatureResponseFeature | Unset): The feature type. ['Payouts' = 0, 'ContentUpload'
            = 1, 'GroupOwnershipTransfer' = 2, 'GameOwnershipTransfer' = 3, 'ForumRead' = 4, 'ForumWrite' = 5]
        is_feature_blocked (bool | Unset): Whether the feature is currently frozen.
        expiration (datetime.datetime | Unset): The UTC time at which the moderator-force expires, allowing the freeze
            to be deactivated upon request. Only present when the feature is forced frozen.
    """

    feature: RobloxGroupsApiGroupFeatureResponseFeature | Unset = UNSET
    is_feature_blocked: bool | Unset = UNSET
    expiration: datetime.datetime | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        feature: str | Unset = UNSET
        if not isinstance(self.feature, Unset):
            feature = self.feature.value

        is_feature_blocked = self.is_feature_blocked

        expiration: str | Unset = UNSET
        if not isinstance(self.expiration, Unset):
            expiration = self.expiration.isoformat()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if feature is not UNSET:
            field_dict["feature"] = feature
        if is_feature_blocked is not UNSET:
            field_dict["isFeatureBlocked"] = is_feature_blocked
        if expiration is not UNSET:
            field_dict["expiration"] = expiration

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _feature = d.pop("feature", UNSET)
        feature: RobloxGroupsApiGroupFeatureResponseFeature | Unset
        if isinstance(_feature, Unset):
            feature = UNSET
        else:
            feature = RobloxGroupsApiGroupFeatureResponseFeature(_feature)

        is_feature_blocked = d.pop("isFeatureBlocked", UNSET)

        _expiration = d.pop("expiration", UNSET)
        expiration: datetime.datetime | Unset
        if isinstance(_expiration, Unset):
            expiration = UNSET
        else:
            expiration = datetime.datetime.fromisoformat(_expiration)

        roblox_groups_api_group_feature_response = cls(
            feature=feature,
            is_feature_blocked=is_feature_blocked,
            expiration=expiration,
        )

        return roblox_groups_api_group_feature_response
