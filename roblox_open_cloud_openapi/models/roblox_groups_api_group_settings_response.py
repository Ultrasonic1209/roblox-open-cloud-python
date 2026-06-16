from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.roblox_groups_api_group_settings_response_account_tenure_requirement import (
    RobloxGroupsApiGroupSettingsResponseAccountTenureRequirement,
)
from ..models.roblox_groups_api_group_settings_response_slowmode import RobloxGroupsApiGroupSettingsResponseSlowmode
from ..models.roblox_groups_api_group_settings_response_verification_level import (
    RobloxGroupsApiGroupSettingsResponseVerificationLevel,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxGroupsApiGroupSettingsResponse")


@_attrs_define
class RobloxGroupsApiGroupSettingsResponse:
    """Response model for Group Settings

    Attributes:
        is_approval_required (bool | Unset): Whether public entry is allowed.
        is_builders_club_required (bool | Unset): Whether Builder's Club is required.
        are_enemies_allowed (bool | Unset): Whether enemy club declarations are allowed.
        are_group_funds_visible (bool | Unset): Whether funds are publicly visible.
        are_group_games_visible (bool | Unset): Whether games are publicly visible.
        is_group_name_change_enabled (bool | Unset): If the group name change feature is enabled for this group.
        verification_level (RobloxGroupsApiGroupSettingsResponseVerificationLevel | Unset): The verification level for
            the group. Null if the verification level could not be determined due to an error.
        account_tenure_requirement (RobloxGroupsApiGroupSettingsResponseAccountTenureRequirement | Unset): The account
            tenure requirement for the group. Null if the account tenure requirement could not be determined due to an
            error.
        slowmode (RobloxGroupsApiGroupSettingsResponseSlowmode | Unset): The slowmode level for the group (0-4).
            0 = No slowmode, 1-4 = Slowmode levels with increasing restrictions.
        is_member_list_visible_to_public (bool | Unset): Whether the group member list is visible to public.
        is_auto_assign_role_disabled (bool | Unset): Whether automatic assignment of the lowest non-guest role is
            disabled for this group.
            For non-legacy groups (created after the multi-role cutoff), this is always true.
            For legacy groups, reflects the persisted GroupFeatureSettings value.
            Null when the value could not be determined.
    """

    is_approval_required: bool | Unset = UNSET
    is_builders_club_required: bool | Unset = UNSET
    are_enemies_allowed: bool | Unset = UNSET
    are_group_funds_visible: bool | Unset = UNSET
    are_group_games_visible: bool | Unset = UNSET
    is_group_name_change_enabled: bool | Unset = UNSET
    verification_level: RobloxGroupsApiGroupSettingsResponseVerificationLevel | Unset = UNSET
    account_tenure_requirement: RobloxGroupsApiGroupSettingsResponseAccountTenureRequirement | Unset = UNSET
    slowmode: RobloxGroupsApiGroupSettingsResponseSlowmode | Unset = UNSET
    is_member_list_visible_to_public: bool | Unset = UNSET
    is_auto_assign_role_disabled: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        is_approval_required = self.is_approval_required

        is_builders_club_required = self.is_builders_club_required

        are_enemies_allowed = self.are_enemies_allowed

        are_group_funds_visible = self.are_group_funds_visible

        are_group_games_visible = self.are_group_games_visible

        is_group_name_change_enabled = self.is_group_name_change_enabled

        verification_level: int | Unset = UNSET
        if not isinstance(self.verification_level, Unset):
            verification_level = self.verification_level.value

        account_tenure_requirement: int | Unset = UNSET
        if not isinstance(self.account_tenure_requirement, Unset):
            account_tenure_requirement = self.account_tenure_requirement.value

        slowmode: int | Unset = UNSET
        if not isinstance(self.slowmode, Unset):
            slowmode = self.slowmode.value

        is_member_list_visible_to_public = self.is_member_list_visible_to_public

        is_auto_assign_role_disabled = self.is_auto_assign_role_disabled

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if is_approval_required is not UNSET:
            field_dict["isApprovalRequired"] = is_approval_required
        if is_builders_club_required is not UNSET:
            field_dict["isBuildersClubRequired"] = is_builders_club_required
        if are_enemies_allowed is not UNSET:
            field_dict["areEnemiesAllowed"] = are_enemies_allowed
        if are_group_funds_visible is not UNSET:
            field_dict["areGroupFundsVisible"] = are_group_funds_visible
        if are_group_games_visible is not UNSET:
            field_dict["areGroupGamesVisible"] = are_group_games_visible
        if is_group_name_change_enabled is not UNSET:
            field_dict["isGroupNameChangeEnabled"] = is_group_name_change_enabled
        if verification_level is not UNSET:
            field_dict["verificationLevel"] = verification_level
        if account_tenure_requirement is not UNSET:
            field_dict["accountTenureRequirement"] = account_tenure_requirement
        if slowmode is not UNSET:
            field_dict["slowmode"] = slowmode
        if is_member_list_visible_to_public is not UNSET:
            field_dict["isMemberListVisibleToPublic"] = is_member_list_visible_to_public
        if is_auto_assign_role_disabled is not UNSET:
            field_dict["isAutoAssignRoleDisabled"] = is_auto_assign_role_disabled

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        is_approval_required = d.pop("isApprovalRequired", UNSET)

        is_builders_club_required = d.pop("isBuildersClubRequired", UNSET)

        are_enemies_allowed = d.pop("areEnemiesAllowed", UNSET)

        are_group_funds_visible = d.pop("areGroupFundsVisible", UNSET)

        are_group_games_visible = d.pop("areGroupGamesVisible", UNSET)

        is_group_name_change_enabled = d.pop("isGroupNameChangeEnabled", UNSET)

        _verification_level = d.pop("verificationLevel", UNSET)
        verification_level: RobloxGroupsApiGroupSettingsResponseVerificationLevel | Unset
        if isinstance(_verification_level, Unset):
            verification_level = UNSET
        else:
            verification_level = RobloxGroupsApiGroupSettingsResponseVerificationLevel(_verification_level)

        _account_tenure_requirement = d.pop("accountTenureRequirement", UNSET)
        account_tenure_requirement: RobloxGroupsApiGroupSettingsResponseAccountTenureRequirement | Unset
        if isinstance(_account_tenure_requirement, Unset):
            account_tenure_requirement = UNSET
        else:
            account_tenure_requirement = RobloxGroupsApiGroupSettingsResponseAccountTenureRequirement(
                _account_tenure_requirement
            )

        _slowmode = d.pop("slowmode", UNSET)
        slowmode: RobloxGroupsApiGroupSettingsResponseSlowmode | Unset
        if isinstance(_slowmode, Unset):
            slowmode = UNSET
        else:
            slowmode = RobloxGroupsApiGroupSettingsResponseSlowmode(_slowmode)

        is_member_list_visible_to_public = d.pop("isMemberListVisibleToPublic", UNSET)

        is_auto_assign_role_disabled = d.pop("isAutoAssignRoleDisabled", UNSET)

        roblox_groups_api_group_settings_response = cls(
            is_approval_required=is_approval_required,
            is_builders_club_required=is_builders_club_required,
            are_enemies_allowed=are_enemies_allowed,
            are_group_funds_visible=are_group_funds_visible,
            are_group_games_visible=are_group_games_visible,
            is_group_name_change_enabled=is_group_name_change_enabled,
            verification_level=verification_level,
            account_tenure_requirement=account_tenure_requirement,
            slowmode=slowmode,
            is_member_list_visible_to_public=is_member_list_visible_to_public,
            is_auto_assign_role_disabled=is_auto_assign_role_disabled,
        )

        return roblox_groups_api_group_settings_response
