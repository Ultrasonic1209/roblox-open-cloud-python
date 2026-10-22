from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..models.benchmark_objective import BenchmarkObjective
from ..models.benchmark_type import BenchmarkType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.query_benchmark_result import QueryBenchmarkResult


T = TypeVar("T", bound="QueryUniverseBenchmarkResponse")


@_attrs_define
class QueryUniverseBenchmarkResponse:
    """QueryUniverseBenchmarkResponse is the response message for QueryUniverseBenchmark.

    Attributes:
        result (QueryBenchmarkResult | Unset): QueryBenchmarkResult is the response object for the benchmark query.
        available_types (list[BenchmarkType] | Unset): The benchmark types available for this universe and metric.
            Request one with `benchmark_type`.
        objective (BenchmarkObjective | Unset): BenchmarkObjective describes which direction is favorable for a metric.
    """

    result: QueryBenchmarkResult | Unset = UNSET
    available_types: list[BenchmarkType] | Unset = UNSET
    objective: BenchmarkObjective | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        result: dict[str, Any] | Unset = UNSET
        if not isinstance(self.result, Unset):
            result = self.result.to_dict()

        available_types: list[str] | Unset = UNSET
        if not isinstance(self.available_types, Unset):
            available_types = []
            for available_types_item_data in self.available_types:
                available_types_item = available_types_item_data.value
                available_types.append(available_types_item)

        objective: str | Unset = UNSET
        if not isinstance(self.objective, Unset):
            objective = self.objective.value

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if result is not UNSET:
            field_dict["result"] = result
        if available_types is not UNSET:
            field_dict["availableTypes"] = available_types
        if objective is not UNSET:
            field_dict["objective"] = objective

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.query_benchmark_result import QueryBenchmarkResult  # noqa: PLC0415

        d = dict(src_dict)
        _result = d.pop("result", UNSET)
        result: QueryBenchmarkResult | Unset
        if isinstance(_result, Unset):
            result = UNSET
        else:
            result = QueryBenchmarkResult.from_dict(_result)

        _available_types = d.pop("availableTypes", UNSET)
        available_types: list[BenchmarkType] | Unset = UNSET
        if _available_types is not UNSET:
            available_types = []
            for available_types_item_data in _available_types:
                available_types_item = BenchmarkType(available_types_item_data)

                available_types.append(available_types_item)

        _objective = d.pop("objective", UNSET)
        objective: BenchmarkObjective | Unset
        if isinstance(_objective, Unset):
            objective = UNSET
        else:
            objective = BenchmarkObjective(_objective)

        query_universe_benchmark_response = cls(
            result=result,
            available_types=available_types,
            objective=objective,
        )

        return query_universe_benchmark_response
