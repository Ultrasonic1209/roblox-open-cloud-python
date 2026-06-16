from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.launch_restart_request_places_type_0 import LaunchRestartRequestPlacesType0


T = TypeVar("T", bound="LaunchRestartRequest")


@_attrs_define
class LaunchRestartRequest:
    """Request model for launching a game restart.

    Attributes:
        bleed_off_duration_minutes (int | None | Unset): Period in minutes before servers begin to be restarted.
            During this time, players will not be matchmade to servers scheduled for restart.
            Valid range: 1-240.
        places (LaunchRestartRequestPlacesType0 | None | Unset): Optional mapping of place ID to specific PlaceFilter
            objects.
            If empty for a place, restart all versions of that place.
            If null/omitted entirely, restart all places in the universe.
        attributes (None | str | Unset): Optional JSON string included in the ServerLifecycleChanged payload published
            to game servers.
            Must be valid JSON and at most 500 bytes (UTF-8).
    """

    bleed_off_duration_minutes: int | None | Unset = UNSET
    places: LaunchRestartRequestPlacesType0 | None | Unset = UNSET
    attributes: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.launch_restart_request_places_type_0 import LaunchRestartRequestPlacesType0

        bleed_off_duration_minutes: int | None | Unset
        if isinstance(self.bleed_off_duration_minutes, Unset):
            bleed_off_duration_minutes = UNSET
        else:
            bleed_off_duration_minutes = self.bleed_off_duration_minutes

        places: dict[str, Any] | None | Unset
        if isinstance(self.places, Unset):
            places = UNSET
        elif isinstance(self.places, LaunchRestartRequestPlacesType0):
            places = self.places.to_dict()
        else:
            places = self.places

        attributes: None | str | Unset
        if isinstance(self.attributes, Unset):
            attributes = UNSET
        else:
            attributes = self.attributes

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if bleed_off_duration_minutes is not UNSET:
            field_dict["bleedOffDurationMinutes"] = bleed_off_duration_minutes
        if places is not UNSET:
            field_dict["places"] = places
        if attributes is not UNSET:
            field_dict["attributes"] = attributes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.launch_restart_request_places_type_0 import LaunchRestartRequestPlacesType0

        d = dict(src_dict)

        def _parse_bleed_off_duration_minutes(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        bleed_off_duration_minutes = _parse_bleed_off_duration_minutes(d.pop("bleedOffDurationMinutes", UNSET))

        def _parse_places(data: object) -> LaunchRestartRequestPlacesType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                places_type_0 = LaunchRestartRequestPlacesType0.from_dict(data)

                return places_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(LaunchRestartRequestPlacesType0 | None | Unset, data)

        places = _parse_places(d.pop("places", UNSET))

        def _parse_attributes(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        attributes = _parse_attributes(d.pop("attributes", UNSET))

        launch_restart_request = cls(
            bleed_off_duration_minutes=bleed_off_duration_minutes,
            places=places,
            attributes=attributes,
        )

        return launch_restart_request
