from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_api_develop_models_build_generated_rating_preview_response_age_recommendation_details_model import (
        RobloxApiDevelopModelsBuildGeneratedRatingPreviewResponseAgeRecommendationDetailsModel,
    )
    from ..models.roblox_api_develop_models_build_generated_rating_preview_response_restricted_country_model import (
        RobloxApiDevelopModelsBuildGeneratedRatingPreviewResponseRestrictedCountryModel,
    )


T = TypeVar("T", bound="RobloxApiDevelopModelsBuildGeneratedRatingPreviewResponse")


@_attrs_define
class RobloxApiDevelopModelsBuildGeneratedRatingPreviewResponse:
    """The complete build-generated rating preview returned by Experience Guidelines.

    Attributes:
        age_recommendation_details
            (RobloxApiDevelopModelsBuildGeneratedRatingPreviewResponseAgeRecommendationDetailsModel | Unset): Age
            recommendation details.
        restricted_countries (list[RobloxApiDevelopModelsBuildGeneratedRatingPreviewResponseRestrictedCountryModel] |
            Unset): Country-specific restrictions produced by the preview.
    """

    age_recommendation_details: (
        RobloxApiDevelopModelsBuildGeneratedRatingPreviewResponseAgeRecommendationDetailsModel | Unset
    ) = UNSET
    restricted_countries: (
        list[RobloxApiDevelopModelsBuildGeneratedRatingPreviewResponseRestrictedCountryModel] | Unset
    ) = UNSET

    def to_dict(self) -> dict[str, Any]:
        age_recommendation_details: dict[str, Any] | Unset = UNSET
        if not isinstance(self.age_recommendation_details, Unset):
            age_recommendation_details = self.age_recommendation_details.to_dict()

        restricted_countries: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.restricted_countries, Unset):
            restricted_countries = []
            for restricted_countries_item_data in self.restricted_countries:
                restricted_countries_item = restricted_countries_item_data.to_dict()
                restricted_countries.append(restricted_countries_item)

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if age_recommendation_details is not UNSET:
            field_dict["ageRecommendationDetails"] = age_recommendation_details
        if restricted_countries is not UNSET:
            field_dict["restrictedCountries"] = restricted_countries

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_api_develop_models_build_generated_rating_preview_response_age_recommendation_details_model import (
            RobloxApiDevelopModelsBuildGeneratedRatingPreviewResponseAgeRecommendationDetailsModel,
        )
        from ..models.roblox_api_develop_models_build_generated_rating_preview_response_restricted_country_model import (
            RobloxApiDevelopModelsBuildGeneratedRatingPreviewResponseRestrictedCountryModel,
        )

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        _age_recommendation_details = d.pop("ageRecommendationDetails", UNSET)
        age_recommendation_details: (
            RobloxApiDevelopModelsBuildGeneratedRatingPreviewResponseAgeRecommendationDetailsModel | Unset
        )
        if isinstance(_age_recommendation_details, Unset):
            age_recommendation_details = UNSET
        else:
            age_recommendation_details = (
                RobloxApiDevelopModelsBuildGeneratedRatingPreviewResponseAgeRecommendationDetailsModel.from_dict(
                    _age_recommendation_details
                )
            )

        _restricted_countries = d.pop("restrictedCountries", UNSET)
        restricted_countries: (
            list[RobloxApiDevelopModelsBuildGeneratedRatingPreviewResponseRestrictedCountryModel] | Unset
        ) = UNSET
        if _restricted_countries is not UNSET:
            restricted_countries = []
            for restricted_countries_item_data in _restricted_countries:
                restricted_countries_item = (
                    RobloxApiDevelopModelsBuildGeneratedRatingPreviewResponseRestrictedCountryModel.from_dict(
                        restricted_countries_item_data
                    )
                )

                restricted_countries.append(restricted_countries_item)

        roblox_api_develop_models_build_generated_rating_preview_response = cls(
            age_recommendation_details=age_recommendation_details,
            restricted_countries=restricted_countries,
        )

        return roblox_api_develop_models_build_generated_rating_preview_response
