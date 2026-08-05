from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.roblox_groups_client_tier_requirement_key import RobloxGroupsClientTierRequirementKey
from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxGroupsClientTierRequirement")


@_attrs_define
class RobloxGroupsClientTierRequirement:
    """
    Attributes:
        key (RobloxGroupsClientTierRequirementKey | Unset):  ['OwnerModerationStatusOk' = 1,
            'OwnerAgeEstimationVerified' = 2, 'OwnerIdVerified' = 3, 'OwnerTwoStepVerified' = 4,
            'CommunityMeetsPlayerRequirement' = 5]
        satisfied (bool | Unset):
    """

    key: RobloxGroupsClientTierRequirementKey | Unset = UNSET
    satisfied: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        key: int | Unset = UNSET
        if not isinstance(self.key, Unset):
            key = self.key.value

        satisfied = self.satisfied

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if key is not UNSET:
            field_dict["key"] = key
        if satisfied is not UNSET:
            field_dict["satisfied"] = satisfied

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        _key = d.pop("key", UNSET)
        key: RobloxGroupsClientTierRequirementKey | Unset
        if isinstance(_key, Unset):
            key = UNSET
        else:
            key = RobloxGroupsClientTierRequirementKey(_key)

        satisfied = d.pop("satisfied", UNSET)

        roblox_groups_client_tier_requirement = cls(
            key=key,
            satisfied=satisfied,
        )

        return roblox_groups_client_tier_requirement
