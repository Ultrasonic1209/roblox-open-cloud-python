from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.summary_card_tile_aggregation_type_0_type_0 import SummaryCardTileAggregationType0Type0
from ..models.summary_card_tile_title_source_type_0_type_0 import SummaryCardTileTitleSourceType0Type0
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dashboard_metric_reference import DashboardMetricReference
    from ..models.tile_filter import TileFilter


T = TypeVar("T", bound="SummaryCardTile")


@_attrs_define
class SummaryCardTile:
    """SummaryCardTile is a top-of-dashboard summary card.

    Attributes:
        tile_id (None | str | Unset):  Default: ''.
        title (None | str | Unset):  Default: ''.
        metric (DashboardMetricReference | None | Unset): DashboardMetricReference identifies either a catalog metric or
            an inline
            computed metric. A future saved custom metric key can be added to this oneof
            without changing tile/document layout.
        aggregation (int | None | SummaryCardTileAggregationType0Type0 | Unset): DashboardAggregation is the aggregation
            applied to a tile or series.
            Enum names follow proto conventions; synthesis adapters map to Creator Hub
            aggregation literal strings (`RAQIV2AggregationType`, summary-card literals,
            and `RAQIV2PercentileType`). Arbitrary `Percentile{N}` literals are not
            represented here and require a future contract extension. Default:
            SummaryCardTileAggregationType0Type0.DASHBOARD_AGGREGATION_INVALID.
        filters (list[TileFilter] | None | Unset):
        title_source (int | None | SummaryCardTileTitleSourceType0Type0 | Unset): DashboardTitleSource describes how a
            dashboard tile title is derived. Default: SummaryCardTileTitleSourceType0Type0.DASHBOARD_TITLE_SOURCE_INVALID.
    """

    tile_id: None | str | Unset = ""
    title: None | str | Unset = ""
    metric: DashboardMetricReference | None | Unset = UNSET
    aggregation: int | None | SummaryCardTileAggregationType0Type0 | Unset = (
        SummaryCardTileAggregationType0Type0.DASHBOARD_AGGREGATION_INVALID
    )
    filters: list[TileFilter] | None | Unset = UNSET
    title_source: int | None | SummaryCardTileTitleSourceType0Type0 | Unset = (
        SummaryCardTileTitleSourceType0Type0.DASHBOARD_TITLE_SOURCE_INVALID
    )

    def to_dict(self) -> dict[str, Any]:
        from ..models.dashboard_metric_reference import DashboardMetricReference  # noqa: PLC0415

        tile_id: None | str | Unset
        if isinstance(self.tile_id, Unset):
            tile_id = UNSET
        else:
            tile_id = self.tile_id

        title: None | str | Unset
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title

        metric: dict[str, Any] | None | Unset
        if isinstance(self.metric, Unset):
            metric = UNSET
        elif isinstance(self.metric, DashboardMetricReference):
            metric = self.metric.to_dict()
        else:
            metric = self.metric

        aggregation: int | None | str | Unset
        if isinstance(self.aggregation, Unset):
            aggregation = UNSET
        elif isinstance(self.aggregation, SummaryCardTileAggregationType0Type0):
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

        title_source: int | None | str | Unset
        if isinstance(self.title_source, Unset):
            title_source = UNSET
        elif isinstance(self.title_source, SummaryCardTileTitleSourceType0Type0):
            title_source = self.title_source.value
        else:
            title_source = self.title_source

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if tile_id is not UNSET:
            field_dict["tileId"] = tile_id
        if title is not UNSET:
            field_dict["title"] = title
        if metric is not UNSET:
            field_dict["metric"] = metric
        if aggregation is not UNSET:
            field_dict["aggregation"] = aggregation
        if filters is not UNSET:
            field_dict["filters"] = filters
        if title_source is not UNSET:
            field_dict["titleSource"] = title_source

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dashboard_metric_reference import DashboardMetricReference  # noqa: PLC0415
        from ..models.tile_filter import TileFilter  # noqa: PLC0415

        d = dict(src_dict)

        def _parse_tile_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tile_id = _parse_tile_id(d.pop("tileId", UNSET))

        def _parse_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        title = _parse_title(d.pop("title", UNSET))

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

        def _parse_aggregation(data: object) -> int | None | SummaryCardTileAggregationType0Type0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                aggregation_type_0_type_0 = SummaryCardTileAggregationType0Type0(data)

                return aggregation_type_0_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(int | None | SummaryCardTileAggregationType0Type0 | Unset, data)

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

        def _parse_title_source(data: object) -> int | None | SummaryCardTileTitleSourceType0Type0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                title_source_type_0_type_0 = SummaryCardTileTitleSourceType0Type0(data)

                return title_source_type_0_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(int | None | SummaryCardTileTitleSourceType0Type0 | Unset, data)

        title_source = _parse_title_source(d.pop("titleSource", UNSET))

        summary_card_tile = cls(
            tile_id=tile_id,
            title=title,
            metric=metric,
            aggregation=aggregation,
            filters=filters,
            title_source=title_source,
        )

        return summary_card_tile
