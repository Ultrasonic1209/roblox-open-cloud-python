from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxGroupsApiUpdateUserRoleRequest")


@_attrs_define
class RobloxGroupsApiUpdateUserRoleRequest:
    """A request model for setting a users role in a group.

    Attributes:
        role_id (int | Unset): The role in the group the user should be put into.
    """

    role_id: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        role_id = self.role_id

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if role_id is not UNSET:
            field_dict["roleId"] = role_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        role_id = d.pop("roleId", UNSET)

        roblox_groups_api_update_user_role_request = cls(
            role_id=role_id,
        )

        return roblox_groups_api_update_user_role_request
