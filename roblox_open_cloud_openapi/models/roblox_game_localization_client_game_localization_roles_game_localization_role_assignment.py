from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

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
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        game_id = self.game_id

        assignee: dict[str, Any] | Unset = UNSET
        if not isinstance(self.assignee, Unset):
            assignee = self.assignee.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if game_id is not UNSET:
            field_dict["gameId"] = game_id
        if assignee is not UNSET:
            field_dict["assignee"] = assignee

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_game_localization_client_game_localization_roles_assignee import (
            RobloxGameLocalizationClientGameLocalizationRolesAssignee,
        )

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
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

        roblox_game_localization_client_game_localization_roles_game_localization_role_assignment.additional_properties = d
        return roblox_game_localization_client_game_localization_roles_game_localization_role_assignment

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
