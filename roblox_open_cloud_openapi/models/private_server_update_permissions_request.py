from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="PrivateServerUpdatePermissionsRequest")


@_attrs_define
class PrivateServerUpdatePermissionsRequest:
    """
    Attributes:
        clan_allowed (bool | None | Unset):
        enemy_clan_id (int | None | Unset):
        friends_allowed (bool | None | Unset):
        users_to_add (list[int] | None | Unset):
        users_to_remove (list[int] | None | Unset):
    """

    clan_allowed: bool | None | Unset = UNSET
    enemy_clan_id: int | None | Unset = UNSET
    friends_allowed: bool | None | Unset = UNSET
    users_to_add: list[int] | None | Unset = UNSET
    users_to_remove: list[int] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        clan_allowed: bool | None | Unset
        if isinstance(self.clan_allowed, Unset):
            clan_allowed = UNSET
        else:
            clan_allowed = self.clan_allowed

        enemy_clan_id: int | None | Unset
        if isinstance(self.enemy_clan_id, Unset):
            enemy_clan_id = UNSET
        else:
            enemy_clan_id = self.enemy_clan_id

        friends_allowed: bool | None | Unset
        if isinstance(self.friends_allowed, Unset):
            friends_allowed = UNSET
        else:
            friends_allowed = self.friends_allowed

        users_to_add: list[int] | None | Unset
        if isinstance(self.users_to_add, Unset):
            users_to_add = UNSET
        elif isinstance(self.users_to_add, list):
            users_to_add = self.users_to_add

        else:
            users_to_add = self.users_to_add

        users_to_remove: list[int] | None | Unset
        if isinstance(self.users_to_remove, Unset):
            users_to_remove = UNSET
        elif isinstance(self.users_to_remove, list):
            users_to_remove = self.users_to_remove

        else:
            users_to_remove = self.users_to_remove

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if clan_allowed is not UNSET:
            field_dict["clanAllowed"] = clan_allowed
        if enemy_clan_id is not UNSET:
            field_dict["enemyClanId"] = enemy_clan_id
        if friends_allowed is not UNSET:
            field_dict["friendsAllowed"] = friends_allowed
        if users_to_add is not UNSET:
            field_dict["usersToAdd"] = users_to_add
        if users_to_remove is not UNSET:
            field_dict["usersToRemove"] = users_to_remove

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}

        def _parse_clan_allowed(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        clan_allowed = _parse_clan_allowed(d.pop("clanAllowed", UNSET))

        def _parse_enemy_clan_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        enemy_clan_id = _parse_enemy_clan_id(d.pop("enemyClanId", UNSET))

        def _parse_friends_allowed(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        friends_allowed = _parse_friends_allowed(d.pop("friendsAllowed", UNSET))

        def _parse_users_to_add(data: object) -> list[int] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                users_to_add_type_0 = cast(list[int], data)

                return users_to_add_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[int] | None | Unset, data)

        users_to_add = _parse_users_to_add(d.pop("usersToAdd", UNSET))

        def _parse_users_to_remove(data: object) -> list[int] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                users_to_remove_type_0 = cast(list[int], data)

                return users_to_remove_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[int] | None | Unset, data)

        users_to_remove = _parse_users_to_remove(d.pop("usersToRemove", UNSET))

        private_server_update_permissions_request = cls(
            clan_allowed=clan_allowed,
            enemy_clan_id=enemy_clan_id,
            friends_allowed=friends_allowed,
            users_to_add=users_to_add,
            users_to_remove=users_to_remove,
        )

        return private_server_update_permissions_request
