from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.planning_campaign_context import PlanningCampaignContext


T = TypeVar("T", bound="AudienceEstimateRequest")


@_attrs_define
class AudienceEstimateRequest:
    """
    Attributes:
        campaign_context (PlanningCampaignContext):
    """

    campaign_context: PlanningCampaignContext
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        campaign_context = self.campaign_context.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "campaignContext": campaign_context,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.planning_campaign_context import PlanningCampaignContext  # noqa: PLC0415

        d = dict(src_dict)
        campaign_context = PlanningCampaignContext.from_dict(d.pop("campaignContext"))

        audience_estimate_request = cls(
            campaign_context=campaign_context,
        )

        audience_estimate_request.additional_properties = d
        return audience_estimate_request

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
