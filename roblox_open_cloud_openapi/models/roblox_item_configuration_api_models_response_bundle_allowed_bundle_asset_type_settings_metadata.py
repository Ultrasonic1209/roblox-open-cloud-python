from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxItemConfigurationApiModelsResponseBundleAllowedBundleAssetTypeSettingsMetadata")


@_attrs_define
class RobloxItemConfigurationApiModelsResponseBundleAllowedBundleAssetTypeSettingsMetadata:
    """This class encapsulates the settings for each asset type which
    is being added to the given bundle.

        Attributes:
            minimum_quantity (int | Unset): This is the minimum number of this particular asset types that must
                exist in this bundle.
            maximum_quantity (int | Unset): This is the maximum number of this particular asset types that must
                exist in this bundle.
            is_eligible_for_upload (bool | Unset): Boolean flag which indicates whether this particular item is allowed
                to have a new upload by the user.
            allowed_file_extensions (list[str] | Unset): List of string specifying allowed file extensions for upload.
    """

    minimum_quantity: int | Unset = UNSET
    maximum_quantity: int | Unset = UNSET
    is_eligible_for_upload: bool | Unset = UNSET
    allowed_file_extensions: list[str] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        minimum_quantity = self.minimum_quantity

        maximum_quantity = self.maximum_quantity

        is_eligible_for_upload = self.is_eligible_for_upload

        allowed_file_extensions: list[str] | Unset = UNSET
        if not isinstance(self.allowed_file_extensions, Unset):
            allowed_file_extensions = self.allowed_file_extensions

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if minimum_quantity is not UNSET:
            field_dict["minimumQuantity"] = minimum_quantity
        if maximum_quantity is not UNSET:
            field_dict["maximumQuantity"] = maximum_quantity
        if is_eligible_for_upload is not UNSET:
            field_dict["isEligibleForUpload"] = is_eligible_for_upload
        if allowed_file_extensions is not UNSET:
            field_dict["allowedFileExtensions"] = allowed_file_extensions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        minimum_quantity = d.pop("minimumQuantity", UNSET)

        maximum_quantity = d.pop("maximumQuantity", UNSET)

        is_eligible_for_upload = d.pop("isEligibleForUpload", UNSET)

        allowed_file_extensions = cast(list[str], d.pop("allowedFileExtensions", UNSET))

        roblox_item_configuration_api_models_response_bundle_allowed_bundle_asset_type_settings_metadata = cls(
            minimum_quantity=minimum_quantity,
            maximum_quantity=maximum_quantity,
            is_eligible_for_upload=is_eligible_for_upload,
            allowed_file_extensions=allowed_file_extensions,
        )

        return roblox_item_configuration_api_models_response_bundle_allowed_bundle_asset_type_settings_metadata
