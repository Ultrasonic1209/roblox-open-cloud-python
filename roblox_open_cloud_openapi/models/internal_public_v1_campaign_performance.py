from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.internal_public_v1_performance_totals import InternalPublicV1PerformanceTotals


T = TypeVar("T", bound="InternalPublicV1CampaignPerformance")


@_attrs_define
class InternalPublicV1CampaignPerformance:
    """
    Attributes:
        campaign_id (str | Unset): The campaign these metrics belong to.
        totals (InternalPublicV1PerformanceTotals | Unset):
    """

    campaign_id: str | Unset = UNSET
    totals: InternalPublicV1PerformanceTotals | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        campaign_id = self.campaign_id

        totals: dict[str, Any] | Unset = UNSET
        if not isinstance(self.totals, Unset):
            totals = self.totals.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if campaign_id is not UNSET:
            field_dict["campaignId"] = campaign_id
        if totals is not UNSET:
            field_dict["totals"] = totals

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.internal_public_v1_performance_totals import InternalPublicV1PerformanceTotals

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        campaign_id = d.pop("campaignId", UNSET)

        _totals = d.pop("totals", UNSET)
        totals: InternalPublicV1PerformanceTotals | Unset
        if isinstance(_totals, Unset):
            totals = UNSET
        else:
            totals = InternalPublicV1PerformanceTotals.from_dict(_totals)

        internal_public_v1_campaign_performance = cls(
            campaign_id=campaign_id,
            totals=totals,
        )

        internal_public_v1_campaign_performance.additional_properties = d
        return internal_public_v1_campaign_performance

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
