from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxGroupsApiGroupNameChangeConfigurationResponse")


@_attrs_define
class RobloxGroupsApiGroupNameChangeConfigurationResponse:
    """
    Attributes:
        cost (int | Unset): The cost of renaming a group
        cooldown_in_days (int | Unset): The cooldown for group name changes in days
        ownership_cooldown_in_days (int | Unset): The ownership cooldown for group name changes in days
    """

    cost: int | Unset = UNSET
    cooldown_in_days: int | Unset = UNSET
    ownership_cooldown_in_days: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        cost = self.cost

        cooldown_in_days = self.cooldown_in_days

        ownership_cooldown_in_days = self.ownership_cooldown_in_days

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if cost is not UNSET:
            field_dict["cost"] = cost
        if cooldown_in_days is not UNSET:
            field_dict["cooldownInDays"] = cooldown_in_days
        if ownership_cooldown_in_days is not UNSET:
            field_dict["ownershipCooldownInDays"] = ownership_cooldown_in_days

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        cost = d.pop("cost", UNSET)

        cooldown_in_days = d.pop("cooldownInDays", UNSET)

        ownership_cooldown_in_days = d.pop("ownershipCooldownInDays", UNSET)

        roblox_groups_api_group_name_change_configuration_response = cls(
            cost=cost,
            cooldown_in_days=cooldown_in_days,
            ownership_cooldown_in_days=ownership_cooldown_in_days,
        )

        return roblox_groups_api_group_name_change_configuration_response
