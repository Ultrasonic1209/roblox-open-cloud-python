from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.targeting_age_groups_item import TargetingAgeGroupsItem
from ..models.targeting_audience_type import TargetingAudienceType
from ..models.targeting_devices_item import TargetingDevicesItem
from ..models.targeting_regions_item import TargetingRegionsItem
from ..types import UNSET, Unset

T = TypeVar("T", bound="Targeting")


@_attrs_define
class Targeting:
    """
    Attributes:
        age_groups (list[TargetingAgeGroupsItem] | Unset): The age brackets to deliver to. Empty means all ages. Values
            can be `AGE_13_17`,
            `AGE_18_24`, or `AGE_25_PLUS`.
        audience_type (TargetingAudienceType | Unset): Omitted or `ALL_PLAYERS` delivers to all players. Other values
            restrict delivery
            to a retargeting audience of the target experience. For `ENGAGEMENT`, only
            omission or `ALL_PLAYERS` is accepted; other targeting fields are rejected.
            Responses always include the resolved value. Default: TargetingAudienceType.ALL_PLAYERS.
        countries (list[str] | Unset): The ISO 3166-1 alpha-2 country codes to deliver to (for example, `US`). Empty
            means all countries. Use this field to target single countries. Can't be
            combined with the region `ALL`, or with the region that contains the country.
        devices (list[TargetingDevicesItem] | Unset): The device types to deliver to. Empty means all devices. Values
            can be `PHONE`,
            `TABLET`, `DESKTOP`, or `CONSOLE`.
        regions (list[TargetingRegionsItem] | Unset): The aggregate geographic regions to deliver to, or `ALL`. Empty
            means all
            regions. Use only the values in campaign-options `targetingDimensions.regions`.
            `ALL` can't be combined with other regions or with countries.
    """

    age_groups: list[TargetingAgeGroupsItem] | Unset = UNSET
    audience_type: TargetingAudienceType | Unset = TargetingAudienceType.ALL_PLAYERS
    countries: list[str] | Unset = UNSET
    devices: list[TargetingDevicesItem] | Unset = UNSET
    regions: list[TargetingRegionsItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        age_groups: list[str] | Unset = UNSET
        if not isinstance(self.age_groups, Unset):
            age_groups = []
            for age_groups_item_data in self.age_groups:
                age_groups_item = age_groups_item_data.value
                age_groups.append(age_groups_item)

        audience_type: str | Unset = UNSET
        if not isinstance(self.audience_type, Unset):
            audience_type = self.audience_type.value

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
        if audience_type is not UNSET:
            field_dict["audienceType"] = audience_type
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
        age_groups: list[TargetingAgeGroupsItem] | Unset = UNSET
        if _age_groups is not UNSET:
            age_groups = []
            for age_groups_item_data in _age_groups:
                age_groups_item = TargetingAgeGroupsItem(age_groups_item_data)

                age_groups.append(age_groups_item)

        _audience_type = d.pop("audienceType", UNSET)
        audience_type: TargetingAudienceType | Unset
        if isinstance(_audience_type, Unset):
            audience_type = UNSET
        else:
            audience_type = TargetingAudienceType(_audience_type)

        countries = cast(list[str], d.pop("countries", UNSET))

        _devices = d.pop("devices", UNSET)
        devices: list[TargetingDevicesItem] | Unset = UNSET
        if _devices is not UNSET:
            devices = []
            for devices_item_data in _devices:
                devices_item = TargetingDevicesItem(devices_item_data)

                devices.append(devices_item)

        _regions = d.pop("regions", UNSET)
        regions: list[TargetingRegionsItem] | Unset = UNSET
        if _regions is not UNSET:
            regions = []
            for regions_item_data in _regions:
                regions_item = TargetingRegionsItem(regions_item_data)

                regions.append(regions_item)

        targeting = cls(
            age_groups=age_groups,
            audience_type=audience_type,
            countries=countries,
            devices=devices,
            regions=regions,
        )

        targeting.additional_properties = d
        return targeting

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
