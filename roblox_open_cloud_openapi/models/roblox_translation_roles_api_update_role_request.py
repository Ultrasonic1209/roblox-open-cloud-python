from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.roblox_translation_roles_api_update_role_request_assignee_type import (
    RobloxTranslationRolesApiUpdateRoleRequestAssigneeType,
)
from ..models.roblox_translation_roles_api_update_role_request_role import (
    RobloxTranslationRolesApiUpdateRoleRequestRole,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxTranslationRolesApiUpdateRoleRequest")


@_attrs_define
class RobloxTranslationRolesApiUpdateRoleRequest:
    """The request body for update role endpoints

    Attributes:
        assignee_id (int | Unset): The id of the assignee
        assignee_type (RobloxTranslationRolesApiUpdateRoleRequestAssigneeType | Unset): The type of the assignee ['User'
            = 0, 'Group' = 1, 'GroupRole' = 2]
        role (RobloxTranslationRolesApiUpdateRoleRequestRole | Unset): The role to be assigned or revoked ['Translator'
            = 0]
        revoke (bool | Unset): To assign or to revoke
    """

    assignee_id: int | Unset = UNSET
    assignee_type: RobloxTranslationRolesApiUpdateRoleRequestAssigneeType | Unset = UNSET
    role: RobloxTranslationRolesApiUpdateRoleRequestRole | Unset = UNSET
    revoke: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        assignee_id = self.assignee_id

        assignee_type: str | Unset = UNSET
        if not isinstance(self.assignee_type, Unset):
            assignee_type = self.assignee_type.value

        role: str | Unset = UNSET
        if not isinstance(self.role, Unset):
            role = self.role.value

        revoke = self.revoke

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if assignee_id is not UNSET:
            field_dict["assigneeId"] = assignee_id
        if assignee_type is not UNSET:
            field_dict["assigneeType"] = assignee_type
        if role is not UNSET:
            field_dict["role"] = role
        if revoke is not UNSET:
            field_dict["revoke"] = revoke

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        assignee_id = d.pop("assigneeId", UNSET)

        _assignee_type = d.pop("assigneeType", UNSET)
        assignee_type: RobloxTranslationRolesApiUpdateRoleRequestAssigneeType | Unset
        if isinstance(_assignee_type, Unset):
            assignee_type = UNSET
        else:
            assignee_type = RobloxTranslationRolesApiUpdateRoleRequestAssigneeType(_assignee_type)

        _role = d.pop("role", UNSET)
        role: RobloxTranslationRolesApiUpdateRoleRequestRole | Unset
        if isinstance(_role, Unset):
            role = UNSET
        else:
            role = RobloxTranslationRolesApiUpdateRoleRequestRole(_role)

        revoke = d.pop("revoke", UNSET)

        roblox_translation_roles_api_update_role_request = cls(
            assignee_id=assignee_id,
            assignee_type=assignee_type,
            role=role,
            revoke=revoke,
        )

        roblox_translation_roles_api_update_role_request.additional_properties = d
        return roblox_translation_roles_api_update_role_request

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
