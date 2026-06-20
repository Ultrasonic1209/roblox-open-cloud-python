from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.restart_state import RestartState
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.place_filter import PlaceFilter


T = TypeVar("T", bound="PlaceRestartStatus")


@_attrs_define
class PlaceRestartStatus:
    """Per-place restart status.

    Attributes:
        state (RestartState | Unset): The current state of a place restart.
        start_time (datetime.datetime | Unset): When the place restart started.
        end_time (datetime.datetime | None | Unset): When the place restart ended (null if still in progress).
        total_players (int | Unset): Initial total count of players to be kicked.
        total_instances (int | Unset): Initial total count of instances to be restarted.
        remaining_players (int | Unset): Remaining players to be kicked.
        remaining_instances (int | Unset): Remaining instances to be closed.
        filter_ (None | PlaceFilter | Unset): The filter that was applied to select which versions to restart.
        latest_version (None | str | Unset): Latest version at the time of the restart.
    """

    state: RestartState | Unset = UNSET
    start_time: datetime.datetime | Unset = UNSET
    end_time: datetime.datetime | None | Unset = UNSET
    total_players: int | Unset = UNSET
    total_instances: int | Unset = UNSET
    remaining_players: int | Unset = UNSET
    remaining_instances: int | Unset = UNSET
    filter_: None | PlaceFilter | Unset = UNSET
    latest_version: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.place_filter import PlaceFilter

        state: str | Unset = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value

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

        total_players = self.total_players

        total_instances = self.total_instances

        remaining_players = self.remaining_players

        remaining_instances = self.remaining_instances

        filter_: dict[str, Any] | None | Unset
        if isinstance(self.filter_, Unset):
            filter_ = UNSET
        elif isinstance(self.filter_, PlaceFilter):
            filter_ = self.filter_.to_dict()
        else:
            filter_ = self.filter_

        latest_version: None | str | Unset
        if isinstance(self.latest_version, Unset):
            latest_version = UNSET
        else:
            latest_version = self.latest_version

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if state is not UNSET:
            field_dict["state"] = state
        if start_time is not UNSET:
            field_dict["startTime"] = start_time
        if end_time is not UNSET:
            field_dict["endTime"] = end_time
        if total_players is not UNSET:
            field_dict["totalPlayers"] = total_players
        if total_instances is not UNSET:
            field_dict["totalInstances"] = total_instances
        if remaining_players is not UNSET:
            field_dict["remainingPlayers"] = remaining_players
        if remaining_instances is not UNSET:
            field_dict["remainingInstances"] = remaining_instances
        if filter_ is not UNSET:
            field_dict["filter"] = filter_
        if latest_version is not UNSET:
            field_dict["latestVersion"] = latest_version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.place_filter import PlaceFilter

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        _state = d.pop("state", UNSET)
        state: RestartState | Unset
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = RestartState(_state)

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

        total_players = d.pop("totalPlayers", UNSET)

        total_instances = d.pop("totalInstances", UNSET)

        remaining_players = d.pop("remainingPlayers", UNSET)

        remaining_instances = d.pop("remainingInstances", UNSET)

        def _parse_filter_(data: object) -> None | PlaceFilter | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                filter_type_1 = PlaceFilter.from_dict(data)

                return filter_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PlaceFilter | Unset, data)

        filter_ = _parse_filter_(d.pop("filter", UNSET))

        def _parse_latest_version(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        latest_version = _parse_latest_version(d.pop("latestVersion", UNSET))

        place_restart_status = cls(
            state=state,
            start_time=start_time,
            end_time=end_time,
            total_players=total_players,
            total_instances=total_instances,
            remaining_players=remaining_players,
            remaining_instances=remaining_instances,
            filter_=filter_,
            latest_version=latest_version,
        )

        return place_restart_status
