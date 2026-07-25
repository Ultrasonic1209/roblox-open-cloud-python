from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_api_develop_models_build_generated_rating_preview_response_experience_descriptor_usage_model import (
        RobloxApiDevelopModelsBuildGeneratedRatingPreviewResponseExperienceDescriptorUsageModel,
    )


T = TypeVar("T", bound="RobloxApiDevelopModelsBuildGeneratedRatingPreviewResponseRestrictedCountryModel")


@_attrs_define
class RobloxApiDevelopModelsBuildGeneratedRatingPreviewResponseRestrictedCountryModel:
    """Country-specific restrictions.

    Attributes:
        country_code (str | Unset): ISO country code.
        experience_descriptor_usages
            (list[RobloxApiDevelopModelsBuildGeneratedRatingPreviewResponseExperienceDescriptorUsageModel] | Unset):
            Descriptor usages responsible for the restriction.
        country_display_name (str | Unset): Localized country display name.
    """

    country_code: str | Unset = UNSET
    experience_descriptor_usages: (
        list[RobloxApiDevelopModelsBuildGeneratedRatingPreviewResponseExperienceDescriptorUsageModel] | Unset
    ) = UNSET
    country_display_name: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        country_code = self.country_code

        experience_descriptor_usages: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.experience_descriptor_usages, Unset):
            experience_descriptor_usages = []
            for experience_descriptor_usages_item_data in self.experience_descriptor_usages:
                experience_descriptor_usages_item = experience_descriptor_usages_item_data.to_dict()
                experience_descriptor_usages.append(experience_descriptor_usages_item)

        country_display_name = self.country_display_name

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if country_code is not UNSET:
            field_dict["countryCode"] = country_code
        if experience_descriptor_usages is not UNSET:
            field_dict["experienceDescriptorUsages"] = experience_descriptor_usages
        if country_display_name is not UNSET:
            field_dict["countryDisplayName"] = country_display_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_api_develop_models_build_generated_rating_preview_response_experience_descriptor_usage_model import (
            RobloxApiDevelopModelsBuildGeneratedRatingPreviewResponseExperienceDescriptorUsageModel,
        )

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        country_code = d.pop("countryCode", UNSET)

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

        country_display_name = d.pop("countryDisplayName", UNSET)

        roblox_api_develop_models_build_generated_rating_preview_response_restricted_country_model = cls(
            country_code=country_code,
            experience_descriptor_usages=experience_descriptor_usages,
            country_display_name=country_display_name,
        )

        return roblox_api_develop_models_build_generated_rating_preview_response_restricted_country_model
