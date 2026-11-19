from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dashboard_computed_metric import DashboardComputedMetric
    from ..models.dashboard_metric_variant_selection import DashboardMetricVariantSelection


T = TypeVar("T", bound="DashboardMetricReference")


@_attrs_define
class DashboardMetricReference:
    """DashboardMetricReference identifies either a catalog metric or an inline
    computed metric. A future saved custom metric key can be added to this oneof
    without changing tile/document layout.

        Attributes:
            metric_key (None | str | Unset):
            computed_metric (DashboardComputedMetric | None | Unset): DashboardComputedMetric is an inline dashboard
                authoring definition. It has
                no standalone resource or persistence lifecycle.
            variant_selections (list[DashboardMetricVariantSelection] | None | Unset):
    """

    metric_key: None | str | Unset = UNSET
    computed_metric: DashboardComputedMetric | None | Unset = UNSET
    variant_selections: list[DashboardMetricVariantSelection] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.dashboard_computed_metric import DashboardComputedMetric  # noqa: PLC0415

        metric_key: None | str | Unset
        if isinstance(self.metric_key, Unset):
            metric_key = UNSET
        else:
            metric_key = self.metric_key

        computed_metric: dict[str, Any] | None | Unset
        if isinstance(self.computed_metric, Unset):
            computed_metric = UNSET
        elif isinstance(self.computed_metric, DashboardComputedMetric):
            computed_metric = self.computed_metric.to_dict()
        else:
            computed_metric = self.computed_metric

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

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if metric_key is not UNSET:
            field_dict["metricKey"] = metric_key
        if computed_metric is not UNSET:
            field_dict["computedMetric"] = computed_metric
        if variant_selections is not UNSET:
            field_dict["variantSelections"] = variant_selections

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dashboard_computed_metric import DashboardComputedMetric  # noqa: PLC0415
        from ..models.dashboard_metric_variant_selection import DashboardMetricVariantSelection  # noqa: PLC0415

        d = dict(src_dict)

        def _parse_metric_key(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        metric_key = _parse_metric_key(d.pop("metricKey", UNSET))

        def _parse_computed_metric(data: object) -> DashboardComputedMetric | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                computed_metric_type_0 = DashboardComputedMetric.from_dict(data)

                return computed_metric_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DashboardComputedMetric | None | Unset, data)

        computed_metric = _parse_computed_metric(d.pop("computedMetric", UNSET))

        def _parse_variant_selections(data: object) -> list[DashboardMetricVariantSelection] | None | Unset:
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
                    variant_selections_type_0_item = DashboardMetricVariantSelection.from_dict(
                        variant_selections_type_0_item_data
                    )

                    variant_selections_type_0.append(variant_selections_type_0_item)

                return variant_selections_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[DashboardMetricVariantSelection] | None | Unset, data)

        variant_selections = _parse_variant_selections(d.pop("variantSelections", UNSET))

        dashboard_metric_reference = cls(
            metric_key=metric_key,
            computed_metric=computed_metric,
            variant_selections=variant_selections,
        )

        return dashboard_metric_reference
