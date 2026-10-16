from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="ShutdownGameInstancesRequest")


@_attrs_define
class ShutdownGameInstancesRequest:
    """Shutdown Game Instance request.

    Attributes:
        place_id (int | Unset): The place ID to shut down.
        private_server_id (int | None | Unset): The private server ID.
        game_id (None | Unset | UUID): The game ID.
    """

    place_id: int | Unset = UNSET
    private_server_id: int | None | Unset = UNSET
    game_id: None | Unset | UUID = UNSET

    def to_dict(self) -> dict[str, Any]:
        place_id = self.place_id

        private_server_id: int | None | Unset
        if isinstance(self.private_server_id, Unset):
            private_server_id = UNSET
        else:
            private_server_id = self.private_server_id

        game_id: None | str | Unset
        if isinstance(self.game_id, Unset):
            game_id = UNSET
        elif isinstance(self.game_id, UUID):
            game_id = str(self.game_id)
        else:
            game_id = self.game_id

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if place_id is not UNSET:
            field_dict["placeId"] = place_id
        if private_server_id is not UNSET:
            field_dict["privateServerId"] = private_server_id
        if game_id is not UNSET:
            field_dict["gameId"] = game_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        place_id = d.pop("placeId", UNSET)

        def _parse_private_server_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        private_server_id = _parse_private_server_id(d.pop("privateServerId", UNSET))

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

        shutdown_game_instances_request = cls(
            place_id=place_id,
            private_server_id=private_server_id,
            game_id=game_id,
        )

        return shutdown_game_instances_request
