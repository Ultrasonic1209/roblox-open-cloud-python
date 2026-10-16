from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_groups_api_user_group_role_response import RobloxGroupsApiUserGroupRoleResponse


T = TypeVar("T", bound="RobloxGroupsApiModelsResponseGroupAuditLogResponseItem")


@_attrs_define
class RobloxGroupsApiModelsResponseGroupAuditLogResponseItem:
    """A group audit log response model

    Attributes:
        actor (RobloxGroupsApiUserGroupRoleResponse | Unset): A user group role response model
        action_type (str | Unset): The action type
        description (Any | Unset): Information on the action performed
        created (datetime.datetime | Unset): Date the group action was performed
    """

    actor: RobloxGroupsApiUserGroupRoleResponse | Unset = UNSET
    action_type: str | Unset = UNSET
    description: Any | Unset = UNSET
    created: datetime.datetime | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        actor: dict[str, Any] | Unset = UNSET
        if not isinstance(self.actor, Unset):
            actor = self.actor.to_dict()

        action_type = self.action_type

        description = self.description

        created: str | Unset = UNSET
        if not isinstance(self.created, Unset):
            created = self.created.isoformat()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if actor is not UNSET:
            field_dict["actor"] = actor
        if action_type is not UNSET:
            field_dict["actionType"] = action_type
        if description is not UNSET:
            field_dict["description"] = description
        if created is not UNSET:
            field_dict["created"] = created

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_groups_api_user_group_role_response import RobloxGroupsApiUserGroupRoleResponse

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        _actor = d.pop("actor", UNSET)
        actor: RobloxGroupsApiUserGroupRoleResponse | Unset
        if isinstance(_actor, Unset):
            actor = UNSET
        else:
            actor = RobloxGroupsApiUserGroupRoleResponse.from_dict(_actor)

        action_type = d.pop("actionType", UNSET)

        description = d.pop("description", UNSET)

        _created = d.pop("created", UNSET)
        created: datetime.datetime | Unset
        if isinstance(_created, Unset):
            created = UNSET
        else:
            created = datetime.datetime.fromisoformat(_created)

        roblox_groups_api_models_response_group_audit_log_response_item = cls(
            actor=actor,
            action_type=action_type,
            description=description,
            created=created,
        )

        return roblox_groups_api_models_response_group_audit_log_response_item
