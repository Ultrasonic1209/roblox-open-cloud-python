from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.launch_update_request_place_id_to_versions_type_0 import LaunchUpdateRequestPlaceIdToVersionsType0


T = TypeVar("T", bound="LaunchUpdateRequest")


@_attrs_define
class LaunchUpdateRequest:
    """Launch Update Request. Contains specification for how update should roll out

    Attributes:
        universe_id (int | Unset): The Universe ID to update.
        place_ids (list[int] | None | Unset): The place IDs to update. If none are specified, we will update all active
            Places in the Universe
        close_old_versions_only (bool | Unset): If true (default in UI), we will only migrate players from servers
            running old PlaceVersions.
            If false, we will migrate all players
        bleed_off_servers (bool | Unset): If true (default in UI), we will stop matchmaking to servers but keep them up
            before shutting them down, allowing
             players to naturally migrate to the newer version.
            If false, we will immediately start shutting down servers
        bleed_off_duration_minutes (int | Unset): If BleedOffServers=true, how long will we allow old servers to stay up
            before shutting them down.
            Valid values: 1 - 60 minutes
        place_id_to_versions (LaunchUpdateRequestPlaceIdToVersionsType0 | None | Unset): Optional. A mapping of PlaceId
            to the specific versions to restart/bleed off for that place.
            When set for a place, only servers running those exact versions will be affected.
            If a place is not in this dictionary or has an empty set, behavior falls back to CloseOldVersionsOnly logic.
        attributes (None | str | Unset): Optional. Attributes string to include in the ServerLifecycleChanged CSM
            payload published to game servers.
    """

    universe_id: int | Unset = UNSET
    place_ids: list[int] | None | Unset = UNSET
    close_old_versions_only: bool | Unset = UNSET
    bleed_off_servers: bool | Unset = UNSET
    bleed_off_duration_minutes: int | Unset = UNSET
    place_id_to_versions: LaunchUpdateRequestPlaceIdToVersionsType0 | None | Unset = UNSET
    attributes: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.launch_update_request_place_id_to_versions_type_0 import LaunchUpdateRequestPlaceIdToVersionsType0

        universe_id = self.universe_id

        place_ids: list[int] | None | Unset
        if isinstance(self.place_ids, Unset):
            place_ids = UNSET
        elif isinstance(self.place_ids, list):
            place_ids = self.place_ids

        else:
            place_ids = self.place_ids

        close_old_versions_only = self.close_old_versions_only

        bleed_off_servers = self.bleed_off_servers

        bleed_off_duration_minutes = self.bleed_off_duration_minutes

        place_id_to_versions: dict[str, Any] | None | Unset
        if isinstance(self.place_id_to_versions, Unset):
            place_id_to_versions = UNSET
        elif isinstance(self.place_id_to_versions, LaunchUpdateRequestPlaceIdToVersionsType0):
            place_id_to_versions = self.place_id_to_versions.to_dict()
        else:
            place_id_to_versions = self.place_id_to_versions

        attributes: None | str | Unset
        if isinstance(self.attributes, Unset):
            attributes = UNSET
        else:
            attributes = self.attributes

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if universe_id is not UNSET:
            field_dict["universeId"] = universe_id
        if place_ids is not UNSET:
            field_dict["placeIds"] = place_ids
        if close_old_versions_only is not UNSET:
            field_dict["closeOldVersionsOnly"] = close_old_versions_only
        if bleed_off_servers is not UNSET:
            field_dict["bleedOffServers"] = bleed_off_servers
        if bleed_off_duration_minutes is not UNSET:
            field_dict["bleedOffDurationMinutes"] = bleed_off_duration_minutes
        if place_id_to_versions is not UNSET:
            field_dict["placeIdToVersions"] = place_id_to_versions
        if attributes is not UNSET:
            field_dict["attributes"] = attributes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.launch_update_request_place_id_to_versions_type_0 import LaunchUpdateRequestPlaceIdToVersionsType0

        d = dict(src_dict)
        universe_id = d.pop("universeId", UNSET)

        def _parse_place_ids(data: object) -> list[int] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                place_ids_type_0 = cast(list[int], data)

                return place_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[int] | None | Unset, data)

        place_ids = _parse_place_ids(d.pop("placeIds", UNSET))

        close_old_versions_only = d.pop("closeOldVersionsOnly", UNSET)

        bleed_off_servers = d.pop("bleedOffServers", UNSET)

        bleed_off_duration_minutes = d.pop("bleedOffDurationMinutes", UNSET)

        def _parse_place_id_to_versions(data: object) -> LaunchUpdateRequestPlaceIdToVersionsType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                place_id_to_versions_type_0 = LaunchUpdateRequestPlaceIdToVersionsType0.from_dict(data)

                return place_id_to_versions_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(LaunchUpdateRequestPlaceIdToVersionsType0 | None | Unset, data)

        place_id_to_versions = _parse_place_id_to_versions(d.pop("placeIdToVersions", UNSET))

        def _parse_attributes(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        attributes = _parse_attributes(d.pop("attributes", UNSET))

        launch_update_request = cls(
            universe_id=universe_id,
            place_ids=place_ids,
            close_old_versions_only=close_old_versions_only,
            bleed_off_servers=bleed_off_servers,
            bleed_off_duration_minutes=bleed_off_duration_minutes,
            place_id_to_versions=place_id_to_versions,
            attributes=attributes,
        )

        return launch_update_request
