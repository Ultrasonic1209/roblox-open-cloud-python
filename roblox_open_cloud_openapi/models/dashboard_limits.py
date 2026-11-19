from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="DashboardLimits")


@_attrs_define
class DashboardLimits:
    """DashboardLimits mirrors the write-time caps enforced by this service. Values
    are resolved per request, so they reflect the current runtime configuration
    rather than the values present at deploy time. A limit of 0 means the cap is
    disabled and the service does not enforce it.

    Clients should treat these as upper bounds and may apply a stricter
    presentation limit of their own; the effective cap for a client is the
    minimum of the two.

        Attributes:
            max_dashboards_per_universe (int | None | Unset): Maximum active dashboards per universe, enforced by the quota
                guard. Default: 0.
            max_document_payload_bytes (int | None | Unset): Maximum encoded dashboard document payload size in bytes.
                Default: 0.
            max_summary_cards_per_dashboard (int | None | Unset): Maximum summary card tiles in one dashboard document.
                Default: 0.
            max_chart_tiles_per_dashboard (int | None | Unset): Maximum chart tiles in one dashboard document. Default: 0.
            max_table_metric_columns (int | None | Unset): Maximum metric columns in a single table chart tile. Default: 0.
            max_dashboard_name_length (int | None | Unset): Maximum dashboard name length in characters. Default: 0.
            max_dashboard_description_length (int | None | Unset): Maximum dashboard description length in characters.
                Default: 0.
            max_tile_title_length (int | None | Unset): Maximum tile title length in characters. Default: 0.
            max_pinned_dashboards_per_universe (int | None | Unset): Maximum pinned dashboards per universe, enforced by the
                quota guard. Default: 0.
            max_idempotency_key_length (int | None | Unset): Maximum `CreateDashboardRequest.idempotency_key` length in
                characters accepted for a new
                create. Because the key is client-supplied and this cap is runtime-configurable, clients
                should read it here rather than assuming a fixed length. Lowering it does not invalidate
                keys that are already bound: those keep replaying at their original length. Default: 0.
    """

    max_dashboards_per_universe: int | None | Unset = 0
    max_document_payload_bytes: int | None | Unset = 0
    max_summary_cards_per_dashboard: int | None | Unset = 0
    max_chart_tiles_per_dashboard: int | None | Unset = 0
    max_table_metric_columns: int | None | Unset = 0
    max_dashboard_name_length: int | None | Unset = 0
    max_dashboard_description_length: int | None | Unset = 0
    max_tile_title_length: int | None | Unset = 0
    max_pinned_dashboards_per_universe: int | None | Unset = 0
    max_idempotency_key_length: int | None | Unset = 0

    def to_dict(self) -> dict[str, Any]:
        max_dashboards_per_universe: int | None | Unset
        if isinstance(self.max_dashboards_per_universe, Unset):
            max_dashboards_per_universe = UNSET
        else:
            max_dashboards_per_universe = self.max_dashboards_per_universe

        max_document_payload_bytes: int | None | Unset
        if isinstance(self.max_document_payload_bytes, Unset):
            max_document_payload_bytes = UNSET
        else:
            max_document_payload_bytes = self.max_document_payload_bytes

        max_summary_cards_per_dashboard: int | None | Unset
        if isinstance(self.max_summary_cards_per_dashboard, Unset):
            max_summary_cards_per_dashboard = UNSET
        else:
            max_summary_cards_per_dashboard = self.max_summary_cards_per_dashboard

        max_chart_tiles_per_dashboard: int | None | Unset
        if isinstance(self.max_chart_tiles_per_dashboard, Unset):
            max_chart_tiles_per_dashboard = UNSET
        else:
            max_chart_tiles_per_dashboard = self.max_chart_tiles_per_dashboard

        max_table_metric_columns: int | None | Unset
        if isinstance(self.max_table_metric_columns, Unset):
            max_table_metric_columns = UNSET
        else:
            max_table_metric_columns = self.max_table_metric_columns

        max_dashboard_name_length: int | None | Unset
        if isinstance(self.max_dashboard_name_length, Unset):
            max_dashboard_name_length = UNSET
        else:
            max_dashboard_name_length = self.max_dashboard_name_length

        max_dashboard_description_length: int | None | Unset
        if isinstance(self.max_dashboard_description_length, Unset):
            max_dashboard_description_length = UNSET
        else:
            max_dashboard_description_length = self.max_dashboard_description_length

        max_tile_title_length: int | None | Unset
        if isinstance(self.max_tile_title_length, Unset):
            max_tile_title_length = UNSET
        else:
            max_tile_title_length = self.max_tile_title_length

        max_pinned_dashboards_per_universe: int | None | Unset
        if isinstance(self.max_pinned_dashboards_per_universe, Unset):
            max_pinned_dashboards_per_universe = UNSET
        else:
            max_pinned_dashboards_per_universe = self.max_pinned_dashboards_per_universe

        max_idempotency_key_length: int | None | Unset
        if isinstance(self.max_idempotency_key_length, Unset):
            max_idempotency_key_length = UNSET
        else:
            max_idempotency_key_length = self.max_idempotency_key_length

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if max_dashboards_per_universe is not UNSET:
            field_dict["maxDashboardsPerUniverse"] = max_dashboards_per_universe
        if max_document_payload_bytes is not UNSET:
            field_dict["maxDocumentPayloadBytes"] = max_document_payload_bytes
        if max_summary_cards_per_dashboard is not UNSET:
            field_dict["maxSummaryCardsPerDashboard"] = max_summary_cards_per_dashboard
        if max_chart_tiles_per_dashboard is not UNSET:
            field_dict["maxChartTilesPerDashboard"] = max_chart_tiles_per_dashboard
        if max_table_metric_columns is not UNSET:
            field_dict["maxTableMetricColumns"] = max_table_metric_columns
        if max_dashboard_name_length is not UNSET:
            field_dict["maxDashboardNameLength"] = max_dashboard_name_length
        if max_dashboard_description_length is not UNSET:
            field_dict["maxDashboardDescriptionLength"] = max_dashboard_description_length
        if max_tile_title_length is not UNSET:
            field_dict["maxTileTitleLength"] = max_tile_title_length
        if max_pinned_dashboards_per_universe is not UNSET:
            field_dict["maxPinnedDashboardsPerUniverse"] = max_pinned_dashboards_per_universe
        if max_idempotency_key_length is not UNSET:
            field_dict["maxIdempotencyKeyLength"] = max_idempotency_key_length

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_max_dashboards_per_universe(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        max_dashboards_per_universe = _parse_max_dashboards_per_universe(d.pop("maxDashboardsPerUniverse", UNSET))

        def _parse_max_document_payload_bytes(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        max_document_payload_bytes = _parse_max_document_payload_bytes(d.pop("maxDocumentPayloadBytes", UNSET))

        def _parse_max_summary_cards_per_dashboard(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        max_summary_cards_per_dashboard = _parse_max_summary_cards_per_dashboard(
            d.pop("maxSummaryCardsPerDashboard", UNSET)
        )

        def _parse_max_chart_tiles_per_dashboard(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        max_chart_tiles_per_dashboard = _parse_max_chart_tiles_per_dashboard(d.pop("maxChartTilesPerDashboard", UNSET))

        def _parse_max_table_metric_columns(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        max_table_metric_columns = _parse_max_table_metric_columns(d.pop("maxTableMetricColumns", UNSET))

        def _parse_max_dashboard_name_length(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        max_dashboard_name_length = _parse_max_dashboard_name_length(d.pop("maxDashboardNameLength", UNSET))

        def _parse_max_dashboard_description_length(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        max_dashboard_description_length = _parse_max_dashboard_description_length(
            d.pop("maxDashboardDescriptionLength", UNSET)
        )

        def _parse_max_tile_title_length(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        max_tile_title_length = _parse_max_tile_title_length(d.pop("maxTileTitleLength", UNSET))

        def _parse_max_pinned_dashboards_per_universe(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        max_pinned_dashboards_per_universe = _parse_max_pinned_dashboards_per_universe(
            d.pop("maxPinnedDashboardsPerUniverse", UNSET)
        )

        def _parse_max_idempotency_key_length(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        max_idempotency_key_length = _parse_max_idempotency_key_length(d.pop("maxIdempotencyKeyLength", UNSET))

        dashboard_limits = cls(
            max_dashboards_per_universe=max_dashboards_per_universe,
            max_document_payload_bytes=max_document_payload_bytes,
            max_summary_cards_per_dashboard=max_summary_cards_per_dashboard,
            max_chart_tiles_per_dashboard=max_chart_tiles_per_dashboard,
            max_table_metric_columns=max_table_metric_columns,
            max_dashboard_name_length=max_dashboard_name_length,
            max_dashboard_description_length=max_dashboard_description_length,
            max_tile_title_length=max_tile_title_length,
            max_pinned_dashboards_per_universe=max_pinned_dashboards_per_universe,
            max_idempotency_key_length=max_idempotency_key_length,
        )

        return dashboard_limits
