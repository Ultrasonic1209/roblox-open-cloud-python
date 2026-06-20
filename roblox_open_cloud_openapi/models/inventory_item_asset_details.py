from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

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
        asset_id (str | Unset): A unique ID that identifies an asset. Example: 12928981934.
        inventory_item_asset_type (InventoryItemAssetDetailsInventoryItemAssetType | Unset): The specific asset type of
            this item.

            Possible values:

              | Value | Description |
              | --- | --- |
              | INVENTORY_ITEM_ASSET_TYPE_UNSPECIFIED | Default InventoryItemAssetType |
              | CLASSIC_TSHIRT | Classic Tshirt |
              | AUDIO | Audio |
              | HAT | Hat |
              | MODEL | Model |
              | CLASSIC_SHIRT | Classic Shirt |
              | CLASSIC_PANTS | Classic Pants |
              | DECAL | Decal |
              | CLASSIC_HEAD | Classic Head |
              | FACE | Face |
              | GEAR | Gear |
              | ANIMATION | Animation |
              | TORSO | Torso |
              | RIGHT_ARM | Right Arm |
              | LEFT_ARM | Left Arm |
              | LEFT_LEG | Left Leg |
              | RIGHT_LEG | Right Leg |
              | PACKAGE | Package |
              | PLUGIN | Plugin |
              | MESH_PART | Mesh Part |
              | HAIR_ACCESSORY | Hair Accessory |
              | FACE_ACCESSORY | Face Accessory |
              | NECK_ACCESSORY | Neck Accessory |
              | SHOULDER_ACCESSORY | Shoulder Accessory |
              | FRONT_ACCESSORY | Front Accessory |
              | BACK_ACCESSORY | Back Accessory |
              | WAIST_ACCESSORY | Waist Accessory |
              | CLIMB_ANIMATION | Climb Animation |
              | DEATH_ANIMATION | Death Animation |
              | FALL_ANIMATION | Fall Animation |
              | IDLE_ANIMATION | Idle Animation |
              | JUMP_ANIMATION | Jump Animation |
              | RUN_ANIMATION | Run Animation |
              | SWIM_ANIMATION | Swim Animation |
              | WALK_ANIMATION | Walk Animation |
              | POSE_ANIMATION | Pose Animation |
              | EMOTE_ANIMATION | Emote Animation |
              | VIDEO | Video |
              | TSHIRT_ACCESSORY | Tshirt Accessory |
              | SHIRT_ACCESSORY | Shirt Accessory |
              | PANTS_ACCESSORY | Pants Accessory |
              | JACKET_ACCESSORY | Jacket Accessory |
              | SWEATER_ACCESSORY | Sweater Accessory |
              | SHORTS_ACCESSORY | Shorts Accessory |
              | LEFT_SHOE_ACCESSORY | Left Shoe Accessory |
              | RIGHT_SHOE_ACCESSORY | Right Shoe Accessory |
              | DRESS_SKIRT_ACCESSORY | Dress Skirt Accessory |
              | EYEBROW_ACCESSORY | Eyebrow Accessory |
              | EYELASH_ACCESSORY | Eyelash Accessory |
              | MOOD_ANIMATION | Mood Animation |
              | DYNAMIC_HEAD | Dynamic Head |
              | CREATED_PLACE | Created Place |
              | PURCHASED_PLACE | Purchased Place | Example: INVENTORY_ITEM_ASSET_TYPE_UNSPECIFIED.
        instance_id (str | Unset): A unique ID that identifies an instance or "copy" of the asset that's
            owned by a user. Example: 173413781720.
        collectible_details (InventoryItemCollectibleDetails | Unset): Specific fields that are applicable to a
            collectible.
    """

    asset_id: str | Unset = UNSET
    inventory_item_asset_type: InventoryItemAssetDetailsInventoryItemAssetType | Unset = UNSET
    instance_id: str | Unset = UNSET
    collectible_details: InventoryItemCollectibleDetails | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

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
        field_dict.update(self.additional_properties)
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

        inventory_item_asset_details.additional_properties = d
        return inventory_item_asset_details

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
