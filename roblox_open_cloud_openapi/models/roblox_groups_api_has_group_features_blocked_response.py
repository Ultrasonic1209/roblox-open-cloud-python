from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxGroupsApiHasGroupFeaturesBlockedResponse")


@_attrs_define
class RobloxGroupsApiHasGroupFeaturesBlockedResponse:
    """Response model for the features/status endpoint.

    Attributes:
        has_features_blocked (bool | Unset): Whether the group has any active feature freezes.
    """

    has_features_blocked: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        has_features_blocked = self.has_features_blocked

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if has_features_blocked is not UNSET:
            field_dict["hasFeaturesBlocked"] = has_features_blocked

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        has_features_blocked = d.pop("hasFeaturesBlocked", UNSET)

        roblox_groups_api_has_group_features_blocked_response = cls(
            has_features_blocked=has_features_blocked,
        )

        return roblox_groups_api_has_group_features_blocked_response
