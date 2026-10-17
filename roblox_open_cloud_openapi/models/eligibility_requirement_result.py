from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.eligibility_requirement import EligibilityRequirement
from ..types import UNSET, Unset

T = TypeVar("T", bound="EligibilityRequirementResult")


@_attrs_define
class EligibilityRequirementResult:
    """The result of an Account's eligibility check for a specific eligibility type.

    Attributes:
        eligibility_requirement (EligibilityRequirement | Unset): A type of eligibility requirement.
        eligible (bool | Unset): Gets or sets a value indicating whether the account is eligible for this eligibility
            type.
    """

    eligibility_requirement: EligibilityRequirement | Unset = UNSET
    eligible: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        eligibility_requirement: str | Unset = UNSET
        if not isinstance(self.eligibility_requirement, Unset):
            eligibility_requirement = self.eligibility_requirement.value

        eligible = self.eligible

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if eligibility_requirement is not UNSET:
            field_dict["eligibilityRequirement"] = eligibility_requirement
        if eligible is not UNSET:
            field_dict["eligible"] = eligible

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        _eligibility_requirement = d.pop("eligibilityRequirement", UNSET)
        eligibility_requirement: EligibilityRequirement | Unset
        if isinstance(_eligibility_requirement, Unset):
            eligibility_requirement = UNSET
        else:
            eligibility_requirement = EligibilityRequirement(_eligibility_requirement)

        eligible = d.pop("eligible", UNSET)

        eligibility_requirement_result = cls(
            eligibility_requirement=eligibility_requirement,
            eligible=eligible,
        )

        return eligibility_requirement_result
