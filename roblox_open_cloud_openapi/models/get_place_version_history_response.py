from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.place_version import PlaceVersion


T = TypeVar("T", bound="GetPlaceVersionHistoryResponse")


@_attrs_define
class GetPlaceVersionHistoryResponse:
    """
    Attributes:
        next_cursor (None | str | Unset):
        has_more (bool | Unset):
        place_versions (list[PlaceVersion] | None | Unset):
    """

    next_cursor: None | str | Unset = UNSET
    has_more: bool | Unset = UNSET
    place_versions: list[PlaceVersion] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        next_cursor: None | str | Unset
        if isinstance(self.next_cursor, Unset):
            next_cursor = UNSET
        else:
            next_cursor = self.next_cursor

        has_more = self.has_more

        place_versions: list[dict[str, Any]] | None | Unset
        if isinstance(self.place_versions, Unset):
            place_versions = UNSET
        elif isinstance(self.place_versions, list):
            place_versions = []
            for place_versions_type_0_item_data in self.place_versions:
                place_versions_type_0_item = place_versions_type_0_item_data.to_dict()
                place_versions.append(place_versions_type_0_item)

        else:
            place_versions = self.place_versions

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if next_cursor is not UNSET:
            field_dict["nextCursor"] = next_cursor
        if has_more is not UNSET:
            field_dict["hasMore"] = has_more
        if place_versions is not UNSET:
            field_dict["placeVersions"] = place_versions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.place_version import PlaceVersion

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}

        def _parse_next_cursor(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        next_cursor = _parse_next_cursor(d.pop("nextCursor", UNSET))

        has_more = d.pop("hasMore", UNSET)

        def _parse_place_versions(data: object) -> list[PlaceVersion] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                place_versions_type_0 = []
                _place_versions_type_0 = data
                for place_versions_type_0_item_data in _place_versions_type_0:
                    place_versions_type_0_item = PlaceVersion.from_dict(place_versions_type_0_item_data)

                    place_versions_type_0.append(place_versions_type_0_item)

                return place_versions_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[PlaceVersion] | None | Unset, data)

        place_versions = _parse_place_versions(d.pop("placeVersions", UNSET))

        get_place_version_history_response = cls(
            next_cursor=next_cursor,
            has_more=has_more,
            place_versions=place_versions,
        )

        return get_place_version_history_response
