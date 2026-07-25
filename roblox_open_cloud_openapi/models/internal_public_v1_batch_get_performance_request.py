from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.internal_public_v1_batch_get_performance_request_period import (
    InternalPublicV1BatchGetPerformanceRequestPeriod,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="InternalPublicV1BatchGetPerformanceRequest")


@_attrs_define
class InternalPublicV1BatchGetPerformanceRequest:
    """
    Attributes:
        campaign_ids (list[str] | Unset): The campaign IDs to report on. Required. At most 100 per request.
        period (InternalPublicV1BatchGetPerformanceRequestPeriod | Unset): The reporting window applied to every
            campaign in the batch. Optional; defaults
            to `LAST_7_DAYS`. Can be `TODAY`, `YESTERDAY`, `LAST_7_DAYS`, `LAST_30_DAYS`,
            `THIS_MONTH`, `LAST_MONTH`, `YEAR_TO_DATE`, or `PREVIOUS_YEAR`.
    """

    campaign_ids: list[str] | Unset = UNSET
    period: InternalPublicV1BatchGetPerformanceRequestPeriod | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        campaign_ids: list[str] | Unset = UNSET
        if not isinstance(self.campaign_ids, Unset):
            campaign_ids = self.campaign_ids

        period: str | Unset = UNSET
        if not isinstance(self.period, Unset):
            period = self.period.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if campaign_ids is not UNSET:
            field_dict["campaignIds"] = campaign_ids
        if period is not UNSET:
            field_dict["period"] = period

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        campaign_ids = cast(list[str], d.pop("campaignIds", UNSET))

        _period = d.pop("period", UNSET)
        period: InternalPublicV1BatchGetPerformanceRequestPeriod | Unset
        if isinstance(_period, Unset):
            period = UNSET
        else:
            period = InternalPublicV1BatchGetPerformanceRequestPeriod(_period)

        internal_public_v1_batch_get_performance_request = cls(
            campaign_ids=campaign_ids,
            period=period,
        )

        internal_public_v1_batch_get_performance_request.additional_properties = d
        return internal_public_v1_batch_get_performance_request

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
