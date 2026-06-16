from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxGroupsApiGroupPostsPermissionsModel")


@_attrs_define
class RobloxGroupsApiGroupPostsPermissionsModel:
    """A model representing group posts permissions

    Attributes:
        view_wall (bool | Unset): View wall permission
        post_to_wall (bool | Unset): Post to wall permission
        delete_from_wall (bool | Unset): Delete from wall permission
        view_status (bool | Unset): View status permission
        post_to_status (bool | Unset): Post to status permission
    """

    view_wall: bool | Unset = UNSET
    post_to_wall: bool | Unset = UNSET
    delete_from_wall: bool | Unset = UNSET
    view_status: bool | Unset = UNSET
    post_to_status: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        view_wall = self.view_wall

        post_to_wall = self.post_to_wall

        delete_from_wall = self.delete_from_wall

        view_status = self.view_status

        post_to_status = self.post_to_status

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if view_wall is not UNSET:
            field_dict["viewWall"] = view_wall
        if post_to_wall is not UNSET:
            field_dict["postToWall"] = post_to_wall
        if delete_from_wall is not UNSET:
            field_dict["deleteFromWall"] = delete_from_wall
        if view_status is not UNSET:
            field_dict["viewStatus"] = view_status
        if post_to_status is not UNSET:
            field_dict["postToStatus"] = post_to_status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        view_wall = d.pop("viewWall", UNSET)

        post_to_wall = d.pop("postToWall", UNSET)

        delete_from_wall = d.pop("deleteFromWall", UNSET)

        view_status = d.pop("viewStatus", UNSET)

        post_to_status = d.pop("postToStatus", UNSET)

        roblox_groups_api_group_posts_permissions_model = cls(
            view_wall=view_wall,
            post_to_wall=post_to_wall,
            delete_from_wall=delete_from_wall,
            view_status=view_status,
            post_to_status=post_to_status,
        )

        return roblox_groups_api_group_posts_permissions_model
