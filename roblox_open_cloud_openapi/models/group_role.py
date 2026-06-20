from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.group_role_role_permissions import GroupRoleRolePermissions


T = TypeVar("T", bound="GroupRole")


@_attrs_define
class GroupRole:
    """A configurable property to grant specific privileges for members within a
    group.

        Attributes:
            path (str | Unset): The resource path of the group role.

                Format: `groups/{group_id}/roles/{group_role_id}` Example: groups/123/roles/123.
            create_time (datetime.datetime | Unset): The timestamp for when the group role was last updated.

                Visible only to owners of the group. Example: 2023-07-05T12:34:56Z.
            update_time (datetime.datetime | Unset): The timestamp when the group role was last updated.

                Visible only to owners of the group. Example: 2023-07-05T12:34:56Z.
            id (str | Unset): A unique ID that identifies a role.

                Distinct from a role's rank, which is only unique within the group. Example: 200.
            display_name (str | Unset): The name of the role.

                Has a maximum limit of 100 characters. Names above the limit are
                rejected. Example: Member.
            description (str | Unset): The description of the role.

                Has a maximum limit of 1000 characters. Strings above the limit are
                rejected. Visible only to owners of the group. Example: This is a description for the role.
            rank (int | Unset): The rank of the role.

                The minimum value is 0. The maximum value is 255. Example: 1.
            member_count (int | Unset): Total number of members within a role.

                This field is not returned for guest roles. Example: 10223136.
            permissions (GroupRoleRolePermissions | Unset): Represents the permissions on a role.
    """

    path: str | Unset = UNSET
    create_time: datetime.datetime | Unset = UNSET
    update_time: datetime.datetime | Unset = UNSET
    id: str | Unset = UNSET
    display_name: str | Unset = UNSET
    description: str | Unset = UNSET
    rank: int | Unset = UNSET
    member_count: int | Unset = UNSET
    permissions: GroupRoleRolePermissions | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        path = self.path

        create_time: str | Unset = UNSET
        if not isinstance(self.create_time, Unset):
            create_time = self.create_time.isoformat()

        update_time: str | Unset = UNSET
        if not isinstance(self.update_time, Unset):
            update_time = self.update_time.isoformat()

        id = self.id

        display_name = self.display_name

        description = self.description

        rank = self.rank

        member_count = self.member_count

        permissions: dict[str, Any] | Unset = UNSET
        if not isinstance(self.permissions, Unset):
            permissions = self.permissions.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if path is not UNSET:
            field_dict["path"] = path
        if create_time is not UNSET:
            field_dict["createTime"] = create_time
        if update_time is not UNSET:
            field_dict["updateTime"] = update_time
        if id is not UNSET:
            field_dict["id"] = id
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if description is not UNSET:
            field_dict["description"] = description
        if rank is not UNSET:
            field_dict["rank"] = rank
        if member_count is not UNSET:
            field_dict["memberCount"] = member_count
        if permissions is not UNSET:
            field_dict["permissions"] = permissions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.group_role_role_permissions import GroupRoleRolePermissions

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
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

        id = d.pop("id", UNSET)

        display_name = d.pop("displayName", UNSET)

        description = d.pop("description", UNSET)

        rank = d.pop("rank", UNSET)

        member_count = d.pop("memberCount", UNSET)

        _permissions = d.pop("permissions", UNSET)
        permissions: GroupRoleRolePermissions | Unset
        if isinstance(_permissions, Unset):
            permissions = UNSET
        else:
            permissions = GroupRoleRolePermissions.from_dict(_permissions)

        group_role = cls(
            path=path,
            create_time=create_time,
            update_time=update_time,
            id=id,
            display_name=display_name,
            description=description,
            rank=rank,
            member_count=member_count,
            permissions=permissions,
        )

        group_role.additional_properties = d
        return group_role

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
