from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.user_restriction_game_join_restriction import UserRestrictionGameJoinRestriction


T = TypeVar("T", bound="UserRestriction")


@_attrs_define
class UserRestriction:
    """Represents a restriction on a user.

    Attributes:
        path (str | Unset): The resource path of the user restriction.

            Formats:
            * `universes/{universe_id}/user-restrictions/{user_restriction_id}`
            * `universes/{universe_id}/places/{place_id}/user-restrictions/{user_restriction_id}` Example:
            universes/123/user-restrictions/123.
        update_time (datetime.datetime | Unset): The timestamp when the user restriction was last updated. Example:
            2023-07-05T12:34:56Z.
        user (str | Unset): The affected user. Example: users/156.
        game_join_restriction (UserRestrictionGameJoinRestriction | Unset): A restriction means the affected user will
            not be able to join the parent
            universe or place, and will be kicked if currently joined.
    """

    path: str | Unset = UNSET
    update_time: datetime.datetime | Unset = UNSET
    user: str | Unset = UNSET
    game_join_restriction: UserRestrictionGameJoinRestriction | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        path = self.path

        update_time: str | Unset = UNSET
        if not isinstance(self.update_time, Unset):
            update_time = self.update_time.isoformat()

        user = self.user

        game_join_restriction: dict[str, Any] | Unset = UNSET
        if not isinstance(self.game_join_restriction, Unset):
            game_join_restriction = self.game_join_restriction.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if path is not UNSET:
            field_dict["path"] = path
        if update_time is not UNSET:
            field_dict["updateTime"] = update_time
        if user is not UNSET:
            field_dict["user"] = user
        if game_join_restriction is not UNSET:
            field_dict["gameJoinRestriction"] = game_join_restriction

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.user_restriction_game_join_restriction import UserRestrictionGameJoinRestriction

        d = dict(src_dict)
        path = d.pop("path", UNSET)

        _update_time = d.pop("updateTime", UNSET)
        update_time: datetime.datetime | Unset
        if isinstance(_update_time, Unset):
            update_time = UNSET
        else:
            update_time = datetime.datetime.fromisoformat(_update_time)

        user = d.pop("user", UNSET)

        _game_join_restriction = d.pop("gameJoinRestriction", UNSET)
        game_join_restriction: UserRestrictionGameJoinRestriction | Unset
        if isinstance(_game_join_restriction, Unset):
            game_join_restriction = UNSET
        else:
            game_join_restriction = UserRestrictionGameJoinRestriction.from_dict(_game_join_restriction)

        user_restriction = cls(
            path=path,
            update_time=update_time,
            user=user,
            game_join_restriction=game_join_restriction,
        )

        user_restriction.additional_properties = d
        return user_restriction

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
