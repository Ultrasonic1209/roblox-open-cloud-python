from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_groups_api_group_notification_preference_data import (
        RobloxGroupsApiGroupNotificationPreferenceData,
    )
    from ..models.roblox_web_responses_groups_group_basic_response import RobloxWebResponsesGroupsGroupBasicResponse
    from ..models.roblox_web_responses_groups_group_role_basic_response import (
        RobloxWebResponsesGroupsGroupRoleBasicResponse,
    )


T = TypeVar("T", bound="RobloxGroupsApiGroupMembershipResponse")


@_attrs_define
class RobloxGroupsApiGroupMembershipResponse:
    """A basic group membership response model

    Attributes:
        group (RobloxWebResponsesGroupsGroupBasicResponse | Unset):
        role (RobloxWebResponsesGroupsGroupRoleBasicResponse | Unset):
        is_notifications_enabled (bool | Unset): Whether the group notification preferences are enabled for the user
            TODO: Deprecate this field - it only returns if announcement notifications are enabled and that information is
            already returned in the NotificationPreferences list below
        notification_preferences (list[RobloxGroupsApiGroupNotificationPreferenceData] | Unset):
    """

    group: RobloxWebResponsesGroupsGroupBasicResponse | Unset = UNSET
    role: RobloxWebResponsesGroupsGroupRoleBasicResponse | Unset = UNSET
    is_notifications_enabled: bool | Unset = UNSET
    notification_preferences: list[RobloxGroupsApiGroupNotificationPreferenceData] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        group: dict[str, Any] | Unset = UNSET
        if not isinstance(self.group, Unset):
            group = self.group.to_dict()

        role: dict[str, Any] | Unset = UNSET
        if not isinstance(self.role, Unset):
            role = self.role.to_dict()

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
        if is_notifications_enabled is not UNSET:
            field_dict["isNotificationsEnabled"] = is_notifications_enabled
        if notification_preferences is not UNSET:
            field_dict["notificationPreferences"] = notification_preferences

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_groups_api_group_notification_preference_data import (
            RobloxGroupsApiGroupNotificationPreferenceData,
        )
        from ..models.roblox_web_responses_groups_group_basic_response import RobloxWebResponsesGroupsGroupBasicResponse
        from ..models.roblox_web_responses_groups_group_role_basic_response import (
            RobloxWebResponsesGroupsGroupRoleBasicResponse,
        )

        d = dict(src_dict)
        _group = d.pop("group", UNSET)
        group: RobloxWebResponsesGroupsGroupBasicResponse | Unset
        if isinstance(_group, Unset):
            group = UNSET
        else:
            group = RobloxWebResponsesGroupsGroupBasicResponse.from_dict(_group)

        _role = d.pop("role", UNSET)
        role: RobloxWebResponsesGroupsGroupRoleBasicResponse | Unset
        if isinstance(_role, Unset):
            role = UNSET
        else:
            role = RobloxWebResponsesGroupsGroupRoleBasicResponse.from_dict(_role)

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

        roblox_groups_api_group_membership_response = cls(
            group=group,
            role=role,
            is_notifications_enabled=is_notifications_enabled,
            notification_preferences=notification_preferences,
        )

        return roblox_groups_api_group_membership_response
