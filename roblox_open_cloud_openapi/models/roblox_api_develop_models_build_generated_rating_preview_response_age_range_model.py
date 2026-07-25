from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxApiDevelopModelsBuildGeneratedRatingPreviewResponseAgeRangeModel")


@_attrs_define
class RobloxApiDevelopModelsBuildGeneratedRatingPreviewResponseAgeRangeModel:
    """Age range for a descriptor usage.

    Attributes:
        min_age_inclusive (int | Unset): Inclusive minimum age.
        max_age_inclusive (int | Unset): Inclusive maximum age.
    """

    min_age_inclusive: int | Unset = UNSET
    max_age_inclusive: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        min_age_inclusive = self.min_age_inclusive

        max_age_inclusive = self.max_age_inclusive

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if min_age_inclusive is not UNSET:
            field_dict["minAgeInclusive"] = min_age_inclusive
        if max_age_inclusive is not UNSET:
            field_dict["maxAgeInclusive"] = max_age_inclusive

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        min_age_inclusive = d.pop("minAgeInclusive", UNSET)

        max_age_inclusive = d.pop("maxAgeInclusive", UNSET)

        roblox_api_develop_models_build_generated_rating_preview_response_age_range_model = cls(
            min_age_inclusive=min_age_inclusive,
            max_age_inclusive=max_age_inclusive,
        )

        return roblox_api_develop_models_build_generated_rating_preview_response_age_range_model
