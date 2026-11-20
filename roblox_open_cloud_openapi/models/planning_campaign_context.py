from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.planning_campaign_context_objective import PlanningCampaignContextObjective
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.targeting import Targeting


T = TypeVar("T", bound="PlanningCampaignContext")


@_attrs_define
class PlanningCampaignContext:
    """
    Attributes:
        objective (PlanningCampaignContextObjective): The advertising goal. Can be `PLAYS`, `ENGAGEMENT`, or
            `ROBUX_SPEND`.
            `ENGAGEMENT` is the API value for the Qualify for Kids and Select objective in Ads Manager.
        target_universe_id (str): The experience to plan for, as a decimal string.
        targeting (Targeting | Unset):
    """

    objective: PlanningCampaignContextObjective
    target_universe_id: str
    targeting: Targeting | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        objective = self.objective.value

        target_universe_id = self.target_universe_id

        targeting: dict[str, Any] | Unset = UNSET
        if not isinstance(self.targeting, Unset):
            targeting = self.targeting.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "objective": objective,
                "targetUniverseId": target_universe_id,
            }
        )
        if targeting is not UNSET:
            field_dict["targeting"] = targeting

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.targeting import Targeting  # noqa: PLC0415

        d = dict(src_dict)
        objective = PlanningCampaignContextObjective(d.pop("objective"))

        target_universe_id = d.pop("targetUniverseId")

        _targeting = d.pop("targeting", UNSET)
        targeting: Targeting | Unset
        if isinstance(_targeting, Unset):
            targeting = UNSET
        else:
            targeting = Targeting.from_dict(_targeting)

        planning_campaign_context = cls(
            objective=objective,
            target_universe_id=target_universe_id,
            targeting=targeting,
        )

        planning_campaign_context.additional_properties = d
        return planning_campaign_context

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
