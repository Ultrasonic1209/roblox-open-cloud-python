from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.internal_public_v1_universe_eligibility_reasons_item import InternalPublicV1UniverseEligibilityReasonsItem
from ..types import UNSET, Unset

T = TypeVar("T", bound="InternalPublicV1UniverseEligibility")


@_attrs_define
class InternalPublicV1UniverseEligibility:
    """
    Attributes:
        eligible (bool | Unset): Whether the experience can currently be advertised.
        reasons (list[InternalPublicV1UniverseEligibilityReasonsItem] | Unset): The reasons the experience is not
            eligible. Omitted when eligible. Values can be
            `NO_PERMISSION` or `BLOCKED`.
        universe_id (str | Unset): The identifier of the experience that was checked.
    """

    eligible: bool | Unset = UNSET
    reasons: list[InternalPublicV1UniverseEligibilityReasonsItem] | Unset = UNSET
    universe_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        eligible = self.eligible

        reasons: list[str] | Unset = UNSET
        if not isinstance(self.reasons, Unset):
            reasons = []
            for reasons_item_data in self.reasons:
                reasons_item = reasons_item_data.value
                reasons.append(reasons_item)

        universe_id = self.universe_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if eligible is not UNSET:
            field_dict["eligible"] = eligible
        if reasons is not UNSET:
            field_dict["reasons"] = reasons
        if universe_id is not UNSET:
            field_dict["universeId"] = universe_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        eligible = d.pop("eligible", UNSET)

        _reasons = d.pop("reasons", UNSET)
        reasons: list[InternalPublicV1UniverseEligibilityReasonsItem] | Unset = UNSET
        if _reasons is not UNSET:
            reasons = []
            for reasons_item_data in _reasons:
                reasons_item = InternalPublicV1UniverseEligibilityReasonsItem(reasons_item_data)

                reasons.append(reasons_item)

        universe_id = d.pop("universeId", UNSET)

        internal_public_v1_universe_eligibility = cls(
            eligible=eligible,
            reasons=reasons,
            universe_id=universe_id,
        )

        internal_public_v1_universe_eligibility.additional_properties = d
        return internal_public_v1_universe_eligibility

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
