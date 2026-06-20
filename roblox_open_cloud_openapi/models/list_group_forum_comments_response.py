from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.group_forum_comment import GroupForumComment


T = TypeVar("T", bound="ListGroupForumCommentsResponse")


@_attrs_define
class ListGroupForumCommentsResponse:
    """A list of GroupForumComments in the parent collection.

    Attributes:
        group_forum_comments (list[GroupForumComment] | Unset): The GroupForumComments from the specified
            GroupForumPost.
        next_page_token (str | Unset): A token that you can send as a `pageToken` parameter to retrieve the next
            page. If this field is omitted, there are no subsequent pages.
    """

    group_forum_comments: list[GroupForumComment] | Unset = UNSET
    next_page_token: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        group_forum_comments: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.group_forum_comments, Unset):
            group_forum_comments = []
            for group_forum_comments_item_data in self.group_forum_comments:
                group_forum_comments_item = group_forum_comments_item_data.to_dict()
                group_forum_comments.append(group_forum_comments_item)

        next_page_token = self.next_page_token

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if group_forum_comments is not UNSET:
            field_dict["groupForumComments"] = group_forum_comments
        if next_page_token is not UNSET:
            field_dict["nextPageToken"] = next_page_token

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.group_forum_comment import GroupForumComment

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        _group_forum_comments = d.pop("groupForumComments", UNSET)
        group_forum_comments: list[GroupForumComment] | Unset = UNSET
        if _group_forum_comments is not UNSET:
            group_forum_comments = []
            for group_forum_comments_item_data in _group_forum_comments:
                group_forum_comments_item = GroupForumComment.from_dict(group_forum_comments_item_data)

                group_forum_comments.append(group_forum_comments_item)

        next_page_token = d.pop("nextPageToken", UNSET)

        list_group_forum_comments_response = cls(
            group_forum_comments=group_forum_comments,
            next_page_token=next_page_token,
        )

        list_group_forum_comments_response.additional_properties = d
        return list_group_forum_comments_response

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
