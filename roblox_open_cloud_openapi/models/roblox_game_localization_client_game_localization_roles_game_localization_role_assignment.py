from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_game_localization_client_game_localization_roles_assignee import (
        RobloxGameLocalizationClientGameLocalizationRolesAssignee,
    )


T = TypeVar("T", bound="RobloxGameLocalizationClientGameLocalizationRolesGameLocalizationRoleAssignment")


@_attrs_define
class RobloxGameLocalizationClientGameLocalizationRolesGameLocalizationRoleAssignment:
    """
    Attributes:
        game_id (int | Unset):
        assignee (RobloxGameLocalizationClientGameLocalizationRolesAssignee | Unset):
    """

    game_id: int | Unset = UNSET
    assignee: RobloxGameLocalizationClientGameLocalizationRolesAssignee | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        game_id = self.game_id

        assignee: dict[str, Any] | Unset = UNSET
        if not isinstance(self.assignee, Unset):
            assignee = self.assignee.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if game_id is not UNSET:
            field_dict["gameId"] = game_id
        if assignee is not UNSET:
            field_dict["assignee"] = assignee

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_game_localization_client_game_localization_roles_assignee import (
            RobloxGameLocalizationClientGameLocalizationRolesAssignee,  # noqa: PLC0415
        )

        d = dict(src_dict)
        game_id = d.pop("gameId", UNSET)

        _assignee = d.pop("assignee", UNSET)
        assignee: RobloxGameLocalizationClientGameLocalizationRolesAssignee | Unset
        if isinstance(_assignee, Unset):
            assignee = UNSET
        else:
            assignee = RobloxGameLocalizationClientGameLocalizationRolesAssignee.from_dict(_assignee)

        roblox_game_localization_client_game_localization_roles_game_localization_role_assignment = cls(
            game_id=game_id,
            assignee=assignee,
        )

        return roblox_game_localization_client_game_localization_roles_game_localization_role_assignment
