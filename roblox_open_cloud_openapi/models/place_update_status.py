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
        place_id (int): The placeId of the game update
        phase (None | str): Which phase is the update in: BleedOff, Migrate, or Done
        start_time (datetime.datetime): When the update started
        start_players_to_be_kicked (int): Number of players in the game update initially, before any players are kicked
        start_instances_to_be_closed (int): Number of instances that will be closed during the game update
        num_players_to_be_kicked (int): How many players are remaining in instances that will be shut down according to
            the update configuration
        instances_to_be_closed (int): Number of places that will be updated
        place_version (int): The version of the place that is being updated
        end_time (datetime.datetime | None | Unset): When the update is expected to end, or null if it has not ended yet
        place_versions_to_be_closed (list[int] | None | Unset): The versions of the place that will be closed during the
            update
    """

    place_id: int
    phase: None | str
    start_time: datetime.datetime
    start_players_to_be_kicked: int
    start_instances_to_be_closed: int
    num_players_to_be_kicked: int
    instances_to_be_closed: int
    place_version: int
    end_time: datetime.datetime | None | Unset = UNSET
    place_versions_to_be_closed: list[int] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        place_id = self.place_id

        phase: None | str
        phase = self.phase

        start_time = self.start_time.isoformat()

        start_players_to_be_kicked = self.start_players_to_be_kicked

        start_instances_to_be_closed = self.start_instances_to_be_closed

        num_players_to_be_kicked = self.num_players_to_be_kicked

        instances_to_be_closed = self.instances_to_be_closed

        place_version = self.place_version

        end_time: None | str | Unset
        if isinstance(self.end_time, Unset):
            end_time = UNSET
        elif isinstance(self.end_time, datetime.datetime):
            end_time = self.end_time.isoformat()
        else:
            end_time = self.end_time

        place_versions_to_be_closed: list[int] | None | Unset
        if isinstance(self.place_versions_to_be_closed, Unset):
            place_versions_to_be_closed = UNSET
        elif isinstance(self.place_versions_to_be_closed, list):
            place_versions_to_be_closed = self.place_versions_to_be_closed

        else:
            place_versions_to_be_closed = self.place_versions_to_be_closed

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "placeId": place_id,
                "phase": phase,
                "startTime": start_time,
                "startPlayersToBeKicked": start_players_to_be_kicked,
                "startInstancesToBeClosed": start_instances_to_be_closed,
                "numPlayersToBeKicked": num_players_to_be_kicked,
                "instancesToBeClosed": instances_to_be_closed,
                "placeVersion": place_version,
            }
        )
        if end_time is not UNSET:
            field_dict["endTime"] = end_time
        if place_versions_to_be_closed is not UNSET:
            field_dict["placeVersionsToBeClosed"] = place_versions_to_be_closed

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        place_id = d.pop("placeId")

        def _parse_phase(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        phase = _parse_phase(d.pop("phase"))

        start_time = datetime.datetime.fromisoformat(d.pop("startTime"))

        start_players_to_be_kicked = d.pop("startPlayersToBeKicked")

        start_instances_to_be_closed = d.pop("startInstancesToBeClosed")

        num_players_to_be_kicked = d.pop("numPlayersToBeKicked")

        instances_to_be_closed = d.pop("instancesToBeClosed")

        place_version = d.pop("placeVersion")

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
            start_players_to_be_kicked=start_players_to_be_kicked,
            start_instances_to_be_closed=start_instances_to_be_closed,
            num_players_to_be_kicked=num_players_to_be_kicked,
            instances_to_be_closed=instances_to_be_closed,
            place_version=place_version,
            end_time=end_time,
            place_versions_to_be_closed=place_versions_to_be_closed,
        )

        return place_update_status
