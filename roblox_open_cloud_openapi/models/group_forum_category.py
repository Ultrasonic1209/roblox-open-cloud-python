from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GroupForumCategory")


@_attrs_define
class GroupForumCategory:
    """Represents a forum category within a group for user discussions.

    Attributes:
        path (str | Unset): The resource path of the group forum category.

            Format: `groups/{group_id}/forum-categories/{group_forum_category_id}` Example: groups/123/forum-
            categories/01234567-89ab-cdef-0123-456789abcdef.
        create_time (datetime.datetime | Unset): The timestamp when the group forum category was created. Example:
            2023-07-05T12:34:56Z.
        update_time (datetime.datetime | Unset): The timestamp when the group forum category was last updated. Example:
            2023-07-05T12:34:56Z.
        group_forum_category_id (str | Unset): The id of the group forum category.
        display_name (str | Unset): The display name of the group forum category.
        creator (str | Unset): The resource path of the user who created the group forum category. Example: users/156.
        archive_time (datetime.datetime | Unset): The timestamp when the group forum category was archived. Example:
            2023-07-05T12:34:56Z.
        archiver (str | Unset): The resource path of the user who archived the group forum category. Example: users/156.
    """

    path: str | Unset = UNSET
    create_time: datetime.datetime | Unset = UNSET
    update_time: datetime.datetime | Unset = UNSET
    group_forum_category_id: str | Unset = UNSET
    display_name: str | Unset = UNSET
    creator: str | Unset = UNSET
    archive_time: datetime.datetime | Unset = UNSET
    archiver: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        path = self.path

        create_time: str | Unset = UNSET
        if not isinstance(self.create_time, Unset):
            create_time = self.create_time.isoformat()

        update_time: str | Unset = UNSET
        if not isinstance(self.update_time, Unset):
            update_time = self.update_time.isoformat()

        group_forum_category_id = self.group_forum_category_id

        display_name = self.display_name

        creator = self.creator

        archive_time: str | Unset = UNSET
        if not isinstance(self.archive_time, Unset):
            archive_time = self.archive_time.isoformat()

        archiver = self.archiver

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if path is not UNSET:
            field_dict["path"] = path
        if create_time is not UNSET:
            field_dict["createTime"] = create_time
        if update_time is not UNSET:
            field_dict["updateTime"] = update_time
        if group_forum_category_id is not UNSET:
            field_dict["groupForumCategoryId"] = group_forum_category_id
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if creator is not UNSET:
            field_dict["creator"] = creator
        if archive_time is not UNSET:
            field_dict["archiveTime"] = archive_time
        if archiver is not UNSET:
            field_dict["archiver"] = archiver

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

        group_forum_category_id = d.pop("groupForumCategoryId", UNSET)

        display_name = d.pop("displayName", UNSET)

        creator = d.pop("creator", UNSET)

        _archive_time = d.pop("archiveTime", UNSET)
        archive_time: datetime.datetime | Unset
        if isinstance(_archive_time, Unset):
            archive_time = UNSET
        else:
            archive_time = datetime.datetime.fromisoformat(_archive_time)

        archiver = d.pop("archiver", UNSET)

        group_forum_category = cls(
            path=path,
            create_time=create_time,
            update_time=update_time,
            group_forum_category_id=group_forum_category_id,
            display_name=display_name,
            creator=creator,
            archive_time=archive_time,
            archiver=archiver,
        )

        group_forum_category.additional_properties = d
        return group_forum_category

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
