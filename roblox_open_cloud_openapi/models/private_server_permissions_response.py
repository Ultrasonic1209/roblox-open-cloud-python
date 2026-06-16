from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.skinny_user_response import SkinnyUserResponse


T = TypeVar("T", bound="PrivateServerPermissionsResponse")


@_attrs_define
class PrivateServerPermissionsResponse:
    """
    Attributes:
        clan_allowed (bool | Unset):
        enemy_clan_id (int | None | Unset):
        friends_allowed (bool | Unset):
        users (list[SkinnyUserResponse] | None | Unset):
    """

    clan_allowed: bool | Unset = UNSET
    enemy_clan_id: int | None | Unset = UNSET
    friends_allowed: bool | Unset = UNSET
    users: list[SkinnyUserResponse] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        clan_allowed = self.clan_allowed

        enemy_clan_id: int | None | Unset
        if isinstance(self.enemy_clan_id, Unset):
            enemy_clan_id = UNSET
        else:
            enemy_clan_id = self.enemy_clan_id

        friends_allowed = self.friends_allowed

        users: list[dict[str, Any]] | None | Unset
        if isinstance(self.users, Unset):
            users = UNSET
        elif isinstance(self.users, list):
            users = []
            for users_type_0_item_data in self.users:
                users_type_0_item = users_type_0_item_data.to_dict()
                users.append(users_type_0_item)

        else:
            users = self.users

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if clan_allowed is not UNSET:
            field_dict["clanAllowed"] = clan_allowed
        if enemy_clan_id is not UNSET:
            field_dict["enemyClanId"] = enemy_clan_id
        if friends_allowed is not UNSET:
            field_dict["friendsAllowed"] = friends_allowed
        if users is not UNSET:
            field_dict["users"] = users

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.skinny_user_response import SkinnyUserResponse

        d = dict(src_dict)
        clan_allowed = d.pop("clanAllowed", UNSET)

        def _parse_enemy_clan_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        enemy_clan_id = _parse_enemy_clan_id(d.pop("enemyClanId", UNSET))

        friends_allowed = d.pop("friendsAllowed", UNSET)

        def _parse_users(data: object) -> list[SkinnyUserResponse] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                users_type_0 = []
                _users_type_0 = data
                for users_type_0_item_data in _users_type_0:
                    users_type_0_item = SkinnyUserResponse.from_dict(users_type_0_item_data)

                    users_type_0.append(users_type_0_item)

                return users_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[SkinnyUserResponse] | None | Unset, data)

        users = _parse_users(d.pop("users", UNSET))

        private_server_permissions_response = cls(
            clan_allowed=clan_allowed,
            enemy_clan_id=enemy_clan_id,
            friends_allowed=friends_allowed,
            users=users,
        )

        return private_server_permissions_response
