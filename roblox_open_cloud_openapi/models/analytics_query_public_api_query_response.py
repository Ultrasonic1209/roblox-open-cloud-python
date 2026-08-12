from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.analytics_query_public_api_metric_value import AnalyticsQueryPublicApiMetricValue


T = TypeVar("T", bound="AnalyticsQueryPublicApiQueryResponse")


@_attrs_define
class AnalyticsQueryPublicApiQueryResponse:
    """The response for a metric query.

    Attributes:
        values (list[AnalyticsQueryPublicApiMetricValue] | Unset): The metric values returned by the query.
    """

    values: list[AnalyticsQueryPublicApiMetricValue] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        values: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.values, Unset):
            values = []
            for values_item_data in self.values:
                values_item = values_item_data.to_dict()
                values.append(values_item)

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if values is not UNSET:
            field_dict["values"] = values

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.analytics_query_public_api_metric_value import AnalyticsQueryPublicApiMetricValue

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        _values = d.pop("values", UNSET)
        values: list[AnalyticsQueryPublicApiMetricValue] | Unset = UNSET
        if _values is not UNSET:
            values = []
            for values_item_data in _values:
                values_item = AnalyticsQueryPublicApiMetricValue.from_dict(values_item_data)

                values.append(values_item)

        analytics_query_public_api_query_response = cls(
            values=values,
        )

        return analytics_query_public_api_query_response
