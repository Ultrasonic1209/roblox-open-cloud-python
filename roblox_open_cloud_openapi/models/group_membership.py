from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GroupMembership")


@_attrs_define
class GroupMembership:
    """A membership to a group. A user ID can be used in place of a membership ID.

    Attributes:
        path (str | Unset): The resource path of the group membership.

            Format: `groups/{group_id}/memberships/{group_membership_id}` Example: groups/123/memberships/123.
        create_time (datetime.datetime | Unset): The timestamp when the group membership was created. Example:
            2023-07-05T12:34:56Z.
        update_time (datetime.datetime | Unset): The timestamp when the group membership was last updated. Example:
            2023-07-05T12:34:56Z.
        user (str | Unset): The resource path of a member of the group. Example: users/21557.
        role (str | Unset): The resource path of the member's highest-ranked role.
            When the member holds multiple roles, this reflects only the
            highest-ranked one. Prefer using the `roles` field, which always
            contains the complete set of assigned roles. Example: groups/7/roles/99513316.
        roles (list[str] | Unset): The resource paths of all roles assigned to the group member.
            This is the recommended field for reading a member's roles, as it
            always contains the complete set of roles held by the member. Example: groups/7/roles/99513316.
    """

    path: str | Unset = UNSET
    create_time: datetime.datetime | Unset = UNSET
    update_time: datetime.datetime | Unset = UNSET
    user: str | Unset = UNSET
    role: str | Unset = UNSET
    roles: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        path = self.path

        create_time: str | Unset = UNSET
        if not isinstance(self.create_time, Unset):
            create_time = self.create_time.isoformat()

        update_time: str | Unset = UNSET
        if not isinstance(self.update_time, Unset):
            update_time = self.update_time.isoformat()

        user = self.user

        role = self.role

        roles: list[str] | Unset = UNSET
        if not isinstance(self.roles, Unset):
            roles = self.roles

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if path is not UNSET:
            field_dict["path"] = path
        if create_time is not UNSET:
            field_dict["createTime"] = create_time
        if update_time is not UNSET:
            field_dict["updateTime"] = update_time
        if user is not UNSET:
            field_dict["user"] = user
        if role is not UNSET:
            field_dict["role"] = role
        if roles is not UNSET:
            field_dict["roles"] = roles

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        path = d.pop("path", UNSET)

        _create_time = d.pop("createTime", UNSET)
        create_time: datetime.datetime | Unset
        if isinstance(_create_time, Unset):
            create_time = UNSET
        else:
            create_time = datetime.datetime.fromisoformat(_create_time)

        _update_time = d.pop("updateTime", UNSET)
        update_time: datetime.datetime | Unset
        if isinstance(_update_time, Unset):
            update_time = UNSET
        else:
            update_time = datetime.datetime.fromisoformat(_update_time)

        user = d.pop("user", UNSET)

        role = d.pop("role", UNSET)

        roles = cast(list[str], d.pop("roles", UNSET))

        group_membership = cls(
            path=path,
            create_time=create_time,
            update_time=update_time,
            user=user,
            role=role,
            roles=roles,
        )

        group_membership.additional_properties = d
        return group_membership

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
