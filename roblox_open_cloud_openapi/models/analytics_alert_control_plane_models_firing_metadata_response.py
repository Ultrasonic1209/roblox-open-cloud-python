from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.alert_storage_alert_condition import AlertStorageAlertCondition
    from ..models.analytics_alert_control_plane_models_alert_query_breakdown import (
        AnalyticsAlertControlPlaneModelsAlertQueryBreakdown,
    )
    from ..models.analytics_alert_control_plane_models_alert_query_filter import (
        AnalyticsAlertControlPlaneModelsAlertQueryFilter,
    )
    from ..models.analytics_alert_control_plane_models_firing_condition_response import (
        AnalyticsAlertControlPlaneModelsFiringConditionResponse,
    )


T = TypeVar("T", bound="AnalyticsAlertControlPlaneModelsFiringMetadataResponse")


@_attrs_define
class AnalyticsAlertControlPlaneModelsFiringMetadataResponse:
    """A snapshot of the alert condition at a specific evaluation, capturing the metric values
    that were firing and any dimension breakdowns involved.

        Attributes:
            condition (AlertStorageAlertCondition): The threshold condition that determines when an alert fires.
            firing_condition (list[AnalyticsAlertControlPlaneModelsFiringConditionResponse]): The specific metric values and
                dimension combinations that caused the condition to fire.
            filter_ (list[AnalyticsAlertControlPlaneModelsAlertQueryFilter] | None | Unset): Dimension filters that were
                active at this evaluation, if any.
            breakdown (list[AnalyticsAlertControlPlaneModelsAlertQueryBreakdown] | None | Unset): Grouping dimensions that
                were active at this evaluation, if any.
    """

    condition: AlertStorageAlertCondition
    firing_condition: list[AnalyticsAlertControlPlaneModelsFiringConditionResponse]
    filter_: list[AnalyticsAlertControlPlaneModelsAlertQueryFilter] | None | Unset = UNSET
    breakdown: list[AnalyticsAlertControlPlaneModelsAlertQueryBreakdown] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        condition = self.condition.to_dict()

        firing_condition = []
        for firing_condition_item_data in self.firing_condition:
            firing_condition_item = firing_condition_item_data.to_dict()
            firing_condition.append(firing_condition_item)

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
                "condition": condition,
                "firingCondition": firing_condition,
            }
        )
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
        from ..models.analytics_alert_control_plane_models_firing_condition_response import (
            AnalyticsAlertControlPlaneModelsFiringConditionResponse,
        )

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        condition = AlertStorageAlertCondition.from_dict(d.pop("condition"))

        firing_condition = []
        _firing_condition = d.pop("firingCondition")
        for firing_condition_item_data in _firing_condition:
            firing_condition_item = AnalyticsAlertControlPlaneModelsFiringConditionResponse.from_dict(
                firing_condition_item_data
            )

            firing_condition.append(firing_condition_item)

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

        analytics_alert_control_plane_models_firing_metadata_response = cls(
            condition=condition,
            firing_condition=firing_condition,
            filter_=filter_,
            breakdown=breakdown,
        )

        return analytics_alert_control_plane_models_firing_metadata_response
