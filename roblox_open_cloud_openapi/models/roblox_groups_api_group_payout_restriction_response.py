from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxGroupsApiGroupPayoutRestrictionResponse")


@_attrs_define
class RobloxGroupsApiGroupPayoutRestrictionResponse:
    """Response model for Group Payout Restriction

    Attributes:
        can_use_recurring_payout (bool | Unset): Whether the group can use recurring payout feature.
        can_use_one_time_payout (bool | Unset): Whether the group can use one-time payout feature.
    """

    can_use_recurring_payout: bool | Unset = UNSET
    can_use_one_time_payout: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        can_use_recurring_payout = self.can_use_recurring_payout

        can_use_one_time_payout = self.can_use_one_time_payout

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if can_use_recurring_payout is not UNSET:
            field_dict["canUseRecurringPayout"] = can_use_recurring_payout
        if can_use_one_time_payout is not UNSET:
            field_dict["canUseOneTimePayout"] = can_use_one_time_payout

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        can_use_recurring_payout = d.pop("canUseRecurringPayout", UNSET)

        can_use_one_time_payout = d.pop("canUseOneTimePayout", UNSET)

        roblox_groups_api_group_payout_restriction_response = cls(
            can_use_recurring_payout=can_use_recurring_payout,
            can_use_one_time_payout=can_use_one_time_payout,
        )

        return roblox_groups_api_group_payout_restriction_response
