from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxGroupsApiGroupMembershipPermissionsModel")


@_attrs_define
class RobloxGroupsApiGroupMembershipPermissionsModel:
    """A model representing data about an Roblox.Platform.Membership.IUser

    Attributes:
        change_rank (bool | Unset): View wall permission
        invite_members (bool | Unset): Post to wall permission
        remove_members (bool | Unset): Remove from group permission
        ban_members (bool | Unset): Ban from group permission
    """

    change_rank: bool | Unset = UNSET
    invite_members: bool | Unset = UNSET
    remove_members: bool | Unset = UNSET
    ban_members: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        change_rank = self.change_rank

        invite_members = self.invite_members

        remove_members = self.remove_members

        ban_members = self.ban_members

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if change_rank is not UNSET:
            field_dict["changeRank"] = change_rank
        if invite_members is not UNSET:
            field_dict["inviteMembers"] = invite_members
        if remove_members is not UNSET:
            field_dict["removeMembers"] = remove_members
        if ban_members is not UNSET:
            field_dict["banMembers"] = ban_members

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        change_rank = d.pop("changeRank", UNSET)

        invite_members = d.pop("inviteMembers", UNSET)

        remove_members = d.pop("removeMembers", UNSET)

        ban_members = d.pop("banMembers", UNSET)

        roblox_groups_api_group_membership_permissions_model = cls(
            change_rank=change_rank,
            invite_members=invite_members,
            remove_members=remove_members,
            ban_members=ban_members,
        )

        return roblox_groups_api_group_membership_permissions_model
