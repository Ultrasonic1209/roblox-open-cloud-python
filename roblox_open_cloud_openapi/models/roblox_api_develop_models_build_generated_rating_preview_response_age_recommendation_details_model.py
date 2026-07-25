from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_api_develop_models_build_generated_rating_preview_response_age_recommendation_summary_model import (
        RobloxApiDevelopModelsBuildGeneratedRatingPreviewResponseAgeRecommendationSummaryModel,
    )
    from ..models.roblox_api_develop_models_build_generated_rating_preview_response_experience_descriptor_usage_model import (
        RobloxApiDevelopModelsBuildGeneratedRatingPreviewResponseExperienceDescriptorUsageModel,
    )


T = TypeVar("T", bound="RobloxApiDevelopModelsBuildGeneratedRatingPreviewResponseAgeRecommendationDetailsModel")


@_attrs_define
class RobloxApiDevelopModelsBuildGeneratedRatingPreviewResponseAgeRecommendationDetailsModel:
    """Age recommendation details.

    Attributes:
        age_recommendation_summary
            (RobloxApiDevelopModelsBuildGeneratedRatingPreviewResponseAgeRecommendationSummaryModel | Unset): Age
            recommendation summary.
        experience_descriptor_usages
            (list[RobloxApiDevelopModelsBuildGeneratedRatingPreviewResponseExperienceDescriptorUsageModel] | Unset):
            Descriptor usages that contributed to the recommendation.
    """

    age_recommendation_summary: (
        RobloxApiDevelopModelsBuildGeneratedRatingPreviewResponseAgeRecommendationSummaryModel | Unset
    ) = UNSET
    experience_descriptor_usages: (
        list[RobloxApiDevelopModelsBuildGeneratedRatingPreviewResponseExperienceDescriptorUsageModel] | Unset
    ) = UNSET

    def to_dict(self) -> dict[str, Any]:
        age_recommendation_summary: dict[str, Any] | Unset = UNSET
        if not isinstance(self.age_recommendation_summary, Unset):
            age_recommendation_summary = self.age_recommendation_summary.to_dict()

        experience_descriptor_usages: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.experience_descriptor_usages, Unset):
            experience_descriptor_usages = []
            for experience_descriptor_usages_item_data in self.experience_descriptor_usages:
                experience_descriptor_usages_item = experience_descriptor_usages_item_data.to_dict()
                experience_descriptor_usages.append(experience_descriptor_usages_item)

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if age_recommendation_summary is not UNSET:
            field_dict["ageRecommendationSummary"] = age_recommendation_summary
        if experience_descriptor_usages is not UNSET:
            field_dict["experienceDescriptorUsages"] = experience_descriptor_usages

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_api_develop_models_build_generated_rating_preview_response_age_recommendation_summary_model import (
            RobloxApiDevelopModelsBuildGeneratedRatingPreviewResponseAgeRecommendationSummaryModel,
        )
        from ..models.roblox_api_develop_models_build_generated_rating_preview_response_experience_descriptor_usage_model import (
            RobloxApiDevelopModelsBuildGeneratedRatingPreviewResponseExperienceDescriptorUsageModel,
        )

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        _age_recommendation_summary = d.pop("ageRecommendationSummary", UNSET)
        age_recommendation_summary: (
            RobloxApiDevelopModelsBuildGeneratedRatingPreviewResponseAgeRecommendationSummaryModel | Unset
        )
        if isinstance(_age_recommendation_summary, Unset):
            age_recommendation_summary = UNSET
        else:
            age_recommendation_summary = (
                RobloxApiDevelopModelsBuildGeneratedRatingPreviewResponseAgeRecommendationSummaryModel.from_dict(
                    _age_recommendation_summary
                )
            )

        _experience_descriptor_usages = d.pop("experienceDescriptorUsages", UNSET)
        experience_descriptor_usages: (
            list[RobloxApiDevelopModelsBuildGeneratedRatingPreviewResponseExperienceDescriptorUsageModel] | Unset
        ) = UNSET
        if _experience_descriptor_usages is not UNSET:
            experience_descriptor_usages = []
            for experience_descriptor_usages_item_data in _experience_descriptor_usages:
                experience_descriptor_usages_item = (
                    RobloxApiDevelopModelsBuildGeneratedRatingPreviewResponseExperienceDescriptorUsageModel.from_dict(
                        experience_descriptor_usages_item_data
                    )
                )

                experience_descriptor_usages.append(experience_descriptor_usages_item)

        roblox_api_develop_models_build_generated_rating_preview_response_age_recommendation_details_model = cls(
            age_recommendation_summary=age_recommendation_summary,
            experience_descriptor_usages=experience_descriptor_usages,
        )

        return roblox_api_develop_models_build_generated_rating_preview_response_age_recommendation_details_model
