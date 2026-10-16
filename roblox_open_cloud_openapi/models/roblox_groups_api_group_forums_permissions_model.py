from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxGroupsApiGroupForumsPermissionsModel")


@_attrs_define
class RobloxGroupsApiGroupForumsPermissionsModel:
    """A model representing group posts permissions

    Attributes:
        view_forums (bool | Unset): View forums permission
        manage_categories (bool | Unset): Manage categories permission
        create_posts (bool | Unset): Create posts permission
        remove_posts (bool | Unset): Remove posts permission
        lock_posts (bool | Unset): Lock posts permission
        pin_posts (bool | Unset): Pin posts permission
        create_comments (bool | Unset): Create comments permission
        remove_comments (bool | Unset): Remove comments permission
        create_bug_reports (bool | Unset): Create bug reports (support ticket) permission. Only emitted when the
            permission is exposed
            (Roblox.Groups.Api.Properties.IGroupsApiSettings.ExposeCreateBugReportsPermission).
    """

    view_forums: bool | Unset = UNSET
    manage_categories: bool | Unset = UNSET
    create_posts: bool | Unset = UNSET
    remove_posts: bool | Unset = UNSET
    lock_posts: bool | Unset = UNSET
    pin_posts: bool | Unset = UNSET
    create_comments: bool | Unset = UNSET
    remove_comments: bool | Unset = UNSET
    create_bug_reports: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        view_forums = self.view_forums

        manage_categories = self.manage_categories

        create_posts = self.create_posts

        remove_posts = self.remove_posts

        lock_posts = self.lock_posts

        pin_posts = self.pin_posts

        create_comments = self.create_comments

        remove_comments = self.remove_comments

        create_bug_reports = self.create_bug_reports

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if view_forums is not UNSET:
            field_dict["viewForums"] = view_forums
        if manage_categories is not UNSET:
            field_dict["manageCategories"] = manage_categories
        if create_posts is not UNSET:
            field_dict["createPosts"] = create_posts
        if remove_posts is not UNSET:
            field_dict["removePosts"] = remove_posts
        if lock_posts is not UNSET:
            field_dict["lockPosts"] = lock_posts
        if pin_posts is not UNSET:
            field_dict["pinPosts"] = pin_posts
        if create_comments is not UNSET:
            field_dict["createComments"] = create_comments
        if remove_comments is not UNSET:
            field_dict["removeComments"] = remove_comments
        if create_bug_reports is not UNSET:
            field_dict["createBugReports"] = create_bug_reports

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        view_forums = d.pop("viewForums", UNSET)

        manage_categories = d.pop("manageCategories", UNSET)

        create_posts = d.pop("createPosts", UNSET)

        remove_posts = d.pop("removePosts", UNSET)

        lock_posts = d.pop("lockPosts", UNSET)

        pin_posts = d.pop("pinPosts", UNSET)

        create_comments = d.pop("createComments", UNSET)

        remove_comments = d.pop("removeComments", UNSET)

        create_bug_reports = d.pop("createBugReports", UNSET)

        roblox_groups_api_group_forums_permissions_model = cls(
            view_forums=view_forums,
            manage_categories=manage_categories,
            create_posts=create_posts,
            remove_posts=remove_posts,
            lock_posts=lock_posts,
            pin_posts=pin_posts,
            create_comments=create_comments,
            remove_comments=remove_comments,
            create_bug_reports=create_bug_reports,
        )

        return roblox_groups_api_group_forums_permissions_model
