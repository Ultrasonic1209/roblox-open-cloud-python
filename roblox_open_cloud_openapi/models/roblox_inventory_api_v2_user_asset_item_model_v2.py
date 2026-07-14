from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.roblox_inventory_api_v2_user_asset_item_model_v2_asset_type import (
    RobloxInventoryApiV2UserAssetItemModelV2AssetType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxInventoryApiV2UserAssetItemModelV2")


@_attrs_define
class RobloxInventoryApiV2UserAssetItemModelV2:
    """The user asset item model for V2 controllers.

    Attributes:
        asset_id (int | Unset): The asset id of the user asset.
        name (str | Unset): The name of asset with id Roblox.Inventory.Api.V2.UserAssetItemModelV2.AssetId.
        asset_type (RobloxInventoryApiV2UserAssetItemModelV2AssetType | Unset): The asset type id of asset with id
            Roblox.Inventory.Api.V2.UserAssetItemModelV2.AssetId. ['Image' = 1, 'TShirt' = 2, 'Audio' = 3, 'Mesh' = 4, 'Lua'
            = 5, 'HTML' = 6, 'Text' = 7, 'Hat' = 8, 'Place' = 9, 'Model' = 10, 'Shirt' = 11, 'Pants' = 12, 'Decal' = 13,
            'Avatar' = 16, 'Head' = 17, 'Face' = 18, 'Gear' = 19, 'Badge' = 21, 'GroupEmblem' = 22, 'Animation' = 24, 'Arms'
            = 25, 'Legs' = 26, 'Torso' = 27, 'RightArm' = 28, 'LeftArm' = 29, 'LeftLeg' = 30, 'RightLeg' = 31, 'Package' =
            32, 'YouTubeVideo' = 33, 'GamePass' = 34, 'App' = 35, 'Code' = 37, 'Plugin' = 38, 'SolidModel' = 39, 'MeshPart'
            = 40, 'HairAccessory' = 41, 'FaceAccessory' = 42, 'NeckAccessory' = 43, 'ShoulderAccessory' = 44,
            'FrontAccessory' = 45, 'BackAccessory' = 46, 'WaistAccessory' = 47, 'ClimbAnimation' = 48, 'DeathAnimation' =
            49, 'FallAnimation' = 50, 'IdleAnimation' = 51, 'JumpAnimation' = 52, 'RunAnimation' = 53, 'SwimAnimation' = 54,
            'WalkAnimation' = 55, 'PoseAnimation' = 56, 'LocalizationTableManifest' = 59, 'LocalizationTableTranslation' =
            60, 'EmoteAnimation' = 61, 'Video' = 62, 'TexturePack' = 63, 'TShirtAccessory' = 64, 'ShirtAccessory' = 65,
            'PantsAccessory' = 66, 'JacketAccessory' = 67, 'SweaterAccessory' = 68, 'ShortsAccessory' = 69,
            'LeftShoeAccessory' = 70, 'RightShoeAccessory' = 71, 'DressSkirtAccessory' = 72, 'FontFamily' = 73, 'FontFace' =
            74, 'MeshHiddenSurfaceRemoval' = 75, 'EyebrowAccessory' = 76, 'EyelashAccessory' = 77, 'MoodAnimation' = 78,
            'DynamicHead' = 79, 'CodeSnippet' = 80, 'AdsVideo' = 81, 'OtaUpdate' = 82, 'Screenshot' = 83,
            'RuntimePropertySet' = 84, 'StorePreviewVideo' = 85, 'GamePreviewVideo' = 86, 'CreatorExperienceConfig' = 87,
            'FaceMakeup' = 88, 'LipMakeup' = 89, 'EyeMakeup' = 90, 'VoxelFragment' = 91, 'AvatarBackground' = 92,
            'TextDocument' = 93, 'Post' = 94]
        created (datetime.datetime | Unset): The created date time of the user asset.
    """

    asset_id: int | Unset = UNSET
    name: str | Unset = UNSET
    asset_type: RobloxInventoryApiV2UserAssetItemModelV2AssetType | Unset = UNSET
    created: datetime.datetime | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        asset_id = self.asset_id

        name = self.name

        asset_type: int | Unset = UNSET
        if not isinstance(self.asset_type, Unset):
            asset_type = self.asset_type.value

        created: str | Unset = UNSET
        if not isinstance(self.created, Unset):
            created = self.created.isoformat()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if asset_id is not UNSET:
            field_dict["assetId"] = asset_id
        if name is not UNSET:
            field_dict["name"] = name
        if asset_type is not UNSET:
            field_dict["assetType"] = asset_type
        if created is not UNSET:
            field_dict["created"] = created

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        asset_id = d.pop("assetId", UNSET)

        name = d.pop("name", UNSET)

        _asset_type = d.pop("assetType", UNSET)
        asset_type: RobloxInventoryApiV2UserAssetItemModelV2AssetType | Unset
        if isinstance(_asset_type, Unset):
            asset_type = UNSET
        else:
            asset_type = RobloxInventoryApiV2UserAssetItemModelV2AssetType(_asset_type)

        _created = d.pop("created", UNSET)
        created: datetime.datetime | Unset
        if isinstance(_created, Unset):
            created = UNSET
        else:
            created = datetime.datetime.fromisoformat(_created)

        roblox_inventory_api_v2_user_asset_item_model_v2 = cls(
            asset_id=asset_id,
            name=name,
            asset_type=asset_type,
            created=created,
        )

        return roblox_inventory_api_v2_user_asset_item_model_v2
