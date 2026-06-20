from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_groups_api_group_detail_response import RobloxGroupsApiGroupDetailResponse
    from ..models.roblox_groups_api_group_notification_preference_data import (
        RobloxGroupsApiGroupNotificationPreferenceData,
    )
    from ..models.roblox_groups_api_group_role_response import RobloxGroupsApiGroupRoleResponse


T = TypeVar("T", bound="RobloxGroupsApiGroupMembershipDetailResponse")


@_attrs_define
class RobloxGroupsApiGroupMembershipDetailResponse:
    """A group membership response model

    Attributes:
        group (RobloxGroupsApiGroupDetailResponse | Unset): A detailed group response model
        role (RobloxGroupsApiGroupRoleResponse | Unset): A group role response model
        is_primary_group (bool | Unset): Whether the group is the user's Primary Group
        is_notifications_enabled (bool | Unset): Whether the group notification preferences are enabled for the user
        notification_preferences (list[RobloxGroupsApiGroupNotificationPreferenceData] | Unset):
    """

    group: RobloxGroupsApiGroupDetailResponse | Unset = UNSET
    role: RobloxGroupsApiGroupRoleResponse | Unset = UNSET
    is_primary_group: bool | Unset = UNSET
    is_notifications_enabled: bool | Unset = UNSET
    notification_preferences: list[RobloxGroupsApiGroupNotificationPreferenceData] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        group: dict[str, Any] | Unset = UNSET
        if not isinstance(self.group, Unset):
            group = self.group.to_dict()

        role: dict[str, Any] | Unset = UNSET
        if not isinstance(self.role, Unset):
            role = self.role.to_dict()

        is_primary_group = self.is_primary_group

        is_notifications_enabled = self.is_notifications_enabled

        notification_preferences: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.notification_preferences, Unset):
            notification_preferences = []
            for notification_preferences_item_data in self.notification_preferences:
                notification_preferences_item = notification_preferences_item_data.to_dict()
                notification_preferences.append(notification_preferences_item)

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if group is not UNSET:
            field_dict["group"] = group
        if role is not UNSET:
            field_dict["role"] = role
        if is_primary_group is not UNSET:
            field_dict["isPrimaryGroup"] = is_primary_group
        if is_notifications_enabled is not UNSET:
            field_dict["isNotificationsEnabled"] = is_notifications_enabled
        if notification_preferences is not UNSET:
            field_dict["notificationPreferences"] = notification_preferences

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_groups_api_group_detail_response import RobloxGroupsApiGroupDetailResponse
        from ..models.roblox_groups_api_group_notification_preference_data import (
            RobloxGroupsApiGroupNotificationPreferenceData,
        )
        from ..models.roblox_groups_api_group_role_response import RobloxGroupsApiGroupRoleResponse

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        _group = d.pop("group", UNSET)
        group: RobloxGroupsApiGroupDetailResponse | Unset
        if isinstance(_group, Unset):
            group = UNSET
        else:
            group = RobloxGroupsApiGroupDetailResponse.from_dict(_group)

        _role = d.pop("role", UNSET)
        role: RobloxGroupsApiGroupRoleResponse | Unset
        if isinstance(_role, Unset):
            role = UNSET
        else:
            role = RobloxGroupsApiGroupRoleResponse.from_dict(_role)

        is_primary_group = d.pop("isPrimaryGroup", UNSET)

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

        roblox_groups_api_group_membership_detail_response = cls(
            group=group,
            role=role,
            is_primary_group=is_primary_group,
            is_notifications_enabled=is_notifications_enabled,
            notification_preferences=notification_preferences,
        )

        return roblox_groups_api_group_membership_detail_response
