from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.chart_tile_metric_aggregation_type_0_type_0 import ChartTileMetricAggregationType0Type0
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dashboard_metric_reference import DashboardMetricReference
    from ..models.tile_filter import TileFilter


T = TypeVar("T", bound="ChartTileMetric")


@_attrs_define
class ChartTileMetric:
    """ChartTileMetric is one rendered series, table column, or metric input on a
    chart tile. `metric` is required. `series_key` is required and must be unique
    within a tile; renderers use it for stable color, legend, and column
    identity across edits. If `aggregation` is set and not INVALID it overrides
    `DashboardChartDataSpec.aggregation` for this series; otherwise the tile-level
    value applies.

        Attributes:
            metric (DashboardMetricReference | None | Unset): DashboardMetricReference identifies either a catalog metric or
                an inline
                computed metric. A future saved custom metric key can be added to this oneof
                without changing tile/document layout.
            series_key (None | str | Unset): Stable per-tile handle used for series identity, color assignment, and table
                column ordering. Default: ''.
            aggregation (ChartTileMetricAggregationType0Type0 | int | None | Unset): Optional per-series aggregation
                override. Default: ChartTileMetricAggregationType0Type0.DASHBOARD_AGGREGATION_INVALID.
            filters (list[TileFilter] | None | Unset): Optional filters scoped to this series or table column. These are
                combined
                conjunctively with ChartTile.data_spec.filters and, for computed metrics,
                the referenced source filters. Filters with the same dimension_key are
                also conjunctive; values within one TileFilter are alternatives (OR).
    """

    metric: DashboardMetricReference | None | Unset = UNSET
    series_key: None | str | Unset = ""
    aggregation: ChartTileMetricAggregationType0Type0 | int | None | Unset = (
        ChartTileMetricAggregationType0Type0.DASHBOARD_AGGREGATION_INVALID
    )
    filters: list[TileFilter] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.dashboard_metric_reference import DashboardMetricReference  # noqa: PLC0415

        metric: dict[str, Any] | None | Unset
        if isinstance(self.metric, Unset):
            metric = UNSET
        elif isinstance(self.metric, DashboardMetricReference):
            metric = self.metric.to_dict()
        else:
            metric = self.metric

        series_key: None | str | Unset
        if isinstance(self.series_key, Unset):
            series_key = UNSET
        else:
            series_key = self.series_key

        aggregation: int | None | str | Unset
        if isinstance(self.aggregation, Unset):
            aggregation = UNSET
        elif isinstance(self.aggregation, ChartTileMetricAggregationType0Type0):
            aggregation = self.aggregation.value
        else:
            aggregation = self.aggregation

        filters: list[dict[str, Any]] | None | Unset
        if isinstance(self.filters, Unset):
            filters = UNSET
        elif isinstance(self.filters, list):
            filters = []
            for filters_type_0_item_data in self.filters:
                filters_type_0_item = filters_type_0_item_data.to_dict()
                filters.append(filters_type_0_item)

        else:
            filters = self.filters

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if metric is not UNSET:
            field_dict["metric"] = metric
        if series_key is not UNSET:
            field_dict["seriesKey"] = series_key
        if aggregation is not UNSET:
            field_dict["aggregation"] = aggregation
        if filters is not UNSET:
            field_dict["filters"] = filters

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dashboard_metric_reference import DashboardMetricReference  # noqa: PLC0415
        from ..models.tile_filter import TileFilter  # noqa: PLC0415

        d = dict(src_dict)

        def _parse_metric(data: object) -> DashboardMetricReference | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metric_type_0 = DashboardMetricReference.from_dict(data)

                return metric_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DashboardMetricReference | None | Unset, data)

        metric = _parse_metric(d.pop("metric", UNSET))

        def _parse_series_key(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        series_key = _parse_series_key(d.pop("seriesKey", UNSET))

        def _parse_aggregation(data: object) -> ChartTileMetricAggregationType0Type0 | int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                aggregation_type_0_type_0 = ChartTileMetricAggregationType0Type0(data)

                return aggregation_type_0_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ChartTileMetricAggregationType0Type0 | int | None | Unset, data)

        aggregation = _parse_aggregation(d.pop("aggregation", UNSET))

        def _parse_filters(data: object) -> list[TileFilter] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                filters_type_0 = []
                _filters_type_0 = data
                for filters_type_0_item_data in _filters_type_0:
                    filters_type_0_item = TileFilter.from_dict(filters_type_0_item_data)

                    filters_type_0.append(filters_type_0_item)

                return filters_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[TileFilter] | None | Unset, data)

        filters = _parse_filters(d.pop("filters", UNSET))

        chart_tile_metric = cls(
            metric=metric,
            series_key=series_key,
            aggregation=aggregation,
            filters=filters,
        )

        return chart_tile_metric
