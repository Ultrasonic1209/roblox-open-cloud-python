from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.game_update_status_place_update_statuses_type_0 import GameUpdateStatusPlaceUpdateStatusesType0


T = TypeVar("T", bound="GameUpdateStatus")


@_attrs_define
class GameUpdateStatus:
    """
    Attributes:
        id (UUID | Unset):
        universe_id (int | Unset):
        start_time (datetime.datetime | Unset):
        close_old_versions_only (bool | Unset):
        bleed_off_end_time (datetime.datetime | Unset):
        place_update_statuses (GameUpdateStatusPlaceUpdateStatusesType0 | None | Unset):
        bleed_off_servers (bool | Unset):
    """

    id: UUID | Unset = UNSET
    universe_id: int | Unset = UNSET
    start_time: datetime.datetime | Unset = UNSET
    close_old_versions_only: bool | Unset = UNSET
    bleed_off_end_time: datetime.datetime | Unset = UNSET
    place_update_statuses: GameUpdateStatusPlaceUpdateStatusesType0 | None | Unset = UNSET
    bleed_off_servers: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.game_update_status_place_update_statuses_type_0 import GameUpdateStatusPlaceUpdateStatusesType0

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        universe_id = self.universe_id

        start_time: str | Unset = UNSET
        if not isinstance(self.start_time, Unset):
            start_time = self.start_time.isoformat()

        close_old_versions_only = self.close_old_versions_only

        bleed_off_end_time: str | Unset = UNSET
        if not isinstance(self.bleed_off_end_time, Unset):
            bleed_off_end_time = self.bleed_off_end_time.isoformat()

        place_update_statuses: dict[str, Any] | None | Unset
        if isinstance(self.place_update_statuses, Unset):
            place_update_statuses = UNSET
        elif isinstance(self.place_update_statuses, GameUpdateStatusPlaceUpdateStatusesType0):
            place_update_statuses = self.place_update_statuses.to_dict()
        else:
            place_update_statuses = self.place_update_statuses

        bleed_off_servers = self.bleed_off_servers

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if universe_id is not UNSET:
            field_dict["universeId"] = universe_id
        if start_time is not UNSET:
            field_dict["startTime"] = start_time
        if close_old_versions_only is not UNSET:
            field_dict["closeOldVersionsOnly"] = close_old_versions_only
        if bleed_off_end_time is not UNSET:
            field_dict["bleedOffEndTime"] = bleed_off_end_time
        if place_update_statuses is not UNSET:
            field_dict["placeUpdateStatuses"] = place_update_statuses
        if bleed_off_servers is not UNSET:
            field_dict["bleedOffServers"] = bleed_off_servers

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.game_update_status_place_update_statuses_type_0 import GameUpdateStatusPlaceUpdateStatusesType0

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = UUID(_id)

        universe_id = d.pop("universeId", UNSET)

        _start_time = d.pop("startTime", UNSET)
        start_time: datetime.datetime | Unset
        if isinstance(_start_time, Unset):
            start_time = UNSET
        else:
            start_time = datetime.datetime.fromisoformat(_start_time)

        close_old_versions_only = d.pop("closeOldVersionsOnly", UNSET)

        _bleed_off_end_time = d.pop("bleedOffEndTime", UNSET)
        bleed_off_end_time: datetime.datetime | Unset
        if isinstance(_bleed_off_end_time, Unset):
            bleed_off_end_time = UNSET
        else:
            bleed_off_end_time = datetime.datetime.fromisoformat(_bleed_off_end_time)

        def _parse_place_update_statuses(data: object) -> GameUpdateStatusPlaceUpdateStatusesType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                place_update_statuses_type_0 = GameUpdateStatusPlaceUpdateStatusesType0.from_dict(data)

                return place_update_statuses_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GameUpdateStatusPlaceUpdateStatusesType0 | None | Unset, data)

        place_update_statuses = _parse_place_update_statuses(d.pop("placeUpdateStatuses", UNSET))

        bleed_off_servers = d.pop("bleedOffServers", UNSET)

        game_update_status = cls(
            id=id,
            universe_id=universe_id,
            start_time=start_time,
            close_old_versions_only=close_old_versions_only,
            bleed_off_end_time=bleed_off_end_time,
            place_update_statuses=place_update_statuses,
            bleed_off_servers=bleed_off_servers,
        )

        return game_update_status
