from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.targeting_dimensions_age_groups_item import TargetingDimensionsAgeGroupsItem
from ..models.targeting_dimensions_devices_item import TargetingDimensionsDevicesItem
from ..models.targeting_dimensions_regions_item import TargetingDimensionsRegionsItem
from ..types import UNSET, Unset

T = TypeVar("T", bound="TargetingDimensions")


@_attrs_define
class TargetingDimensions:
    """
    Attributes:
        age_groups (list[TargetingDimensionsAgeGroupsItem] | Unset): The selectable age brackets. Values can be
            `AGE_13_17`, `AGE_18_24`, or `AGE_25_PLUS`.
        countries (list[str] | Unset): The selectable ISO 3166-1 alpha-2 country codes (for example, `US`).
        devices (list[TargetingDimensionsDevicesItem] | Unset): The selectable device types. Values can be `PHONE`,
            `TABLET`, `DESKTOP`, or `CONSOLE`.
        regions (list[TargetingDimensionsRegionsItem] | Unset): The selectable geographic regions: `ALL` and the
            aggregate region codes. To
            target a single country, use countries.
    """

    age_groups: list[TargetingDimensionsAgeGroupsItem] | Unset = UNSET
    countries: list[str] | Unset = UNSET
    devices: list[TargetingDimensionsDevicesItem] | Unset = UNSET
    regions: list[TargetingDimensionsRegionsItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        age_groups: list[str] | Unset = UNSET
        if not isinstance(self.age_groups, Unset):
            age_groups = []
            for age_groups_item_data in self.age_groups:
                age_groups_item = age_groups_item_data.value
                age_groups.append(age_groups_item)

        countries: list[str] | Unset = UNSET
        if not isinstance(self.countries, Unset):
            countries = self.countries

        devices: list[str] | Unset = UNSET
        if not isinstance(self.devices, Unset):
            devices = []
            for devices_item_data in self.devices:
                devices_item = devices_item_data.value
                devices.append(devices_item)

        regions: list[str] | Unset = UNSET
        if not isinstance(self.regions, Unset):
            regions = []
            for regions_item_data in self.regions:
                regions_item = regions_item_data.value
                regions.append(regions_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if age_groups is not UNSET:
            field_dict["ageGroups"] = age_groups
        if countries is not UNSET:
            field_dict["countries"] = countries
        if devices is not UNSET:
            field_dict["devices"] = devices
        if regions is not UNSET:
            field_dict["regions"] = regions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _age_groups = d.pop("ageGroups", UNSET)
        age_groups: list[TargetingDimensionsAgeGroupsItem] | Unset = UNSET
        if _age_groups is not UNSET:
            age_groups = []
            for age_groups_item_data in _age_groups:
                age_groups_item = TargetingDimensionsAgeGroupsItem(age_groups_item_data)

                age_groups.append(age_groups_item)

        countries = cast(list[str], d.pop("countries", UNSET))

        _devices = d.pop("devices", UNSET)
        devices: list[TargetingDimensionsDevicesItem] | Unset = UNSET
        if _devices is not UNSET:
            devices = []
            for devices_item_data in _devices:
                devices_item = TargetingDimensionsDevicesItem(devices_item_data)

                devices.append(devices_item)

        _regions = d.pop("regions", UNSET)
        regions: list[TargetingDimensionsRegionsItem] | Unset = UNSET
        if _regions is not UNSET:
            regions = []
            for regions_item_data in _regions:
                regions_item = TargetingDimensionsRegionsItem(regions_item_data)

                regions.append(regions_item)

        targeting_dimensions = cls(
            age_groups=age_groups,
            countries=countries,
            devices=devices,
            regions=regions,
        )

        targeting_dimensions.additional_properties = d
        return targeting_dimensions

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
