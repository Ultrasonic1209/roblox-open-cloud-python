from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.analytics_query_public_api_metric_granularity import AnalyticsQueryPublicApiMetricGranularity
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.analytics_query_public_api_query_filter import AnalyticsQueryPublicApiQueryFilter


T = TypeVar("T", bound="AnalyticsQueryPublicApiDimensionValuesRequest")


@_attrs_define
class AnalyticsQueryPublicApiDimensionValuesRequest:
    """A request to query dimension values.

    Attributes:
        metric (str): The metric that provides context for resolving dimension namespaces.
        start_time (datetime.datetime): The inclusive start of the query time range. Any UTC offset is accepted; results
            are always bucketed in UTC.
        end_time (datetime.datetime): The exclusive end of the query time range. Any UTC offset is accepted; results are
            always bucketed in UTC.
        dimensions (list[str] | Unset): The dimensions to retrieve values for. Each entry is a single dimension name.
        filter_ (list[AnalyticsQueryPublicApiQueryFilter] | Unset): Filters to apply to the query.
        granularity (AnalyticsQueryPublicApiMetricGranularity | Unset): The time granularity of metric data points in a
            query.
        limit (int | Unset): The maximum number of values to return per dimension.
    """

    metric: str
    start_time: datetime.datetime
    end_time: datetime.datetime
    dimensions: list[str] | Unset = UNSET
    filter_: list[AnalyticsQueryPublicApiQueryFilter] | Unset = UNSET
    granularity: AnalyticsQueryPublicApiMetricGranularity | Unset = UNSET
    limit: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        metric = self.metric

        start_time = self.start_time.isoformat()

        end_time = self.end_time.isoformat()

        dimensions: list[str] | Unset = UNSET
        if not isinstance(self.dimensions, Unset):
            dimensions = self.dimensions

        filter_: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.filter_, Unset):
            filter_ = []
            for filter_item_data in self.filter_:
                filter_item = filter_item_data.to_dict()
                filter_.append(filter_item)

        granularity: str | Unset = UNSET
        if not isinstance(self.granularity, Unset):
            granularity = self.granularity.value

        limit = self.limit

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "metric": metric,
                "startTime": start_time,
                "endTime": end_time,
            }
        )
        if dimensions is not UNSET:
            field_dict["dimensions"] = dimensions
        if filter_ is not UNSET:
            field_dict["filter"] = filter_
        if granularity is not UNSET:
            field_dict["granularity"] = granularity
        if limit is not UNSET:
            field_dict["limit"] = limit

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.analytics_query_public_api_query_filter import AnalyticsQueryPublicApiQueryFilter

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        metric = d.pop("metric")

        start_time = datetime.datetime.fromisoformat(d.pop("startTime"))

        end_time = datetime.datetime.fromisoformat(d.pop("endTime"))

        dimensions = cast(list[str], d.pop("dimensions", UNSET))

        _filter_ = d.pop("filter", UNSET)
        filter_: list[AnalyticsQueryPublicApiQueryFilter] | Unset = UNSET
        if _filter_ is not UNSET:
            filter_ = []
            for filter_item_data in _filter_:
                filter_item = AnalyticsQueryPublicApiQueryFilter.from_dict(filter_item_data)

                filter_.append(filter_item)

        _granularity = d.pop("granularity", UNSET)
        granularity: AnalyticsQueryPublicApiMetricGranularity | Unset
        if isinstance(_granularity, Unset):
            granularity = UNSET
        else:
            granularity = AnalyticsQueryPublicApiMetricGranularity(_granularity)

        limit = d.pop("limit", UNSET)

        analytics_query_public_api_dimension_values_request = cls(
            metric=metric,
            start_time=start_time,
            end_time=end_time,
            dimensions=dimensions,
            filter_=filter_,
            granularity=granularity,
            limit=limit,
        )

        return analytics_query_public_api_dimension_values_request
