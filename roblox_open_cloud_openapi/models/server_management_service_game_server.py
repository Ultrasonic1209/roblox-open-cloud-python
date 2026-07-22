from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.server_status import ServerStatus
from ..models.server_type import ServerType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ServerManagementServiceGameServer")


@_attrs_define
class ServerManagementServiceGameServer:
    """Response model for listing a Game Server

    Attributes:
        place_id (None | str | Unset): The place ID this game server belongs to.
        place_version (None | str | Unset): The place version this game server belongs to.
        job_id (None | str | Unset): The unique ID for this server.
        engine_version (None | str | Unset): The RCC Version the server is running
        create_time (datetime.datetime | Unset): The time this server was created.
        uptime (str | Unset): How long this server has been running. Example: 1.02:03:04.
        memory_usage_bytes (int | Unset): The Memory Usage of the server in bytes.
        frame_rate (float | None | Unset): The Server Frame Rate.
        occupancy (int | Unset): The current number of users in the server.
        max_occupancy (int | Unset): The maximum number of users in the server.
        type_ (ServerType | Unset): Defines the different types of servers
        full (bool | Unset): Whether the server is at max occupancy.
        shut_down (bool | Unset): Whether the server has been shutdown.
        status (ServerStatus | Unset): Server status that is visible to creators.
            This is derived from the shutdown reason for shutdown rows; it is always "Active" for currently live servers.
        termination_time (datetime.datetime | None | Unset): The time the server terminated. Null while
            ServerManagementService.V2.Models.GameServer.ShutDown is false.
        player_ids (list[int] | None | Unset): The list of PlayerIds in the server
    """

    place_id: None | str | Unset = UNSET
    place_version: None | str | Unset = UNSET
    job_id: None | str | Unset = UNSET
    engine_version: None | str | Unset = UNSET
    create_time: datetime.datetime | Unset = UNSET
    uptime: str | Unset = UNSET
    memory_usage_bytes: int | Unset = UNSET
    frame_rate: float | None | Unset = UNSET
    occupancy: int | Unset = UNSET
    max_occupancy: int | Unset = UNSET
    type_: ServerType | Unset = UNSET
    full: bool | Unset = UNSET
    shut_down: bool | Unset = UNSET
    status: ServerStatus | Unset = UNSET
    termination_time: datetime.datetime | None | Unset = UNSET
    player_ids: list[int] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        place_id: None | str | Unset
        if isinstance(self.place_id, Unset):
            place_id = UNSET
        else:
            place_id = self.place_id

        place_version: None | str | Unset
        if isinstance(self.place_version, Unset):
            place_version = UNSET
        else:
            place_version = self.place_version

        job_id: None | str | Unset
        if isinstance(self.job_id, Unset):
            job_id = UNSET
        else:
            job_id = self.job_id

        engine_version: None | str | Unset
        if isinstance(self.engine_version, Unset):
            engine_version = UNSET
        else:
            engine_version = self.engine_version

        create_time: str | Unset = UNSET
        if not isinstance(self.create_time, Unset):
            create_time = self.create_time.isoformat()

        uptime = self.uptime

        memory_usage_bytes = self.memory_usage_bytes

        frame_rate: float | None | Unset
        if isinstance(self.frame_rate, Unset):
            frame_rate = UNSET
        else:
            frame_rate = self.frame_rate

        occupancy = self.occupancy

        max_occupancy = self.max_occupancy

        type_: int | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        full = self.full

        shut_down = self.shut_down

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        termination_time: None | str | Unset
        if isinstance(self.termination_time, Unset):
            termination_time = UNSET
        elif isinstance(self.termination_time, datetime.datetime):
            termination_time = self.termination_time.isoformat()
        else:
            termination_time = self.termination_time

        player_ids: list[int] | None | Unset
        if isinstance(self.player_ids, Unset):
            player_ids = UNSET
        elif isinstance(self.player_ids, list):
            player_ids = self.player_ids

        else:
            player_ids = self.player_ids

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if place_id is not UNSET:
            field_dict["placeId"] = place_id
        if place_version is not UNSET:
            field_dict["placeVersion"] = place_version
        if job_id is not UNSET:
            field_dict["jobId"] = job_id
        if engine_version is not UNSET:
            field_dict["engineVersion"] = engine_version
        if create_time is not UNSET:
            field_dict["createTime"] = create_time
        if uptime is not UNSET:
            field_dict["uptime"] = uptime
        if memory_usage_bytes is not UNSET:
            field_dict["memoryUsageBytes"] = memory_usage_bytes
        if frame_rate is not UNSET:
            field_dict["frameRate"] = frame_rate
        if occupancy is not UNSET:
            field_dict["occupancy"] = occupancy
        if max_occupancy is not UNSET:
            field_dict["maxOccupancy"] = max_occupancy
        if type_ is not UNSET:
            field_dict["type"] = type_
        if full is not UNSET:
            field_dict["full"] = full
        if shut_down is not UNSET:
            field_dict["shutDown"] = shut_down
        if status is not UNSET:
            field_dict["status"] = status
        if termination_time is not UNSET:
            field_dict["terminationTime"] = termination_time
        if player_ids is not UNSET:
            field_dict["playerIds"] = player_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}

        def _parse_place_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        place_id = _parse_place_id(d.pop("placeId", UNSET))

        def _parse_place_version(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        place_version = _parse_place_version(d.pop("placeVersion", UNSET))

        def _parse_job_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        job_id = _parse_job_id(d.pop("jobId", UNSET))

        def _parse_engine_version(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        engine_version = _parse_engine_version(d.pop("engineVersion", UNSET))

        _create_time = d.pop("createTime", UNSET)
        create_time: datetime.datetime | Unset
        if isinstance(_create_time, Unset):
            create_time = UNSET
        else:
            create_time = datetime.datetime.fromisoformat(_create_time)

        uptime = d.pop("uptime", UNSET)

        memory_usage_bytes = d.pop("memoryUsageBytes", UNSET)

        def _parse_frame_rate(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        frame_rate = _parse_frame_rate(d.pop("frameRate", UNSET))

        occupancy = d.pop("occupancy", UNSET)

        max_occupancy = d.pop("maxOccupancy", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: ServerType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = ServerType(_type_)

        full = d.pop("full", UNSET)

        shut_down = d.pop("shutDown", UNSET)

        _status = d.pop("status", UNSET)
        status: ServerStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = ServerStatus(_status)

        def _parse_termination_time(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                termination_time_type_0 = datetime.datetime.fromisoformat(data)

                return termination_time_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        termination_time = _parse_termination_time(d.pop("terminationTime", UNSET))

        def _parse_player_ids(data: object) -> list[int] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                player_ids_type_0 = cast(list[int], data)

                return player_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[int] | None | Unset, data)

        player_ids = _parse_player_ids(d.pop("playerIds", UNSET))

        server_management_service_game_server = cls(
            place_id=place_id,
            place_version=place_version,
            job_id=job_id,
            engine_version=engine_version,
            create_time=create_time,
            uptime=uptime,
            memory_usage_bytes=memory_usage_bytes,
            frame_rate=frame_rate,
            occupancy=occupancy,
            max_occupancy=max_occupancy,
            type_=type_,
            full=full,
            shut_down=shut_down,
            status=status,
            termination_time=termination_time,
            player_ids=player_ids,
        )

        return server_management_service_game_server
