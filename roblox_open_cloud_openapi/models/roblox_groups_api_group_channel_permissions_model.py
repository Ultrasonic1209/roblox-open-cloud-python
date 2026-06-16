from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_groups_api_group_forums_permissions_model import RobloxGroupsApiGroupForumsPermissionsModel


T = TypeVar("T", bound="RobloxGroupsApiGroupChannelPermissionsModel")


@_attrs_define
class RobloxGroupsApiGroupChannelPermissionsModel:
    """A model for communication channel permissions.

    Attributes:
        channel_id (str | Unset): Group Channel Id
        group_forums_permissions (RobloxGroupsApiGroupForumsPermissionsModel | Unset): A model representing group posts
            permissions
    """

    channel_id: str | Unset = UNSET
    group_forums_permissions: RobloxGroupsApiGroupForumsPermissionsModel | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        channel_id = self.channel_id

        group_forums_permissions: dict[str, Any] | Unset = UNSET
        if not isinstance(self.group_forums_permissions, Unset):
            group_forums_permissions = self.group_forums_permissions.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if channel_id is not UNSET:
            field_dict["channelId"] = channel_id
        if group_forums_permissions is not UNSET:
            field_dict["groupForumsPermissions"] = group_forums_permissions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_groups_api_group_forums_permissions_model import RobloxGroupsApiGroupForumsPermissionsModel

        d = dict(src_dict)
        channel_id = d.pop("channelId", UNSET)

        _group_forums_permissions = d.pop("groupForumsPermissions", UNSET)
        group_forums_permissions: RobloxGroupsApiGroupForumsPermissionsModel | Unset
        if isinstance(_group_forums_permissions, Unset):
            group_forums_permissions = UNSET
        else:
            group_forums_permissions = RobloxGroupsApiGroupForumsPermissionsModel.from_dict(_group_forums_permissions)

        roblox_groups_api_group_channel_permissions_model = cls(
            channel_id=channel_id,
            group_forums_permissions=group_forums_permissions,
        )

        return roblox_groups_api_group_channel_permissions_model
