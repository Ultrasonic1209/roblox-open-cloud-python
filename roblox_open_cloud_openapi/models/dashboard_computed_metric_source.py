from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.computed_metric_filter import ComputedMetricFilter
    from ..models.computed_metric_variant_selection import ComputedMetricVariantSelection
    from ..models.dashboard_atomic_metric import DashboardAtomicMetric


T = TypeVar("T", bound="DashboardComputedMetricSource")


@_attrs_define
class DashboardComputedMetricSource:
    """DashboardComputedMetricSource describes one named formula source.

    Attributes:
        source_key (None | str | Unset):  Default: ''.
        filters (list[ComputedMetricFilter] | None | Unset): Keep this message wire-compatible with TileFilter because
            field 3 is
            retained for schema-v1 documents.
        variant_selections (list[ComputedMetricVariantSelection] | None | Unset): Keep this message wire-compatible with
            DashboardMetricVariantSelection
            because field 4 is retained for schema-v1 documents.
        metric_key (None | str | Unset):  Default: ''.
        metric (DashboardAtomicMetric | None | Unset): Compatibility-only wire field for schema-v1 documents and
            already-compiled
            protobuf clients. New authors must use metric_key, filters, and
            variant_selections instead.
    """

    source_key: None | str | Unset = ""
    filters: list[ComputedMetricFilter] | None | Unset = UNSET
    variant_selections: list[ComputedMetricVariantSelection] | None | Unset = UNSET
    metric_key: None | str | Unset = ""
    metric: DashboardAtomicMetric | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.dashboard_atomic_metric import DashboardAtomicMetric  # noqa: PLC0415

        source_key: None | str | Unset
        if isinstance(self.source_key, Unset):
            source_key = UNSET
        else:
            source_key = self.source_key

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

        variant_selections: list[dict[str, Any]] | None | Unset
        if isinstance(self.variant_selections, Unset):
            variant_selections = UNSET
        elif isinstance(self.variant_selections, list):
            variant_selections = []
            for variant_selections_type_0_item_data in self.variant_selections:
                variant_selections_type_0_item = variant_selections_type_0_item_data.to_dict()
                variant_selections.append(variant_selections_type_0_item)

        else:
            variant_selections = self.variant_selections

        metric_key: None | str | Unset
        if isinstance(self.metric_key, Unset):
            metric_key = UNSET
        else:
            metric_key = self.metric_key

        metric: dict[str, Any] | None | Unset
        if isinstance(self.metric, Unset):
            metric = UNSET
        elif isinstance(self.metric, DashboardAtomicMetric):
            metric = self.metric.to_dict()
        else:
            metric = self.metric

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if source_key is not UNSET:
            field_dict["sourceKey"] = source_key
        if filters is not UNSET:
            field_dict["filters"] = filters
        if variant_selections is not UNSET:
            field_dict["variantSelections"] = variant_selections
        if metric_key is not UNSET:
            field_dict["metricKey"] = metric_key
        if metric is not UNSET:
            field_dict["metric"] = metric

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.computed_metric_filter import ComputedMetricFilter  # noqa: PLC0415
        from ..models.computed_metric_variant_selection import ComputedMetricVariantSelection  # noqa: PLC0415
        from ..models.dashboard_atomic_metric import DashboardAtomicMetric  # noqa: PLC0415

        d = dict(src_dict)

        def _parse_source_key(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        source_key = _parse_source_key(d.pop("sourceKey", UNSET))

        def _parse_filters(data: object) -> list[ComputedMetricFilter] | None | Unset:
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
                    filters_type_0_item = ComputedMetricFilter.from_dict(filters_type_0_item_data)

                    filters_type_0.append(filters_type_0_item)

                return filters_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ComputedMetricFilter] | None | Unset, data)

        filters = _parse_filters(d.pop("filters", UNSET))

        def _parse_variant_selections(data: object) -> list[ComputedMetricVariantSelection] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                variant_selections_type_0 = []
                _variant_selections_type_0 = data
                for variant_selections_type_0_item_data in _variant_selections_type_0:
                    variant_selections_type_0_item = ComputedMetricVariantSelection.from_dict(
                        variant_selections_type_0_item_data
                    )

                    variant_selections_type_0.append(variant_selections_type_0_item)

                return variant_selections_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ComputedMetricVariantSelection] | None | Unset, data)

        variant_selections = _parse_variant_selections(d.pop("variantSelections", UNSET))

        def _parse_metric_key(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        metric_key = _parse_metric_key(d.pop("metricKey", UNSET))

        def _parse_metric(data: object) -> DashboardAtomicMetric | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metric_type_0 = DashboardAtomicMetric.from_dict(data)

                return metric_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DashboardAtomicMetric | None | Unset, data)

        metric = _parse_metric(d.pop("metric", UNSET))

        dashboard_computed_metric_source = cls(
            source_key=source_key,
            filters=filters,
            variant_selections=variant_selections,
            metric_key=metric_key,
            metric=metric,
        )

        return dashboard_computed_metric_source
