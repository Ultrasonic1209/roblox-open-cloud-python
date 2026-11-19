from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.dashboard_custom_event_metric_aggregation_type_0_type_0 import (
    DashboardCustomEventMetricAggregationType0Type0,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="DashboardCustomEventMetric")


@_attrs_define
class DashboardCustomEventMetric:
    """DashboardCustomEventMetric is the legacy custom-event source representation.

    Attributes:
        metric_key (None | str | Unset):  Default: ''.
        custom_event_name (None | str | Unset):  Default: ''.
        aggregation (DashboardCustomEventMetricAggregationType0Type0 | int | None | Unset): DashboardAggregation is the
            aggregation applied to a tile or series.
            Enum names follow proto conventions; synthesis adapters map to Creator Hub
            aggregation literal strings (`RAQIV2AggregationType`, summary-card literals,
            and `RAQIV2PercentileType`). Arbitrary `Percentile{N}` literals are not
            represented here and require a future contract extension. Default:
            DashboardCustomEventMetricAggregationType0Type0.DASHBOARD_AGGREGATION_INVALID.
    """

    metric_key: None | str | Unset = ""
    custom_event_name: None | str | Unset = ""
    aggregation: DashboardCustomEventMetricAggregationType0Type0 | int | None | Unset = (
        DashboardCustomEventMetricAggregationType0Type0.DASHBOARD_AGGREGATION_INVALID
    )

    def to_dict(self) -> dict[str, Any]:
        metric_key: None | str | Unset
        if isinstance(self.metric_key, Unset):
            metric_key = UNSET
        else:
            metric_key = self.metric_key

        custom_event_name: None | str | Unset
        if isinstance(self.custom_event_name, Unset):
            custom_event_name = UNSET
        else:
            custom_event_name = self.custom_event_name

        aggregation: int | None | str | Unset
        if isinstance(self.aggregation, Unset):
            aggregation = UNSET
        elif isinstance(self.aggregation, DashboardCustomEventMetricAggregationType0Type0):
            aggregation = self.aggregation.value
        else:
            aggregation = self.aggregation

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if metric_key is not UNSET:
            field_dict["metricKey"] = metric_key
        if custom_event_name is not UNSET:
            field_dict["customEventName"] = custom_event_name
        if aggregation is not UNSET:
            field_dict["aggregation"] = aggregation

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_metric_key(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        metric_key = _parse_metric_key(d.pop("metricKey", UNSET))

        def _parse_custom_event_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        custom_event_name = _parse_custom_event_name(d.pop("customEventName", UNSET))

        def _parse_aggregation(data: object) -> DashboardCustomEventMetricAggregationType0Type0 | int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                aggregation_type_0_type_0 = DashboardCustomEventMetricAggregationType0Type0(data)

                return aggregation_type_0_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DashboardCustomEventMetricAggregationType0Type0 | int | None | Unset, data)

        aggregation = _parse_aggregation(d.pop("aggregation", UNSET))

        dashboard_custom_event_metric = cls(
            metric_key=metric_key,
            custom_event_name=custom_event_name,
            aggregation=aggregation,
        )

        return dashboard_custom_event_metric
