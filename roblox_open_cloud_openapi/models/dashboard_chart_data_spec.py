from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.dashboard_chart_data_spec_aggregation_type_0_type_0 import DashboardChartDataSpecAggregationType0Type0
from ..models.dashboard_chart_data_spec_granularity_type_0_type_0 import DashboardChartDataSpecGranularityType0Type0
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.chart_tile_metric import ChartTileMetric
    from ..models.tile_filter import TileFilter


T = TypeVar("T", bound="DashboardChartDataSpec")


@_attrs_define
class DashboardChartDataSpec:
    """DashboardChartDataSpec carries chart query inputs synthesized into RAQI requests.

    Attributes:
        metrics (list[ChartTileMetric] | None | Unset): Cardinality rules for `metrics`:
              - `metrics` MUST be non-empty.
              - `DASHBOARD_CHART_TYPE_TABLE` accepts one or more metrics (one per rendered column).
              - All other chart types accept exactly one metric in v1beta1.
        aggregation (DashboardChartDataSpecAggregationType0Type0 | int | None | Unset): Default aggregation for metrics
            without a per-series override. Default:
            DashboardChartDataSpecAggregationType0Type0.DASHBOARD_AGGREGATION_INVALID.
        breakdown_dimension_keys (list[str] | None | Unset): Ordered breakdown dimension keys. Synthesis maps to
            `QueryBreakdown` in
            `universe_analytics_query.proto` / RAQI breakdown lists.
        granularity (DashboardChartDataSpecGranularityType0Type0 | int | None | Unset): Time bucketing for chart
            queries. Default: DashboardChartDataSpecGranularityType0Type0.DASHBOARD_GRANULARITY_INVALID.
        filters (list[TileFilter] | None | Unset):
    """

    metrics: list[ChartTileMetric] | None | Unset = UNSET
    aggregation: DashboardChartDataSpecAggregationType0Type0 | int | None | Unset = (
        DashboardChartDataSpecAggregationType0Type0.DASHBOARD_AGGREGATION_INVALID
    )
    breakdown_dimension_keys: list[str] | None | Unset = UNSET
    granularity: DashboardChartDataSpecGranularityType0Type0 | int | None | Unset = (
        DashboardChartDataSpecGranularityType0Type0.DASHBOARD_GRANULARITY_INVALID
    )
    filters: list[TileFilter] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        metrics: list[dict[str, Any]] | None | Unset
        if isinstance(self.metrics, Unset):
            metrics = UNSET
        elif isinstance(self.metrics, list):
            metrics = []
            for metrics_type_0_item_data in self.metrics:
                metrics_type_0_item = metrics_type_0_item_data.to_dict()
                metrics.append(metrics_type_0_item)

        else:
            metrics = self.metrics

        aggregation: int | None | str | Unset
        if isinstance(self.aggregation, Unset):
            aggregation = UNSET
        elif isinstance(self.aggregation, DashboardChartDataSpecAggregationType0Type0):
            aggregation = self.aggregation.value
        else:
            aggregation = self.aggregation

        breakdown_dimension_keys: list[str] | None | Unset
        if isinstance(self.breakdown_dimension_keys, Unset):
            breakdown_dimension_keys = UNSET
        elif isinstance(self.breakdown_dimension_keys, list):
            breakdown_dimension_keys = self.breakdown_dimension_keys

        else:
            breakdown_dimension_keys = self.breakdown_dimension_keys

        granularity: int | None | str | Unset
        if isinstance(self.granularity, Unset):
            granularity = UNSET
        elif isinstance(self.granularity, DashboardChartDataSpecGranularityType0Type0):
            granularity = self.granularity.value
        else:
            granularity = self.granularity

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
        if metrics is not UNSET:
            field_dict["metrics"] = metrics
        if aggregation is not UNSET:
            field_dict["aggregation"] = aggregation
        if breakdown_dimension_keys is not UNSET:
            field_dict["breakdownDimensionKeys"] = breakdown_dimension_keys
        if granularity is not UNSET:
            field_dict["granularity"] = granularity
        if filters is not UNSET:
            field_dict["filters"] = filters

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.chart_tile_metric import ChartTileMetric  # noqa: PLC0415
        from ..models.tile_filter import TileFilter  # noqa: PLC0415

        d = dict(src_dict)

        def _parse_metrics(data: object) -> list[ChartTileMetric] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                metrics_type_0 = []
                _metrics_type_0 = data
                for metrics_type_0_item_data in _metrics_type_0:
                    metrics_type_0_item = ChartTileMetric.from_dict(metrics_type_0_item_data)

                    metrics_type_0.append(metrics_type_0_item)

                return metrics_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ChartTileMetric] | None | Unset, data)

        metrics = _parse_metrics(d.pop("metrics", UNSET))

        def _parse_aggregation(data: object) -> DashboardChartDataSpecAggregationType0Type0 | int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                aggregation_type_0_type_0 = DashboardChartDataSpecAggregationType0Type0(data)

                return aggregation_type_0_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DashboardChartDataSpecAggregationType0Type0 | int | None | Unset, data)

        aggregation = _parse_aggregation(d.pop("aggregation", UNSET))

        def _parse_breakdown_dimension_keys(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                breakdown_dimension_keys_type_0 = cast(list[str], data)

                return breakdown_dimension_keys_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        breakdown_dimension_keys = _parse_breakdown_dimension_keys(d.pop("breakdownDimensionKeys", UNSET))

        def _parse_granularity(data: object) -> DashboardChartDataSpecGranularityType0Type0 | int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                granularity_type_0_type_0 = DashboardChartDataSpecGranularityType0Type0(data)

                return granularity_type_0_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DashboardChartDataSpecGranularityType0Type0 | int | None | Unset, data)

        granularity = _parse_granularity(d.pop("granularity", UNSET))

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

        dashboard_chart_data_spec = cls(
            metrics=metrics,
            aggregation=aggregation,
            breakdown_dimension_keys=breakdown_dimension_keys,
            granularity=granularity,
            filters=filters,
        )

        return dashboard_chart_data_spec
