from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_groups_api_group_permissions_model import RobloxGroupsApiGroupPermissionsModel
    from ..models.roblox_groups_api_group_role_response import RobloxGroupsApiGroupRoleResponse


T = TypeVar("T", bound="RobloxGroupsApiGroupPermissionsResponse")


@_attrs_define
class RobloxGroupsApiGroupPermissionsResponse:
    """A group role's permissions response model

    Attributes:
        group_id (int | Unset): The group id
        role (RobloxGroupsApiGroupRoleResponse | Unset): A group role response model
        permissions (RobloxGroupsApiGroupPermissionsModel | Unset): A model for group permissions.
    """

    group_id: int | Unset = UNSET
    role: RobloxGroupsApiGroupRoleResponse | Unset = UNSET
    permissions: RobloxGroupsApiGroupPermissionsModel | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        group_id = self.group_id

        role: dict[str, Any] | Unset = UNSET
        if not isinstance(self.role, Unset):
            role = self.role.to_dict()

        permissions: dict[str, Any] | Unset = UNSET
        if not isinstance(self.permissions, Unset):
            permissions = self.permissions.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if group_id is not UNSET:
            field_dict["groupId"] = group_id
        if role is not UNSET:
            field_dict["role"] = role
        if permissions is not UNSET:
            field_dict["permissions"] = permissions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_groups_api_group_permissions_model import RobloxGroupsApiGroupPermissionsModel
        from ..models.roblox_groups_api_group_role_response import RobloxGroupsApiGroupRoleResponse

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        group_id = d.pop("groupId", UNSET)

        _role = d.pop("role", UNSET)
        role: RobloxGroupsApiGroupRoleResponse | Unset
        if isinstance(_role, Unset):
            role = UNSET
        else:
            role = RobloxGroupsApiGroupRoleResponse.from_dict(_role)

        _permissions = d.pop("permissions", UNSET)
        permissions: RobloxGroupsApiGroupPermissionsModel | Unset
        if isinstance(_permissions, Unset):
            permissions = UNSET
        else:
            permissions = RobloxGroupsApiGroupPermissionsModel.from_dict(_permissions)

        roblox_groups_api_group_permissions_response = cls(
            group_id=group_id,
            role=role,
            permissions=permissions,
        )

        return roblox_groups_api_group_permissions_response
