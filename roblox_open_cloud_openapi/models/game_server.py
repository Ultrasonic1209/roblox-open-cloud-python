from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.server_status import ServerStatus
from ..models.server_type import ServerType
from ..types import UNSET, Unset

T = TypeVar("T", bound="GameServer")


@_attrs_define
class GameServer:
    """Response model for listing a Game Server

    Attributes:
        place_id (None | str): The place ID this game server belongs to.
        place_version (None | str): The place version this game server belongs to.
        job_id (None | str): The unique ID for this server.
        engine_version (None | str): The RCC Version the server is running
        create_time (datetime.datetime): The time this server was created.
        uptime (str): How long this server has been running. Example: 1.02:03:04.
        memory_usage_bytes (int): The Memory Usage of the server in bytes.
        frame_rate (float | None): The Server Frame Rate.
        occupancy (int): The current number of users in the server.
        max_occupancy (int): The maximum number of users in the server.
        type_ (ServerType): Defines the different types of servers
        full (bool): Whether the server is at max occupancy.
        shut_down (bool): Whether the server has been shutdown.
        status (ServerStatus): Server status that is visible to creators.
            This is derived from the shutdown reason for shutdown rows; it is always "Active" for currently live servers.
        termination_time (datetime.datetime | None): The time the server terminated. Null while
            ServerManagementService.V2.Models.GameServer.ShutDown is false.
        player_ids (list[int] | None): The list of PlayerIds in the server
        server_region (None | str | Unset): The region of the server, as nearest Airport Code (Metro)
    """

    place_id: None | str
    place_version: None | str
    job_id: None | str
    engine_version: None | str
    create_time: datetime.datetime
    uptime: str
    memory_usage_bytes: int
    frame_rate: float | None
    occupancy: int
    max_occupancy: int
    type_: ServerType
    full: bool
    shut_down: bool
    status: ServerStatus
    termination_time: datetime.datetime | None
    player_ids: list[int] | None
    server_region: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        place_id: None | str
        place_id = self.place_id

        place_version: None | str
        place_version = self.place_version

        job_id: None | str
        job_id = self.job_id

        engine_version: None | str
        engine_version = self.engine_version

        create_time = self.create_time.isoformat()

        uptime = self.uptime

        memory_usage_bytes = self.memory_usage_bytes

        frame_rate: float | None
        frame_rate = self.frame_rate

        occupancy = self.occupancy

        max_occupancy = self.max_occupancy

        type_ = self.type_.value

        full = self.full

        shut_down = self.shut_down

        status = self.status.value

        termination_time: None | str
        if isinstance(self.termination_time, datetime.datetime):
            termination_time = self.termination_time.isoformat()
        else:
            termination_time = self.termination_time

        player_ids: list[int] | None
        if isinstance(self.player_ids, list):
            player_ids = self.player_ids

        else:
            player_ids = self.player_ids

        server_region: None | str | Unset
        if isinstance(self.server_region, Unset):
            server_region = UNSET
        else:
            server_region = self.server_region

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "placeId": place_id,
                "placeVersion": place_version,
                "jobId": job_id,
                "engineVersion": engine_version,
                "createTime": create_time,
                "uptime": uptime,
                "memoryUsageBytes": memory_usage_bytes,
                "frameRate": frame_rate,
                "occupancy": occupancy,
                "maxOccupancy": max_occupancy,
                "type": type_,
                "full": full,
                "shutDown": shut_down,
                "status": status,
                "terminationTime": termination_time,
                "playerIds": player_ids,
            }
        )
        if server_region is not UNSET:
            field_dict["serverRegion"] = server_region

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_place_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        place_id = _parse_place_id(d.pop("placeId"))

        def _parse_place_version(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        place_version = _parse_place_version(d.pop("placeVersion"))

        def _parse_job_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        job_id = _parse_job_id(d.pop("jobId"))

        def _parse_engine_version(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        engine_version = _parse_engine_version(d.pop("engineVersion"))

        create_time = datetime.datetime.fromisoformat(d.pop("createTime"))

        uptime = d.pop("uptime")

        memory_usage_bytes = d.pop("memoryUsageBytes")

        def _parse_frame_rate(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        frame_rate = _parse_frame_rate(d.pop("frameRate"))

        occupancy = d.pop("occupancy")

        max_occupancy = d.pop("maxOccupancy")

        type_ = ServerType(d.pop("type"))

        full = d.pop("full")

        shut_down = d.pop("shutDown")

        status = ServerStatus(d.pop("status"))

        def _parse_termination_time(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                termination_time_type_0 = datetime.datetime.fromisoformat(data)

                return termination_time_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        termination_time = _parse_termination_time(d.pop("terminationTime"))

        def _parse_player_ids(data: object) -> list[int] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                player_ids_type_0 = cast(list[int], data)

                return player_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[int] | None, data)

        player_ids = _parse_player_ids(d.pop("playerIds"))

        def _parse_server_region(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        server_region = _parse_server_region(d.pop("serverRegion", UNSET))

        game_server = cls(
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
            server_region=server_region,
        )

        return game_server
