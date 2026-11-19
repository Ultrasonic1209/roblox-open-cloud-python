from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_item_configuration_api_asset_details import RobloxItemConfigurationApiAssetDetails
    from ..models.roblox_item_configuration_api_bundle_details import RobloxItemConfigurationApiBundleDetails


T = TypeVar("T", bound="RobloxItemConfigurationApiMarketplaceItemDetails")


@_attrs_define
class RobloxItemConfigurationApiMarketplaceItemDetails:
    """The marketplace item details.
    Only one of the AssetDetails and BundleDetails will be set.

        Attributes:
            asset_details (RobloxItemConfigurationApiAssetDetails | Unset): The asset details.
            bundle_details (RobloxItemConfigurationApiBundleDetails | Unset): The bundle details.
    """

    asset_details: RobloxItemConfigurationApiAssetDetails | Unset = UNSET
    bundle_details: RobloxItemConfigurationApiBundleDetails | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        asset_details: dict[str, Any] | Unset = UNSET
        if not isinstance(self.asset_details, Unset):
            asset_details = self.asset_details.to_dict()

        bundle_details: dict[str, Any] | Unset = UNSET
        if not isinstance(self.bundle_details, Unset):
            bundle_details = self.bundle_details.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if asset_details is not UNSET:
            field_dict["assetDetails"] = asset_details
        if bundle_details is not UNSET:
            field_dict["bundleDetails"] = bundle_details

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_item_configuration_api_asset_details import RobloxItemConfigurationApiAssetDetails  # noqa: PLC0415
        from ..models.roblox_item_configuration_api_bundle_details import RobloxItemConfigurationApiBundleDetails  # noqa: PLC0415

        d = dict(src_dict)
        _asset_details = d.pop("assetDetails", UNSET)
        asset_details: RobloxItemConfigurationApiAssetDetails | Unset
        if isinstance(_asset_details, Unset):
            asset_details = UNSET
        else:
            asset_details = RobloxItemConfigurationApiAssetDetails.from_dict(_asset_details)

        _bundle_details = d.pop("bundleDetails", UNSET)
        bundle_details: RobloxItemConfigurationApiBundleDetails | Unset
        if isinstance(_bundle_details, Unset):
            bundle_details = UNSET
        else:
            bundle_details = RobloxItemConfigurationApiBundleDetails.from_dict(_bundle_details)

        roblox_item_configuration_api_marketplace_item_details = cls(
            asset_details=asset_details,
            bundle_details=bundle_details,
        )

        return roblox_item_configuration_api_marketplace_item_details
