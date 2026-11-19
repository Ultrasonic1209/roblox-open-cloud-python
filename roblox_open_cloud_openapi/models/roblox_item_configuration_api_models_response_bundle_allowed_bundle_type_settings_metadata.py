from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_item_configuration_api_models_response_bundle_allowed_bundle_type_settings_metadata_allowed_asset_type_settings import (
        RobloxItemConfigurationApiModelsResponseBundleAllowedBundleTypeSettingsMetadataAllowedAssetTypeSettings,
    )
    from ..models.roblox_item_configuration_api_models_response_bundle_price_range import (
        RobloxItemConfigurationApiModelsResponseBundlePriceRange,
    )


T = TypeVar("T", bound="RobloxItemConfigurationApiModelsResponseBundleAllowedBundleTypeSettingsMetadata")


@_attrs_define
class RobloxItemConfigurationApiModelsResponseBundleAllowedBundleTypeSettingsMetadata:
    """Detailed metadata settings for a bundle type.

    Attributes:
        allowed_asset_type_settings
            (RobloxItemConfigurationApiModelsResponseBundleAllowedBundleTypeSettingsMetadataAllowedAssetTypeSettings |
            Unset): For this particular bundle type, provides a map containing allowed asset type and its
            appropriate settings.
        marketplace_fee_percentage (int | Unset): The marketplace fee for uploading this particular bundle type.
        allowed_price_range (RobloxItemConfigurationApiModelsResponseBundlePriceRange | Unset): DTO containing price
            range.
    """

    allowed_asset_type_settings: (
        RobloxItemConfigurationApiModelsResponseBundleAllowedBundleTypeSettingsMetadataAllowedAssetTypeSettings | Unset
    ) = UNSET
    marketplace_fee_percentage: int | Unset = UNSET
    allowed_price_range: RobloxItemConfigurationApiModelsResponseBundlePriceRange | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        allowed_asset_type_settings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.allowed_asset_type_settings, Unset):
            allowed_asset_type_settings = self.allowed_asset_type_settings.to_dict()

        marketplace_fee_percentage = self.marketplace_fee_percentage

        allowed_price_range: dict[str, Any] | Unset = UNSET
        if not isinstance(self.allowed_price_range, Unset):
            allowed_price_range = self.allowed_price_range.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if allowed_asset_type_settings is not UNSET:
            field_dict["allowedAssetTypeSettings"] = allowed_asset_type_settings
        if marketplace_fee_percentage is not UNSET:
            field_dict["marketplaceFeePercentage"] = marketplace_fee_percentage
        if allowed_price_range is not UNSET:
            field_dict["allowedPriceRange"] = allowed_price_range

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_item_configuration_api_models_response_bundle_allowed_bundle_type_settings_metadata_allowed_asset_type_settings import (
            RobloxItemConfigurationApiModelsResponseBundleAllowedBundleTypeSettingsMetadataAllowedAssetTypeSettings,  # noqa: PLC0415
        )
        from ..models.roblox_item_configuration_api_models_response_bundle_price_range import (
            RobloxItemConfigurationApiModelsResponseBundlePriceRange,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _allowed_asset_type_settings = d.pop("allowedAssetTypeSettings", UNSET)
        allowed_asset_type_settings: (
            RobloxItemConfigurationApiModelsResponseBundleAllowedBundleTypeSettingsMetadataAllowedAssetTypeSettings
            | Unset
        )
        if isinstance(_allowed_asset_type_settings, Unset):
            allowed_asset_type_settings = UNSET
        else:
            allowed_asset_type_settings = RobloxItemConfigurationApiModelsResponseBundleAllowedBundleTypeSettingsMetadataAllowedAssetTypeSettings.from_dict(
                _allowed_asset_type_settings
            )

        marketplace_fee_percentage = d.pop("marketplaceFeePercentage", UNSET)

        _allowed_price_range = d.pop("allowedPriceRange", UNSET)
        allowed_price_range: RobloxItemConfigurationApiModelsResponseBundlePriceRange | Unset
        if isinstance(_allowed_price_range, Unset):
            allowed_price_range = UNSET
        else:
            allowed_price_range = RobloxItemConfigurationApiModelsResponseBundlePriceRange.from_dict(
                _allowed_price_range
            )

        roblox_item_configuration_api_models_response_bundle_allowed_bundle_type_settings_metadata = cls(
            allowed_asset_type_settings=allowed_asset_type_settings,
            marketplace_fee_percentage=marketplace_fee_percentage,
            allowed_price_range=allowed_price_range,
        )

        return roblox_item_configuration_api_models_response_bundle_allowed_bundle_type_settings_metadata
