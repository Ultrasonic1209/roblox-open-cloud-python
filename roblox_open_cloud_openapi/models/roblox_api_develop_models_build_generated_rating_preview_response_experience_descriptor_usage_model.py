from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_api_develop_models_build_generated_rating_preview_response_age_range_model import (
        RobloxApiDevelopModelsBuildGeneratedRatingPreviewResponseAgeRangeModel,
    )
    from ..models.roblox_api_develop_models_build_generated_rating_preview_response_experience_descriptor_dimension_usage_model import (
        RobloxApiDevelopModelsBuildGeneratedRatingPreviewResponseExperienceDescriptorDimensionUsageModel,
    )
    from ..models.roblox_api_develop_models_build_generated_rating_preview_response_experience_descriptor_model import (
        RobloxApiDevelopModelsBuildGeneratedRatingPreviewResponseExperienceDescriptorModel,
    )


T = TypeVar("T", bound="RobloxApiDevelopModelsBuildGeneratedRatingPreviewResponseExperienceDescriptorUsageModel")


@_attrs_define
class RobloxApiDevelopModelsBuildGeneratedRatingPreviewResponseExperienceDescriptorUsageModel:
    """A descriptor usage that contributed to a recommendation.

    Attributes:
        name (str | Unset): Descriptor usage name.
        follows_compliance_api (bool | Unset): Whether this usage follows the Compliance API, when specified.
        experience_descriptor (RobloxApiDevelopModelsBuildGeneratedRatingPreviewResponseExperienceDescriptorModel |
            Unset): Experience descriptor definition.
        experience_descriptor_dimension_usages
            (list[RobloxApiDevelopModelsBuildGeneratedRatingPreviewResponseExperienceDescriptorDimensionUsageModel] |
            Unset): Dimensions associated with this usage.
        contains (bool | Unset): Whether the experience contains this descriptor.
        age_range (RobloxApiDevelopModelsBuildGeneratedRatingPreviewResponseAgeRangeModel | Unset): Age range for a
            descriptor usage.
        descriptor_display_name (str | Unset): Localized descriptor display name.
        age_range_display_name (str | Unset): Localized age-range display name.
    """

    name: str | Unset = UNSET
    follows_compliance_api: bool | Unset = UNSET
    experience_descriptor: (
        RobloxApiDevelopModelsBuildGeneratedRatingPreviewResponseExperienceDescriptorModel | Unset
    ) = UNSET
    experience_descriptor_dimension_usages: (
        list[RobloxApiDevelopModelsBuildGeneratedRatingPreviewResponseExperienceDescriptorDimensionUsageModel] | Unset
    ) = UNSET
    contains: bool | Unset = UNSET
    age_range: RobloxApiDevelopModelsBuildGeneratedRatingPreviewResponseAgeRangeModel | Unset = UNSET
    descriptor_display_name: str | Unset = UNSET
    age_range_display_name: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        follows_compliance_api = self.follows_compliance_api

        experience_descriptor: dict[str, Any] | Unset = UNSET
        if not isinstance(self.experience_descriptor, Unset):
            experience_descriptor = self.experience_descriptor.to_dict()

        experience_descriptor_dimension_usages: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.experience_descriptor_dimension_usages, Unset):
            experience_descriptor_dimension_usages = []
            for experience_descriptor_dimension_usages_item_data in self.experience_descriptor_dimension_usages:
                experience_descriptor_dimension_usages_item = experience_descriptor_dimension_usages_item_data.to_dict()
                experience_descriptor_dimension_usages.append(experience_descriptor_dimension_usages_item)

        contains = self.contains

        age_range: dict[str, Any] | Unset = UNSET
        if not isinstance(self.age_range, Unset):
            age_range = self.age_range.to_dict()

        descriptor_display_name = self.descriptor_display_name

        age_range_display_name = self.age_range_display_name

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if follows_compliance_api is not UNSET:
            field_dict["followsComplianceApi"] = follows_compliance_api
        if experience_descriptor is not UNSET:
            field_dict["experienceDescriptor"] = experience_descriptor
        if experience_descriptor_dimension_usages is not UNSET:
            field_dict["experienceDescriptorDimensionUsages"] = experience_descriptor_dimension_usages
        if contains is not UNSET:
            field_dict["contains"] = contains
        if age_range is not UNSET:
            field_dict["ageRange"] = age_range
        if descriptor_display_name is not UNSET:
            field_dict["descriptorDisplayName"] = descriptor_display_name
        if age_range_display_name is not UNSET:
            field_dict["ageRangeDisplayName"] = age_range_display_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_api_develop_models_build_generated_rating_preview_response_age_range_model import (
            RobloxApiDevelopModelsBuildGeneratedRatingPreviewResponseAgeRangeModel,
        )
        from ..models.roblox_api_develop_models_build_generated_rating_preview_response_experience_descriptor_dimension_usage_model import (
            RobloxApiDevelopModelsBuildGeneratedRatingPreviewResponseExperienceDescriptorDimensionUsageModel,
        )
        from ..models.roblox_api_develop_models_build_generated_rating_preview_response_experience_descriptor_model import (
            RobloxApiDevelopModelsBuildGeneratedRatingPreviewResponseExperienceDescriptorModel,
        )

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        name = d.pop("name", UNSET)

        follows_compliance_api = d.pop("followsComplianceApi", UNSET)

        _experience_descriptor = d.pop("experienceDescriptor", UNSET)
        experience_descriptor: (
            RobloxApiDevelopModelsBuildGeneratedRatingPreviewResponseExperienceDescriptorModel | Unset
        )
        if isinstance(_experience_descriptor, Unset):
            experience_descriptor = UNSET
        else:
            experience_descriptor = (
                RobloxApiDevelopModelsBuildGeneratedRatingPreviewResponseExperienceDescriptorModel.from_dict(
                    _experience_descriptor
                )
            )

        _experience_descriptor_dimension_usages = d.pop("experienceDescriptorDimensionUsages", UNSET)
        experience_descriptor_dimension_usages: (
            list[RobloxApiDevelopModelsBuildGeneratedRatingPreviewResponseExperienceDescriptorDimensionUsageModel]
            | Unset
        ) = UNSET
        if _experience_descriptor_dimension_usages is not UNSET:
            experience_descriptor_dimension_usages = []
            for experience_descriptor_dimension_usages_item_data in _experience_descriptor_dimension_usages:
                experience_descriptor_dimension_usages_item = RobloxApiDevelopModelsBuildGeneratedRatingPreviewResponseExperienceDescriptorDimensionUsageModel.from_dict(
                    experience_descriptor_dimension_usages_item_data
                )

                experience_descriptor_dimension_usages.append(experience_descriptor_dimension_usages_item)

        contains = d.pop("contains", UNSET)

        _age_range = d.pop("ageRange", UNSET)
        age_range: RobloxApiDevelopModelsBuildGeneratedRatingPreviewResponseAgeRangeModel | Unset
        if isinstance(_age_range, Unset):
            age_range = UNSET
        else:
            age_range = RobloxApiDevelopModelsBuildGeneratedRatingPreviewResponseAgeRangeModel.from_dict(_age_range)

        descriptor_display_name = d.pop("descriptorDisplayName", UNSET)

        age_range_display_name = d.pop("ageRangeDisplayName", UNSET)

        roblox_api_develop_models_build_generated_rating_preview_response_experience_descriptor_usage_model = cls(
            name=name,
            follows_compliance_api=follows_compliance_api,
            experience_descriptor=experience_descriptor,
            experience_descriptor_dimension_usages=experience_descriptor_dimension_usages,
            contains=contains,
            age_range=age_range,
            descriptor_display_name=descriptor_display_name,
            age_range_display_name=age_range_display_name,
        )

        return roblox_api_develop_models_build_generated_rating_preview_response_experience_descriptor_usage_model
