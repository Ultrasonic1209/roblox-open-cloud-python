from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.place_version import PlaceVersion


T = TypeVar("T", bound="UpdatePlaceVersionNotesResponse")


@_attrs_define
class UpdatePlaceVersionNotesResponse:
    """
    Attributes:
        place_version (None | PlaceVersion | Unset):
    """

    place_version: None | PlaceVersion | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.place_version import PlaceVersion

        place_version: dict[str, Any] | None | Unset
        if isinstance(self.place_version, Unset):
            place_version = UNSET
        elif isinstance(self.place_version, PlaceVersion):
            place_version = self.place_version.to_dict()
        else:
            place_version = self.place_version

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if place_version is not UNSET:
            field_dict["placeVersion"] = place_version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.place_version import PlaceVersion

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}

        def _parse_place_version(data: object) -> None | PlaceVersion | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                place_version_type_1 = PlaceVersion.from_dict(data)

                return place_version_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PlaceVersion | Unset, data)

        place_version = _parse_place_version(d.pop("placeVersion", UNSET))

        update_place_version_notes_response = cls(
            place_version=place_version,
        )

        return update_place_version_notes_response
