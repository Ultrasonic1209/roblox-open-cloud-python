from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_groups_api_update_permissions_request_permissions import (
        RobloxGroupsApiUpdatePermissionsRequestPermissions,
    )


T = TypeVar("T", bound="RobloxGroupsApiUpdatePermissionsRequest")


@_attrs_define
class RobloxGroupsApiUpdatePermissionsRequest:
    """A request model for updating a group's roleset's permissions.

    Attributes:
        permissions (RobloxGroupsApiUpdatePermissionsRequestPermissions | Unset): The permission-value pairs to be
            updated.
    """

    permissions: RobloxGroupsApiUpdatePermissionsRequestPermissions | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        permissions: dict[str, Any] | Unset = UNSET
        if not isinstance(self.permissions, Unset):
            permissions = self.permissions.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if permissions is not UNSET:
            field_dict["permissions"] = permissions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_groups_api_update_permissions_request_permissions import (
            RobloxGroupsApiUpdatePermissionsRequestPermissions,
        )

        d = dict(src_dict)
        _permissions = d.pop("permissions", UNSET)
        permissions: RobloxGroupsApiUpdatePermissionsRequestPermissions | Unset
        if isinstance(_permissions, Unset):
            permissions = UNSET
        else:
            permissions = RobloxGroupsApiUpdatePermissionsRequestPermissions.from_dict(_permissions)

        roblox_groups_api_update_permissions_request = cls(
            permissions=permissions,
        )

        return roblox_groups_api_update_permissions_request
