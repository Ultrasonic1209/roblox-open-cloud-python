from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.user_restriction_log_moderator_game_server_script import UserRestrictionLogModeratorGameServerScript


T = TypeVar("T", bound="UserRestrictionLogModerator")


@_attrs_define
class UserRestrictionLogModerator:
    """An entity capturing the author of a state change.

    Attributes:
        roblox_user (str | Unset): A moderator identified by the User resource. Example: users/156.
        game_server_script (UserRestrictionLogModeratorGameServerScript | Unset): Represents a user-written Lua script
            executed on game server.
    """

    roblox_user: str | Unset = UNSET
    game_server_script: UserRestrictionLogModeratorGameServerScript | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        roblox_user = self.roblox_user

        game_server_script: dict[str, Any] | Unset = UNSET
        if not isinstance(self.game_server_script, Unset):
            game_server_script = self.game_server_script.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if roblox_user is not UNSET:
            field_dict["robloxUser"] = roblox_user
        if game_server_script is not UNSET:
            field_dict["gameServerScript"] = game_server_script

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.user_restriction_log_moderator_game_server_script import (
            UserRestrictionLogModeratorGameServerScript,
        )

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        roblox_user = d.pop("robloxUser", UNSET)

        _game_server_script = d.pop("gameServerScript", UNSET)
        game_server_script: UserRestrictionLogModeratorGameServerScript | Unset
        if isinstance(_game_server_script, Unset):
            game_server_script = UNSET
        else:
            game_server_script = UserRestrictionLogModeratorGameServerScript.from_dict(_game_server_script)

        user_restriction_log_moderator = cls(
            roblox_user=roblox_user,
            game_server_script=game_server_script,
        )

        user_restriction_log_moderator.additional_properties = d
        return user_restriction_log_moderator

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
