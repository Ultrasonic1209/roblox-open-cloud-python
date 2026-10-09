from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.alert_storage_alert_interval import AlertStorageAlertInterval
from ..models.alert_storage_severity import AlertStorageSeverity
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.alert_storage_webhook_receiver_config import AlertStorageWebhookReceiverConfig
    from ..models.analytics_alert_control_plane_models_alert_condition_input import (
        AnalyticsAlertControlPlaneModelsAlertConditionInput,
    )
    from ..models.analytics_alert_control_plane_models_alert_query_breakdown import (
        AnalyticsAlertControlPlaneModelsAlertQueryBreakdown,
    )
    from ..models.analytics_alert_control_plane_models_alert_query_filter import (
        AnalyticsAlertControlPlaneModelsAlertQueryFilter,
    )


T = TypeVar("T", bound="AnalyticsAlertControlPlaneModelsCreateAlertConfigRequest")


@_attrs_define
class AnalyticsAlertControlPlaneModelsCreateAlertConfigRequest:
    """Request body for creating a new alert configuration.

    Attributes:
        name (str): Display name of the alert. Must be unique within the resource. Maximum length is 128
            characters and the value is subject to Roblox text-moderation policies.
        metric (str): Name of the metric this alert should evaluate.
        severity (AlertStorageSeverity): Severity level assigned to an alert configuration.

            SEV_0

            SEV_1

            SEV_2
        interval (AlertStorageAlertInterval): How frequently an alert condition is evaluated.

            OneMinute

            HalfHour

            OneHour

            OneDay
        consecutive_occurrences (int): Number of consecutive evaluation periods the condition must be met before the
            alert
            fires. Must be at least 1. For example, a value of 3 with a 1-minute interval means
            the condition must hold for 3 consecutive minutes before an incident is opened.
        condition (AnalyticsAlertControlPlaneModelsAlertConditionInput): The threshold condition for an alert. Specifies
            the comparison operator, threshold value,
            and how the metric value is derived before comparison.

            On create, `operator`, `threshold`, and `evaluationMode` are all required.
            On update (PATCH), the entire `condition` object is optional; when included, any
            sub-field can be omitted to keep its current value.

            `periodOffsetMultiplier` only applies when `evaluationMode` is
            `PeriodOverPeriod`. It is ignored for `Absolute` conditions.
        description (None | str | Unset): Optional free-text description of the alert's purpose.
        breakdown (list[AnalyticsAlertControlPlaneModelsAlertQueryBreakdown] | None | Unset): Optional grouping
            dimensions for the metric query. When set, the alert evaluates
            the metric independently for each combination of dimension values and fires if any
            group breaches the condition.
        filter_ (list[AnalyticsAlertControlPlaneModelsAlertQueryFilter] | None | Unset): Optional dimension filters
            applied to the metric query. Each entry restricts the metric
            to rows where the specified dimension matches one of the given values.
        webhook_receiver_config (AlertStorageWebhookReceiverConfig | Unset): Webhook notification settings for an alert.
            When set, each webhook in the
            `receivers` list will be called whenever the alert fires or resolves.
            Set to `null` to disable webhook notifications for the alert.
    """

    name: str
    metric: str
    severity: AlertStorageSeverity
    interval: AlertStorageAlertInterval
    consecutive_occurrences: int
    condition: AnalyticsAlertControlPlaneModelsAlertConditionInput
    description: None | str | Unset = UNSET
    breakdown: list[AnalyticsAlertControlPlaneModelsAlertQueryBreakdown] | None | Unset = UNSET
    filter_: list[AnalyticsAlertControlPlaneModelsAlertQueryFilter] | None | Unset = UNSET
    webhook_receiver_config: AlertStorageWebhookReceiverConfig | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        metric = self.metric

        severity = self.severity.value

        interval = self.interval.value

        consecutive_occurrences = self.consecutive_occurrences

        condition = self.condition.to_dict()

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

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

        webhook_receiver_config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.webhook_receiver_config, Unset):
            webhook_receiver_config = self.webhook_receiver_config.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "name": name,
                "metric": metric,
                "severity": severity,
                "interval": interval,
                "consecutiveOccurrences": consecutive_occurrences,
                "condition": condition,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if breakdown is not UNSET:
            field_dict["breakdown"] = breakdown
        if filter_ is not UNSET:
            field_dict["filter"] = filter_
        if webhook_receiver_config is not UNSET:
            field_dict["webhookReceiverConfig"] = webhook_receiver_config

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.alert_storage_webhook_receiver_config import AlertStorageWebhookReceiverConfig
        from ..models.analytics_alert_control_plane_models_alert_condition_input import (
            AnalyticsAlertControlPlaneModelsAlertConditionInput,
        )
        from ..models.analytics_alert_control_plane_models_alert_query_breakdown import (
            AnalyticsAlertControlPlaneModelsAlertQueryBreakdown,
        )
        from ..models.analytics_alert_control_plane_models_alert_query_filter import (
            AnalyticsAlertControlPlaneModelsAlertQueryFilter,
        )

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        name = d.pop("name")

        metric = d.pop("metric")

        severity = AlertStorageSeverity(d.pop("severity"))

        interval = AlertStorageAlertInterval(d.pop("interval"))

        consecutive_occurrences = d.pop("consecutiveOccurrences")

        condition = AnalyticsAlertControlPlaneModelsAlertConditionInput.from_dict(d.pop("condition"))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

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

        _webhook_receiver_config = d.pop("webhookReceiverConfig", UNSET)
        webhook_receiver_config: AlertStorageWebhookReceiverConfig | Unset
        if isinstance(_webhook_receiver_config, Unset):
            webhook_receiver_config = UNSET
        else:
            webhook_receiver_config = AlertStorageWebhookReceiverConfig.from_dict(_webhook_receiver_config)

        analytics_alert_control_plane_models_create_alert_config_request = cls(
            name=name,
            metric=metric,
            severity=severity,
            interval=interval,
            consecutive_occurrences=consecutive_occurrences,
            condition=condition,
            description=description,
            breakdown=breakdown,
            filter_=filter_,
            webhook_receiver_config=webhook_receiver_config,
        )

        return analytics_alert_control_plane_models_create_alert_config_request
