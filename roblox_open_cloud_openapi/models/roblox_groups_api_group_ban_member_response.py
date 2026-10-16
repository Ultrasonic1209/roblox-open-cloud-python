from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_groups_api_models_response_user_model import RobloxGroupsApiModelsResponseUserModel
    from ..models.roblox_groups_api_user_group_role_response import RobloxGroupsApiUserGroupRoleResponse


T = TypeVar("T", bound="RobloxGroupsApiGroupBanMemberResponse")


@_attrs_define
class RobloxGroupsApiGroupBanMemberResponse:
    """A ban member from group response

    Attributes:
        user (RobloxGroupsApiModelsResponseUserModel | Unset): A model representing data about an
            Roblox.Platform.Membership.IUser
        acting_user (RobloxGroupsApiUserGroupRoleResponse | Unset): A user group role response model
        created (datetime.datetime | Unset): The group ban's created time
    """

    user: RobloxGroupsApiModelsResponseUserModel | Unset = UNSET
    acting_user: RobloxGroupsApiUserGroupRoleResponse | Unset = UNSET
    created: datetime.datetime | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        user: dict[str, Any] | Unset = UNSET
        if not isinstance(self.user, Unset):
            user = self.user.to_dict()

        acting_user: dict[str, Any] | Unset = UNSET
        if not isinstance(self.acting_user, Unset):
            acting_user = self.acting_user.to_dict()

        created: str | Unset = UNSET
        if not isinstance(self.created, Unset):
            created = self.created.isoformat()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if user is not UNSET:
            field_dict["user"] = user
        if acting_user is not UNSET:
            field_dict["actingUser"] = acting_user
        if created is not UNSET:
            field_dict["created"] = created

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_groups_api_models_response_user_model import RobloxGroupsApiModelsResponseUserModel
        from ..models.roblox_groups_api_user_group_role_response import RobloxGroupsApiUserGroupRoleResponse

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        _user = d.pop("user", UNSET)
        user: RobloxGroupsApiModelsResponseUserModel | Unset
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = RobloxGroupsApiModelsResponseUserModel.from_dict(_user)

        _acting_user = d.pop("actingUser", UNSET)
        acting_user: RobloxGroupsApiUserGroupRoleResponse | Unset
        if isinstance(_acting_user, Unset):
            acting_user = UNSET
        else:
            acting_user = RobloxGroupsApiUserGroupRoleResponse.from_dict(_acting_user)

        _created = d.pop("created", UNSET)
        created: datetime.datetime | Unset
        if isinstance(_created, Unset):
            created = UNSET
        else:
            created = datetime.datetime.fromisoformat(_created)

        roblox_groups_api_group_ban_member_response = cls(
            user=user,
            acting_user=acting_user,
            created=created,
        )

        return roblox_groups_api_group_ban_member_response
