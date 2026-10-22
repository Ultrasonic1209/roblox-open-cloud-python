from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.metric_value import MetricValue


T = TypeVar("T", bound="QueryBenchmarkResult")


@_attrs_define
class QueryBenchmarkResult:
    """QueryBenchmarkResult is the response object for the benchmark query.

    Attributes:
        values (list[MetricValue] | Unset): The benchmark series, one per percentile.
    """

    values: list[MetricValue] | Unset = UNSET

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
        from ..models.metric_value import MetricValue  # noqa: PLC0415

        d = dict(src_dict)
        _values = d.pop("values", UNSET)
        values: list[MetricValue] | Unset = UNSET
        if _values is not UNSET:
            values = []
            for values_item_data in _values:
                values_item = MetricValue.from_dict(values_item_data)

                values.append(values_item)

        query_benchmark_result = cls(
            values=values,
        )

        return query_benchmark_result
