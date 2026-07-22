from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxGroupsClientCommunityTierInfoResponse")


@_attrs_define
class RobloxGroupsClientCommunityTierInfoResponse:
    """
    Attributes:
        group_id (int | Unset):
        current_tier (int | Unset):
        previous_tier (int | Unset):
        tier_updated_time (datetime.datetime | Unset):
        last_evaluated_time (datetime.datetime | Unset):
    """

    group_id: int | Unset = UNSET
    current_tier: int | Unset = UNSET
    previous_tier: int | Unset = UNSET
    tier_updated_time: datetime.datetime | Unset = UNSET
    last_evaluated_time: datetime.datetime | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        group_id = self.group_id

        current_tier = self.current_tier

        previous_tier = self.previous_tier

        tier_updated_time: str | Unset = UNSET
        if not isinstance(self.tier_updated_time, Unset):
            tier_updated_time = self.tier_updated_time.isoformat()

        last_evaluated_time: str | Unset = UNSET
        if not isinstance(self.last_evaluated_time, Unset):
            last_evaluated_time = self.last_evaluated_time.isoformat()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if group_id is not UNSET:
            field_dict["groupId"] = group_id
        if current_tier is not UNSET:
            field_dict["currentTier"] = current_tier
        if previous_tier is not UNSET:
            field_dict["previousTier"] = previous_tier
        if tier_updated_time is not UNSET:
            field_dict["tierUpdatedTime"] = tier_updated_time
        if last_evaluated_time is not UNSET:
            field_dict["lastEvaluatedTime"] = last_evaluated_time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        group_id = d.pop("groupId", UNSET)

        current_tier = d.pop("currentTier", UNSET)

        previous_tier = d.pop("previousTier", UNSET)

        _tier_updated_time = d.pop("tierUpdatedTime", UNSET)
        tier_updated_time: datetime.datetime | Unset
        if isinstance(_tier_updated_time, Unset):
            tier_updated_time = UNSET
        else:
            tier_updated_time = datetime.datetime.fromisoformat(_tier_updated_time)

        _last_evaluated_time = d.pop("lastEvaluatedTime", UNSET)
        last_evaluated_time: datetime.datetime | Unset
        if isinstance(_last_evaluated_time, Unset):
            last_evaluated_time = UNSET
        else:
            last_evaluated_time = datetime.datetime.fromisoformat(_last_evaluated_time)

        roblox_groups_client_community_tier_info_response = cls(
            group_id=group_id,
            current_tier=current_tier,
            previous_tier=previous_tier,
            tier_updated_time=tier_updated_time,
            last_evaluated_time=last_evaluated_time,
        )

        return roblox_groups_client_community_tier_info_response
