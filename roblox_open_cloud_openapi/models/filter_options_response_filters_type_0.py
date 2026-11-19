from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.filter_field_info import FilterFieldInfo


T = TypeVar("T", bound="FilterOptionsResponseFiltersType0")


@_attrs_define
class FilterOptionsResponseFiltersType0:
    """A dictionary of filter field names to their metadata and available values.

    Attributes:
        engine_version (FilterFieldInfo | Unset): Describes the metadata and available values for a single filter field.
        place_version (FilterFieldInfo | Unset): Describes the metadata and available values for a single filter field.
        all_ (FilterFieldInfo | Unset): Describes the metadata and available values for a single filter field.
        server_region (FilterFieldInfo | Unset): Describes the metadata and available values for a single filter field.
    """

    engine_version: FilterFieldInfo | Unset = UNSET
    place_version: FilterFieldInfo | Unset = UNSET
    all_: FilterFieldInfo | Unset = UNSET
    server_region: FilterFieldInfo | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        engine_version: dict[str, Any] | Unset = UNSET
        if not isinstance(self.engine_version, Unset):
            engine_version = self.engine_version.to_dict()

        place_version: dict[str, Any] | Unset = UNSET
        if not isinstance(self.place_version, Unset):
            place_version = self.place_version.to_dict()

        all_: dict[str, Any] | Unset = UNSET
        if not isinstance(self.all_, Unset):
            all_ = self.all_.to_dict()

        server_region: dict[str, Any] | Unset = UNSET
        if not isinstance(self.server_region, Unset):
            server_region = self.server_region.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if engine_version is not UNSET:
            field_dict["EngineVersion"] = engine_version
        if place_version is not UNSET:
            field_dict["PlaceVersion"] = place_version
        if all_ is not UNSET:
            field_dict["ALL"] = all_
        if server_region is not UNSET:
            field_dict["ServerRegion"] = server_region

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.filter_field_info import FilterFieldInfo  # noqa: PLC0415

        d = dict(src_dict)
        _engine_version = d.pop("EngineVersion", UNSET)
        engine_version: FilterFieldInfo | Unset
        if isinstance(_engine_version, Unset):
            engine_version = UNSET
        else:
            engine_version = FilterFieldInfo.from_dict(_engine_version)

        _place_version = d.pop("PlaceVersion", UNSET)
        place_version: FilterFieldInfo | Unset
        if isinstance(_place_version, Unset):
            place_version = UNSET
        else:
            place_version = FilterFieldInfo.from_dict(_place_version)

        _all_ = d.pop("ALL", UNSET)
        all_: FilterFieldInfo | Unset
        if isinstance(_all_, Unset):
            all_ = UNSET
        else:
            all_ = FilterFieldInfo.from_dict(_all_)

        _server_region = d.pop("ServerRegion", UNSET)
        server_region: FilterFieldInfo | Unset
        if isinstance(_server_region, Unset):
            server_region = UNSET
        else:
            server_region = FilterFieldInfo.from_dict(_server_region)

        filter_options_response_filters_type_0 = cls(
            engine_version=engine_version,
            place_version=place_version,
            all_=all_,
            server_region=server_region,
        )

        return filter_options_response_filters_type_0
