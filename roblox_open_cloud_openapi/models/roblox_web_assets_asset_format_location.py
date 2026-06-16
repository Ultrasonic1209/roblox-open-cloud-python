from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_asset_delivery_api_asset_metadata import RobloxAssetDeliveryApiAssetMetadata


T = TypeVar("T", bound="RobloxWebAssetsAssetFormatLocation")


@_attrs_define
class RobloxWebAssetsAssetFormatLocation:
    """
    Attributes:
        asset_format (str | Unset):
        location (str | Unset):
        asset_metadatas (list[RobloxAssetDeliveryApiAssetMetadata] | Unset):
    """

    asset_format: str | Unset = UNSET
    location: str | Unset = UNSET
    asset_metadatas: list[RobloxAssetDeliveryApiAssetMetadata] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        asset_format = self.asset_format

        location = self.location

        asset_metadatas: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.asset_metadatas, Unset):
            asset_metadatas = []
            for asset_metadatas_item_data in self.asset_metadatas:
                asset_metadatas_item = asset_metadatas_item_data.to_dict()
                asset_metadatas.append(asset_metadatas_item)

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if asset_format is not UNSET:
            field_dict["assetFormat"] = asset_format
        if location is not UNSET:
            field_dict["location"] = location
        if asset_metadatas is not UNSET:
            field_dict["assetMetadatas"] = asset_metadatas

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_asset_delivery_api_asset_metadata import RobloxAssetDeliveryApiAssetMetadata

        d = dict(src_dict)
        asset_format = d.pop("assetFormat", UNSET)

        location = d.pop("location", UNSET)

        _asset_metadatas = d.pop("assetMetadatas", UNSET)
        asset_metadatas: list[RobloxAssetDeliveryApiAssetMetadata] | Unset = UNSET
        if _asset_metadatas is not UNSET:
            asset_metadatas = []
            for asset_metadatas_item_data in _asset_metadatas:
                asset_metadatas_item = RobloxAssetDeliveryApiAssetMetadata.from_dict(asset_metadatas_item_data)

                asset_metadatas.append(asset_metadatas_item)

        roblox_web_assets_asset_format_location = cls(
            asset_format=asset_format,
            location=location,
            asset_metadatas=asset_metadatas,
        )

        return roblox_web_assets_asset_format_location
