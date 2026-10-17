from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxGroupsApiGroupPolicyResponse")


@_attrs_define
class RobloxGroupsApiGroupPolicyResponse:
    """
    Attributes:
        can_view_group (bool | Unset):
        group_id (int | Unset):
    """

    can_view_group: bool | Unset = UNSET
    group_id: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        can_view_group = self.can_view_group

        group_id = self.group_id

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if can_view_group is not UNSET:
            field_dict["canViewGroup"] = can_view_group
        if group_id is not UNSET:
            field_dict["groupId"] = group_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        can_view_group = d.pop("canViewGroup", UNSET)

        group_id = d.pop("groupId", UNSET)

        roblox_groups_api_group_policy_response = cls(
            can_view_group=can_view_group,
            group_id=group_id,
        )

        return roblox_groups_api_group_policy_response
