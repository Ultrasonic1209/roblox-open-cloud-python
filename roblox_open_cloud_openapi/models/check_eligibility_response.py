from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.eligibility_requirement_result import EligibilityRequirementResult


T = TypeVar("T", bound="CheckEligibilityResponse")


@_attrs_define
class CheckEligibilityResponse:
    """Response object for Roblox.CloudPricing.ServiceEfficiencyApi.Operations.CheckEligibilityOperation

    Attributes:
        eligibility_requirement_results (list[EligibilityRequirementResult] | None | Unset): Gets or sets the
            eligibility requirement results for the provided creator.
    """

    eligibility_requirement_results: list[EligibilityRequirementResult] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        eligibility_requirement_results: list[dict[str, Any]] | None | Unset
        if isinstance(self.eligibility_requirement_results, Unset):
            eligibility_requirement_results = UNSET
        elif isinstance(self.eligibility_requirement_results, list):
            eligibility_requirement_results = []
            for eligibility_requirement_results_type_0_item_data in self.eligibility_requirement_results:
                eligibility_requirement_results_type_0_item = eligibility_requirement_results_type_0_item_data.to_dict()
                eligibility_requirement_results.append(eligibility_requirement_results_type_0_item)

        else:
            eligibility_requirement_results = self.eligibility_requirement_results

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if eligibility_requirement_results is not UNSET:
            field_dict["eligibilityRequirementResults"] = eligibility_requirement_results

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.eligibility_requirement_result import EligibilityRequirementResult

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}

        def _parse_eligibility_requirement_results(data: object) -> list[EligibilityRequirementResult] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                eligibility_requirement_results_type_0 = []
                _eligibility_requirement_results_type_0 = data
                for eligibility_requirement_results_type_0_item_data in _eligibility_requirement_results_type_0:
                    eligibility_requirement_results_type_0_item = EligibilityRequirementResult.from_dict(
                        eligibility_requirement_results_type_0_item_data
                    )

                    eligibility_requirement_results_type_0.append(eligibility_requirement_results_type_0_item)

                return eligibility_requirement_results_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[EligibilityRequirementResult] | None | Unset, data)

        eligibility_requirement_results = _parse_eligibility_requirement_results(
            d.pop("eligibilityRequirementResults", UNSET)
        )

        check_eligibility_response = cls(
            eligibility_requirement_results=eligibility_requirement_results,
        )

        return check_eligibility_response
