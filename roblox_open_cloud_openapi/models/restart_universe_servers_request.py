from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RestartUniverseServersRequest")


@_attrs_define
class RestartUniverseServersRequest:
    """Restarts all of the universe's servers.

    Attributes:
        place_ids (list[int] | Unset): The place IDs to update. If none are specified, all active places in the
            universe will be updated.
        close_all_versions (bool | Unset): If true, players from servers running both old and new place versions will
            be restarted. If false, restarts all active servers for a specific universe
            if and only if a new version of the experience has been published. Example: True.
        bleed_off_servers (bool | Unset): If true, matchmaking to servers will stop, but servers will stay up for
            bleed_off_duration_minutes before shutting down.
            This setting gives players time to naturally migrate to the newer version.
            If false, servers will immediately start shutting down. Example: True.
        bleed_off_duration_minutes (int | Unset): If bleed_off_servers is true, how long (in minutes) old servers are
            allowed
            to stay up before shutting them down. Valid values: 1-60 minutes. Example: 10.
    """

    place_ids: list[int] | Unset = UNSET
    close_all_versions: bool | Unset = UNSET
    bleed_off_servers: bool | Unset = UNSET
    bleed_off_duration_minutes: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        place_ids: list[int] | Unset = UNSET
        if not isinstance(self.place_ids, Unset):
            place_ids = self.place_ids

        close_all_versions = self.close_all_versions

        bleed_off_servers = self.bleed_off_servers

        bleed_off_duration_minutes = self.bleed_off_duration_minutes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
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
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        place_ids = cast(list[int], d.pop("placeIds", UNSET))

        close_all_versions = d.pop("closeAllVersions", UNSET)

        bleed_off_servers = d.pop("bleedOffServers", UNSET)

        bleed_off_duration_minutes = d.pop("bleedOffDurationMinutes", UNSET)

        restart_universe_servers_request = cls(
            place_ids=place_ids,
            close_all_versions=close_all_versions,
            bleed_off_servers=bleed_off_servers,
            bleed_off_duration_minutes=bleed_off_duration_minutes,
        )

        restart_universe_servers_request.additional_properties = d
        return restart_universe_servers_request

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
