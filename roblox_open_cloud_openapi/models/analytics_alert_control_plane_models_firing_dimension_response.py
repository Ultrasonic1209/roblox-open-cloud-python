from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="AnalyticsAlertControlPlaneModelsFiringDimensionResponse")


@_attrs_define
class AnalyticsAlertControlPlaneModelsFiringDimensionResponse:
    """A dimension name/value pair that identifies which slice of the metric was firing.

    Attributes:
        dimension (str): Name of the dimension (e.g. `platform`).
        value (str): Value of the dimension for the slice that was firing (e.g. `Mobile`).
    """

    dimension: str
    value: str

    def to_dict(self) -> dict[str, Any]:
        dimension = self.dimension

        value = self.value

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "dimension": dimension,
                "value": value,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        dimension = d.pop("dimension")

        value = d.pop("value")

        analytics_alert_control_plane_models_firing_dimension_response = cls(
            dimension=dimension,
            value=value,
        )

        return analytics_alert_control_plane_models_firing_dimension_response
