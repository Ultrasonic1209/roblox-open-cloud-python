from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.benchmark_type import BenchmarkType
from ..types import UNSET, Unset

T = TypeVar("T", bound="DataPointMetadata")


@_attrs_define
class DataPointMetadata:
    """DataPointMetadata metadata for a data point.

    Attributes:
        benchmark_type (BenchmarkType | Unset): BenchmarkType is to store the type of benchmark.
            `BENCHMARK_TYPE_SIMILARITY` compares against experiences with similar players.
            `BENCHMARK_TYPE_GENRE` compares against experiences in the same genre, or against all experiences
            when the universe has no genre or its genre doesn't qualify for genre benchmarks.
            `BENCHMARK_TYPE_TOP_EXPERIENCES` compares against the top experiences on Roblox, and is the only type
            for `DailyActiveUsers`, `DailyRevenue`, `MonthlyActiveUsers`, `PayingUsers`, `TotalPlayTimeHours`,
            `UniqueAbuseReportSubmittersPer1000PlaytimeHours`, and `Visits`.
        genre (str | Unset): The genre compared against, set for `BENCHMARK_TYPE_GENRE` data points. `general` means all
            experiences.
    """

    benchmark_type: BenchmarkType | Unset = UNSET
    genre: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        benchmark_type: str | Unset = UNSET
        if not isinstance(self.benchmark_type, Unset):
            benchmark_type = self.benchmark_type.value

        genre = self.genre

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if benchmark_type is not UNSET:
            field_dict["benchmarkType"] = benchmark_type
        if genre is not UNSET:
            field_dict["genre"] = genre

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _benchmark_type = d.pop("benchmarkType", UNSET)
        benchmark_type: BenchmarkType | Unset
        if isinstance(_benchmark_type, Unset):
            benchmark_type = UNSET
        else:
            benchmark_type = BenchmarkType(_benchmark_type)

        genre = d.pop("genre", UNSET)

        data_point_metadata = cls(
            benchmark_type=benchmark_type,
            genre=genre,
        )

        return data_point_metadata
