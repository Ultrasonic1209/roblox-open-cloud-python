from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.roblox_item_configuration_api_release_configuration_response_model_sale_availability_locations_item import (
    RobloxItemConfigurationApiReleaseConfigurationResponseModelSaleAvailabilityLocationsItem,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxItemConfigurationApiReleaseConfigurationResponseModel")


@_attrs_define
class RobloxItemConfigurationApiReleaseConfigurationResponseModel:
    """Defines the configuration options associated with releasing an item.

    Attributes:
        sale_availability_locations
            (list[RobloxItemConfigurationApiReleaseConfigurationResponseModelSaleAvailabilityLocationsItem] | Unset): Get or
            sets the sale availability locations list.
    """

    sale_availability_locations: (
        list[RobloxItemConfigurationApiReleaseConfigurationResponseModelSaleAvailabilityLocationsItem] | Unset
    ) = UNSET

    def to_dict(self) -> dict[str, Any]:
        sale_availability_locations: list[str] | Unset = UNSET
        if not isinstance(self.sale_availability_locations, Unset):
            sale_availability_locations = []
            for sale_availability_locations_item_data in self.sale_availability_locations:
                sale_availability_locations_item = sale_availability_locations_item_data.value
                sale_availability_locations.append(sale_availability_locations_item)

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if sale_availability_locations is not UNSET:
            field_dict["saleAvailabilityLocations"] = sale_availability_locations

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _sale_availability_locations = d.pop("saleAvailabilityLocations", UNSET)
        sale_availability_locations: (
            list[RobloxItemConfigurationApiReleaseConfigurationResponseModelSaleAvailabilityLocationsItem] | Unset
        ) = UNSET
        if _sale_availability_locations is not UNSET:
            sale_availability_locations = []
            for sale_availability_locations_item_data in _sale_availability_locations:
                sale_availability_locations_item = (
                    RobloxItemConfigurationApiReleaseConfigurationResponseModelSaleAvailabilityLocationsItem(
                        sale_availability_locations_item_data
                    )
                )

                sale_availability_locations.append(sale_availability_locations_item)

        roblox_item_configuration_api_release_configuration_response_model = cls(
            sale_availability_locations=sale_availability_locations,
        )

        return roblox_item_configuration_api_release_configuration_response_model
