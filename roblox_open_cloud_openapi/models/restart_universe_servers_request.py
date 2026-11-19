from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RestartUniverseServersRequest")


@_attrs_define
class RestartUniverseServersRequest:
    """Restarts all of the universe's servers.

    Attributes:
        path (str | Unset): The path of the universe.

            Format: `universes/{universe_id}`
        place_ids (list[int] | Unset): The place IDs to update. If none are specified, all active places in the
            universe will be updated.
        close_all_versions (bool | Unset): If true, players from servers running both old and new place versions will
            be restarted. If false, restarts all active servers for a specific universe
            if and only if a new version of the experience has been published.
        bleed_off_servers (bool | Unset): If true, matchmaking to servers will stop, but servers will stay up for
            bleed_off_duration_minutes before shutting down.
            This setting gives players time to naturally migrate to the newer version.
            If false, servers will immediately start shutting down.
        bleed_off_duration_minutes (int | Unset): If bleed_off_servers is true, how long (in minutes) old servers are
            allowed
            to stay up before shutting them down. Valid values: 1-60 minutes.
    """

    path: str | Unset = UNSET
    place_ids: list[int] | Unset = UNSET
    close_all_versions: bool | Unset = UNSET
    bleed_off_servers: bool | Unset = UNSET
    bleed_off_duration_minutes: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        path = self.path

        place_ids: list[int] | Unset = UNSET
        if not isinstance(self.place_ids, Unset):
            place_ids = self.place_ids

        close_all_versions = self.close_all_versions

        bleed_off_servers = self.bleed_off_servers

        bleed_off_duration_minutes = self.bleed_off_duration_minutes

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if path is not UNSET:
            field_dict["path"] = path
        if place_ids is not UNSET:
            field_dict["placeIds"] = place_ids
        if close_all_versions is not UNSET:
            field_dict["closeAllVersions"] = close_all_versions
        if bleed_off_servers is not UNSET:
            field_dict["bleedOffServers"] = bleed_off_servers
        if bleed_off_duration_minutes is not UNSET:
            field_dict["bleedOffDurationMinutes"] = bleed_off_duration_minutes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        path = d.pop("path", UNSET)

        place_ids = cast(list[int], d.pop("placeIds", UNSET))

        close_all_versions = d.pop("closeAllVersions", UNSET)

        bleed_off_servers = d.pop("bleedOffServers", UNSET)

        bleed_off_duration_minutes = d.pop("bleedOffDurationMinutes", UNSET)

        restart_universe_servers_request = cls(
            path=path,
            place_ids=place_ids,
            close_all_versions=close_all_versions,
            bleed_off_servers=bleed_off_servers,
            bleed_off_duration_minutes=bleed_off_duration_minutes,
        )

        return restart_universe_servers_request
