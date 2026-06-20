from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.roblox_web_responses_related_entity_type_response_roblox_platform_assets_asset_type_type import (
    RobloxWebResponsesRelatedEntityTypeResponseRobloxPlatformAssetsAssetTypeType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxWebResponsesRelatedEntityTypeResponseRobloxPlatformAssetsAssetType")


@_attrs_define
class RobloxWebResponsesRelatedEntityTypeResponseRobloxPlatformAssetsAssetType:
    """
    Attributes:
        id (int | Unset):
        type_ (RobloxWebResponsesRelatedEntityTypeResponseRobloxPlatformAssetsAssetTypeType | Unset):  ['Image' = 1,
            'TShirt' = 2, 'Audio' = 3, 'Mesh' = 4, 'Lua' = 5, 'HTML' = 6, 'Text' = 7, 'Hat' = 8, 'Place' = 9, 'Model' = 10,
            'Shirt' = 11, 'Pants' = 12, 'Decal' = 13, 'Avatar' = 16, 'Head' = 17, 'Face' = 18, 'Gear' = 19, 'Badge' = 21,
            'GroupEmblem' = 22, 'Animation' = 24, 'Arms' = 25, 'Legs' = 26, 'Torso' = 27, 'RightArm' = 28, 'LeftArm' = 29,
            'LeftLeg' = 30, 'RightLeg' = 31, 'Package' = 32, 'YouTubeVideo' = 33, 'GamePass' = 34, 'App' = 35, 'Code' = 37,
            'Plugin' = 38, 'SolidModel' = 39, 'MeshPart' = 40, 'HairAccessory' = 41, 'FaceAccessory' = 42, 'NeckAccessory' =
            43, 'ShoulderAccessory' = 44, 'FrontAccessory' = 45, 'BackAccessory' = 46, 'WaistAccessory' = 47,
            'ClimbAnimation' = 48, 'DeathAnimation' = 49, 'FallAnimation' = 50, 'IdleAnimation' = 51, 'JumpAnimation' = 52,
            'RunAnimation' = 53, 'SwimAnimation' = 54, 'WalkAnimation' = 55, 'PoseAnimation' = 56,
            'LocalizationTableManifest' = 59, 'LocalizationTableTranslation' = 60, 'EmoteAnimation' = 61, 'Video' = 62,
            'TexturePack' = 63, 'TShirtAccessory' = 64, 'ShirtAccessory' = 65, 'PantsAccessory' = 66, 'JacketAccessory' =
            67, 'SweaterAccessory' = 68, 'ShortsAccessory' = 69, 'LeftShoeAccessory' = 70, 'RightShoeAccessory' = 71,
            'DressSkirtAccessory' = 72, 'FontFamily' = 73, 'FontFace' = 74, 'MeshHiddenSurfaceRemoval' = 75,
            'EyebrowAccessory' = 76, 'EyelashAccessory' = 77, 'MoodAnimation' = 78, 'DynamicHead' = 79, 'CodeSnippet' = 80,
            'AdsVideo' = 81, 'OtaUpdate' = 82, 'Screenshot' = 83, 'RuntimePropertySet' = 84, 'StorePreviewVideo' = 85,
            'GamePreviewVideo' = 86, 'CreatorExperienceConfig' = 87, 'FaceMakeup' = 88, 'LipMakeup' = 89, 'EyeMakeup' = 90,
            'VoxelFragment' = 91, 'AvatarBackground' = 92, 'TextDocument' = 93]
        name (str | Unset):
    """

    id: int | Unset = UNSET
    type_: RobloxWebResponsesRelatedEntityTypeResponseRobloxPlatformAssetsAssetTypeType | Unset = UNSET
    name: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        type_: int | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        name = self.name

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if type_ is not UNSET:
            field_dict["type"] = type_
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        id = d.pop("id", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: RobloxWebResponsesRelatedEntityTypeResponseRobloxPlatformAssetsAssetTypeType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = RobloxWebResponsesRelatedEntityTypeResponseRobloxPlatformAssetsAssetTypeType(_type_)

        name = d.pop("name", UNSET)

        roblox_web_responses_related_entity_type_response_roblox_platform_assets_asset_type = cls(
            id=id,
            type_=type_,
            name=name,
        )

        return roblox_web_responses_related_entity_type_response_roblox_platform_assets_asset_type
