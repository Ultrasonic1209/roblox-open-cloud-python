from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..models.matchmaking_attribute_value_location_case import MatchmakingAttributeValueLocationCase
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.data_store_location import DataStoreLocation


T = TypeVar("T", bound="MatchmakingAttributeValueLocation")


@_attrs_define
class MatchmakingAttributeValueLocation:
    """Describes where an attribute value exists.

    Attributes:
        location_case (MatchmakingAttributeValueLocationCase | Unset): The storage solution used for this
            MatchmakingPlayerAttributeDefinition.
        data_store_location (DataStoreLocation | Unset): Describes where an attribute value exists in DataStore.
    """

    location_case: MatchmakingAttributeValueLocationCase | Unset = UNSET
    data_store_location: DataStoreLocation | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        location_case: str | Unset = UNSET
        if not isinstance(self.location_case, Unset):
            location_case = self.location_case.value

        data_store_location: dict[str, Any] | Unset = UNSET
        if not isinstance(self.data_store_location, Unset):
            data_store_location = self.data_store_location.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if location_case is not UNSET:
            field_dict["locationCase"] = location_case
        if data_store_location is not UNSET:
            field_dict["dataStoreLocation"] = data_store_location

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.data_store_location import DataStoreLocation

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        _location_case = d.pop("locationCase", UNSET)
        location_case: MatchmakingAttributeValueLocationCase | Unset
        if isinstance(_location_case, Unset):
            location_case = UNSET
        else:
            location_case = MatchmakingAttributeValueLocationCase(_location_case)

        _data_store_location = d.pop("dataStoreLocation", UNSET)
        data_store_location: DataStoreLocation | Unset
        if isinstance(_data_store_location, Unset):
            data_store_location = UNSET
        else:
            data_store_location = DataStoreLocation.from_dict(_data_store_location)

        matchmaking_attribute_value_location = cls(
            location_case=location_case,
            data_store_location=data_store_location,
        )

        return matchmaking_attribute_value_location
