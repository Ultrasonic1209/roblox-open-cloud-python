from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.place_summary_for_game_restart_instances_per_version_type_0 import (
        PlaceSummaryForGameRestartInstancesPerVersionType0,
    )
    from ..models.place_summary_for_game_restart_players_per_version_type_0 import (
        PlaceSummaryForGameRestartPlayersPerVersionType0,
    )


T = TypeVar("T", bound="PlaceSummaryForGameRestart")


@_attrs_define
class PlaceSummaryForGameRestart:
    """Per-place forecast data for a game restart.

    Attributes:
        players_impacted (int | Unset): Number of players that would be kicked during the restart.
        total_players (int | Unset): Total players currently in the place, including those not impacted.
        instances_impacted (int | Unset): Number of instances that would be closed.
        total_instances (int | Unset): Total instances for the place.
        latest_place_version (None | str | Unset): The most recent version of the place in any active server.
        publish_time (datetime.datetime | Unset): Timestamp for the publication of the latest place version.
        is_not_in_universe (bool | Unset): Whether the place does not belong to the universe.
            True when a place moved to a different universe but still has active servers from before.
        players_per_version (None | PlaceSummaryForGameRestartPlayersPerVersionType0 | Unset): Player count per place
            version.
        instances_per_version (None | PlaceSummaryForGameRestartInstancesPerVersionType0 | Unset): Instance count per
            place version.
    """

    players_impacted: int | Unset = UNSET
    total_players: int | Unset = UNSET
    instances_impacted: int | Unset = UNSET
    total_instances: int | Unset = UNSET
    latest_place_version: None | str | Unset = UNSET
    publish_time: datetime.datetime | Unset = UNSET
    is_not_in_universe: bool | Unset = UNSET
    players_per_version: None | PlaceSummaryForGameRestartPlayersPerVersionType0 | Unset = UNSET
    instances_per_version: None | PlaceSummaryForGameRestartInstancesPerVersionType0 | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.place_summary_for_game_restart_instances_per_version_type_0 import (
            PlaceSummaryForGameRestartInstancesPerVersionType0,
        )
        from ..models.place_summary_for_game_restart_players_per_version_type_0 import (
            PlaceSummaryForGameRestartPlayersPerVersionType0,
        )

        players_impacted = self.players_impacted

        total_players = self.total_players

        instances_impacted = self.instances_impacted

        total_instances = self.total_instances

        latest_place_version: None | str | Unset
        if isinstance(self.latest_place_version, Unset):
            latest_place_version = UNSET
        else:
            latest_place_version = self.latest_place_version

        publish_time: str | Unset = UNSET
        if not isinstance(self.publish_time, Unset):
            publish_time = self.publish_time.isoformat()

        is_not_in_universe = self.is_not_in_universe

        players_per_version: dict[str, Any] | None | Unset
        if isinstance(self.players_per_version, Unset):
            players_per_version = UNSET
        elif isinstance(self.players_per_version, PlaceSummaryForGameRestartPlayersPerVersionType0):
            players_per_version = self.players_per_version.to_dict()
        else:
            players_per_version = self.players_per_version

        instances_per_version: dict[str, Any] | None | Unset
        if isinstance(self.instances_per_version, Unset):
            instances_per_version = UNSET
        elif isinstance(self.instances_per_version, PlaceSummaryForGameRestartInstancesPerVersionType0):
            instances_per_version = self.instances_per_version.to_dict()
        else:
            instances_per_version = self.instances_per_version

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if players_impacted is not UNSET:
            field_dict["playersImpacted"] = players_impacted
        if total_players is not UNSET:
            field_dict["totalPlayers"] = total_players
        if instances_impacted is not UNSET:
            field_dict["instancesImpacted"] = instances_impacted
        if total_instances is not UNSET:
            field_dict["totalInstances"] = total_instances
        if latest_place_version is not UNSET:
            field_dict["latestPlaceVersion"] = latest_place_version
        if publish_time is not UNSET:
            field_dict["publishTime"] = publish_time
        if is_not_in_universe is not UNSET:
            field_dict["isNotInUniverse"] = is_not_in_universe
        if players_per_version is not UNSET:
            field_dict["playersPerVersion"] = players_per_version
        if instances_per_version is not UNSET:
            field_dict["instancesPerVersion"] = instances_per_version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.place_summary_for_game_restart_instances_per_version_type_0 import (
            PlaceSummaryForGameRestartInstancesPerVersionType0,
        )
        from ..models.place_summary_for_game_restart_players_per_version_type_0 import (
            PlaceSummaryForGameRestartPlayersPerVersionType0,
        )

        d = dict(src_dict)
        players_impacted = d.pop("playersImpacted", UNSET)

        total_players = d.pop("totalPlayers", UNSET)

        instances_impacted = d.pop("instancesImpacted", UNSET)

        total_instances = d.pop("totalInstances", UNSET)

        def _parse_latest_place_version(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        latest_place_version = _parse_latest_place_version(d.pop("latestPlaceVersion", UNSET))

        _publish_time = d.pop("publishTime", UNSET)
        publish_time: datetime.datetime | Unset
        if isinstance(_publish_time, Unset):
            publish_time = UNSET
        else:
            publish_time = datetime.datetime.fromisoformat(_publish_time)

        is_not_in_universe = d.pop("isNotInUniverse", UNSET)

        def _parse_players_per_version(data: object) -> None | PlaceSummaryForGameRestartPlayersPerVersionType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                players_per_version_type_0 = PlaceSummaryForGameRestartPlayersPerVersionType0.from_dict(data)

                return players_per_version_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PlaceSummaryForGameRestartPlayersPerVersionType0 | Unset, data)

        players_per_version = _parse_players_per_version(d.pop("playersPerVersion", UNSET))

        def _parse_instances_per_version(
            data: object,
        ) -> None | PlaceSummaryForGameRestartInstancesPerVersionType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                instances_per_version_type_0 = PlaceSummaryForGameRestartInstancesPerVersionType0.from_dict(data)

                return instances_per_version_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PlaceSummaryForGameRestartInstancesPerVersionType0 | Unset, data)

        instances_per_version = _parse_instances_per_version(d.pop("instancesPerVersion", UNSET))

        place_summary_for_game_restart = cls(
            players_impacted=players_impacted,
            total_players=total_players,
            instances_impacted=instances_impacted,
            total_instances=total_instances,
            latest_place_version=latest_place_version,
            publish_time=publish_time,
            is_not_in_universe=is_not_in_universe,
            players_per_version=players_per_version,
            instances_per_version=instances_per_version,
        )

        return place_summary_for_game_restart
