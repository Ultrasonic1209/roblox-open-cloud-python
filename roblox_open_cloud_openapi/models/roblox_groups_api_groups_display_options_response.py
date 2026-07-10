from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxGroupsApiGroupsDisplayOptionsResponse")


@_attrs_define
class RobloxGroupsApiGroupsDisplayOptionsResponse:
    """A group roles response model

    Attributes:
        group_limit (int | Unset): The user's builders club membership group limit
        current_group_count (int | Unset): The user's current group membership count
        group_status_max_length (int | Unset): The maximum length of a group status
        are_profile_groups_hidden (bool | Unset): If set to true, groups showcase will not show on users profiles.

            If set to false, group showcase will display on users profiles.
        is_group_details_policy_enabled (bool | Unset): If set to true, group details will respect GUAC policies for
            group details

            If set to false, group details will not respect GUAC policies
        show_previous_group_names (bool | Unset): Whether or not we should show previous names of this group
        are_group_bans_enabled (bool | Unset): Whether or not group bans are enabled
        can_enable_group_notifications (bool | Unset): Whether or not group notifications can be enabled
    """

    group_limit: int | Unset = UNSET
    current_group_count: int | Unset = UNSET
    group_status_max_length: int | Unset = UNSET
    are_profile_groups_hidden: bool | Unset = UNSET
    is_group_details_policy_enabled: bool | Unset = UNSET
    show_previous_group_names: bool | Unset = UNSET
    are_group_bans_enabled: bool | Unset = UNSET
    can_enable_group_notifications: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        group_limit = self.group_limit

        current_group_count = self.current_group_count

        group_status_max_length = self.group_status_max_length

        are_profile_groups_hidden = self.are_profile_groups_hidden

        is_group_details_policy_enabled = self.is_group_details_policy_enabled

        show_previous_group_names = self.show_previous_group_names

        are_group_bans_enabled = self.are_group_bans_enabled

        can_enable_group_notifications = self.can_enable_group_notifications

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if group_limit is not UNSET:
            field_dict["groupLimit"] = group_limit
        if current_group_count is not UNSET:
            field_dict["currentGroupCount"] = current_group_count
        if group_status_max_length is not UNSET:
            field_dict["groupStatusMaxLength"] = group_status_max_length
        if are_profile_groups_hidden is not UNSET:
            field_dict["areProfileGroupsHidden"] = are_profile_groups_hidden
        if is_group_details_policy_enabled is not UNSET:
            field_dict["isGroupDetailsPolicyEnabled"] = is_group_details_policy_enabled
        if show_previous_group_names is not UNSET:
            field_dict["showPreviousGroupNames"] = show_previous_group_names
        if are_group_bans_enabled is not UNSET:
            field_dict["areGroupBansEnabled"] = are_group_bans_enabled
        if can_enable_group_notifications is not UNSET:
            field_dict["canEnableGroupNotifications"] = can_enable_group_notifications

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        group_limit = d.pop("groupLimit", UNSET)

        current_group_count = d.pop("currentGroupCount", UNSET)

        group_status_max_length = d.pop("groupStatusMaxLength", UNSET)

        are_profile_groups_hidden = d.pop("areProfileGroupsHidden", UNSET)

        is_group_details_policy_enabled = d.pop("isGroupDetailsPolicyEnabled", UNSET)

        show_previous_group_names = d.pop("showPreviousGroupNames", UNSET)

        are_group_bans_enabled = d.pop("areGroupBansEnabled", UNSET)

        can_enable_group_notifications = d.pop("canEnableGroupNotifications", UNSET)

        roblox_groups_api_groups_display_options_response = cls(
            group_limit=group_limit,
            current_group_count=current_group_count,
            group_status_max_length=group_status_max_length,
            are_profile_groups_hidden=are_profile_groups_hidden,
            is_group_details_policy_enabled=is_group_details_policy_enabled,
            show_previous_group_names=show_previous_group_names,
            are_group_bans_enabled=are_group_bans_enabled,
            can_enable_group_notifications=can_enable_group_notifications,
        )

        return roblox_groups_api_groups_display_options_response
