from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.group_forum_post import GroupForumPost


T = TypeVar("T", bound="ListGroupForumPostsResponse")


@_attrs_define
class ListGroupForumPostsResponse:
    """A list of GroupForumPosts in the parent collection.

    Attributes:
        group_forum_posts (list[GroupForumPost] | Unset): The GroupForumPosts from the specified GroupForumCategory.
        next_page_token (str | Unset): A token that you can send as a `pageToken` parameter to retrieve the next
            page. If this field is omitted, there are no subsequent pages.
    """

    group_forum_posts: list[GroupForumPost] | Unset = UNSET
    next_page_token: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        group_forum_posts: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.group_forum_posts, Unset):
            group_forum_posts = []
            for group_forum_posts_item_data in self.group_forum_posts:
                group_forum_posts_item = group_forum_posts_item_data.to_dict()
                group_forum_posts.append(group_forum_posts_item)

        next_page_token = self.next_page_token

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if group_forum_posts is not UNSET:
            field_dict["groupForumPosts"] = group_forum_posts
        if next_page_token is not UNSET:
            field_dict["nextPageToken"] = next_page_token

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.group_forum_post import GroupForumPost

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        _group_forum_posts = d.pop("groupForumPosts", UNSET)
        group_forum_posts: list[GroupForumPost] | Unset = UNSET
        if _group_forum_posts is not UNSET:
            group_forum_posts = []
            for group_forum_posts_item_data in _group_forum_posts:
                group_forum_posts_item = GroupForumPost.from_dict(group_forum_posts_item_data)

                group_forum_posts.append(group_forum_posts_item)

        next_page_token = d.pop("nextPageToken", UNSET)

        list_group_forum_posts_response = cls(
            group_forum_posts=group_forum_posts,
            next_page_token=next_page_token,
        )

        list_group_forum_posts_response.additional_properties = d
        return list_group_forum_posts_response

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
