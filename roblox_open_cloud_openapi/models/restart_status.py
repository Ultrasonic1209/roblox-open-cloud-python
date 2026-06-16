from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.restart_status_place_restart_statuses_type_0 import RestartStatusPlaceRestartStatusesType0


T = TypeVar("T", bound="RestartStatus")


@_attrs_define
class RestartStatus:
    """Status of a game restart.

    Attributes:
        universe_id (None | str | Unset): Universe ID.
        scheduled_time (datetime.datetime | Unset): When the restart was launched (scheduled time).
        start_time (datetime.datetime | Unset): When the bleed-off period ends and restarts begin.
        place_restart_statuses (None | RestartStatusPlaceRestartStatusesType0 | Unset): Per-place statuses keyed by
            place ID.
    """

    universe_id: None | str | Unset = UNSET
    scheduled_time: datetime.datetime | Unset = UNSET
    start_time: datetime.datetime | Unset = UNSET
    place_restart_statuses: None | RestartStatusPlaceRestartStatusesType0 | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.restart_status_place_restart_statuses_type_0 import RestartStatusPlaceRestartStatusesType0

        universe_id: None | str | Unset
        if isinstance(self.universe_id, Unset):
            universe_id = UNSET
        else:
            universe_id = self.universe_id

        scheduled_time: str | Unset = UNSET
        if not isinstance(self.scheduled_time, Unset):
            scheduled_time = self.scheduled_time.isoformat()

        start_time: str | Unset = UNSET
        if not isinstance(self.start_time, Unset):
            start_time = self.start_time.isoformat()

        place_restart_statuses: dict[str, Any] | None | Unset
        if isinstance(self.place_restart_statuses, Unset):
            place_restart_statuses = UNSET
        elif isinstance(self.place_restart_statuses, RestartStatusPlaceRestartStatusesType0):
            place_restart_statuses = self.place_restart_statuses.to_dict()
        else:
            place_restart_statuses = self.place_restart_statuses

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if universe_id is not UNSET:
            field_dict["universeId"] = universe_id
        if scheduled_time is not UNSET:
            field_dict["scheduledTime"] = scheduled_time
        if start_time is not UNSET:
            field_dict["startTime"] = start_time
        if place_restart_statuses is not UNSET:
            field_dict["placeRestartStatuses"] = place_restart_statuses

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.restart_status_place_restart_statuses_type_0 import RestartStatusPlaceRestartStatusesType0

        d = dict(src_dict)

        def _parse_universe_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        universe_id = _parse_universe_id(d.pop("universeId", UNSET))

        _scheduled_time = d.pop("scheduledTime", UNSET)
        scheduled_time: datetime.datetime | Unset
        if isinstance(_scheduled_time, Unset):
            scheduled_time = UNSET
        else:
            scheduled_time = datetime.datetime.fromisoformat(_scheduled_time)

        _start_time = d.pop("startTime", UNSET)
        start_time: datetime.datetime | Unset
        if isinstance(_start_time, Unset):
            start_time = UNSET
        else:
            start_time = datetime.datetime.fromisoformat(_start_time)

        def _parse_place_restart_statuses(data: object) -> None | RestartStatusPlaceRestartStatusesType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                place_restart_statuses_type_0 = RestartStatusPlaceRestartStatusesType0.from_dict(data)

                return place_restart_statuses_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | RestartStatusPlaceRestartStatusesType0 | Unset, data)

        place_restart_statuses = _parse_place_restart_statuses(d.pop("placeRestartStatuses", UNSET))

        restart_status = cls(
            universe_id=universe_id,
            scheduled_time=scheduled_time,
            start_time=start_time,
            place_restart_statuses=place_restart_statuses,
        )

        return restart_status
