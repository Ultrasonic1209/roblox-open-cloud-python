from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.place_summary_for_game_update_version_to_instance_counts_type_0 import (
        PlaceSummaryForGameUpdateVersionToInstanceCountsType0,
    )
    from ..models.place_summary_for_game_update_version_to_player_counts_type_0 import (
        PlaceSummaryForGameUpdateVersionToPlayerCountsType0,
    )


T = TypeVar("T", bound="PlaceSummaryForGameUpdate")


@_attrs_define
class PlaceSummaryForGameUpdate:
    """Summary of a place for a game update.

    Attributes:
        place_id (int | Unset): Place ID of the place to be updated.
        players_to_be_kicked (int | Unset): Number of players to be kicked from the place during the game update.
        total_players (int | Unset): Total number of players in the place.
        instances_to_be_closed (int | Unset): Number of instances to be closed for the place during the game update.
        total_instances (int | Unset): Total number of instances for the place.
        place_version (int | Unset): Lastest version of the place to be updated.
        last_updated (datetime.datetime | Unset): The timestamp of the last update to the place summary.
        is_in_universe (bool | Unset): Indicates whether the place is still part of the universe.
            A place may have active games but is no longer in the universe if it has been removed from the universe.
        version_to_player_counts (None | PlaceSummaryForGameUpdateVersionToPlayerCountsType0 | Unset): Player counts
            broken down by place version.
            Key is the place version, value is the number of players on that version.
        version_to_instance_counts (None | PlaceSummaryForGameUpdateVersionToInstanceCountsType0 | Unset): Instance
            counts broken down by place version.
            Key is the place version, value is the number of instances on that version.
    """

    place_id: int | Unset = UNSET
    players_to_be_kicked: int | Unset = UNSET
    total_players: int | Unset = UNSET
    instances_to_be_closed: int | Unset = UNSET
    total_instances: int | Unset = UNSET
    place_version: int | Unset = UNSET
    last_updated: datetime.datetime | Unset = UNSET
    is_in_universe: bool | Unset = UNSET
    version_to_player_counts: None | PlaceSummaryForGameUpdateVersionToPlayerCountsType0 | Unset = UNSET
    version_to_instance_counts: None | PlaceSummaryForGameUpdateVersionToInstanceCountsType0 | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.place_summary_for_game_update_version_to_instance_counts_type_0 import (
            PlaceSummaryForGameUpdateVersionToInstanceCountsType0,
        )
        from ..models.place_summary_for_game_update_version_to_player_counts_type_0 import (
            PlaceSummaryForGameUpdateVersionToPlayerCountsType0,
        )

        place_id = self.place_id

        players_to_be_kicked = self.players_to_be_kicked

        total_players = self.total_players

        instances_to_be_closed = self.instances_to_be_closed

        total_instances = self.total_instances

        place_version = self.place_version

        last_updated: str | Unset = UNSET
        if not isinstance(self.last_updated, Unset):
            last_updated = self.last_updated.isoformat()

        is_in_universe = self.is_in_universe

        version_to_player_counts: dict[str, Any] | None | Unset
        if isinstance(self.version_to_player_counts, Unset):
            version_to_player_counts = UNSET
        elif isinstance(self.version_to_player_counts, PlaceSummaryForGameUpdateVersionToPlayerCountsType0):
            version_to_player_counts = self.version_to_player_counts.to_dict()
        else:
            version_to_player_counts = self.version_to_player_counts

        version_to_instance_counts: dict[str, Any] | None | Unset
        if isinstance(self.version_to_instance_counts, Unset):
            version_to_instance_counts = UNSET
        elif isinstance(self.version_to_instance_counts, PlaceSummaryForGameUpdateVersionToInstanceCountsType0):
            version_to_instance_counts = self.version_to_instance_counts.to_dict()
        else:
            version_to_instance_counts = self.version_to_instance_counts

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if place_id is not UNSET:
            field_dict["placeId"] = place_id
        if players_to_be_kicked is not UNSET:
            field_dict["playersToBeKicked"] = players_to_be_kicked
        if total_players is not UNSET:
            field_dict["totalPlayers"] = total_players
        if instances_to_be_closed is not UNSET:
            field_dict["instancesToBeClosed"] = instances_to_be_closed
        if total_instances is not UNSET:
            field_dict["totalInstances"] = total_instances
        if place_version is not UNSET:
            field_dict["placeVersion"] = place_version
        if last_updated is not UNSET:
            field_dict["lastUpdated"] = last_updated
        if is_in_universe is not UNSET:
            field_dict["isInUniverse"] = is_in_universe
        if version_to_player_counts is not UNSET:
            field_dict["versionToPlayerCounts"] = version_to_player_counts
        if version_to_instance_counts is not UNSET:
            field_dict["versionToInstanceCounts"] = version_to_instance_counts

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.place_summary_for_game_update_version_to_instance_counts_type_0 import (
            PlaceSummaryForGameUpdateVersionToInstanceCountsType0,
        )
        from ..models.place_summary_for_game_update_version_to_player_counts_type_0 import (
            PlaceSummaryForGameUpdateVersionToPlayerCountsType0,
        )

        d = dict(src_dict)
        place_id = d.pop("placeId", UNSET)

        players_to_be_kicked = d.pop("playersToBeKicked", UNSET)

        total_players = d.pop("totalPlayers", UNSET)

        instances_to_be_closed = d.pop("instancesToBeClosed", UNSET)

        total_instances = d.pop("totalInstances", UNSET)

        place_version = d.pop("placeVersion", UNSET)

        _last_updated = d.pop("lastUpdated", UNSET)
        last_updated: datetime.datetime | Unset
        if isinstance(_last_updated, Unset):
            last_updated = UNSET
        else:
            last_updated = datetime.datetime.fromisoformat(_last_updated)

        is_in_universe = d.pop("isInUniverse", UNSET)

        def _parse_version_to_player_counts(
            data: object,
        ) -> None | PlaceSummaryForGameUpdateVersionToPlayerCountsType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                version_to_player_counts_type_0 = PlaceSummaryForGameUpdateVersionToPlayerCountsType0.from_dict(data)

                return version_to_player_counts_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PlaceSummaryForGameUpdateVersionToPlayerCountsType0 | Unset, data)

        version_to_player_counts = _parse_version_to_player_counts(d.pop("versionToPlayerCounts", UNSET))

        def _parse_version_to_instance_counts(
            data: object,
        ) -> None | PlaceSummaryForGameUpdateVersionToInstanceCountsType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                version_to_instance_counts_type_0 = PlaceSummaryForGameUpdateVersionToInstanceCountsType0.from_dict(
                    data
                )

                return version_to_instance_counts_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PlaceSummaryForGameUpdateVersionToInstanceCountsType0 | Unset, data)

        version_to_instance_counts = _parse_version_to_instance_counts(d.pop("versionToInstanceCounts", UNSET))

        place_summary_for_game_update = cls(
            place_id=place_id,
            players_to_be_kicked=players_to_be_kicked,
            total_players=total_players,
            instances_to_be_closed=instances_to_be_closed,
            total_instances=total_instances,
            place_version=place_version,
            last_updated=last_updated,
            is_in_universe=is_in_universe,
            version_to_player_counts=version_to_player_counts,
            version_to_instance_counts=version_to_instance_counts,
        )

        return place_summary_for_game_update
