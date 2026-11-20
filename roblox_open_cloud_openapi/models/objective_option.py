from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.objective_option_audience_types_item import ObjectiveOptionAudienceTypesItem
from ..models.objective_option_objective import ObjectiveOptionObjective
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.reason import Reason


T = TypeVar("T", bound="ObjectiveOption")


@_attrs_define
class ObjectiveOption:
    """
    Attributes:
        audience_types (list[ObjectiveOptionAudienceTypesItem]): Accepted targeting.audienceType values. Only
            ALL_PLAYERS for ENGAGEMENT, which rejects targeting restrictions.
        available (bool): Whether the objective can currently be used.
        objective (ObjectiveOptionObjective): The objective. Values can be `PLAYS`, `ENGAGEMENT`, or `ROBUX_SPEND`.
            `ENGAGEMENT` is the API value for the Qualify for Kids and Select objective in Ads Manager.
        supports_targeting (bool): Whether create accepts targeting restrictions for this objective. False only for
            `ENGAGEMENT`.
        unavailable_reasons (list[Reason] | Unset): Why the objective is unavailable. Present only when available is
            false.
    """

    audience_types: list[ObjectiveOptionAudienceTypesItem]
    available: bool
    objective: ObjectiveOptionObjective
    supports_targeting: bool
    unavailable_reasons: list[Reason] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        audience_types = []
        for audience_types_item_data in self.audience_types:
            audience_types_item = audience_types_item_data.value
            audience_types.append(audience_types_item)

        available = self.available

        objective = self.objective.value

        supports_targeting = self.supports_targeting

        unavailable_reasons: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.unavailable_reasons, Unset):
            unavailable_reasons = []
            for unavailable_reasons_item_data in self.unavailable_reasons:
                unavailable_reasons_item = unavailable_reasons_item_data.to_dict()
                unavailable_reasons.append(unavailable_reasons_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "audienceTypes": audience_types,
                "available": available,
                "objective": objective,
                "supportsTargeting": supports_targeting,
            }
        )
        if unavailable_reasons is not UNSET:
            field_dict["unavailableReasons"] = unavailable_reasons

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.reason import Reason  # noqa: PLC0415

        d = dict(src_dict)
        audience_types = []
        _audience_types = d.pop("audienceTypes")
        for audience_types_item_data in _audience_types:
            audience_types_item = ObjectiveOptionAudienceTypesItem(audience_types_item_data)

            audience_types.append(audience_types_item)

        available = d.pop("available")

        objective = ObjectiveOptionObjective(d.pop("objective"))

        supports_targeting = d.pop("supportsTargeting")

        _unavailable_reasons = d.pop("unavailableReasons", UNSET)
        unavailable_reasons: list[Reason] | Unset = UNSET
        if _unavailable_reasons is not UNSET:
            unavailable_reasons = []
            for unavailable_reasons_item_data in _unavailable_reasons:
                unavailable_reasons_item = Reason.from_dict(unavailable_reasons_item_data)

                unavailable_reasons.append(unavailable_reasons_item)

        objective_option = cls(
            audience_types=audience_types,
            available=available,
            objective=objective,
            supports_targeting=supports_targeting,
            unavailable_reasons=unavailable_reasons,
        )

        objective_option.additional_properties = d
        return objective_option

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
