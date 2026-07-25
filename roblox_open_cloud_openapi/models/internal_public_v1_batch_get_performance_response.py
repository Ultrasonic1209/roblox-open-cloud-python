from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.internal_public_v1_batch_get_performance_response_period import (
    InternalPublicV1BatchGetPerformanceResponsePeriod,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.internal_public_v1_campaign_id_failure import InternalPublicV1CampaignIDFailure
    from ..models.internal_public_v1_campaign_performance import InternalPublicV1CampaignPerformance


T = TypeVar("T", bound="InternalPublicV1BatchGetPerformanceResponse")


@_attrs_define
class InternalPublicV1BatchGetPerformanceResponse:
    """
    Attributes:
        data_as_of (str | Unset): The time the metrics were current, as an RFC 3339 UTC timestamp.
        end_date (str | Unset): The last day of the window (inclusive), as YYYY-MM-DD in the account's time zone.
        failures (list[InternalPublicV1CampaignIDFailure] | Unset): The IDs that could not be resolved. Omitted when
            every ID resolved.
        period (InternalPublicV1BatchGetPerformanceResponsePeriod | Unset): The reporting window applied to every
            campaign. Can be `TODAY`, `YESTERDAY`,
            `LAST_7_DAYS`, `LAST_30_DAYS`, `THIS_MONTH`, `LAST_MONTH`, `YEAR_TO_DATE`, or `PREVIOUS_YEAR`.
        results (list[InternalPublicV1CampaignPerformance] | Unset): One entry per successfully resolved campaign.
        start_date (str | Unset): The first day of the window (inclusive), as YYYY-MM-DD in the account's time zone.
        time_zone (str | Unset): The IANA time zone the window and metrics are computed in.
    """

    data_as_of: str | Unset = UNSET
    end_date: str | Unset = UNSET
    failures: list[InternalPublicV1CampaignIDFailure] | Unset = UNSET
    period: InternalPublicV1BatchGetPerformanceResponsePeriod | Unset = UNSET
    results: list[InternalPublicV1CampaignPerformance] | Unset = UNSET
    start_date: str | Unset = UNSET
    time_zone: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data_as_of = self.data_as_of

        end_date = self.end_date

        failures: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.failures, Unset):
            failures = []
            for failures_item_data in self.failures:
                failures_item = failures_item_data.to_dict()
                failures.append(failures_item)

        period: str | Unset = UNSET
        if not isinstance(self.period, Unset):
            period = self.period.value

        results: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.results, Unset):
            results = []
            for results_item_data in self.results:
                results_item = results_item_data.to_dict()
                results.append(results_item)

        start_date = self.start_date

        time_zone = self.time_zone

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data_as_of is not UNSET:
            field_dict["dataAsOf"] = data_as_of
        if end_date is not UNSET:
            field_dict["endDate"] = end_date
        if failures is not UNSET:
            field_dict["failures"] = failures
        if period is not UNSET:
            field_dict["period"] = period
        if results is not UNSET:
            field_dict["results"] = results
        if start_date is not UNSET:
            field_dict["startDate"] = start_date
        if time_zone is not UNSET:
            field_dict["timeZone"] = time_zone

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.internal_public_v1_campaign_id_failure import InternalPublicV1CampaignIDFailure
        from ..models.internal_public_v1_campaign_performance import InternalPublicV1CampaignPerformance

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        data_as_of = d.pop("dataAsOf", UNSET)

        end_date = d.pop("endDate", UNSET)

        _failures = d.pop("failures", UNSET)
        failures: list[InternalPublicV1CampaignIDFailure] | Unset = UNSET
        if _failures is not UNSET:
            failures = []
            for failures_item_data in _failures:
                failures_item = InternalPublicV1CampaignIDFailure.from_dict(failures_item_data)

                failures.append(failures_item)

        _period = d.pop("period", UNSET)
        period: InternalPublicV1BatchGetPerformanceResponsePeriod | Unset
        if isinstance(_period, Unset):
            period = UNSET
        else:
            period = InternalPublicV1BatchGetPerformanceResponsePeriod(_period)

        _results = d.pop("results", UNSET)
        results: list[InternalPublicV1CampaignPerformance] | Unset = UNSET
        if _results is not UNSET:
            results = []
            for results_item_data in _results:
                results_item = InternalPublicV1CampaignPerformance.from_dict(results_item_data)

                results.append(results_item)

        start_date = d.pop("startDate", UNSET)

        time_zone = d.pop("timeZone", UNSET)

        internal_public_v1_batch_get_performance_response = cls(
            data_as_of=data_as_of,
            end_date=end_date,
            failures=failures,
            period=period,
            results=results,
            start_date=start_date,
            time_zone=time_zone,
        )

        internal_public_v1_batch_get_performance_response.additional_properties = d
        return internal_public_v1_batch_get_performance_response

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
