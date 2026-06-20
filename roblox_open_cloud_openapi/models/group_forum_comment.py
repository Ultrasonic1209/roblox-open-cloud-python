from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.content_message import ContentMessage


T = TypeVar("T", bound="GroupForumComment")


@_attrs_define
class GroupForumComment:
    """Represents a forum comment on a group's forum post.

    Attributes:
        path (str | Unset): The resource path of the group forum comment.

            Format:
            `groups/{group_id}/forum-
            categories/{group_forum_category_id}/posts/{group_forum_post_id}/comments/{group_forum_comment_id}` Example:
            groups/123/forum-categories/01234567-89ab-cdef-0123-456789abcdef/posts/01234567-89ab-
            cdef-0123-456789abcdef/comments/01234567-89ab-cdef-0123-456789abcdef.
        group_forum_comment_id (str | Unset): The id of the group forum comment.
        message (ContentMessage | Unset): Represents the content of a message.
    """

    path: str | Unset = UNSET
    group_forum_comment_id: str | Unset = UNSET
    message: ContentMessage | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        path = self.path

        group_forum_comment_id = self.group_forum_comment_id

        message: dict[str, Any] | Unset = UNSET
        if not isinstance(self.message, Unset):
            message = self.message.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if path is not UNSET:
            field_dict["path"] = path
        if group_forum_comment_id is not UNSET:
            field_dict["groupForumCommentId"] = group_forum_comment_id
        if message is not UNSET:
            field_dict["message"] = message

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.content_message import ContentMessage

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        path = d.pop("path", UNSET)

        group_forum_comment_id = d.pop("groupForumCommentId", UNSET)

        _message = d.pop("message", UNSET)
        message: ContentMessage | Unset
        if isinstance(_message, Unset):
            message = UNSET
        else:
            message = ContentMessage.from_dict(_message)

        group_forum_comment = cls(
            path=path,
            group_forum_comment_id=group_forum_comment_id,
            message=message,
        )

        group_forum_comment.additional_properties = d
        return group_forum_comment

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
