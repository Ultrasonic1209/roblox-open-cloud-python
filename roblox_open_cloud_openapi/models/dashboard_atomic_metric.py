from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dashboard_custom_event_metric import DashboardCustomEventMetric


T = TypeVar("T", bound="DashboardAtomicMetric")


@_attrs_define
class DashboardAtomicMetric:
    """DashboardAtomicMetric is retained solely to deserialize schema-v1 dashboard
    documents and clients. It is not part of the current authoring interface.

        Attributes:
            metric_key (None | str | Unset):
            custom_event_metric (DashboardCustomEventMetric | None | Unset): DashboardCustomEventMetric is the legacy
                custom-event source representation.
    """

    metric_key: None | str | Unset = UNSET
    custom_event_metric: DashboardCustomEventMetric | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.dashboard_custom_event_metric import DashboardCustomEventMetric  # noqa: PLC0415

        metric_key: None | str | Unset
        if isinstance(self.metric_key, Unset):
            metric_key = UNSET
        else:
            metric_key = self.metric_key

        custom_event_metric: dict[str, Any] | None | Unset
        if isinstance(self.custom_event_metric, Unset):
            custom_event_metric = UNSET
        elif isinstance(self.custom_event_metric, DashboardCustomEventMetric):
            custom_event_metric = self.custom_event_metric.to_dict()
        else:
            custom_event_metric = self.custom_event_metric

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if metric_key is not UNSET:
            field_dict["metricKey"] = metric_key
        if custom_event_metric is not UNSET:
            field_dict["customEventMetric"] = custom_event_metric

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dashboard_custom_event_metric import DashboardCustomEventMetric  # noqa: PLC0415

        d = dict(src_dict)

        def _parse_metric_key(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        metric_key = _parse_metric_key(d.pop("metricKey", UNSET))

        def _parse_custom_event_metric(data: object) -> DashboardCustomEventMetric | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                custom_event_metric_type_0 = DashboardCustomEventMetric.from_dict(data)

                return custom_event_metric_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DashboardCustomEventMetric | None | Unset, data)

        custom_event_metric = _parse_custom_event_metric(d.pop("customEventMetric", UNSET))

        dashboard_atomic_metric = cls(
            metric_key=metric_key,
            custom_event_metric=custom_event_metric,
        )

        return dashboard_atomic_metric
