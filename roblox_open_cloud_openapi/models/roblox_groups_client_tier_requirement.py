from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.roblox_groups_client_tier_requirement_key import RobloxGroupsClientTierRequirementKey

T = TypeVar("T", bound="RobloxGroupsClientTierRequirement")


@_attrs_define
class RobloxGroupsClientTierRequirement:
    """
    Attributes:
        key (RobloxGroupsClientTierRequirementKey):  ['OwnerModerationStatusOk' = 1, 'OwnerAgeEstimationVerified' = 2,
            'OwnerIdVerified' = 3, 'OwnerTwoStepVerified' = 4, 'CommunityMeetsPlayerRequirement' = 5]
        satisfied (bool):
    """

    key: RobloxGroupsClientTierRequirementKey
    satisfied: bool

    def to_dict(self) -> dict[str, Any]:
        key = self.key.value

        satisfied = self.satisfied

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "key": key,
                "satisfied": satisfied,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        key = RobloxGroupsClientTierRequirementKey(d.pop("key"))

        satisfied = d.pop("satisfied")

        roblox_groups_client_tier_requirement = cls(
            key=key,
            satisfied=satisfied,
        )

        return roblox_groups_client_tier_requirement
