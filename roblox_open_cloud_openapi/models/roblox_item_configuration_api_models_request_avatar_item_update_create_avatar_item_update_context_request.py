from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.roblox_item_configuration_api_models_request_avatar_item_update_create_avatar_item_update_context_request_asset_type import (
    RobloxItemConfigurationApiModelsRequestAvatarItemUpdateCreateAvatarItemUpdateContextRequestAssetType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxItemConfigurationApiModelsRequestAvatarItemUpdateCreateAvatarItemUpdateContextRequest")


@_attrs_define
class RobloxItemConfigurationApiModelsRequestAvatarItemUpdateCreateAvatarItemUpdateContextRequest:
    """DTO of the incoming request from the client to create an avatar item update context, which mints
    the parent update operation for an existing catalog avatar item.

        Attributes:
            original_asset_id (int | Unset): The asset id of the existing catalog item being updated.
            asset_type (RobloxItemConfigurationApiModelsRequestAvatarItemUpdateCreateAvatarItemUpdateContextRequestAssetType
                | Unset): The asset type of the item being updated. Must match the original item's asset type: an
                update swaps content on the same item, it cannot change the item's type. ['Invalid' = 0, 'Image' = 1, 'Tshirt' =
                2, 'Audio' = 3, 'Mesh' = 4, 'Lua' = 5, 'Html' = 6, 'Text' = 7, 'Hat' = 8, 'Place' = 9, 'Model' = 10, 'Shirt' =
                11, 'Pants' = 12, 'Decal' = 13, 'Avatar' = 16, 'Head' = 17, 'Face' = 18, 'Gear' = 19, 'Badge' = 21,
                'GroupEmblem' = 22, 'Animation' = 24, 'Arms' = 25, 'Legs' = 26, 'Torso' = 27, 'RightArm' = 28, 'LeftArm' = 29,
                'LeftLeg' = 30, 'RightLeg' = 31, 'Package' = 32, 'YoutubeVideo' = 33, 'GamePass' = 34, 'App' = 35, 'Code' = 37,
                'Plugin' = 38, 'SolidModel' = 39, 'MeshPart' = 40, 'HairAccessory' = 41, 'FaceAccessory' = 42, 'NeckAccessory' =
                43, 'ShoulderAccessory' = 44, 'FrontAccessory' = 45, 'BackAccessory' = 46, 'WaistAccessory' = 47,
                'ClimbAnimation' = 48, 'DeathAnimation' = 49, 'FallAnimation' = 50, 'IdleAnimation' = 51, 'JumpAnimation' = 52,
                'RunAnimation' = 53, 'SwimAnimation' = 54, 'WalkAnimation' = 55, 'PoseAnimation' = 56,
                'LocalizationTableManifest' = 59, 'LocalizationTableTranslation' = 60, 'EmoteAnimation' = 61, 'Video' = 62,
                'TexturePack' = 63, 'TshirtAccessory' = 64, 'ShirtAccessory' = 65, 'PantsAccessory' = 66, 'JacketAccessory' =
                67, 'SweaterAccessory' = 68, 'ShortsAccessory' = 69, 'LeftShoeAccessory' = 70, 'RightShoeAccessory' = 71,
                'DressSkirtAccessory' = 72, 'FontFamily' = 73, 'FontFace' = 74, 'MeshHiddenSurfaceRemoval' = 75,
                'EyebrowAccessory' = 76, 'EyelashAccessory' = 77, 'MoodAnimation' = 78, 'DynamicHead' = 79, 'CodeSnippet' = 80,
                'AdsVideo' = 81, 'OtaUpdate' = 82, 'Screenshot' = 83, 'RuntimePropertySet' = 84, 'StorePreviewVideo' = 85,
                'GamePreviewVideo' = 86, 'CreatorExperienceConfig' = 87, 'FaceMakeup' = 88, 'LipMakeup' = 89, 'EyeMakeup' = 90,
                'VoxelFragment' = 91, 'AvatarBackground' = 92, 'TextDocument' = 93, 'Post' = 94, 'AnimatedImage' = 95,
                'ComputeFunction' = 96, 'AvatarSpawnEffect' = 97, 'Voice' = 98]
    """

    original_asset_id: int | Unset = UNSET
    asset_type: (
        RobloxItemConfigurationApiModelsRequestAvatarItemUpdateCreateAvatarItemUpdateContextRequestAssetType | Unset
    ) = UNSET

    def to_dict(self) -> dict[str, Any]:
        original_asset_id = self.original_asset_id

        asset_type: int | Unset = UNSET
        if not isinstance(self.asset_type, Unset):
            asset_type = self.asset_type.value

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if original_asset_id is not UNSET:
            field_dict["originalAssetId"] = original_asset_id
        if asset_type is not UNSET:
            field_dict["assetType"] = asset_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        original_asset_id = d.pop("originalAssetId", UNSET)

        _asset_type = d.pop("assetType", UNSET)
        asset_type: (
            RobloxItemConfigurationApiModelsRequestAvatarItemUpdateCreateAvatarItemUpdateContextRequestAssetType | Unset
        )
        if isinstance(_asset_type, Unset):
            asset_type = UNSET
        else:
            asset_type = (
                RobloxItemConfigurationApiModelsRequestAvatarItemUpdateCreateAvatarItemUpdateContextRequestAssetType(
                    _asset_type
                )
            )

        roblox_item_configuration_api_models_request_avatar_item_update_create_avatar_item_update_context_request = cls(
            original_asset_id=original_asset_id,
            asset_type=asset_type,
        )

        return roblox_item_configuration_api_models_request_avatar_item_update_create_avatar_item_update_context_request
