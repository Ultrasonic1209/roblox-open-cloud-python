from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_groups_api_group_policy_response import RobloxGroupsApiGroupPolicyResponse


T = TypeVar("T", bound="RobloxGroupsApiGroupPoliciesResponse")


@_attrs_define
class RobloxGroupsApiGroupPoliciesResponse:
    """
    Attributes:
        groups (list[RobloxGroupsApiGroupPolicyResponse] | Unset):
    """

    groups: list[RobloxGroupsApiGroupPolicyResponse] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        groups: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.groups, Unset):
            groups = []
            for groups_item_data in self.groups:
                groups_item = groups_item_data.to_dict()
                groups.append(groups_item)

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if groups is not UNSET:
            field_dict["groups"] = groups

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_groups_api_group_policy_response import RobloxGroupsApiGroupPolicyResponse

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        _groups = d.pop("groups", UNSET)
        groups: list[RobloxGroupsApiGroupPolicyResponse] | Unset = UNSET
        if _groups is not UNSET:
            groups = []
            for groups_item_data in _groups:
                groups_item = RobloxGroupsApiGroupPolicyResponse.from_dict(groups_item_data)

                groups.append(groups_item)

        roblox_groups_api_group_policies_response = cls(
            groups=groups,
        )

        return roblox_groups_api_group_policies_response
