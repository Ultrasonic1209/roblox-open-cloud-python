from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_groups_api_group_membership_detail_response import RobloxGroupsApiGroupMembershipDetailResponse
    from ..models.roblox_groups_api_models_response_user_model import RobloxGroupsApiModelsResponseUserModel


T = TypeVar("T", bound="RobloxGroupsApiUserGroupMembershipResponse")


@_attrs_define
class RobloxGroupsApiUserGroupMembershipResponse:
    """A users group membership response model

    Attributes:
        user (RobloxGroupsApiModelsResponseUserModel | Unset): A model representing data about an
            Roblox.Platform.Membership.IUser
        groups (list[RobloxGroupsApiGroupMembershipDetailResponse] | Unset): The list of group memberships
    """

    user: RobloxGroupsApiModelsResponseUserModel | Unset = UNSET
    groups: list[RobloxGroupsApiGroupMembershipDetailResponse] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        user: dict[str, Any] | Unset = UNSET
        if not isinstance(self.user, Unset):
            user = self.user.to_dict()

        groups: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.groups, Unset):
            groups = []
            for groups_item_data in self.groups:
                groups_item = groups_item_data.to_dict()
                groups.append(groups_item)

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if user is not UNSET:
            field_dict["user"] = user
        if groups is not UNSET:
            field_dict["groups"] = groups

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_groups_api_group_membership_detail_response import (
            RobloxGroupsApiGroupMembershipDetailResponse,
        )
        from ..models.roblox_groups_api_models_response_user_model import RobloxGroupsApiModelsResponseUserModel

        d = dict(src_dict)
        _user = d.pop("user", UNSET)
        user: RobloxGroupsApiModelsResponseUserModel | Unset
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = RobloxGroupsApiModelsResponseUserModel.from_dict(_user)

        _groups = d.pop("groups", UNSET)
        groups: list[RobloxGroupsApiGroupMembershipDetailResponse] | Unset = UNSET
        if _groups is not UNSET:
            groups = []
            for groups_item_data in _groups:
                groups_item = RobloxGroupsApiGroupMembershipDetailResponse.from_dict(groups_item_data)

                groups.append(groups_item)

        roblox_groups_api_user_group_membership_response = cls(
            user=user,
            groups=groups,
        )

        return roblox_groups_api_user_group_membership_response
