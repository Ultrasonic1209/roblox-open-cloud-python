from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.analytics_query_public_api_breakdown_value import AnalyticsQueryPublicApiBreakdownValue
    from ..models.analytics_query_public_api_data_point import AnalyticsQueryPublicApiDataPoint


T = TypeVar("T", bound="AnalyticsQueryPublicApiMetricValue")


@_attrs_define
class AnalyticsQueryPublicApiMetricValue:
    """A metric value for a single breakdown series.

    Attributes:
        breakdowns (list[AnalyticsQueryPublicApiBreakdownValue] | Unset): The breakdown values for this series.
        data_points (list[AnalyticsQueryPublicApiDataPoint] | Unset): The data points for this series.
    """

    breakdowns: list[AnalyticsQueryPublicApiBreakdownValue] | Unset = UNSET
    data_points: list[AnalyticsQueryPublicApiDataPoint] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        breakdowns: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.breakdowns, Unset):
            breakdowns = []
            for breakdowns_item_data in self.breakdowns:
                breakdowns_item = breakdowns_item_data.to_dict()
                breakdowns.append(breakdowns_item)

        data_points: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.data_points, Unset):
            data_points = []
            for data_points_item_data in self.data_points:
                data_points_item = data_points_item_data.to_dict()
                data_points.append(data_points_item)

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if breakdowns is not UNSET:
            field_dict["breakdowns"] = breakdowns
        if data_points is not UNSET:
            field_dict["dataPoints"] = data_points

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.analytics_query_public_api_breakdown_value import AnalyticsQueryPublicApiBreakdownValue
        from ..models.analytics_query_public_api_data_point import AnalyticsQueryPublicApiDataPoint

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        _breakdowns = d.pop("breakdowns", UNSET)
        breakdowns: list[AnalyticsQueryPublicApiBreakdownValue] | Unset = UNSET
        if _breakdowns is not UNSET:
            breakdowns = []
            for breakdowns_item_data in _breakdowns:
                breakdowns_item = AnalyticsQueryPublicApiBreakdownValue.from_dict(breakdowns_item_data)

                breakdowns.append(breakdowns_item)

        _data_points = d.pop("dataPoints", UNSET)
        data_points: list[AnalyticsQueryPublicApiDataPoint] | Unset = UNSET
        if _data_points is not UNSET:
            data_points = []
            for data_points_item_data in _data_points:
                data_points_item = AnalyticsQueryPublicApiDataPoint.from_dict(data_points_item_data)

                data_points.append(data_points_item)

        analytics_query_public_api_metric_value = cls(
            breakdowns=breakdowns,
            data_points=data_points,
        )

        return analytics_query_public_api_metric_value
