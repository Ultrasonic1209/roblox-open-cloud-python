from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.benchmark_type import BenchmarkType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.breakdown_filter import BreakdownFilter


T = TypeVar("T", bound="BenchmarkQuery")


@_attrs_define
class BenchmarkQuery:
    """BenchmarkQuery is the request object for the benchmark query.

    Attributes:
        metric (str | Unset): The metric to benchmark, such as `ForwardD1Retention`, using the same metric names as the
            Analytics Query API. Metrics without benchmark data return no data points.
        start_time (str | Unset): The start of the date range, inclusive. Required. Each benchmark value has a midnight
            UTC date, so a
            start time later in the day excludes that day.
        end_time (str | Unset): The end of the date range, inclusive. Required. For
            `/v1/universes/{universe_id}/benchmarks`, it must
            not be earlier than `start_time`, and must be at most 400 days after it.
        filter_ (list[BreakdownFilter] | Unset): Dimension filters. Only applied to `BENCHMARK_TYPE_TOP_EXPERIENCES`
            benchmarks, and ignored
            otherwise. Filter values without benchmark data return no data points.
        benchmark_type (BenchmarkType | Unset): BenchmarkType is to store the type of benchmark.
            `BENCHMARK_TYPE_SIMILARITY` compares against experiences with similar players.
            `BENCHMARK_TYPE_GENRE` compares against experiences in the same genre, or against all experiences
            when the universe has no genre or its genre doesn't qualify for genre benchmarks.
            `BENCHMARK_TYPE_TOP_EXPERIENCES` compares against the top experiences on Roblox, and is the only type
            for `DailyActiveUsers`, `DailyRevenue`, `MonthlyActiveUsers`, `PayingUsers`, `TotalPlayTimeHours`,
            `UniqueAbuseReportSubmittersPer1000PlaytimeHours`, and `Visits`.
        percentiles (list[int] | Unset): The percentiles to return, each between 0 and 100, with at most 10 values.
            Defaults to 50 and 90,
            or 10 and 50 when lower values are favorable. Percentiles without benchmark data return no data
            points. Ignored for `BENCHMARK_TYPE_TOP_EXPERIENCES` benchmarks, which return a single percentile
            chosen from the universe's own average over the last 30 days, or a fixed percentile for some metrics.
        benchmark_variant_id (str | Unset): The metric variant to benchmark. The only supported value is `l7_average`,
            which benchmarks the
            7-day rolling average of `metric`. Not every metric has this variant, and the API rejects requests
            for metrics without it. Omit to benchmark `metric` itself.
    """

    metric: str | Unset = UNSET
    start_time: str | Unset = UNSET
    end_time: str | Unset = UNSET
    filter_: list[BreakdownFilter] | Unset = UNSET
    benchmark_type: BenchmarkType | Unset = UNSET
    percentiles: list[int] | Unset = UNSET
    benchmark_variant_id: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        metric = self.metric

        start_time = self.start_time

        end_time = self.end_time

        filter_: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.filter_, Unset):
            filter_ = []
            for filter_item_data in self.filter_:
                filter_item = filter_item_data.to_dict()
                filter_.append(filter_item)

        benchmark_type: str | Unset = UNSET
        if not isinstance(self.benchmark_type, Unset):
            benchmark_type = self.benchmark_type.value

        percentiles: list[int] | Unset = UNSET
        if not isinstance(self.percentiles, Unset):
            percentiles = self.percentiles

        benchmark_variant_id = self.benchmark_variant_id

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if metric is not UNSET:
            field_dict["metric"] = metric
        if start_time is not UNSET:
            field_dict["startTime"] = start_time
        if end_time is not UNSET:
            field_dict["endTime"] = end_time
        if filter_ is not UNSET:
            field_dict["filter"] = filter_
        if benchmark_type is not UNSET:
            field_dict["benchmarkType"] = benchmark_type
        if percentiles is not UNSET:
            field_dict["percentiles"] = percentiles
        if benchmark_variant_id is not UNSET:
            field_dict["benchmarkVariantId"] = benchmark_variant_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.breakdown_filter import BreakdownFilter  # noqa: PLC0415

        d = dict(src_dict)
        metric = d.pop("metric", UNSET)

        start_time = d.pop("startTime", UNSET)

        end_time = d.pop("endTime", UNSET)

        _filter_ = d.pop("filter", UNSET)
        filter_: list[BreakdownFilter] | Unset = UNSET
        if _filter_ is not UNSET:
            filter_ = []
            for filter_item_data in _filter_:
                filter_item = BreakdownFilter.from_dict(filter_item_data)

                filter_.append(filter_item)

        _benchmark_type = d.pop("benchmarkType", UNSET)
        benchmark_type: BenchmarkType | Unset
        if isinstance(_benchmark_type, Unset):
            benchmark_type = UNSET
        else:
            benchmark_type = BenchmarkType(_benchmark_type)

        percentiles = cast(list[int], d.pop("percentiles", UNSET))

        benchmark_variant_id = d.pop("benchmarkVariantId", UNSET)

        benchmark_query = cls(
            metric=metric,
            start_time=start_time,
            end_time=end_time,
            filter_=filter_,
            benchmark_type=benchmark_type,
            percentiles=percentiles,
            benchmark_variant_id=benchmark_variant_id,
        )

        return benchmark_query
