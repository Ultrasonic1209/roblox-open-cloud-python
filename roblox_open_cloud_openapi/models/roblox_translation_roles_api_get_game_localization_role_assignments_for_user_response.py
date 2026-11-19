from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

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
            RobloxGameLocalizationClientGameLocalizationRolesGameLocalizationRoleAssignment,  # noqa: PLC0415
        )

        d = dict(src_dict)
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

        return roblox_translation_roles_api_get_game_localization_role_assignments_for_user_response
