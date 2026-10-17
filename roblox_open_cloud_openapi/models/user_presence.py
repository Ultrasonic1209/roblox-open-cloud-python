from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..models.presence_type import PresenceType
from ..types import UNSET, Unset

T = TypeVar("T", bound="UserPresence")


@_attrs_define
class UserPresence:
    """
    Attributes:
        user_presence_type (PresenceType | Unset):
        last_location (None | str | Unset):
        place_id (int | None | Unset):
        root_place_id (int | None | Unset):
        game_id (None | Unset | UUID):
        universe_id (int | None | Unset):
        user_id (int | Unset):
    """

    user_presence_type: PresenceType | Unset = UNSET
    last_location: None | str | Unset = UNSET
    place_id: int | None | Unset = UNSET
    root_place_id: int | None | Unset = UNSET
    game_id: None | Unset | UUID = UNSET
    universe_id: int | None | Unset = UNSET
    user_id: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        user_presence_type: int | Unset = UNSET
        if not isinstance(self.user_presence_type, Unset):
            user_presence_type = self.user_presence_type.value

        last_location: None | str | Unset
        if isinstance(self.last_location, Unset):
            last_location = UNSET
        else:
            last_location = self.last_location

        place_id: int | None | Unset
        if isinstance(self.place_id, Unset):
            place_id = UNSET
        else:
            place_id = self.place_id

        root_place_id: int | None | Unset
        if isinstance(self.root_place_id, Unset):
            root_place_id = UNSET
        else:
            root_place_id = self.root_place_id

        game_id: None | str | Unset
        if isinstance(self.game_id, Unset):
            game_id = UNSET
        elif isinstance(self.game_id, UUID):
            game_id = str(self.game_id)
        else:
            game_id = self.game_id

        universe_id: int | None | Unset
        if isinstance(self.universe_id, Unset):
            universe_id = UNSET
        else:
            universe_id = self.universe_id

        user_id = self.user_id

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if user_presence_type is not UNSET:
            field_dict["userPresenceType"] = user_presence_type
        if last_location is not UNSET:
            field_dict["lastLocation"] = last_location
        if place_id is not UNSET:
            field_dict["placeId"] = place_id
        if root_place_id is not UNSET:
            field_dict["rootPlaceId"] = root_place_id
        if game_id is not UNSET:
            field_dict["gameId"] = game_id
        if universe_id is not UNSET:
            field_dict["universeId"] = universe_id
        if user_id is not UNSET:
            field_dict["userId"] = user_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _user_presence_type = d.pop("userPresenceType", UNSET)
        user_presence_type: PresenceType | Unset
        if isinstance(_user_presence_type, Unset):
            user_presence_type = UNSET
        else:
            user_presence_type = PresenceType(_user_presence_type)

        def _parse_last_location(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        last_location = _parse_last_location(d.pop("lastLocation", UNSET))

        def _parse_place_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        place_id = _parse_place_id(d.pop("placeId", UNSET))

        def _parse_root_place_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        root_place_id = _parse_root_place_id(d.pop("rootPlaceId", UNSET))

        def _parse_game_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                game_id_type_0 = UUID(data)

                return game_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        game_id = _parse_game_id(d.pop("gameId", UNSET))

        def _parse_universe_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        universe_id = _parse_universe_id(d.pop("universeId", UNSET))

        user_id = d.pop("userId", UNSET)

        user_presence = cls(
            user_presence_type=user_presence_type,
            last_location=last_location,
            place_id=place_id,
            root_place_id=root_place_id,
            game_id=game_id,
            universe_id=universe_id,
            user_id=user_id,
        )

        return user_presence
