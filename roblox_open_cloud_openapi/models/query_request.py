from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.metric_granularity import MetricGranularity
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.query_filter import QueryFilter


T = TypeVar("T", bound="QueryRequest")


@_attrs_define
class QueryRequest:
    """A request to query time series metric data.

    Attributes:
        metric (str): The metric to query.
        granularity (MetricGranularity): The time granularity of metric data points in a query.
        start_time (datetime.datetime): The inclusive start of the query time range. Any UTC offset is accepted; results
            are always bucketed in UTC.
        end_time (datetime.datetime): The exclusive end of the query time range. Any UTC offset is accepted; results are
            always bucketed in UTC.
        breakdown (list[str] | Unset): The dimensions to group results by. Each entry is a single dimension name.
        filter_ (list[QueryFilter] | Unset): Filters to apply to the query.
        limit (int | Unset): The maximum number of breakdown series to return.
    """

    metric: str
    granularity: MetricGranularity
    start_time: datetime.datetime
    end_time: datetime.datetime
    breakdown: list[str] | Unset = UNSET
    filter_: list[QueryFilter] | Unset = UNSET
    limit: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        metric = self.metric

        granularity = self.granularity.value

        start_time = self.start_time.isoformat()

        end_time = self.end_time.isoformat()

        breakdown: list[str] | Unset = UNSET
        if not isinstance(self.breakdown, Unset):
            breakdown = self.breakdown

        filter_: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.filter_, Unset):
            filter_ = []
            for filter_item_data in self.filter_:
                filter_item = filter_item_data.to_dict()
                filter_.append(filter_item)

        limit = self.limit

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "metric": metric,
                "granularity": granularity,
                "startTime": start_time,
                "endTime": end_time,
            }
        )
        if breakdown is not UNSET:
            field_dict["breakdown"] = breakdown
        if filter_ is not UNSET:
            field_dict["filter"] = filter_
        if limit is not UNSET:
            field_dict["limit"] = limit

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.query_filter import QueryFilter

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        metric = d.pop("metric")

        granularity = MetricGranularity(d.pop("granularity"))

        start_time = datetime.datetime.fromisoformat(d.pop("startTime"))

        end_time = datetime.datetime.fromisoformat(d.pop("endTime"))

        breakdown = cast(list[str], d.pop("breakdown", UNSET))

        _filter_ = d.pop("filter", UNSET)
        filter_: list[QueryFilter] | Unset = UNSET
        if _filter_ is not UNSET:
            filter_ = []
            for filter_item_data in _filter_:
                filter_item = QueryFilter.from_dict(filter_item_data)

                filter_.append(filter_item)

        limit = d.pop("limit", UNSET)

        query_request = cls(
            metric=metric,
            granularity=granularity,
            start_time=start_time,
            end_time=end_time,
            breakdown=breakdown,
            filter_=filter_,
            limit=limit,
        )

        return query_request
