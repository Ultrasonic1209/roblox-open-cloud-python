from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_groups_api_group_content_moderation_permissions_model import (
        RobloxGroupsApiGroupContentModerationPermissionsModel,
    )
    from ..models.roblox_groups_api_group_economy_permissions_model import RobloxGroupsApiGroupEconomyPermissionsModel
    from ..models.roblox_groups_api_group_forums_permissions_model import RobloxGroupsApiGroupForumsPermissionsModel
    from ..models.roblox_groups_api_group_management_permissions_model import (
        RobloxGroupsApiGroupManagementPermissionsModel,
    )
    from ..models.roblox_groups_api_group_membership_permissions_model import (
        RobloxGroupsApiGroupMembershipPermissionsModel,
    )
    from ..models.roblox_groups_api_group_open_cloud_permissions_model import (
        RobloxGroupsApiGroupOpenCloudPermissionsModel,
    )
    from ..models.roblox_groups_api_group_posts_permissions_model import RobloxGroupsApiGroupPostsPermissionsModel


T = TypeVar("T", bound="RobloxGroupsApiGroupPermissionsModel")


@_attrs_define
class RobloxGroupsApiGroupPermissionsModel:
    """A model for group permissions.

    Attributes:
        group_posts_permissions (RobloxGroupsApiGroupPostsPermissionsModel | Unset): A model representing group posts
            permissions
        group_forums_permissions (RobloxGroupsApiGroupForumsPermissionsModel | Unset): A model representing group posts
            permissions
        group_content_moderation_permissions (RobloxGroupsApiGroupContentModerationPermissionsModel | Unset): A model
            representing group content moderation permissions
        group_membership_permissions (RobloxGroupsApiGroupMembershipPermissionsModel | Unset): A model representing data
            about an Roblox.Platform.Membership.IUser
        group_management_permissions (RobloxGroupsApiGroupManagementPermissionsModel | Unset): A model representing data
            about an Roblox.Platform.Membership.IUser
        group_economy_permissions (RobloxGroupsApiGroupEconomyPermissionsModel | Unset): A model representing data about
            an Roblox.Platform.Membership.IUser
        group_open_cloud_permissions (RobloxGroupsApiGroupOpenCloudPermissionsModel | Unset):
    """

    group_posts_permissions: RobloxGroupsApiGroupPostsPermissionsModel | Unset = UNSET
    group_forums_permissions: RobloxGroupsApiGroupForumsPermissionsModel | Unset = UNSET
    group_content_moderation_permissions: RobloxGroupsApiGroupContentModerationPermissionsModel | Unset = UNSET
    group_membership_permissions: RobloxGroupsApiGroupMembershipPermissionsModel | Unset = UNSET
    group_management_permissions: RobloxGroupsApiGroupManagementPermissionsModel | Unset = UNSET
    group_economy_permissions: RobloxGroupsApiGroupEconomyPermissionsModel | Unset = UNSET
    group_open_cloud_permissions: RobloxGroupsApiGroupOpenCloudPermissionsModel | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        group_posts_permissions: dict[str, Any] | Unset = UNSET
        if not isinstance(self.group_posts_permissions, Unset):
            group_posts_permissions = self.group_posts_permissions.to_dict()

        group_forums_permissions: dict[str, Any] | Unset = UNSET
        if not isinstance(self.group_forums_permissions, Unset):
            group_forums_permissions = self.group_forums_permissions.to_dict()

        group_content_moderation_permissions: dict[str, Any] | Unset = UNSET
        if not isinstance(self.group_content_moderation_permissions, Unset):
            group_content_moderation_permissions = self.group_content_moderation_permissions.to_dict()

        group_membership_permissions: dict[str, Any] | Unset = UNSET
        if not isinstance(self.group_membership_permissions, Unset):
            group_membership_permissions = self.group_membership_permissions.to_dict()

        group_management_permissions: dict[str, Any] | Unset = UNSET
        if not isinstance(self.group_management_permissions, Unset):
            group_management_permissions = self.group_management_permissions.to_dict()

        group_economy_permissions: dict[str, Any] | Unset = UNSET
        if not isinstance(self.group_economy_permissions, Unset):
            group_economy_permissions = self.group_economy_permissions.to_dict()

        group_open_cloud_permissions: dict[str, Any] | Unset = UNSET
        if not isinstance(self.group_open_cloud_permissions, Unset):
            group_open_cloud_permissions = self.group_open_cloud_permissions.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if group_posts_permissions is not UNSET:
            field_dict["groupPostsPermissions"] = group_posts_permissions
        if group_forums_permissions is not UNSET:
            field_dict["groupForumsPermissions"] = group_forums_permissions
        if group_content_moderation_permissions is not UNSET:
            field_dict["groupContentModerationPermissions"] = group_content_moderation_permissions
        if group_membership_permissions is not UNSET:
            field_dict["groupMembershipPermissions"] = group_membership_permissions
        if group_management_permissions is not UNSET:
            field_dict["groupManagementPermissions"] = group_management_permissions
        if group_economy_permissions is not UNSET:
            field_dict["groupEconomyPermissions"] = group_economy_permissions
        if group_open_cloud_permissions is not UNSET:
            field_dict["groupOpenCloudPermissions"] = group_open_cloud_permissions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_groups_api_group_content_moderation_permissions_model import (
            RobloxGroupsApiGroupContentModerationPermissionsModel,
        )
        from ..models.roblox_groups_api_group_economy_permissions_model import (
            RobloxGroupsApiGroupEconomyPermissionsModel,
        )
        from ..models.roblox_groups_api_group_forums_permissions_model import RobloxGroupsApiGroupForumsPermissionsModel
        from ..models.roblox_groups_api_group_management_permissions_model import (
            RobloxGroupsApiGroupManagementPermissionsModel,
        )
        from ..models.roblox_groups_api_group_membership_permissions_model import (
            RobloxGroupsApiGroupMembershipPermissionsModel,
        )
        from ..models.roblox_groups_api_group_open_cloud_permissions_model import (
            RobloxGroupsApiGroupOpenCloudPermissionsModel,
        )
        from ..models.roblox_groups_api_group_posts_permissions_model import RobloxGroupsApiGroupPostsPermissionsModel

        d = dict(src_dict)
        _group_posts_permissions = d.pop("groupPostsPermissions", UNSET)
        group_posts_permissions: RobloxGroupsApiGroupPostsPermissionsModel | Unset
        if isinstance(_group_posts_permissions, Unset):
            group_posts_permissions = UNSET
        else:
            group_posts_permissions = RobloxGroupsApiGroupPostsPermissionsModel.from_dict(_group_posts_permissions)

        _group_forums_permissions = d.pop("groupForumsPermissions", UNSET)
        group_forums_permissions: RobloxGroupsApiGroupForumsPermissionsModel | Unset
        if isinstance(_group_forums_permissions, Unset):
            group_forums_permissions = UNSET
        else:
            group_forums_permissions = RobloxGroupsApiGroupForumsPermissionsModel.from_dict(_group_forums_permissions)

        _group_content_moderation_permissions = d.pop("groupContentModerationPermissions", UNSET)
        group_content_moderation_permissions: RobloxGroupsApiGroupContentModerationPermissionsModel | Unset
        if isinstance(_group_content_moderation_permissions, Unset):
            group_content_moderation_permissions = UNSET
        else:
            group_content_moderation_permissions = RobloxGroupsApiGroupContentModerationPermissionsModel.from_dict(
                _group_content_moderation_permissions
            )

        _group_membership_permissions = d.pop("groupMembershipPermissions", UNSET)
        group_membership_permissions: RobloxGroupsApiGroupMembershipPermissionsModel | Unset
        if isinstance(_group_membership_permissions, Unset):
            group_membership_permissions = UNSET
        else:
            group_membership_permissions = RobloxGroupsApiGroupMembershipPermissionsModel.from_dict(
                _group_membership_permissions
            )

        _group_management_permissions = d.pop("groupManagementPermissions", UNSET)
        group_management_permissions: RobloxGroupsApiGroupManagementPermissionsModel | Unset
        if isinstance(_group_management_permissions, Unset):
            group_management_permissions = UNSET
        else:
            group_management_permissions = RobloxGroupsApiGroupManagementPermissionsModel.from_dict(
                _group_management_permissions
            )

        _group_economy_permissions = d.pop("groupEconomyPermissions", UNSET)
        group_economy_permissions: RobloxGroupsApiGroupEconomyPermissionsModel | Unset
        if isinstance(_group_economy_permissions, Unset):
            group_economy_permissions = UNSET
        else:
            group_economy_permissions = RobloxGroupsApiGroupEconomyPermissionsModel.from_dict(
                _group_economy_permissions
            )

        _group_open_cloud_permissions = d.pop("groupOpenCloudPermissions", UNSET)
        group_open_cloud_permissions: RobloxGroupsApiGroupOpenCloudPermissionsModel | Unset
        if isinstance(_group_open_cloud_permissions, Unset):
            group_open_cloud_permissions = UNSET
        else:
            group_open_cloud_permissions = RobloxGroupsApiGroupOpenCloudPermissionsModel.from_dict(
                _group_open_cloud_permissions
            )

        roblox_groups_api_group_permissions_model = cls(
            group_posts_permissions=group_posts_permissions,
            group_forums_permissions=group_forums_permissions,
            group_content_moderation_permissions=group_content_moderation_permissions,
            group_membership_permissions=group_membership_permissions,
            group_management_permissions=group_management_permissions,
            group_economy_permissions=group_economy_permissions,
            group_open_cloud_permissions=group_open_cloud_permissions,
        )

        return roblox_groups_api_group_permissions_model
