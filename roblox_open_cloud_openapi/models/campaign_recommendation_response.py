from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.campaign_recommendation_response_budget_type import CampaignRecommendationResponseBudgetType

T = TypeVar("T", bound="CampaignRecommendationResponse")


@_attrs_define
class CampaignRecommendationResponse:
    """
    Attributes:
        budget_options_micros (list[str]): A lower, the recommended, and a higher daily budget in micro-USD, as decimal
            strings in ascending order.
        budget_type (CampaignRecommendationResponseBudgetType): Recommendations are always daily budgets.
        duration_options_in_days (list[int]): Suggested campaign lengths for a duration picker, in ascending order.
        recommended_budget_micros (str): The suggested daily budget in micro-USD, as a decimal string. Always one of
            budgetOptionsMicros.
    """

    budget_options_micros: list[str]
    budget_type: CampaignRecommendationResponseBudgetType
    duration_options_in_days: list[int]
    recommended_budget_micros: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        budget_options_micros = self.budget_options_micros

        budget_type = self.budget_type.value

        duration_options_in_days = self.duration_options_in_days

        recommended_budget_micros = self.recommended_budget_micros

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "budgetOptionsMicros": budget_options_micros,
                "budgetType": budget_type,
                "durationOptionsInDays": duration_options_in_days,
                "recommendedBudgetMicros": recommended_budget_micros,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        budget_options_micros = cast(list[str], d.pop("budgetOptionsMicros"))

        budget_type = CampaignRecommendationResponseBudgetType(d.pop("budgetType"))

        duration_options_in_days = cast(list[int], d.pop("durationOptionsInDays"))

        recommended_budget_micros = d.pop("recommendedBudgetMicros")

        campaign_recommendation_response = cls(
            budget_options_micros=budget_options_micros,
            budget_type=budget_type,
            duration_options_in_days=duration_options_in_days,
            recommended_budget_micros=recommended_budget_micros,
        )

        campaign_recommendation_response.additional_properties = d
        return campaign_recommendation_response

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
