from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.alert_storage_alert_interval import AlertStorageAlertInterval
from ..models.alert_storage_severity import AlertStorageSeverity
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.alert_storage_alert_condition import AlertStorageAlertCondition
    from ..models.analytics_alert_control_plane_models_alert_query_breakdown import (
        AnalyticsAlertControlPlaneModelsAlertQueryBreakdown,
    )
    from ..models.analytics_alert_control_plane_models_alert_query_filter import (
        AnalyticsAlertControlPlaneModelsAlertQueryFilter,
    )


T = TypeVar("T", bound="AnalyticsAlertControlPlaneModelsAlertConfigSummary")


@_attrs_define
class AnalyticsAlertControlPlaneModelsAlertConfigSummary:
    """Key fields of the alert configuration that triggered an incident.

    Attributes:
        id (str): Unique identifier of the alert configuration (string-encoded 64-bit integer).
        name (str): Display name of the alert configuration.
        metric (str): Name of the metric this alert evaluates.
        severity (AlertStorageSeverity): Severity level assigned to an alert configuration.

            SEV_0

            SEV_1

            SEV_2
        interval (AlertStorageAlertInterval): How frequently an alert condition is evaluated.

            OneMinute

            HalfHour

            OneHour

            OneDay
        condition (AlertStorageAlertCondition): The threshold condition that determines when an alert fires.
        description (None | str | Unset): Optional free-text description of the alert's purpose.
        filter_ (list[AnalyticsAlertControlPlaneModelsAlertQueryFilter] | None | Unset): Dimension filters applied to
            the metric query, if any.
        breakdown (list[AnalyticsAlertControlPlaneModelsAlertQueryBreakdown] | None | Unset): Grouping dimensions for
            the metric query, if any.
    """

    id: str
    name: str
    metric: str
    severity: AlertStorageSeverity
    interval: AlertStorageAlertInterval
    condition: AlertStorageAlertCondition
    description: None | str | Unset = UNSET
    filter_: list[AnalyticsAlertControlPlaneModelsAlertQueryFilter] | None | Unset = UNSET
    breakdown: list[AnalyticsAlertControlPlaneModelsAlertQueryBreakdown] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        metric = self.metric

        severity = self.severity.value

        interval = self.interval.value

        condition = self.condition.to_dict()

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        filter_: list[dict[str, Any]] | None | Unset
        if isinstance(self.filter_, Unset):
            filter_ = UNSET
        elif isinstance(self.filter_, list):
            filter_ = []
            for filter_type_0_item_data in self.filter_:
                filter_type_0_item = filter_type_0_item_data.to_dict()
                filter_.append(filter_type_0_item)

        else:
            filter_ = self.filter_

        breakdown: list[dict[str, Any]] | None | Unset
        if isinstance(self.breakdown, Unset):
            breakdown = UNSET
        elif isinstance(self.breakdown, list):
            breakdown = []
            for breakdown_type_0_item_data in self.breakdown:
                breakdown_type_0_item = breakdown_type_0_item_data.to_dict()
                breakdown.append(breakdown_type_0_item)

        else:
            breakdown = self.breakdown

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "name": name,
                "metric": metric,
                "severity": severity,
                "interval": interval,
                "condition": condition,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if filter_ is not UNSET:
            field_dict["filter"] = filter_
        if breakdown is not UNSET:
            field_dict["breakdown"] = breakdown

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.alert_storage_alert_condition import AlertStorageAlertCondition
        from ..models.analytics_alert_control_plane_models_alert_query_breakdown import (
            AnalyticsAlertControlPlaneModelsAlertQueryBreakdown,
        )
        from ..models.analytics_alert_control_plane_models_alert_query_filter import (
            AnalyticsAlertControlPlaneModelsAlertQueryFilter,
        )

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        id = d.pop("id")

        name = d.pop("name")

        metric = d.pop("metric")

        severity = AlertStorageSeverity(d.pop("severity"))

        interval = AlertStorageAlertInterval(d.pop("interval"))

        condition = AlertStorageAlertCondition.from_dict(d.pop("condition"))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_filter_(data: object) -> list[AnalyticsAlertControlPlaneModelsAlertQueryFilter] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                filter_type_0 = []
                _filter_type_0 = data
                for filter_type_0_item_data in _filter_type_0:
                    filter_type_0_item = AnalyticsAlertControlPlaneModelsAlertQueryFilter.from_dict(
                        filter_type_0_item_data
                    )

                    filter_type_0.append(filter_type_0_item)

                return filter_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[AnalyticsAlertControlPlaneModelsAlertQueryFilter] | None | Unset, data)

        filter_ = _parse_filter_(d.pop("filter", UNSET))

        def _parse_breakdown(data: object) -> list[AnalyticsAlertControlPlaneModelsAlertQueryBreakdown] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                breakdown_type_0 = []
                _breakdown_type_0 = data
                for breakdown_type_0_item_data in _breakdown_type_0:
                    breakdown_type_0_item = AnalyticsAlertControlPlaneModelsAlertQueryBreakdown.from_dict(
                        breakdown_type_0_item_data
                    )

                    breakdown_type_0.append(breakdown_type_0_item)

                return breakdown_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[AnalyticsAlertControlPlaneModelsAlertQueryBreakdown] | None | Unset, data)

        breakdown = _parse_breakdown(d.pop("breakdown", UNSET))

        analytics_alert_control_plane_models_alert_config_summary = cls(
            id=id,
            name=name,
            metric=metric,
            severity=severity,
            interval=interval,
            condition=condition,
            description=description,
            filter_=filter_,
            breakdown=breakdown,
        )

        return analytics_alert_control_plane_models_alert_config_summary
