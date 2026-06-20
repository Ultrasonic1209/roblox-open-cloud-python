from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_groups_api_group_channel_permissions_model import RobloxGroupsApiGroupChannelPermissionsModel
    from ..models.roblox_groups_api_group_notification_preference_data import (
        RobloxGroupsApiGroupNotificationPreferenceData,
    )
    from ..models.roblox_groups_api_group_permissions_model import RobloxGroupsApiGroupPermissionsModel
    from ..models.roblox_groups_api_user_group_role_response import RobloxGroupsApiUserGroupRoleResponse


T = TypeVar("T", bound="RobloxGroupsApiGroupMembershipMetadataResponse")


@_attrs_define
class RobloxGroupsApiGroupMembershipMetadataResponse:
    """A user's group membership metadata response model

    Attributes:
        group_id (int | Unset): The group id
        is_primary (bool | Unset): Whether the group is primary
        is_pending_join (bool | Unset): Whether there has been a request to join this group
        user_role (RobloxGroupsApiUserGroupRoleResponse | Unset): A user group role response model
        permissions (RobloxGroupsApiGroupPermissionsModel | Unset): A model for group permissions.
        channel_permissions (list[RobloxGroupsApiGroupChannelPermissionsModel] | Unset): The users's permissions for
            each communication channel in the group
        are_group_games_visible (bool | Unset): Whether group games are visible
        are_group_funds_visible (bool | Unset): Whether group funds are visible
        are_enemies_allowed (bool | Unset): Whether enemies are allowed
        can_configure (bool | Unset): If the user can configure the group
        is_notifications_enabled (bool | Unset): Whether the group's notification preferences set to enabled for the
            user
        notification_preferences (list[RobloxGroupsApiGroupNotificationPreferenceData] | Unset):
        is_banned_from_group (bool | Unset): Whether the user is banned from the group
        can_view_member_list (bool | Unset): Whether the user can view the group member list
        is_owner (bool | Unset): Whether the authenticated user is the owner of the group
    """

    group_id: int | Unset = UNSET
    is_primary: bool | Unset = UNSET
    is_pending_join: bool | Unset = UNSET
    user_role: RobloxGroupsApiUserGroupRoleResponse | Unset = UNSET
    permissions: RobloxGroupsApiGroupPermissionsModel | Unset = UNSET
    channel_permissions: list[RobloxGroupsApiGroupChannelPermissionsModel] | Unset = UNSET
    are_group_games_visible: bool | Unset = UNSET
    are_group_funds_visible: bool | Unset = UNSET
    are_enemies_allowed: bool | Unset = UNSET
    can_configure: bool | Unset = UNSET
    is_notifications_enabled: bool | Unset = UNSET
    notification_preferences: list[RobloxGroupsApiGroupNotificationPreferenceData] | Unset = UNSET
    is_banned_from_group: bool | Unset = UNSET
    can_view_member_list: bool | Unset = UNSET
    is_owner: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        group_id = self.group_id

        is_primary = self.is_primary

        is_pending_join = self.is_pending_join

        user_role: dict[str, Any] | Unset = UNSET
        if not isinstance(self.user_role, Unset):
            user_role = self.user_role.to_dict()

        permissions: dict[str, Any] | Unset = UNSET
        if not isinstance(self.permissions, Unset):
            permissions = self.permissions.to_dict()

        channel_permissions: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.channel_permissions, Unset):
            channel_permissions = []
            for channel_permissions_item_data in self.channel_permissions:
                channel_permissions_item = channel_permissions_item_data.to_dict()
                channel_permissions.append(channel_permissions_item)

        are_group_games_visible = self.are_group_games_visible

        are_group_funds_visible = self.are_group_funds_visible

        are_enemies_allowed = self.are_enemies_allowed

        can_configure = self.can_configure

        is_notifications_enabled = self.is_notifications_enabled

        notification_preferences: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.notification_preferences, Unset):
            notification_preferences = []
            for notification_preferences_item_data in self.notification_preferences:
                notification_preferences_item = notification_preferences_item_data.to_dict()
                notification_preferences.append(notification_preferences_item)

        is_banned_from_group = self.is_banned_from_group

        can_view_member_list = self.can_view_member_list

        is_owner = self.is_owner

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if group_id is not UNSET:
            field_dict["groupId"] = group_id
        if is_primary is not UNSET:
            field_dict["isPrimary"] = is_primary
        if is_pending_join is not UNSET:
            field_dict["isPendingJoin"] = is_pending_join
        if user_role is not UNSET:
            field_dict["userRole"] = user_role
        if permissions is not UNSET:
            field_dict["permissions"] = permissions
        if channel_permissions is not UNSET:
            field_dict["channelPermissions"] = channel_permissions
        if are_group_games_visible is not UNSET:
            field_dict["areGroupGamesVisible"] = are_group_games_visible
        if are_group_funds_visible is not UNSET:
            field_dict["areGroupFundsVisible"] = are_group_funds_visible
        if are_enemies_allowed is not UNSET:
            field_dict["areEnemiesAllowed"] = are_enemies_allowed
        if can_configure is not UNSET:
            field_dict["canConfigure"] = can_configure
        if is_notifications_enabled is not UNSET:
            field_dict["isNotificationsEnabled"] = is_notifications_enabled
        if notification_preferences is not UNSET:
            field_dict["notificationPreferences"] = notification_preferences
        if is_banned_from_group is not UNSET:
            field_dict["isBannedFromGroup"] = is_banned_from_group
        if can_view_member_list is not UNSET:
            field_dict["canViewMemberList"] = can_view_member_list
        if is_owner is not UNSET:
            field_dict["isOwner"] = is_owner

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_groups_api_group_channel_permissions_model import (
            RobloxGroupsApiGroupChannelPermissionsModel,
        )
        from ..models.roblox_groups_api_group_notification_preference_data import (
            RobloxGroupsApiGroupNotificationPreferenceData,
        )
        from ..models.roblox_groups_api_group_permissions_model import RobloxGroupsApiGroupPermissionsModel
        from ..models.roblox_groups_api_user_group_role_response import RobloxGroupsApiUserGroupRoleResponse

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        group_id = d.pop("groupId", UNSET)

        is_primary = d.pop("isPrimary", UNSET)

        is_pending_join = d.pop("isPendingJoin", UNSET)

        _user_role = d.pop("userRole", UNSET)
        user_role: RobloxGroupsApiUserGroupRoleResponse | Unset
        if isinstance(_user_role, Unset):
            user_role = UNSET
        else:
            user_role = RobloxGroupsApiUserGroupRoleResponse.from_dict(_user_role)

        _permissions = d.pop("permissions", UNSET)
        permissions: RobloxGroupsApiGroupPermissionsModel | Unset
        if isinstance(_permissions, Unset):
            permissions = UNSET
        else:
            permissions = RobloxGroupsApiGroupPermissionsModel.from_dict(_permissions)

        _channel_permissions = d.pop("channelPermissions", UNSET)
        channel_permissions: list[RobloxGroupsApiGroupChannelPermissionsModel] | Unset = UNSET
        if _channel_permissions is not UNSET:
            channel_permissions = []
            for channel_permissions_item_data in _channel_permissions:
                channel_permissions_item = RobloxGroupsApiGroupChannelPermissionsModel.from_dict(
                    channel_permissions_item_data
                )

                channel_permissions.append(channel_permissions_item)

        are_group_games_visible = d.pop("areGroupGamesVisible", UNSET)

        are_group_funds_visible = d.pop("areGroupFundsVisible", UNSET)

        are_enemies_allowed = d.pop("areEnemiesAllowed", UNSET)

        can_configure = d.pop("canConfigure", UNSET)

        is_notifications_enabled = d.pop("isNotificationsEnabled", UNSET)

        _notification_preferences = d.pop("notificationPreferences", UNSET)
        notification_preferences: list[RobloxGroupsApiGroupNotificationPreferenceData] | Unset = UNSET
        if _notification_preferences is not UNSET:
            notification_preferences = []
            for notification_preferences_item_data in _notification_preferences:
                notification_preferences_item = RobloxGroupsApiGroupNotificationPreferenceData.from_dict(
                    notification_preferences_item_data
                )

                notification_preferences.append(notification_preferences_item)

        is_banned_from_group = d.pop("isBannedFromGroup", UNSET)

        can_view_member_list = d.pop("canViewMemberList", UNSET)

        is_owner = d.pop("isOwner", UNSET)

        roblox_groups_api_group_membership_metadata_response = cls(
            group_id=group_id,
            is_primary=is_primary,
            is_pending_join=is_pending_join,
            user_role=user_role,
            permissions=permissions,
            channel_permissions=channel_permissions,
            are_group_games_visible=are_group_games_visible,
            are_group_funds_visible=are_group_funds_visible,
            are_enemies_allowed=are_enemies_allowed,
            can_configure=can_configure,
            is_notifications_enabled=is_notifications_enabled,
            notification_preferences=notification_preferences,
            is_banned_from_group=is_banned_from_group,
            can_view_member_list=can_view_member_list,
            is_owner=is_owner,
        )

        return roblox_groups_api_group_membership_metadata_response
