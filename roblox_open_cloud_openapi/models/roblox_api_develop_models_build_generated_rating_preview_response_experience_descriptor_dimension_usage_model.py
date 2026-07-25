from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar(
    "T", bound="RobloxApiDevelopModelsBuildGeneratedRatingPreviewResponseExperienceDescriptorDimensionUsageModel"
)


@_attrs_define
class RobloxApiDevelopModelsBuildGeneratedRatingPreviewResponseExperienceDescriptorDimensionUsageModel:
    """Descriptor dimension usage.

    Attributes:
        dimension_name (str | Unset): Dimension name.
        dimension_value (str | Unset): Dimension value.
    """

    dimension_name: str | Unset = UNSET
    dimension_value: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        dimension_name = self.dimension_name

        dimension_value = self.dimension_value

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if dimension_name is not UNSET:
            field_dict["dimensionName"] = dimension_name
        if dimension_value is not UNSET:
            field_dict["dimensionValue"] = dimension_value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        dimension_name = d.pop("dimensionName", UNSET)

        dimension_value = d.pop("dimensionValue", UNSET)

        roblox_api_develop_models_build_generated_rating_preview_response_experience_descriptor_dimension_usage_model = cls(
            dimension_name=dimension_name,
            dimension_value=dimension_value,
        )

        return roblox_api_develop_models_build_generated_rating_preview_response_experience_descriptor_dimension_usage_model
