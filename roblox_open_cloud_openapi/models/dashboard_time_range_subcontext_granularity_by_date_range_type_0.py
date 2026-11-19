from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.dashboard_time_range_subcontext_granularity_by_date_range_type_0_additional_property_type_0 import (
    DashboardTimeRangeSubcontextGranularityByDateRangeType0AdditionalPropertyType0,
)

T = TypeVar("T", bound="DashboardTimeRangeSubcontextGranularityByDateRangeType0")


@_attrs_define
class DashboardTimeRangeSubcontextGranularityByDateRangeType0:
    additional_properties: dict[
        str, DashboardTimeRangeSubcontextGranularityByDateRangeType0AdditionalPropertyType0 | int
    ] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            if isinstance(prop, DashboardTimeRangeSubcontextGranularityByDateRangeType0AdditionalPropertyType0):
                field_dict[prop_name] = prop.value
            else:
                field_dict[prop_name] = prop

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        dashboard_time_range_subcontext_granularity_by_date_range_type_0 = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():

            def _parse_additional_property(
                data: object,
            ) -> DashboardTimeRangeSubcontextGranularityByDateRangeType0AdditionalPropertyType0 | int:
                try:
                    if not isinstance(data, str):
                        raise TypeError()
                    additional_property_type_0 = (
                        DashboardTimeRangeSubcontextGranularityByDateRangeType0AdditionalPropertyType0(data)
                    )

                    return additional_property_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                return cast(DashboardTimeRangeSubcontextGranularityByDateRangeType0AdditionalPropertyType0 | int, data)

            additional_property = _parse_additional_property(prop_dict)

            additional_properties[prop_name] = additional_property

        dashboard_time_range_subcontext_granularity_by_date_range_type_0.additional_properties = additional_properties
        return dashboard_time_range_subcontext_granularity_by_date_range_type_0

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(
        self, key: str
    ) -> DashboardTimeRangeSubcontextGranularityByDateRangeType0AdditionalPropertyType0 | int:
        return self.additional_properties[key]

    def __setitem__(
        self, key: str, value: DashboardTimeRangeSubcontextGranularityByDateRangeType0AdditionalPropertyType0 | int
    ) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
