from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.analytics_query_public_api_filter_operation import AnalyticsQueryPublicApiFilterOperation
from ..types import UNSET, Unset

T = TypeVar("T", bound="AnalyticsQueryPublicApiQueryFilter")


@_attrs_define
class AnalyticsQueryPublicApiQueryFilter:
    """A filter applied to a query dimension.

    Attributes:
        dimension (str): The dimension name to filter on.
        operation (AnalyticsQueryPublicApiFilterOperation): The operation to apply to a query filter.
        values (list[str] | Unset): The values to filter by.
    """

    dimension: str
    operation: AnalyticsQueryPublicApiFilterOperation
    values: list[str] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        dimension = self.dimension

        operation = self.operation.value

        values: list[str] | Unset = UNSET
        if not isinstance(self.values, Unset):
            values = self.values

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "dimension": dimension,
                "operation": operation,
            }
        )
        if values is not UNSET:
            field_dict["values"] = values

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        dimension = d.pop("dimension")

        operation = AnalyticsQueryPublicApiFilterOperation(d.pop("operation"))

        values = cast(list[str], d.pop("values", UNSET))

        analytics_query_public_api_query_filter = cls(
            dimension=dimension,
            operation=operation,
            values=values,
        )

        return analytics_query_public_api_query_filter
