from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.game_update_status_place_update_statuses_type_0 import GameUpdateStatusPlaceUpdateStatusesType0


T = TypeVar("T", bound="GameUpdateStatus")


@_attrs_define
class GameUpdateStatus:
    """
    Attributes:
        id (UUID):
        universe_id (int):
        start_time (datetime.datetime):
        close_old_versions_only (bool):
        bleed_off_end_time (datetime.datetime):
        place_update_statuses (GameUpdateStatusPlaceUpdateStatusesType0 | None):
        bleed_off_servers (bool):
    """

    id: UUID
    universe_id: int
    start_time: datetime.datetime
    close_old_versions_only: bool
    bleed_off_end_time: datetime.datetime
    place_update_statuses: GameUpdateStatusPlaceUpdateStatusesType0 | None
    bleed_off_servers: bool

    def to_dict(self) -> dict[str, Any]:
        from ..models.game_update_status_place_update_statuses_type_0 import GameUpdateStatusPlaceUpdateStatusesType0  # noqa: PLC0415

        id = str(self.id)

        universe_id = self.universe_id

        start_time = self.start_time.isoformat()

        close_old_versions_only = self.close_old_versions_only

        bleed_off_end_time = self.bleed_off_end_time.isoformat()

        place_update_statuses: dict[str, Any] | None
        if isinstance(self.place_update_statuses, GameUpdateStatusPlaceUpdateStatusesType0):
            place_update_statuses = self.place_update_statuses.to_dict()
        else:
            place_update_statuses = self.place_update_statuses

        bleed_off_servers = self.bleed_off_servers

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "universeId": universe_id,
                "startTime": start_time,
                "closeOldVersionsOnly": close_old_versions_only,
                "bleedOffEndTime": bleed_off_end_time,
                "placeUpdateStatuses": place_update_statuses,
                "bleedOffServers": bleed_off_servers,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.game_update_status_place_update_statuses_type_0 import GameUpdateStatusPlaceUpdateStatusesType0  # noqa: PLC0415

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        universe_id = d.pop("universeId")

        start_time = datetime.datetime.fromisoformat(d.pop("startTime"))

        close_old_versions_only = d.pop("closeOldVersionsOnly")

        bleed_off_end_time = datetime.datetime.fromisoformat(d.pop("bleedOffEndTime"))

        def _parse_place_update_statuses(data: object) -> GameUpdateStatusPlaceUpdateStatusesType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                place_update_statuses_type_0 = GameUpdateStatusPlaceUpdateStatusesType0.from_dict(data)

                return place_update_statuses_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GameUpdateStatusPlaceUpdateStatusesType0 | None, data)

        place_update_statuses = _parse_place_update_statuses(d.pop("placeUpdateStatuses"))

        bleed_off_servers = d.pop("bleedOffServers")

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
