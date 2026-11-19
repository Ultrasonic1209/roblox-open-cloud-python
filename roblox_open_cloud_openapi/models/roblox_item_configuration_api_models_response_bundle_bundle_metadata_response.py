from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_item_configuration_api_models_response_bundle_bundle_metadata_response_allowed_bundle_type_settings import (
        RobloxItemConfigurationApiModelsResponseBundleBundleMetadataResponseAllowedBundleTypeSettings,
    )


T = TypeVar("T", bound="RobloxItemConfigurationApiModelsResponseBundleBundleMetadataResponse")


@_attrs_define
class RobloxItemConfigurationApiModelsResponseBundleBundleMetadataResponse:
    """Metadata response for Bundle.

    Attributes:
        is_bundles_controller_enabled (bool | Unset): Indicates whether the entire controller is allowed to be accessed.
        is_bundles_creation_enabled (bool | Unset): Indicates whether bundles creation is allowed.
        is_bundles_publishing_enabled (bool | Unset): Indicates whether bundles publishing is allowed.
        allowed_bundle_type_settings
            (RobloxItemConfigurationApiModelsResponseBundleBundleMetadataResponseAllowedBundleTypeSettings | Unset): A map
            containing allowed bundle type to all of its settings metadata.
        is_group_bundles_upload_enabled (bool | Unset): Whether group bundle upload is enabled.
    """

    is_bundles_controller_enabled: bool | Unset = UNSET
    is_bundles_creation_enabled: bool | Unset = UNSET
    is_bundles_publishing_enabled: bool | Unset = UNSET
    allowed_bundle_type_settings: (
        RobloxItemConfigurationApiModelsResponseBundleBundleMetadataResponseAllowedBundleTypeSettings | Unset
    ) = UNSET
    is_group_bundles_upload_enabled: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        is_bundles_controller_enabled = self.is_bundles_controller_enabled

        is_bundles_creation_enabled = self.is_bundles_creation_enabled

        is_bundles_publishing_enabled = self.is_bundles_publishing_enabled

        allowed_bundle_type_settings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.allowed_bundle_type_settings, Unset):
            allowed_bundle_type_settings = self.allowed_bundle_type_settings.to_dict()

        is_group_bundles_upload_enabled = self.is_group_bundles_upload_enabled

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if is_bundles_controller_enabled is not UNSET:
            field_dict["isBundlesControllerEnabled"] = is_bundles_controller_enabled
        if is_bundles_creation_enabled is not UNSET:
            field_dict["isBundlesCreationEnabled"] = is_bundles_creation_enabled
        if is_bundles_publishing_enabled is not UNSET:
            field_dict["isBundlesPublishingEnabled"] = is_bundles_publishing_enabled
        if allowed_bundle_type_settings is not UNSET:
            field_dict["allowedBundleTypeSettings"] = allowed_bundle_type_settings
        if is_group_bundles_upload_enabled is not UNSET:
            field_dict["isGroupBundlesUploadEnabled"] = is_group_bundles_upload_enabled

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_item_configuration_api_models_response_bundle_bundle_metadata_response_allowed_bundle_type_settings import (
            RobloxItemConfigurationApiModelsResponseBundleBundleMetadataResponseAllowedBundleTypeSettings,  # noqa: PLC0415
        )

        d = dict(src_dict)
        is_bundles_controller_enabled = d.pop("isBundlesControllerEnabled", UNSET)

        is_bundles_creation_enabled = d.pop("isBundlesCreationEnabled", UNSET)

        is_bundles_publishing_enabled = d.pop("isBundlesPublishingEnabled", UNSET)

        _allowed_bundle_type_settings = d.pop("allowedBundleTypeSettings", UNSET)
        allowed_bundle_type_settings: (
            RobloxItemConfigurationApiModelsResponseBundleBundleMetadataResponseAllowedBundleTypeSettings | Unset
        )
        if isinstance(_allowed_bundle_type_settings, Unset):
            allowed_bundle_type_settings = UNSET
        else:
            allowed_bundle_type_settings = (
                RobloxItemConfigurationApiModelsResponseBundleBundleMetadataResponseAllowedBundleTypeSettings.from_dict(
                    _allowed_bundle_type_settings
                )
            )

        is_group_bundles_upload_enabled = d.pop("isGroupBundlesUploadEnabled", UNSET)

        roblox_item_configuration_api_models_response_bundle_bundle_metadata_response = cls(
            is_bundles_controller_enabled=is_bundles_controller_enabled,
            is_bundles_creation_enabled=is_bundles_creation_enabled,
            is_bundles_publishing_enabled=is_bundles_publishing_enabled,
            allowed_bundle_type_settings=allowed_bundle_type_settings,
            is_group_bundles_upload_enabled=is_group_bundles_upload_enabled,
        )

        return roblox_item_configuration_api_models_response_bundle_bundle_metadata_response
