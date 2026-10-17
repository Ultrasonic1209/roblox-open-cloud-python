from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.roblox_groups_api_update_group_settings_request_account_tenure_requirement import (
    RobloxGroupsApiUpdateGroupSettingsRequestAccountTenureRequirement,
)
from ..models.roblox_groups_api_update_group_settings_request_slowmode import (
    RobloxGroupsApiUpdateGroupSettingsRequestSlowmode,
)
from ..models.roblox_groups_api_update_group_settings_request_verification_level import (
    RobloxGroupsApiUpdateGroupSettingsRequestVerificationLevel,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxGroupsApiUpdateGroupSettingsRequest")


@_attrs_define
class RobloxGroupsApiUpdateGroupSettingsRequest:
    """A request model for updating a group's settings.

    Attributes:
        is_approval_required (bool | Unset): Whether public entry is allowed.
        are_enemies_allowed (bool | Unset): Whether enemy club declarations are allowed.
        are_group_funds_visible (bool | Unset): Whether funds are publicly visible.
        are_group_games_visible (bool | Unset): Whether games are publicly visible.
        verification_level (RobloxGroupsApiUpdateGroupSettingsRequestVerificationLevel | Unset): The verification level
            for the group.
        account_tenure_requirement (RobloxGroupsApiUpdateGroupSettingsRequestAccountTenureRequirement | Unset): The
            account tenure requirement for the group.
        slowmode (RobloxGroupsApiUpdateGroupSettingsRequestSlowmode | Unset): The slowmode level for the group (0-4).
            0 = No slowmode, 1-4 = Slowmode levels with increasing restrictions.
            Null = No change to current slowmode setting.
        is_member_list_visible_to_public (bool | Unset): Whether the group member list is visible to public.
    """

    is_approval_required: bool | Unset = UNSET
    are_enemies_allowed: bool | Unset = UNSET
    are_group_funds_visible: bool | Unset = UNSET
    are_group_games_visible: bool | Unset = UNSET
    verification_level: RobloxGroupsApiUpdateGroupSettingsRequestVerificationLevel | Unset = UNSET
    account_tenure_requirement: RobloxGroupsApiUpdateGroupSettingsRequestAccountTenureRequirement | Unset = UNSET
    slowmode: RobloxGroupsApiUpdateGroupSettingsRequestSlowmode | Unset = UNSET
    is_member_list_visible_to_public: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        is_approval_required = self.is_approval_required

        are_enemies_allowed = self.are_enemies_allowed

        are_group_funds_visible = self.are_group_funds_visible

        are_group_games_visible = self.are_group_games_visible

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

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if is_approval_required is not UNSET:
            field_dict["isApprovalRequired"] = is_approval_required
        if are_enemies_allowed is not UNSET:
            field_dict["areEnemiesAllowed"] = are_enemies_allowed
        if are_group_funds_visible is not UNSET:
            field_dict["areGroupFundsVisible"] = are_group_funds_visible
        if are_group_games_visible is not UNSET:
            field_dict["areGroupGamesVisible"] = are_group_games_visible
        if verification_level is not UNSET:
            field_dict["verificationLevel"] = verification_level
        if account_tenure_requirement is not UNSET:
            field_dict["accountTenureRequirement"] = account_tenure_requirement
        if slowmode is not UNSET:
            field_dict["slowmode"] = slowmode
        if is_member_list_visible_to_public is not UNSET:
            field_dict["isMemberListVisibleToPublic"] = is_member_list_visible_to_public

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        is_approval_required = d.pop("isApprovalRequired", UNSET)

        are_enemies_allowed = d.pop("areEnemiesAllowed", UNSET)

        are_group_funds_visible = d.pop("areGroupFundsVisible", UNSET)

        are_group_games_visible = d.pop("areGroupGamesVisible", UNSET)

        _verification_level = d.pop("verificationLevel", UNSET)
        verification_level: RobloxGroupsApiUpdateGroupSettingsRequestVerificationLevel | Unset
        if isinstance(_verification_level, Unset):
            verification_level = UNSET
        else:
            verification_level = RobloxGroupsApiUpdateGroupSettingsRequestVerificationLevel(_verification_level)

        _account_tenure_requirement = d.pop("accountTenureRequirement", UNSET)
        account_tenure_requirement: RobloxGroupsApiUpdateGroupSettingsRequestAccountTenureRequirement | Unset
        if isinstance(_account_tenure_requirement, Unset):
            account_tenure_requirement = UNSET
        else:
            account_tenure_requirement = RobloxGroupsApiUpdateGroupSettingsRequestAccountTenureRequirement(
                _account_tenure_requirement
            )

        _slowmode = d.pop("slowmode", UNSET)
        slowmode: RobloxGroupsApiUpdateGroupSettingsRequestSlowmode | Unset
        if isinstance(_slowmode, Unset):
            slowmode = UNSET
        else:
            slowmode = RobloxGroupsApiUpdateGroupSettingsRequestSlowmode(_slowmode)

        is_member_list_visible_to_public = d.pop("isMemberListVisibleToPublic", UNSET)

        roblox_groups_api_update_group_settings_request = cls(
            is_approval_required=is_approval_required,
            are_enemies_allowed=are_enemies_allowed,
            are_group_funds_visible=are_group_funds_visible,
            are_group_games_visible=are_group_games_visible,
            verification_level=verification_level,
            account_tenure_requirement=account_tenure_requirement,
            slowmode=slowmode,
            is_member_list_visible_to_public=is_member_list_visible_to_public,
        )

        return roblox_groups_api_update_group_settings_request
