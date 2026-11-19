from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.roblox_game_localization_client_game_localization_roles_assignee_assignee_type import (
    RobloxGameLocalizationClientGameLocalizationRolesAssigneeAssigneeType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxGameLocalizationClientGameLocalizationRolesAssignee")


@_attrs_define
class RobloxGameLocalizationClientGameLocalizationRolesAssignee:
    """
    Attributes:
        assignee_type (RobloxGameLocalizationClientGameLocalizationRolesAssigneeAssigneeType | Unset):  ['User' = 0,
            'Group' = 1, 'GroupRole' = 2]
        id (int | Unset):
    """

    assignee_type: RobloxGameLocalizationClientGameLocalizationRolesAssigneeAssigneeType | Unset = UNSET
    id: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        assignee_type: str | Unset = UNSET
        if not isinstance(self.assignee_type, Unset):
            assignee_type = self.assignee_type.value

        id = self.id

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if assignee_type is not UNSET:
            field_dict["assigneeType"] = assignee_type
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _assignee_type = d.pop("assigneeType", UNSET)
        assignee_type: RobloxGameLocalizationClientGameLocalizationRolesAssigneeAssigneeType | Unset
        if isinstance(_assignee_type, Unset):
            assignee_type = UNSET
        else:
            assignee_type = RobloxGameLocalizationClientGameLocalizationRolesAssigneeAssigneeType(_assignee_type)

        id = d.pop("id", UNSET)

        roblox_game_localization_client_game_localization_roles_assignee = cls(
            assignee_type=assignee_type,
            id=id,
        )

        return roblox_game_localization_client_game_localization_roles_assignee
