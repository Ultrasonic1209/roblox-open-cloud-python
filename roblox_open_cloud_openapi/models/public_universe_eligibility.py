from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.public_universe_eligibility_reasons_item import PublicUniverseEligibilityReasonsItem
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.reason import Reason


T = TypeVar("T", bound="PublicUniverseEligibility")


@_attrs_define
class PublicUniverseEligibility:
    """
    Attributes:
        details (list[Reason] | Unset): Structured reasons with remediation, one per entry in reasons.
        eligible (bool | Unset): Whether the experience can currently be advertised.
        reasons (list[PublicUniverseEligibilityReasonsItem] | Unset): The reasons the experience is not eligible.
            Omitted when eligible. Values can be
            `NO_PERMISSION`, `BLOCKED`, or `OBJECTIVE_NOT_SUPPORTED`. `OBJECTIVE_NOT_SUPPORTED`
            appears only with the objective query parameter, when the experience can't use
            that objective.
        universe_id (str | Unset): The identifier of the experience that was checked.
    """

    details: list[Reason] | Unset = UNSET
    eligible: bool | Unset = UNSET
    reasons: list[PublicUniverseEligibilityReasonsItem] | Unset = UNSET
    universe_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        details: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.details, Unset):
            details = []
            for details_item_data in self.details:
                details_item = details_item_data.to_dict()
                details.append(details_item)

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
        if details is not UNSET:
            field_dict["details"] = details
        if eligible is not UNSET:
            field_dict["eligible"] = eligible
        if reasons is not UNSET:
            field_dict["reasons"] = reasons
        if universe_id is not UNSET:
            field_dict["universeId"] = universe_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.reason import Reason  # noqa: PLC0415

        d = dict(src_dict)
        _details = d.pop("details", UNSET)
        details: list[Reason] | Unset = UNSET
        if _details is not UNSET:
            details = []
            for details_item_data in _details:
                details_item = Reason.from_dict(details_item_data)

                details.append(details_item)

        eligible = d.pop("eligible", UNSET)

        _reasons = d.pop("reasons", UNSET)
        reasons: list[PublicUniverseEligibilityReasonsItem] | Unset = UNSET
        if _reasons is not UNSET:
            reasons = []
            for reasons_item_data in _reasons:
                reasons_item = PublicUniverseEligibilityReasonsItem(reasons_item_data)

                reasons.append(reasons_item)

        universe_id = d.pop("universeId", UNSET)

        public_universe_eligibility = cls(
            details=details,
            eligible=eligible,
            reasons=reasons,
            universe_id=universe_id,
        )

        public_universe_eligibility.additional_properties = d
        return public_universe_eligibility

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
