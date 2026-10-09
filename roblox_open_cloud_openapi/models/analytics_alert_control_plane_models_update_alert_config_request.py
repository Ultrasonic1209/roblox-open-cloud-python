from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.alert_storage_alert_config_state import AlertStorageAlertConfigState
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


T = TypeVar("T", bound="AnalyticsAlertControlPlaneModelsUpdateAlertConfigRequest")


@_attrs_define
class AnalyticsAlertControlPlaneModelsUpdateAlertConfigRequest:
    """Request body for partially updating an alert configuration (PATCH semantics). All fields
    are optional; only the fields present in the request body are updated.

        Attributes:
            name (None | str | Unset): New display name for the alert. Must be unique within the resource. Subject to
                Roblox text-moderation policies.
            metric (None | str | Unset): New metric name this alert should evaluate.
            description (None | str | Unset): New free-text description of the alert's purpose.
            severity (AlertStorageSeverity | Unset): Severity level assigned to an alert configuration.

                SEV_0

                SEV_1

                SEV_2
            interval (AlertStorageAlertInterval | Unset): How frequently an alert condition is evaluated.

                OneMinute

                HalfHour

                OneHour

                OneDay
            consecutive_occurrences (int | None | Unset): New consecutive-occurrences count. When set, the alert will
                require the condition to
                hold for this many consecutive evaluation periods before firing. Must be at least 1.
            breakdown (list[AnalyticsAlertControlPlaneModelsAlertQueryBreakdown] | None | Unset): New grouping dimensions
                for the metric query. Replaces the existing breakdown entirely
                when provided.
            filter_ (list[AnalyticsAlertControlPlaneModelsAlertQueryFilter] | None | Unset): New dimension filters for the
                metric query. Replaces the existing filter list entirely
                when provided.
            condition (AnalyticsAlertControlPlaneModelsAlertConditionInput | Unset): The threshold condition for an alert.
                Specifies the comparison operator, threshold value,
                and how the metric value is derived before comparison.

                On create, `operator`, `threshold`, and `evaluationMode` are all required.
                On update (PATCH), the entire `condition` object is optional; when included, any
                sub-field can be omitted to keep its current value.

                `periodOffsetMultiplier` only applies when `evaluationMode` is
                `PeriodOverPeriod`. It is ignored for `Absolute` conditions.
            webhook_receiver_config (AlertStorageWebhookReceiverConfig | Unset): Webhook notification settings for an alert.
                When set, each webhook in the
                `receivers` list will be called whenever the alert fires or resolves.
                Set to `null` to disable webhook notifications for the alert.
            config_state (AlertStorageAlertConfigState | Unset): The current lifecycle state of an alert configuration.

                Enabled

                Disabled

                PausedByRoblox

                Syncing

                Error
    """

    name: None | str | Unset = UNSET
    metric: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    severity: AlertStorageSeverity | Unset = UNSET
    interval: AlertStorageAlertInterval | Unset = UNSET
    consecutive_occurrences: int | None | Unset = UNSET
    breakdown: list[AnalyticsAlertControlPlaneModelsAlertQueryBreakdown] | None | Unset = UNSET
    filter_: list[AnalyticsAlertControlPlaneModelsAlertQueryFilter] | None | Unset = UNSET
    condition: AnalyticsAlertControlPlaneModelsAlertConditionInput | Unset = UNSET
    webhook_receiver_config: AlertStorageWebhookReceiverConfig | Unset = UNSET
    config_state: AlertStorageAlertConfigState | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        metric: None | str | Unset
        if isinstance(self.metric, Unset):
            metric = UNSET
        else:
            metric = self.metric

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        severity: str | Unset = UNSET
        if not isinstance(self.severity, Unset):
            severity = self.severity.value

        interval: str | Unset = UNSET
        if not isinstance(self.interval, Unset):
            interval = self.interval.value

        consecutive_occurrences: int | None | Unset
        if isinstance(self.consecutive_occurrences, Unset):
            consecutive_occurrences = UNSET
        else:
            consecutive_occurrences = self.consecutive_occurrences

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

        condition: dict[str, Any] | Unset = UNSET
        if not isinstance(self.condition, Unset):
            condition = self.condition.to_dict()

        webhook_receiver_config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.webhook_receiver_config, Unset):
            webhook_receiver_config = self.webhook_receiver_config.to_dict()

        config_state: str | Unset = UNSET
        if not isinstance(self.config_state, Unset):
            config_state = self.config_state.value

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if metric is not UNSET:
            field_dict["metric"] = metric
        if description is not UNSET:
            field_dict["description"] = description
        if severity is not UNSET:
            field_dict["severity"] = severity
        if interval is not UNSET:
            field_dict["interval"] = interval
        if consecutive_occurrences is not UNSET:
            field_dict["consecutiveOccurrences"] = consecutive_occurrences
        if breakdown is not UNSET:
            field_dict["breakdown"] = breakdown
        if filter_ is not UNSET:
            field_dict["filter"] = filter_
        if condition is not UNSET:
            field_dict["condition"] = condition
        if webhook_receiver_config is not UNSET:
            field_dict["webhookReceiverConfig"] = webhook_receiver_config
        if config_state is not UNSET:
            field_dict["configState"] = config_state

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

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_metric(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        metric = _parse_metric(d.pop("metric", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        _severity = d.pop("severity", UNSET)
        severity: AlertStorageSeverity | Unset
        if isinstance(_severity, Unset):
            severity = UNSET
        else:
            severity = AlertStorageSeverity(_severity)

        _interval = d.pop("interval", UNSET)
        interval: AlertStorageAlertInterval | Unset
        if isinstance(_interval, Unset):
            interval = UNSET
        else:
            interval = AlertStorageAlertInterval(_interval)

        def _parse_consecutive_occurrences(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        consecutive_occurrences = _parse_consecutive_occurrences(d.pop("consecutiveOccurrences", UNSET))

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

        _condition = d.pop("condition", UNSET)
        condition: AnalyticsAlertControlPlaneModelsAlertConditionInput | Unset
        if isinstance(_condition, Unset):
            condition = UNSET
        else:
            condition = AnalyticsAlertControlPlaneModelsAlertConditionInput.from_dict(_condition)

        _webhook_receiver_config = d.pop("webhookReceiverConfig", UNSET)
        webhook_receiver_config: AlertStorageWebhookReceiverConfig | Unset
        if isinstance(_webhook_receiver_config, Unset):
            webhook_receiver_config = UNSET
        else:
            webhook_receiver_config = AlertStorageWebhookReceiverConfig.from_dict(_webhook_receiver_config)

        _config_state = d.pop("configState", UNSET)
        config_state: AlertStorageAlertConfigState | Unset
        if isinstance(_config_state, Unset):
            config_state = UNSET
        else:
            config_state = AlertStorageAlertConfigState(_config_state)

        analytics_alert_control_plane_models_update_alert_config_request = cls(
            name=name,
            metric=metric,
            description=description,
            severity=severity,
            interval=interval,
            consecutive_occurrences=consecutive_occurrences,
            breakdown=breakdown,
            filter_=filter_,
            condition=condition,
            webhook_receiver_config=webhook_receiver_config,
            config_state=config_state,
        )

        return analytics_alert_control_plane_models_update_alert_config_request
