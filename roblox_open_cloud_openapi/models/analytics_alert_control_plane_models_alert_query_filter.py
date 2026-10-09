from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="AnalyticsAlertControlPlaneModelsAlertQueryFilter")


@_attrs_define
class AnalyticsAlertControlPlaneModelsAlertQueryFilter:
    """A dimension filter applied to the metric query. Restricts the metric to rows where the
    specified dimension matches one of the given values.

        Attributes:
            dimension (str): Name of the dimension to filter on (e.g. `platform`).
            values (list[str]): The allowed values for this dimension. A metric data point is included only if its
                dimension value is in this list.
    """

    dimension: str
    values: list[str]

    def to_dict(self) -> dict[str, Any]:
        dimension = self.dimension

        values = self.values

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "dimension": dimension,
                "values": values,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        dimension = d.pop("dimension")

        values = cast(list[str], d.pop("values"))

        analytics_alert_control_plane_models_alert_query_filter = cls(
            dimension=dimension,
            values=values,
        )

        return analytics_alert_control_plane_models_alert_query_filter
