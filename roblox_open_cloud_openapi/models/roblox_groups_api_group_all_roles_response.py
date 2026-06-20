from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_groups_api_group_role_response import RobloxGroupsApiGroupRoleResponse


T = TypeVar("T", bound="RobloxGroupsApiGroupAllRolesResponse")


@_attrs_define
class RobloxGroupsApiGroupAllRolesResponse:
    """A group roles response model

    Attributes:
        group_id (int | Unset): The group id
        roles (list[RobloxGroupsApiGroupRoleResponse] | Unset): The roles in the group
    """

    group_id: int | Unset = UNSET
    roles: list[RobloxGroupsApiGroupRoleResponse] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        group_id = self.group_id

        roles: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.roles, Unset):
            roles = []
            for roles_item_data in self.roles:
                roles_item = roles_item_data.to_dict()
                roles.append(roles_item)

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if group_id is not UNSET:
            field_dict["groupId"] = group_id
        if roles is not UNSET:
            field_dict["roles"] = roles

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_groups_api_group_role_response import RobloxGroupsApiGroupRoleResponse

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        group_id = d.pop("groupId", UNSET)

        _roles = d.pop("roles", UNSET)
        roles: list[RobloxGroupsApiGroupRoleResponse] | Unset = UNSET
        if _roles is not UNSET:
            roles = []
            for roles_item_data in _roles:
                roles_item = RobloxGroupsApiGroupRoleResponse.from_dict(roles_item_data)

                roles.append(roles_item)

        roblox_groups_api_group_all_roles_response = cls(
            group_id=group_id,
            roles=roles,
        )

        return roblox_groups_api_group_all_roles_response
