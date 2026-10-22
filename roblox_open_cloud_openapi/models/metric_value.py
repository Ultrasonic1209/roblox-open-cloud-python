from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.breakdown_value import BreakdownValue
    from ..models.data_point import DataPoint


T = TypeVar("T", bound="MetricValue")


@_attrs_define
class MetricValue:
    """MetricValue content of a query result.

    Attributes:
        breakdown_value (list[BreakdownValue] | Unset): The dimensions identifying the series. Always includes a
            `Percentile` dimension.
            `BENCHMARK_TYPE_TOP_EXPERIENCES` series also include the requested filters.
        data_points (list[DataPoint] | Unset): The data points for the breakdown.
    """

    breakdown_value: list[BreakdownValue] | Unset = UNSET
    data_points: list[DataPoint] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        breakdown_value: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.breakdown_value, Unset):
            breakdown_value = []
            for breakdown_value_item_data in self.breakdown_value:
                breakdown_value_item = breakdown_value_item_data.to_dict()
                breakdown_value.append(breakdown_value_item)

        data_points: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.data_points, Unset):
            data_points = []
            for data_points_item_data in self.data_points:
                data_points_item = data_points_item_data.to_dict()
                data_points.append(data_points_item)

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if breakdown_value is not UNSET:
            field_dict["breakdownValue"] = breakdown_value
        if data_points is not UNSET:
            field_dict["dataPoints"] = data_points

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.breakdown_value import BreakdownValue  # noqa: PLC0415
        from ..models.data_point import DataPoint  # noqa: PLC0415

        d = dict(src_dict)
        _breakdown_value = d.pop("breakdownValue", UNSET)
        breakdown_value: list[BreakdownValue] | Unset = UNSET
        if _breakdown_value is not UNSET:
            breakdown_value = []
            for breakdown_value_item_data in _breakdown_value:
                breakdown_value_item = BreakdownValue.from_dict(breakdown_value_item_data)

                breakdown_value.append(breakdown_value_item)

        _data_points = d.pop("dataPoints", UNSET)
        data_points: list[DataPoint] | Unset = UNSET
        if _data_points is not UNSET:
            data_points = []
            for data_points_item_data in _data_points:
                data_points_item = DataPoint.from_dict(data_points_item_data)

                data_points.append(data_points_item)

        metric_value = cls(
            breakdown_value=breakdown_value,
            data_points=data_points,
        )

        return metric_value
