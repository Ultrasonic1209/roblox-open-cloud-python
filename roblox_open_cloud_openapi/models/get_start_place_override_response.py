from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

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
    """

    data_store_location: DataStoreLocation | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        data_store_location: dict[str, Any] | Unset = UNSET
        if not isinstance(self.data_store_location, Unset):
            data_store_location = self.data_store_location.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if data_store_location is not UNSET:
            field_dict["dataStoreLocation"] = data_store_location

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.data_store_location import DataStoreLocation

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        _data_store_location = d.pop("dataStoreLocation", UNSET)
        data_store_location: DataStoreLocation | Unset
        if isinstance(_data_store_location, Unset):
            data_store_location = UNSET
        else:
            data_store_location = DataStoreLocation.from_dict(_data_store_location)

        get_start_place_override_response = cls(
            data_store_location=data_store_location,
        )

        return get_start_place_override_response
