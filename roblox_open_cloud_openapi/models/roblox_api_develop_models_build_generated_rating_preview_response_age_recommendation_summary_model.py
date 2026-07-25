from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_api_develop_models_build_generated_rating_preview_response_age_recommendation_model import (
        RobloxApiDevelopModelsBuildGeneratedRatingPreviewResponseAgeRecommendationModel,
    )


T = TypeVar("T", bound="RobloxApiDevelopModelsBuildGeneratedRatingPreviewResponseAgeRecommendationSummaryModel")


@_attrs_define
class RobloxApiDevelopModelsBuildGeneratedRatingPreviewResponseAgeRecommendationSummaryModel:
    """Age recommendation summary.

    Attributes:
        age_recommendation (RobloxApiDevelopModelsBuildGeneratedRatingPreviewResponseAgeRecommendationModel | Unset):
            Age recommendation.
    """

    age_recommendation: RobloxApiDevelopModelsBuildGeneratedRatingPreviewResponseAgeRecommendationModel | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        age_recommendation: dict[str, Any] | Unset = UNSET
        if not isinstance(self.age_recommendation, Unset):
            age_recommendation = self.age_recommendation.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if age_recommendation is not UNSET:
            field_dict["ageRecommendation"] = age_recommendation

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_api_develop_models_build_generated_rating_preview_response_age_recommendation_model import (
            RobloxApiDevelopModelsBuildGeneratedRatingPreviewResponseAgeRecommendationModel,
        )

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        _age_recommendation = d.pop("ageRecommendation", UNSET)
        age_recommendation: RobloxApiDevelopModelsBuildGeneratedRatingPreviewResponseAgeRecommendationModel | Unset
        if isinstance(_age_recommendation, Unset):
            age_recommendation = UNSET
        else:
            age_recommendation = (
                RobloxApiDevelopModelsBuildGeneratedRatingPreviewResponseAgeRecommendationModel.from_dict(
                    _age_recommendation
                )
            )

        roblox_api_develop_models_build_generated_rating_preview_response_age_recommendation_summary_model = cls(
            age_recommendation=age_recommendation,
        )

        return roblox_api_develop_models_build_generated_rating_preview_response_age_recommendation_summary_model
