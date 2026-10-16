from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="PlaceUpdateStatus")


@_attrs_define
class PlaceUpdateStatus:
    """Container for the status of a game update.

    Attributes:
        place_id (int | Unset): The placeId of the game update
        phase (None | str | Unset): Which phase is the update in: BleedOff, Migrate, or Done
        start_time (datetime.datetime | Unset): When the update started
        end_time (datetime.datetime | None | Unset): When the update is expected to end, or null if it has not ended yet
        start_players_to_be_kicked (int | Unset): Number of players in the game update initially, before any players are
            kicked
        start_instances_to_be_closed (int | Unset): Number of instances that will be closed during the game update
        num_players_to_be_kicked (int | Unset): How many players are remaining in instances that will be shut down
            according to the update configuration
        instances_to_be_closed (int | Unset): Number of places that will be updated
        place_version (int | Unset): The version of the place that is being updated
        place_versions_to_be_closed (list[int] | None | Unset): The versions of the place that will be closed during the
            update
    """

    place_id: int | Unset = UNSET
    phase: None | str | Unset = UNSET
    start_time: datetime.datetime | Unset = UNSET
    end_time: datetime.datetime | None | Unset = UNSET
    start_players_to_be_kicked: int | Unset = UNSET
    start_instances_to_be_closed: int | Unset = UNSET
    num_players_to_be_kicked: int | Unset = UNSET
    instances_to_be_closed: int | Unset = UNSET
    place_version: int | Unset = UNSET
    place_versions_to_be_closed: list[int] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        place_id = self.place_id

        phase: None | str | Unset
        if isinstance(self.phase, Unset):
            phase = UNSET
        else:
            phase = self.phase

        start_time: str | Unset = UNSET
        if not isinstance(self.start_time, Unset):
            start_time = self.start_time.isoformat()

        end_time: None | str | Unset
        if isinstance(self.end_time, Unset):
            end_time = UNSET
        elif isinstance(self.end_time, datetime.datetime):
            end_time = self.end_time.isoformat()
        else:
            end_time = self.end_time

        start_players_to_be_kicked = self.start_players_to_be_kicked

        start_instances_to_be_closed = self.start_instances_to_be_closed

        num_players_to_be_kicked = self.num_players_to_be_kicked

        instances_to_be_closed = self.instances_to_be_closed

        place_version = self.place_version

        place_versions_to_be_closed: list[int] | None | Unset
        if isinstance(self.place_versions_to_be_closed, Unset):
            place_versions_to_be_closed = UNSET
        elif isinstance(self.place_versions_to_be_closed, list):
            place_versions_to_be_closed = self.place_versions_to_be_closed

        else:
            place_versions_to_be_closed = self.place_versions_to_be_closed

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if place_id is not UNSET:
            field_dict["placeId"] = place_id
        if phase is not UNSET:
            field_dict["phase"] = phase
        if start_time is not UNSET:
            field_dict["startTime"] = start_time
        if end_time is not UNSET:
            field_dict["endTime"] = end_time
        if start_players_to_be_kicked is not UNSET:
            field_dict["startPlayersToBeKicked"] = start_players_to_be_kicked
        if start_instances_to_be_closed is not UNSET:
            field_dict["startInstancesToBeClosed"] = start_instances_to_be_closed
        if num_players_to_be_kicked is not UNSET:
            field_dict["numPlayersToBeKicked"] = num_players_to_be_kicked
        if instances_to_be_closed is not UNSET:
            field_dict["instancesToBeClosed"] = instances_to_be_closed
        if place_version is not UNSET:
            field_dict["placeVersion"] = place_version
        if place_versions_to_be_closed is not UNSET:
            field_dict["placeVersionsToBeClosed"] = place_versions_to_be_closed

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        place_id = d.pop("placeId", UNSET)

        def _parse_phase(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        phase = _parse_phase(d.pop("phase", UNSET))

        _start_time = d.pop("startTime", UNSET)
        start_time: datetime.datetime | Unset
        if isinstance(_start_time, Unset):
            start_time = UNSET
        else:
            start_time = datetime.datetime.fromisoformat(_start_time)

        def _parse_end_time(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                end_time_type_0 = datetime.datetime.fromisoformat(data)

                return end_time_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        end_time = _parse_end_time(d.pop("endTime", UNSET))

        start_players_to_be_kicked = d.pop("startPlayersToBeKicked", UNSET)

        start_instances_to_be_closed = d.pop("startInstancesToBeClosed", UNSET)

        num_players_to_be_kicked = d.pop("numPlayersToBeKicked", UNSET)

        instances_to_be_closed = d.pop("instancesToBeClosed", UNSET)

        place_version = d.pop("placeVersion", UNSET)

        def _parse_place_versions_to_be_closed(data: object) -> list[int] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                place_versions_to_be_closed_type_0 = cast(list[int], data)

                return place_versions_to_be_closed_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[int] | None | Unset, data)

        place_versions_to_be_closed = _parse_place_versions_to_be_closed(d.pop("placeVersionsToBeClosed", UNSET))

        place_update_status = cls(
            place_id=place_id,
            phase=phase,
            start_time=start_time,
            end_time=end_time,
            start_players_to_be_kicked=start_players_to_be_kicked,
            start_instances_to_be_closed=start_instances_to_be_closed,
            num_players_to_be_kicked=num_players_to_be_kicked,
            instances_to_be_closed=instances_to_be_closed,
            place_version=place_version,
            place_versions_to_be_closed=place_versions_to_be_closed,
        )

        return place_update_status
