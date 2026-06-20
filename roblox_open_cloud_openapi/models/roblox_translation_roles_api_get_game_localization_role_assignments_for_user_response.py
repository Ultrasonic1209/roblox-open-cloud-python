from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_game_localization_client_game_localization_roles_game_localization_role_assignment import (
        RobloxGameLocalizationClientGameLocalizationRolesGameLocalizationRoleAssignment,
    )


T = TypeVar("T", bound="RobloxTranslationRolesApiGetGameLocalizationRoleAssignmentsForUserResponse")


@_attrs_define
class RobloxTranslationRolesApiGetGameLocalizationRoleAssignmentsForUserResponse:
    """Response model containing a list of games and associated role assignment info for the requested user and role.

    Attributes:
        games (list[RobloxGameLocalizationClientGameLocalizationRolesGameLocalizationRoleAssignment] | Unset): List of
            games with associated role assignment info.
        previous_page_cursor (str | Unset): Cursor which can be used for navigating to previous page.
        next_page_cursor (str | Unset): Cursor which can be used for navigating to next page.
    """

    games: list[RobloxGameLocalizationClientGameLocalizationRolesGameLocalizationRoleAssignment] | Unset = UNSET
    previous_page_cursor: str | Unset = UNSET
    next_page_cursor: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        games: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.games, Unset):
            games = []
            for games_item_data in self.games:
                games_item = games_item_data.to_dict()
                games.append(games_item)

        previous_page_cursor = self.previous_page_cursor

        next_page_cursor = self.next_page_cursor

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if games is not UNSET:
            field_dict["games"] = games
        if previous_page_cursor is not UNSET:
            field_dict["previousPageCursor"] = previous_page_cursor
        if next_page_cursor is not UNSET:
            field_dict["nextPageCursor"] = next_page_cursor

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_game_localization_client_game_localization_roles_game_localization_role_assignment import (
            RobloxGameLocalizationClientGameLocalizationRolesGameLocalizationRoleAssignment,
        )

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        _games = d.pop("games", UNSET)
        games: list[RobloxGameLocalizationClientGameLocalizationRolesGameLocalizationRoleAssignment] | Unset = UNSET
        if _games is not UNSET:
            games = []
            for games_item_data in _games:
                games_item = RobloxGameLocalizationClientGameLocalizationRolesGameLocalizationRoleAssignment.from_dict(
                    games_item_data
                )

                games.append(games_item)

        previous_page_cursor = d.pop("previousPageCursor", UNSET)

        next_page_cursor = d.pop("nextPageCursor", UNSET)

        roblox_translation_roles_api_get_game_localization_role_assignments_for_user_response = cls(
            games=games,
            previous_page_cursor=previous_page_cursor,
            next_page_cursor=next_page_cursor,
        )

        roblox_translation_roles_api_get_game_localization_role_assignments_for_user_response.additional_properties = d
        return roblox_translation_roles_api_get_game_localization_role_assignments_for_user_response

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
