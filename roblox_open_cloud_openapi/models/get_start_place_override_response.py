from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.data_store_location import DataStoreLocation


T = TypeVar("T", bound="GetStartPlaceOverrideResponse")


@_attrs_define
class GetStartPlaceOverrideResponse:
    """Response for getting the start place override for a universe.

    Attributes:
        data_store_location (DataStoreLocation | Unset): Describes where an attribute value exists in DataStore.
        enabled (bool | None | Unset): Whether game join routes players with the universe's start place override.
            Null when no start place override is configured for the universe.
    """

    data_store_location: DataStoreLocation | Unset = UNSET
    enabled: bool | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        data_store_location: dict[str, Any] | Unset = UNSET
        if not isinstance(self.data_store_location, Unset):
            data_store_location = self.data_store_location.to_dict()

        enabled: bool | None | Unset
        if isinstance(self.enabled, Unset):
            enabled = UNSET
        else:
            enabled = self.enabled

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if data_store_location is not UNSET:
            field_dict["dataStoreLocation"] = data_store_location
        if enabled is not UNSET:
            field_dict["enabled"] = enabled

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.data_store_location import DataStoreLocation  # noqa: PLC0415

        d = dict(src_dict)
        _data_store_location = d.pop("dataStoreLocation", UNSET)
        data_store_location: DataStoreLocation | Unset
        if isinstance(_data_store_location, Unset):
            data_store_location = UNSET
        else:
            data_store_location = DataStoreLocation.from_dict(_data_store_location)

        def _parse_enabled(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        enabled = _parse_enabled(d.pop("enabled", UNSET))

        get_start_place_override_response = cls(
            data_store_location=data_store_location,
            enabled=enabled,
        )

        return get_start_place_override_response
