from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxUsersApiUserRolesResponse")


@_attrs_define
class RobloxUsersApiUserRolesResponse:
    """A user roles response model.

    Attributes:
        roles (list[str] | Unset): The roles of the user.
    """

    roles: list[str] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        roles: list[str] | Unset = UNSET
        if not isinstance(self.roles, Unset):
            roles = self.roles

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if roles is not UNSET:
            field_dict["roles"] = roles

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        roles = cast(list[str], d.pop("roles", UNSET))

        roblox_users_api_user_roles_response = cls(
            roles=roles,
        )

        return roblox_users_api_user_roles_response
