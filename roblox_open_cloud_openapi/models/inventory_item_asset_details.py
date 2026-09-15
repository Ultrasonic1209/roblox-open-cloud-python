from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..models.inventory_item_asset_details_inventory_item_asset_type import (
    InventoryItemAssetDetailsInventoryItemAssetType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.inventory_item_collectible_details import InventoryItemCollectibleDetails


T = TypeVar("T", bound="InventoryItemAssetDetails")


@_attrs_define
class InventoryItemAssetDetails:
    """Specific fields only applicable to assets

    Attributes:
        asset_id (str | Unset): A unique ID that identifies an asset.
        inventory_item_asset_type (InventoryItemAssetDetailsInventoryItemAssetType | Unset): The specific asset type of
            this item.
        instance_id (str | Unset): A unique ID that identifies an instance or "copy" of the asset that's
            owned by a user.
        collectible_details (InventoryItemCollectibleDetails | Unset): Specific fields that are applicable to a
            collectible.
    """

    asset_id: str | Unset = UNSET
    inventory_item_asset_type: InventoryItemAssetDetailsInventoryItemAssetType | Unset = UNSET
    instance_id: str | Unset = UNSET
    collectible_details: InventoryItemCollectibleDetails | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        asset_id = self.asset_id

        inventory_item_asset_type: str | Unset = UNSET
        if not isinstance(self.inventory_item_asset_type, Unset):
            inventory_item_asset_type = self.inventory_item_asset_type.value

        instance_id = self.instance_id

        collectible_details: dict[str, Any] | Unset = UNSET
        if not isinstance(self.collectible_details, Unset):
            collectible_details = self.collectible_details.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if asset_id is not UNSET:
            field_dict["assetId"] = asset_id
        if inventory_item_asset_type is not UNSET:
            field_dict["inventoryItemAssetType"] = inventory_item_asset_type
        if instance_id is not UNSET:
            field_dict["instanceId"] = instance_id
        if collectible_details is not UNSET:
            field_dict["collectibleDetails"] = collectible_details

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.inventory_item_collectible_details import InventoryItemCollectibleDetails

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        asset_id = d.pop("assetId", UNSET)

        _inventory_item_asset_type = d.pop("inventoryItemAssetType", UNSET)
        inventory_item_asset_type: InventoryItemAssetDetailsInventoryItemAssetType | Unset
        if isinstance(_inventory_item_asset_type, Unset):
            inventory_item_asset_type = UNSET
        else:
            inventory_item_asset_type = InventoryItemAssetDetailsInventoryItemAssetType(_inventory_item_asset_type)

        instance_id = d.pop("instanceId", UNSET)

        _collectible_details = d.pop("collectibleDetails", UNSET)
        collectible_details: InventoryItemCollectibleDetails | Unset
        if isinstance(_collectible_details, Unset):
            collectible_details = UNSET
        else:
            collectible_details = InventoryItemCollectibleDetails.from_dict(_collectible_details)

        inventory_item_asset_details = cls(
            asset_id=asset_id,
            inventory_item_asset_type=inventory_item_asset_type,
            instance_id=instance_id,
            collectible_details=collectible_details,
        )

        return inventory_item_asset_details
