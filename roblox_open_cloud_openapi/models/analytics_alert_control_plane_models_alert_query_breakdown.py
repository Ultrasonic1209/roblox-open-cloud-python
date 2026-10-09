from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="AnalyticsAlertControlPlaneModelsAlertQueryBreakdown")


@_attrs_define
class AnalyticsAlertControlPlaneModelsAlertQueryBreakdown:
    """A set of dimensions used to group the metric query. When a breakdown is specified, the
    alert evaluates each unique combination of dimension values independently and fires if any
    group breaches the condition.

        Attributes:
            dimensions (list[str]): Names of the dimensions to group by (e.g. `["platform", "age_bracket"]`).
    """

    dimensions: list[str]

    def to_dict(self) -> dict[str, Any]:
        dimensions = self.dimensions

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "dimensions": dimensions,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        dimensions = cast(list[str], d.pop("dimensions"))

        analytics_alert_control_plane_models_alert_query_breakdown = cls(
            dimensions=dimensions,
        )

        return analytics_alert_control_plane_models_alert_query_breakdown
