from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.alert_storage_alert_config_state import AlertStorageAlertConfigState
from ..models.alert_storage_alert_interval import AlertStorageAlertInterval
from ..models.alert_storage_firing_status import AlertStorageFiringStatus
from ..models.alert_storage_resource_type import AlertStorageResourceType
from ..models.alert_storage_severity import AlertStorageSeverity
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.alert_storage_alert_condition import AlertStorageAlertCondition
    from ..models.alert_storage_webhook_receiver_config import AlertStorageWebhookReceiverConfig
    from ..models.analytics_alert_control_plane_models_alert_query_breakdown import (
        AnalyticsAlertControlPlaneModelsAlertQueryBreakdown,
    )
    from ..models.analytics_alert_control_plane_models_alert_query_filter import (
        AnalyticsAlertControlPlaneModelsAlertQueryFilter,
    )


T = TypeVar("T", bound="AnalyticsAlertControlPlaneModelsAlertDetailResponse")


@_attrs_define
class AnalyticsAlertControlPlaneModelsAlertDetailResponse:
    """Full details of a saved alert configuration.

    Attributes:
        alert_id (str): Unique identifier of the alert configuration (string-encoded 64-bit integer).
        resource_type (AlertStorageResourceType): The type of resource an alert is attached to.

            Universe
        resource_id (str): Numeric ID of the resource this alert monitors (e.g. the universe ID).
        name (str): Display name of the alert. Must be unique within the resource.
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
        consecutive_occurrences (int): Number of consecutive evaluation periods the condition must be met before the
            alert fires.
            Must be at least 1. For example, a value of 3 with a 1-minute interval means the condition
            must hold for 3 consecutive minutes before an incident is opened.
        condition (AlertStorageAlertCondition): The threshold condition that determines when an alert fires.
        config_state (AlertStorageAlertConfigState): The current lifecycle state of an alert configuration.

            Enabled

            Disabled

            PausedByRoblox

            Syncing

            Error
        firing_status (AlertStorageFiringStatus): Whether an alert is currently in a firing or resolved state.

            OK

            Firing
        created_at (datetime.datetime): Timestamp when this alert configuration was created (UTC).
        last_modified_at (datetime.datetime): Timestamp of the most recent modification to this alert configuration
            (UTC).
        description (None | str | Unset): Optional free-text description of the alert's purpose.
        filter_ (list[AnalyticsAlertControlPlaneModelsAlertQueryFilter] | None | Unset): Optional dimension filters
            applied to the metric query. Each entry restricts the metric
            to rows where the specified dimension matches one of the given values.
        breakdown (list[AnalyticsAlertControlPlaneModelsAlertQueryBreakdown] | None | Unset): Optional grouping
            dimensions for the metric query. When set, the alert evaluates
            the metric independently for each combination of dimension values and fires if any
            group breaches the condition.
        webhook_receiver_config (AlertStorageWebhookReceiverConfig | Unset): Webhook notification settings for an alert.
            When set, each webhook in the
            `receivers` list will be called whenever the alert fires or resolves.
            Set to `null` to disable webhook notifications for the alert.
        last_fired_at (datetime.datetime | None | Unset): Timestamp of the most recent firing event. `null` if the alert
            has never fired.
        last_modified_by (None | str | Unset): ID of the user who last modified this alert configuration.
            `null` if the last modification was made by the system.
    """

    alert_id: str
    resource_type: AlertStorageResourceType
    resource_id: str
    name: str
    metric: str
    severity: AlertStorageSeverity
    interval: AlertStorageAlertInterval
    consecutive_occurrences: int
    condition: AlertStorageAlertCondition
    config_state: AlertStorageAlertConfigState
    firing_status: AlertStorageFiringStatus
    created_at: datetime.datetime
    last_modified_at: datetime.datetime
    description: None | str | Unset = UNSET
    filter_: list[AnalyticsAlertControlPlaneModelsAlertQueryFilter] | None | Unset = UNSET
    breakdown: list[AnalyticsAlertControlPlaneModelsAlertQueryBreakdown] | None | Unset = UNSET
    webhook_receiver_config: AlertStorageWebhookReceiverConfig | Unset = UNSET
    last_fired_at: datetime.datetime | None | Unset = UNSET
    last_modified_by: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        alert_id = self.alert_id

        resource_type = self.resource_type.value

        resource_id = self.resource_id

        name = self.name

        metric = self.metric

        severity = self.severity.value

        interval = self.interval.value

        consecutive_occurrences = self.consecutive_occurrences

        condition = self.condition.to_dict()

        config_state = self.config_state.value

        firing_status = self.firing_status.value

        created_at = self.created_at.isoformat()

        last_modified_at = self.last_modified_at.isoformat()

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

        webhook_receiver_config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.webhook_receiver_config, Unset):
            webhook_receiver_config = self.webhook_receiver_config.to_dict()

        last_fired_at: None | str | Unset
        if isinstance(self.last_fired_at, Unset):
            last_fired_at = UNSET
        elif isinstance(self.last_fired_at, datetime.datetime):
            last_fired_at = self.last_fired_at.isoformat()
        else:
            last_fired_at = self.last_fired_at

        last_modified_by: None | str | Unset
        if isinstance(self.last_modified_by, Unset):
            last_modified_by = UNSET
        else:
            last_modified_by = self.last_modified_by

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "alertId": alert_id,
                "resourceType": resource_type,
                "resourceId": resource_id,
                "name": name,
                "metric": metric,
                "severity": severity,
                "interval": interval,
                "consecutiveOccurrences": consecutive_occurrences,
                "condition": condition,
                "configState": config_state,
                "firingStatus": firing_status,
                "createdAt": created_at,
                "lastModifiedAt": last_modified_at,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if filter_ is not UNSET:
            field_dict["filter"] = filter_
        if breakdown is not UNSET:
            field_dict["breakdown"] = breakdown
        if webhook_receiver_config is not UNSET:
            field_dict["webhookReceiverConfig"] = webhook_receiver_config
        if last_fired_at is not UNSET:
            field_dict["lastFiredAt"] = last_fired_at
        if last_modified_by is not UNSET:
            field_dict["lastModifiedBy"] = last_modified_by

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.alert_storage_alert_condition import AlertStorageAlertCondition
        from ..models.alert_storage_webhook_receiver_config import AlertStorageWebhookReceiverConfig
        from ..models.analytics_alert_control_plane_models_alert_query_breakdown import (
            AnalyticsAlertControlPlaneModelsAlertQueryBreakdown,
        )
        from ..models.analytics_alert_control_plane_models_alert_query_filter import (
            AnalyticsAlertControlPlaneModelsAlertQueryFilter,
        )

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        alert_id = d.pop("alertId")

        resource_type = AlertStorageResourceType(d.pop("resourceType"))

        resource_id = d.pop("resourceId")

        name = d.pop("name")

        metric = d.pop("metric")

        severity = AlertStorageSeverity(d.pop("severity"))

        interval = AlertStorageAlertInterval(d.pop("interval"))

        consecutive_occurrences = d.pop("consecutiveOccurrences")

        condition = AlertStorageAlertCondition.from_dict(d.pop("condition"))

        config_state = AlertStorageAlertConfigState(d.pop("configState"))

        firing_status = AlertStorageFiringStatus(d.pop("firingStatus"))

        created_at = datetime.datetime.fromisoformat(d.pop("createdAt"))

        last_modified_at = datetime.datetime.fromisoformat(d.pop("lastModifiedAt"))

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

        _webhook_receiver_config = d.pop("webhookReceiverConfig", UNSET)
        webhook_receiver_config: AlertStorageWebhookReceiverConfig | Unset
        if isinstance(_webhook_receiver_config, Unset):
            webhook_receiver_config = UNSET
        else:
            webhook_receiver_config = AlertStorageWebhookReceiverConfig.from_dict(_webhook_receiver_config)

        def _parse_last_fired_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_fired_at_type_0 = datetime.datetime.fromisoformat(data)

                return last_fired_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_fired_at = _parse_last_fired_at(d.pop("lastFiredAt", UNSET))

        def _parse_last_modified_by(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        last_modified_by = _parse_last_modified_by(d.pop("lastModifiedBy", UNSET))

        analytics_alert_control_plane_models_alert_detail_response = cls(
            alert_id=alert_id,
            resource_type=resource_type,
            resource_id=resource_id,
            name=name,
            metric=metric,
            severity=severity,
            interval=interval,
            consecutive_occurrences=consecutive_occurrences,
            condition=condition,
            config_state=config_state,
            firing_status=firing_status,
            created_at=created_at,
            last_modified_at=last_modified_at,
            description=description,
            filter_=filter_,
            breakdown=breakdown,
            webhook_receiver_config=webhook_receiver_config,
            last_fired_at=last_fired_at,
            last_modified_by=last_modified_by,
        )

        return analytics_alert_control_plane_models_alert_detail_response
