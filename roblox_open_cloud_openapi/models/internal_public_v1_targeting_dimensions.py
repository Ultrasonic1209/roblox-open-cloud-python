from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.internal_public_v1_targeting_dimensions_age_groups_item import (
    InternalPublicV1TargetingDimensionsAgeGroupsItem,
)
from ..models.internal_public_v1_targeting_dimensions_devices_item import InternalPublicV1TargetingDimensionsDevicesItem
from ..types import UNSET, Unset

T = TypeVar("T", bound="InternalPublicV1TargetingDimensions")


@_attrs_define
class InternalPublicV1TargetingDimensions:
    """
    Attributes:
        age_groups (list[InternalPublicV1TargetingDimensionsAgeGroupsItem] | Unset): The selectable age brackets. Values
            can be `AGE_13_17`, `AGE_18_24`, or `AGE_25_PLUS`.
        countries (list[str] | Unset): The selectable ISO 3166-1 alpha-2 country codes (for example, `US`).
        devices (list[InternalPublicV1TargetingDimensionsDevicesItem] | Unset): The selectable device types. Values can
            be `PHONE`, `TABLET`, `DESKTOP`, or `CONSOLE`.
    """

    age_groups: list[InternalPublicV1TargetingDimensionsAgeGroupsItem] | Unset = UNSET
    countries: list[str] | Unset = UNSET
    devices: list[InternalPublicV1TargetingDimensionsDevicesItem] | Unset = UNSET
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

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if age_groups is not UNSET:
            field_dict["ageGroups"] = age_groups
        if countries is not UNSET:
            field_dict["countries"] = countries
        if devices is not UNSET:
            field_dict["devices"] = devices

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        _age_groups = d.pop("ageGroups", UNSET)
        age_groups: list[InternalPublicV1TargetingDimensionsAgeGroupsItem] | Unset = UNSET
        if _age_groups is not UNSET:
            age_groups = []
            for age_groups_item_data in _age_groups:
                age_groups_item = InternalPublicV1TargetingDimensionsAgeGroupsItem(age_groups_item_data)

                age_groups.append(age_groups_item)

        countries = cast(list[str], d.pop("countries", UNSET))

        _devices = d.pop("devices", UNSET)
        devices: list[InternalPublicV1TargetingDimensionsDevicesItem] | Unset = UNSET
        if _devices is not UNSET:
            devices = []
            for devices_item_data in _devices:
                devices_item = InternalPublicV1TargetingDimensionsDevicesItem(devices_item_data)

                devices.append(devices_item)

        internal_public_v1_targeting_dimensions = cls(
            age_groups=age_groups,
            countries=countries,
            devices=devices,
        )

        internal_public_v1_targeting_dimensions.additional_properties = d
        return internal_public_v1_targeting_dimensions

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
