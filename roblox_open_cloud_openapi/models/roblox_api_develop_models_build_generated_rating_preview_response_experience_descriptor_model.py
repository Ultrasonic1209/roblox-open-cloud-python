from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxApiDevelopModelsBuildGeneratedRatingPreviewResponseExperienceDescriptorModel")


@_attrs_define
class RobloxApiDevelopModelsBuildGeneratedRatingPreviewResponseExperienceDescriptorModel:
    """Experience descriptor definition.

    Attributes:
        name (str | Unset): Descriptor name.
        display_name (str | Unset): Localized descriptor display name.
        compliance_api_supported (bool | Unset): Whether the descriptor is supported by the Compliance API.
        icon_url (str | Unset): Descriptor icon URL.
    """

    name: str | Unset = UNSET
    display_name: str | Unset = UNSET
    compliance_api_supported: bool | Unset = UNSET
    icon_url: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        display_name = self.display_name

        compliance_api_supported = self.compliance_api_supported

        icon_url = self.icon_url

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if compliance_api_supported is not UNSET:
            field_dict["complianceApiSupported"] = compliance_api_supported
        if icon_url is not UNSET:
            field_dict["iconUrl"] = icon_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        name = d.pop("name", UNSET)

        display_name = d.pop("displayName", UNSET)

        compliance_api_supported = d.pop("complianceApiSupported", UNSET)

        icon_url = d.pop("iconUrl", UNSET)

        roblox_api_develop_models_build_generated_rating_preview_response_experience_descriptor_model = cls(
            name=name,
            display_name=display_name,
            compliance_api_supported=compliance_api_supported,
            icon_url=icon_url,
        )

        return roblox_api_develop_models_build_generated_rating_preview_response_experience_descriptor_model
