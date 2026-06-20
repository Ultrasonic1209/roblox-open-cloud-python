from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.group_forum_comment import GroupForumComment


T = TypeVar("T", bound="GroupForumPost")


@_attrs_define
class GroupForumPost:
    """Represents a forum post within a group's forum category.

    Attributes:
        path (str | Unset): The resource path of the group forum post.

            Format:
            `groups/{group_id}/forum-categories/{group_forum_category_id}/posts/{group_forum_post_id}` Example:
            groups/123/forum-categories/01234567-89ab-cdef-0123-456789abcdef/posts/01234567-89ab-cdef-0123-456789abcdef.
        create_time (datetime.datetime | Unset): The timestamp when the group forum post was created. Example:
            2023-07-05T12:34:56Z.
        update_time (datetime.datetime | Unset): The timestamp when the group forum post was last updated. Example:
            2023-07-05T12:34:56Z.
        pinned (bool | Unset): Whether the group forum post is pinned. Example: True.
        locked (bool | Unset): Whether the group forum post is locked. Example: True.
        group_forum_post_id (str | Unset): The id of the group forum post.
        title (str | Unset): The title of the group forum post.
        first_comment (GroupForumComment | Unset): Represents a forum comment on a group's forum post.
        author (str | Unset): The resource path of the user who created the group forum post. Example: users/156.
        archive_time (datetime.datetime | Unset): The timestamp when the group forum post was archived. Example:
            2023-07-05T12:34:56Z.
        archiver (str | Unset): The resource path of the user who archived the group forum post. Example: users/156.
        comment_count (int | Unset): The number of comments on the group forum post. This includes the first
            comment (post content).
    """

    path: str | Unset = UNSET
    create_time: datetime.datetime | Unset = UNSET
    update_time: datetime.datetime | Unset = UNSET
    pinned: bool | Unset = UNSET
    locked: bool | Unset = UNSET
    group_forum_post_id: str | Unset = UNSET
    title: str | Unset = UNSET
    first_comment: GroupForumComment | Unset = UNSET
    author: str | Unset = UNSET
    archive_time: datetime.datetime | Unset = UNSET
    archiver: str | Unset = UNSET
    comment_count: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        path = self.path

        create_time: str | Unset = UNSET
        if not isinstance(self.create_time, Unset):
            create_time = self.create_time.isoformat()

        update_time: str | Unset = UNSET
        if not isinstance(self.update_time, Unset):
            update_time = self.update_time.isoformat()

        pinned = self.pinned

        locked = self.locked

        group_forum_post_id = self.group_forum_post_id

        title = self.title

        first_comment: dict[str, Any] | Unset = UNSET
        if not isinstance(self.first_comment, Unset):
            first_comment = self.first_comment.to_dict()

        author = self.author

        archive_time: str | Unset = UNSET
        if not isinstance(self.archive_time, Unset):
            archive_time = self.archive_time.isoformat()

        archiver = self.archiver

        comment_count = self.comment_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if path is not UNSET:
            field_dict["path"] = path
        if create_time is not UNSET:
            field_dict["createTime"] = create_time
        if update_time is not UNSET:
            field_dict["updateTime"] = update_time
        if pinned is not UNSET:
            field_dict["pinned"] = pinned
        if locked is not UNSET:
            field_dict["locked"] = locked
        if group_forum_post_id is not UNSET:
            field_dict["groupForumPostId"] = group_forum_post_id
        if title is not UNSET:
            field_dict["title"] = title
        if first_comment is not UNSET:
            field_dict["firstComment"] = first_comment
        if author is not UNSET:
            field_dict["author"] = author
        if archive_time is not UNSET:
            field_dict["archiveTime"] = archive_time
        if archiver is not UNSET:
            field_dict["archiver"] = archiver
        if comment_count is not UNSET:
            field_dict["commentCount"] = comment_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.group_forum_comment import GroupForumComment

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

        pinned = d.pop("pinned", UNSET)

        locked = d.pop("locked", UNSET)

        group_forum_post_id = d.pop("groupForumPostId", UNSET)

        title = d.pop("title", UNSET)

        _first_comment = d.pop("firstComment", UNSET)
        first_comment: GroupForumComment | Unset
        if isinstance(_first_comment, Unset):
            first_comment = UNSET
        else:
            first_comment = GroupForumComment.from_dict(_first_comment)

        author = d.pop("author", UNSET)

        _archive_time = d.pop("archiveTime", UNSET)
        archive_time: datetime.datetime | Unset
        if isinstance(_archive_time, Unset):
            archive_time = UNSET
        else:
            archive_time = datetime.datetime.fromisoformat(_archive_time)

        archiver = d.pop("archiver", UNSET)

        comment_count = d.pop("commentCount", UNSET)

        group_forum_post = cls(
            path=path,
            create_time=create_time,
            update_time=update_time,
            pinned=pinned,
            locked=locked,
            group_forum_post_id=group_forum_post_id,
            title=title,
            first_comment=first_comment,
            author=author,
            archive_time=archive_time,
            archiver=archiver,
            comment_count=comment_count,
        )

        group_forum_post.additional_properties = d
        return group_forum_post

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
