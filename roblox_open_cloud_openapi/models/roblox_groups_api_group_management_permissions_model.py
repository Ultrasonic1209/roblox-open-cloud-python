from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxGroupsApiGroupManagementPermissionsModel")


@_attrs_define
class RobloxGroupsApiGroupManagementPermissionsModel:
    """A model representing data about an Roblox.Platform.Membership.IUser

    Attributes:
        manage_relationships (bool | Unset): Manage group relationships permission
        manage_clan (bool | Unset): Manage clan permission
        view_audit_logs (bool | Unset): View audit logs permission
        bypass_slowmode (bool | Unset): Bypass slowmode permission.
        view_community_analytics (bool | Unset): View community analytics permission.
    """

    manage_relationships: bool | Unset = UNSET
    manage_clan: bool | Unset = UNSET
    view_audit_logs: bool | Unset = UNSET
    bypass_slowmode: bool | Unset = UNSET
    view_community_analytics: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        manage_relationships = self.manage_relationships

        manage_clan = self.manage_clan

        view_audit_logs = self.view_audit_logs

        bypass_slowmode = self.bypass_slowmode

        view_community_analytics = self.view_community_analytics

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if manage_relationships is not UNSET:
            field_dict["manageRelationships"] = manage_relationships
        if manage_clan is not UNSET:
            field_dict["manageClan"] = manage_clan
        if view_audit_logs is not UNSET:
            field_dict["viewAuditLogs"] = view_audit_logs
        if bypass_slowmode is not UNSET:
            field_dict["bypassSlowmode"] = bypass_slowmode
        if view_community_analytics is not UNSET:
            field_dict["viewCommunityAnalytics"] = view_community_analytics

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        manage_relationships = d.pop("manageRelationships", UNSET)

        manage_clan = d.pop("manageClan", UNSET)

        view_audit_logs = d.pop("viewAuditLogs", UNSET)

        bypass_slowmode = d.pop("bypassSlowmode", UNSET)

        view_community_analytics = d.pop("viewCommunityAnalytics", UNSET)

        roblox_groups_api_group_management_permissions_model = cls(
            manage_relationships=manage_relationships,
            manage_clan=manage_clan,
            view_audit_logs=view_audit_logs,
            bypass_slowmode=bypass_slowmode,
            view_community_analytics=view_community_analytics,
        )

        return roblox_groups_api_group_management_permissions_model
