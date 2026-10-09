from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.analytics_alert_control_plane_models_firing_dimension_response import (
        AnalyticsAlertControlPlaneModelsFiringDimensionResponse,
    )


T = TypeVar("T", bound="AnalyticsAlertControlPlaneModelsFiringConditionResponse")


@_attrs_define
class AnalyticsAlertControlPlaneModelsFiringConditionResponse:
    """A single metric value that breached the alert threshold, optionally scoped to a specific
    dimension value when the alert uses a breakdown.

        Attributes:
            firing_value (float): The metric value that exceeded the threshold at the time of evaluation.
            firing_dimension (AnalyticsAlertControlPlaneModelsFiringDimensionResponse | Unset): A dimension name/value pair
                that identifies which slice of the metric was firing.
    """

    firing_value: float
    firing_dimension: AnalyticsAlertControlPlaneModelsFiringDimensionResponse | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        firing_value = self.firing_value

        firing_dimension: dict[str, Any] | Unset = UNSET
        if not isinstance(self.firing_dimension, Unset):
            firing_dimension = self.firing_dimension.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "firingValue": firing_value,
            }
        )
        if firing_dimension is not UNSET:
            field_dict["firingDimension"] = firing_dimension

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.analytics_alert_control_plane_models_firing_dimension_response import (
            AnalyticsAlertControlPlaneModelsFiringDimensionResponse,
        )

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        firing_value = d.pop("firingValue")

        _firing_dimension = d.pop("firingDimension", UNSET)
        firing_dimension: AnalyticsAlertControlPlaneModelsFiringDimensionResponse | Unset
        if isinstance(_firing_dimension, Unset):
            firing_dimension = UNSET
        else:
            firing_dimension = AnalyticsAlertControlPlaneModelsFiringDimensionResponse.from_dict(_firing_dimension)

        analytics_alert_control_plane_models_firing_condition_response = cls(
            firing_value=firing_value,
            firing_dimension=firing_dimension,
        )

        return analytics_alert_control_plane_models_firing_condition_response
