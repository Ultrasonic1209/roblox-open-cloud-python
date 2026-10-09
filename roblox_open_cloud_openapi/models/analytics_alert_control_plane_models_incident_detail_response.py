from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.alert_storage_firing_status import AlertStorageFiringStatus
from ..models.alert_storage_resource_type import AlertStorageResourceType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.analytics_alert_control_plane_models_alert_config_summary import (
        AnalyticsAlertControlPlaneModelsAlertConfigSummary,
    )
    from ..models.analytics_alert_control_plane_models_firing_metadata_response import (
        AnalyticsAlertControlPlaneModelsFiringMetadataResponse,
    )


T = TypeVar("T", bound="AnalyticsAlertControlPlaneModelsIncidentDetailResponse")


@_attrs_define
class AnalyticsAlertControlPlaneModelsIncidentDetailResponse:
    """Details of a single alert incident.

    Attributes:
        id (str): Unique identifier of this incident.
        resource_type (AlertStorageResourceType): The type of resource an alert is attached to.

            Universe
        resource_id (str): Numeric ID of the resource this incident belongs to (e.g. the universe ID).
        status (AlertStorageFiringStatus): Whether an alert is currently in a firing or resolved state.

            OK

            Firing
        opened_at (datetime.datetime): Timestamp when this incident was first opened (UTC).
        opened_window_start_at (datetime.datetime): Start of the evaluation window that first satisfied the alert
            condition and opened this
            incident (UTC).
        first_firing_metadata (AnalyticsAlertControlPlaneModelsFiringMetadataResponse): A snapshot of the alert
            condition at a specific evaluation, capturing the metric values
            that were firing and any dimension breakdowns involved.
        latest_firing_metadata (AnalyticsAlertControlPlaneModelsFiringMetadataResponse): A snapshot of the alert
            condition at a specific evaluation, capturing the metric values
            that were firing and any dimension breakdowns involved.
        alert_config (AnalyticsAlertControlPlaneModelsAlertConfigSummary): Key fields of the alert configuration that
            triggered an incident.
        resolved_at (datetime.datetime | None | Unset): Timestamp when this incident was resolved (UTC). `null` if the
            incident is still
            active.
        resolved_window_start_at (datetime.datetime | None | Unset): Start of the evaluation window in which the alert
            condition was no longer satisfied,
            causing the incident to be resolved (UTC). `null` if the incident is still active.
    """

    id: str
    resource_type: AlertStorageResourceType
    resource_id: str
    status: AlertStorageFiringStatus
    opened_at: datetime.datetime
    opened_window_start_at: datetime.datetime
    first_firing_metadata: AnalyticsAlertControlPlaneModelsFiringMetadataResponse
    latest_firing_metadata: AnalyticsAlertControlPlaneModelsFiringMetadataResponse
    alert_config: AnalyticsAlertControlPlaneModelsAlertConfigSummary
    resolved_at: datetime.datetime | None | Unset = UNSET
    resolved_window_start_at: datetime.datetime | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        resource_type = self.resource_type.value

        resource_id = self.resource_id

        status = self.status.value

        opened_at = self.opened_at.isoformat()

        opened_window_start_at = self.opened_window_start_at.isoformat()

        first_firing_metadata = self.first_firing_metadata.to_dict()

        latest_firing_metadata = self.latest_firing_metadata.to_dict()

        alert_config = self.alert_config.to_dict()

        resolved_at: None | str | Unset
        if isinstance(self.resolved_at, Unset):
            resolved_at = UNSET
        elif isinstance(self.resolved_at, datetime.datetime):
            resolved_at = self.resolved_at.isoformat()
        else:
            resolved_at = self.resolved_at

        resolved_window_start_at: None | str | Unset
        if isinstance(self.resolved_window_start_at, Unset):
            resolved_window_start_at = UNSET
        elif isinstance(self.resolved_window_start_at, datetime.datetime):
            resolved_window_start_at = self.resolved_window_start_at.isoformat()
        else:
            resolved_window_start_at = self.resolved_window_start_at

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "resourceType": resource_type,
                "resourceId": resource_id,
                "status": status,
                "openedAt": opened_at,
                "openedWindowStartAt": opened_window_start_at,
                "firstFiringMetadata": first_firing_metadata,
                "latestFiringMetadata": latest_firing_metadata,
                "alertConfig": alert_config,
            }
        )
        if resolved_at is not UNSET:
            field_dict["resolvedAt"] = resolved_at
        if resolved_window_start_at is not UNSET:
            field_dict["resolvedWindowStartAt"] = resolved_window_start_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.analytics_alert_control_plane_models_alert_config_summary import (
            AnalyticsAlertControlPlaneModelsAlertConfigSummary,
        )
        from ..models.analytics_alert_control_plane_models_firing_metadata_response import (
            AnalyticsAlertControlPlaneModelsFiringMetadataResponse,
        )

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        id = d.pop("id")

        resource_type = AlertStorageResourceType(d.pop("resourceType"))

        resource_id = d.pop("resourceId")

        status = AlertStorageFiringStatus(d.pop("status"))

        opened_at = datetime.datetime.fromisoformat(d.pop("openedAt"))

        opened_window_start_at = datetime.datetime.fromisoformat(d.pop("openedWindowStartAt"))

        first_firing_metadata = AnalyticsAlertControlPlaneModelsFiringMetadataResponse.from_dict(
            d.pop("firstFiringMetadata")
        )

        latest_firing_metadata = AnalyticsAlertControlPlaneModelsFiringMetadataResponse.from_dict(
            d.pop("latestFiringMetadata")
        )

        alert_config = AnalyticsAlertControlPlaneModelsAlertConfigSummary.from_dict(d.pop("alertConfig"))

        def _parse_resolved_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                resolved_at_type_0 = datetime.datetime.fromisoformat(data)

                return resolved_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        resolved_at = _parse_resolved_at(d.pop("resolvedAt", UNSET))

        def _parse_resolved_window_start_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                resolved_window_start_at_type_0 = datetime.datetime.fromisoformat(data)

                return resolved_window_start_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        resolved_window_start_at = _parse_resolved_window_start_at(d.pop("resolvedWindowStartAt", UNSET))

        analytics_alert_control_plane_models_incident_detail_response = cls(
            id=id,
            resource_type=resource_type,
            resource_id=resource_id,
            status=status,
            opened_at=opened_at,
            opened_window_start_at=opened_window_start_at,
            first_firing_metadata=first_firing_metadata,
            latest_firing_metadata=latest_firing_metadata,
            alert_config=alert_config,
            resolved_at=resolved_at,
            resolved_window_start_at=resolved_window_start_at,
        )

        return analytics_alert_control_plane_models_incident_detail_response
