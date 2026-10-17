from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Group")


@_attrs_define
class Group:
    """A mini-community within Roblox for communication, discussions, and more.

    Attributes:
        path (str | Unset): The resource path of the group.

            Format: `groups/{group_id}` Example: groups/123.
        create_time (datetime.datetime | Unset): The timestamp when the group was created. Example:
            2023-07-05T12:34:56Z.
        update_time (datetime.datetime | Unset): The timestamp when the group was last updated. Example:
            2023-07-05T12:34:56Z.
        id (str | Unset): A unique ID that identifies the group. Example: 7.
        display_name (str | Unset): The name of the group.

            Must be non-empty. Has a maximum limit of 50 characters. Example: Roblox.
        description (str | Unset): The description of the group.

            Has a maximum limit of 1000 characters. Example: Official fan club of Roblox!.
        owner (str | Unset): The resource path of the owner.

            If the group is abandoned and has no owner, this field is not returned. Example: users/21557.
        member_count (int | Unset): The total number of members within a group. Example: 10196297.
        public_entry_allowed (bool | Unset): Whether the group allows public entry. Example: True.
        locked (bool | Unset): Whether the group is locked.

            A locked group is a group that has been
            moderated/banned by Roblox. Example: True.
        verified (bool | Unset): Whether the group has the verified badge. Example: True.
    """

    path: str | Unset = UNSET
    create_time: datetime.datetime | Unset = UNSET
    update_time: datetime.datetime | Unset = UNSET
    id: str | Unset = UNSET
    display_name: str | Unset = UNSET
    description: str | Unset = UNSET
    owner: str | Unset = UNSET
    member_count: int | Unset = UNSET
    public_entry_allowed: bool | Unset = UNSET
    locked: bool | Unset = UNSET
    verified: bool | Unset = UNSET
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

        owner = self.owner

        member_count = self.member_count

        public_entry_allowed = self.public_entry_allowed

        locked = self.locked

        verified = self.verified

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
        if owner is not UNSET:
            field_dict["owner"] = owner
        if member_count is not UNSET:
            field_dict["memberCount"] = member_count
        if public_entry_allowed is not UNSET:
            field_dict["publicEntryAllowed"] = public_entry_allowed
        if locked is not UNSET:
            field_dict["locked"] = locked
        if verified is not UNSET:
            field_dict["verified"] = verified

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

        id = d.pop("id", UNSET)

        display_name = d.pop("displayName", UNSET)

        description = d.pop("description", UNSET)

        owner = d.pop("owner", UNSET)

        member_count = d.pop("memberCount", UNSET)

        public_entry_allowed = d.pop("publicEntryAllowed", UNSET)

        locked = d.pop("locked", UNSET)

        verified = d.pop("verified", UNSET)

        group = cls(
            path=path,
            create_time=create_time,
            update_time=update_time,
            id=id,
            display_name=display_name,
            description=description,
            owner=owner,
            member_count=member_count,
            public_entry_allowed=public_entry_allowed,
            locked=locked,
            verified=verified,
        )

        group.additional_properties = d
        return group

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
