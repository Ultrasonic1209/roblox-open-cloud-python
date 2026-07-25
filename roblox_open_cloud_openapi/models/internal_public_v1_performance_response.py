from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.internal_public_v1_performance_response_period import InternalPublicV1PerformanceResponsePeriod
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.internal_public_v1_performance_totals import InternalPublicV1PerformanceTotals


T = TypeVar("T", bound="InternalPublicV1PerformanceResponse")


@_attrs_define
class InternalPublicV1PerformanceResponse:
    """
    Attributes:
        campaign_id (str | Unset): The campaign these metrics belong to.
        data_as_of (str | Unset): The time the metrics were current, as an RFC 3339 UTC timestamp.
        end_date (str | Unset): The last day of the window (inclusive), as YYYY-MM-DD in the account's time zone.
        period (InternalPublicV1PerformanceResponsePeriod | Unset): The reporting window applied. Can be `TODAY`,
            `YESTERDAY`, `LAST_7_DAYS`,
            `LAST_30_DAYS`, `THIS_MONTH`, `LAST_MONTH`, `YEAR_TO_DATE`, or `PREVIOUS_YEAR`.
        start_date (str | Unset): The first day of the window (inclusive), as YYYY-MM-DD in the account's time zone.
        time_zone (str | Unset): The IANA time zone the window and metrics are computed in.
        totals (InternalPublicV1PerformanceTotals | Unset):
    """

    campaign_id: str | Unset = UNSET
    data_as_of: str | Unset = UNSET
    end_date: str | Unset = UNSET
    period: InternalPublicV1PerformanceResponsePeriod | Unset = UNSET
    start_date: str | Unset = UNSET
    time_zone: str | Unset = UNSET
    totals: InternalPublicV1PerformanceTotals | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        campaign_id = self.campaign_id

        data_as_of = self.data_as_of

        end_date = self.end_date

        period: str | Unset = UNSET
        if not isinstance(self.period, Unset):
            period = self.period.value

        start_date = self.start_date

        time_zone = self.time_zone

        totals: dict[str, Any] | Unset = UNSET
        if not isinstance(self.totals, Unset):
            totals = self.totals.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if campaign_id is not UNSET:
            field_dict["campaignId"] = campaign_id
        if data_as_of is not UNSET:
            field_dict["dataAsOf"] = data_as_of
        if end_date is not UNSET:
            field_dict["endDate"] = end_date
        if period is not UNSET:
            field_dict["period"] = period
        if start_date is not UNSET:
            field_dict["startDate"] = start_date
        if time_zone is not UNSET:
            field_dict["timeZone"] = time_zone
        if totals is not UNSET:
            field_dict["totals"] = totals

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.internal_public_v1_performance_totals import InternalPublicV1PerformanceTotals

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        campaign_id = d.pop("campaignId", UNSET)

        data_as_of = d.pop("dataAsOf", UNSET)

        end_date = d.pop("endDate", UNSET)

        _period = d.pop("period", UNSET)
        period: InternalPublicV1PerformanceResponsePeriod | Unset
        if isinstance(_period, Unset):
            period = UNSET
        else:
            period = InternalPublicV1PerformanceResponsePeriod(_period)

        start_date = d.pop("startDate", UNSET)

        time_zone = d.pop("timeZone", UNSET)

        _totals = d.pop("totals", UNSET)
        totals: InternalPublicV1PerformanceTotals | Unset
        if isinstance(_totals, Unset):
            totals = UNSET
        else:
            totals = InternalPublicV1PerformanceTotals.from_dict(_totals)

        internal_public_v1_performance_response = cls(
            campaign_id=campaign_id,
            data_as_of=data_as_of,
            end_date=end_date,
            period=period,
            start_date=start_date,
            time_zone=time_zone,
            totals=totals,
        )

        internal_public_v1_performance_response.additional_properties = d
        return internal_public_v1_performance_response

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
