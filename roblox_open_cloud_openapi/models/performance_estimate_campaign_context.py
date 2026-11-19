from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.performance_estimate_campaign_context_objective import PerformanceEstimateCampaignContextObjective

T = TypeVar("T", bound="PerformanceEstimateCampaignContext")


@_attrs_define
class PerformanceEstimateCampaignContext:
    """
    Attributes:
        objective (PerformanceEstimateCampaignContextObjective): The advertising goal. Only PLAYS is supported.
        target_universe_id (str): The experience to estimate, as a decimal string.
    """

    objective: PerformanceEstimateCampaignContextObjective
    target_universe_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        objective = self.objective.value

        target_universe_id = self.target_universe_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "objective": objective,
                "targetUniverseId": target_universe_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        objective = PerformanceEstimateCampaignContextObjective(d.pop("objective"))

        target_universe_id = d.pop("targetUniverseId")

        performance_estimate_campaign_context = cls(
            objective=objective,
            target_universe_id=target_universe_id,
        )

        performance_estimate_campaign_context.additional_properties = d
        return performance_estimate_campaign_context

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
