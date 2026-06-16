from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_groups_api_group_role_response import RobloxGroupsApiGroupRoleResponse
    from ..models.roblox_groups_api_models_response_user_model import RobloxGroupsApiModelsResponseUserModel


T = TypeVar("T", bound="RobloxGroupsApiUserGroupRoleResponse")


@_attrs_define
class RobloxGroupsApiUserGroupRoleResponse:
    """A user group role response model

    Attributes:
        user (RobloxGroupsApiModelsResponseUserModel | Unset): A model representing data about an
            Roblox.Platform.Membership.IUser
        role (RobloxGroupsApiGroupRoleResponse | Unset): A group role response model
    """

    user: RobloxGroupsApiModelsResponseUserModel | Unset = UNSET
    role: RobloxGroupsApiGroupRoleResponse | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        user: dict[str, Any] | Unset = UNSET
        if not isinstance(self.user, Unset):
            user = self.user.to_dict()

        role: dict[str, Any] | Unset = UNSET
        if not isinstance(self.role, Unset):
            role = self.role.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if user is not UNSET:
            field_dict["user"] = user
        if role is not UNSET:
            field_dict["role"] = role

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_groups_api_group_role_response import RobloxGroupsApiGroupRoleResponse
        from ..models.roblox_groups_api_models_response_user_model import RobloxGroupsApiModelsResponseUserModel

        d = dict(src_dict)
        _user = d.pop("user", UNSET)
        user: RobloxGroupsApiModelsResponseUserModel | Unset
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = RobloxGroupsApiModelsResponseUserModel.from_dict(_user)

        _role = d.pop("role", UNSET)
        role: RobloxGroupsApiGroupRoleResponse | Unset
        if isinstance(_role, Unset):
            role = UNSET
        else:
            role = RobloxGroupsApiGroupRoleResponse.from_dict(_role)

        roblox_groups_api_user_group_role_response = cls(
            user=user,
            role=role,
        )

        return roblox_groups_api_user_group_role_response
