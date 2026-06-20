from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.user_restriction_log_restriction_type_game_join_restriction import (
        UserRestrictionLogRestrictionTypeGameJoinRestriction,
    )


T = TypeVar("T", bound="UserRestrictionLogRestrictionType")


@_attrs_define
class UserRestrictionLogRestrictionType:
    """The type of restriction.

    Attributes:
        game_join_restriction (UserRestrictionLogRestrictionTypeGameJoinRestriction | Unset): Represents game join
            restriction.
    """

    game_join_restriction: UserRestrictionLogRestrictionTypeGameJoinRestriction | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        game_join_restriction: dict[str, Any] | Unset = UNSET
        if not isinstance(self.game_join_restriction, Unset):
            game_join_restriction = self.game_join_restriction.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if game_join_restriction is not UNSET:
            field_dict["gameJoinRestriction"] = game_join_restriction

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.user_restriction_log_restriction_type_game_join_restriction import (
            UserRestrictionLogRestrictionTypeGameJoinRestriction,
        )

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        _game_join_restriction = d.pop("gameJoinRestriction", UNSET)
        game_join_restriction: UserRestrictionLogRestrictionTypeGameJoinRestriction | Unset
        if isinstance(_game_join_restriction, Unset):
            game_join_restriction = UNSET
        else:
            game_join_restriction = UserRestrictionLogRestrictionTypeGameJoinRestriction.from_dict(
                _game_join_restriction
            )

        user_restriction_log_restriction_type = cls(
            game_join_restriction=game_join_restriction,
        )

        user_restriction_log_restriction_type.additional_properties = d
        return user_restriction_log_restriction_type

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
