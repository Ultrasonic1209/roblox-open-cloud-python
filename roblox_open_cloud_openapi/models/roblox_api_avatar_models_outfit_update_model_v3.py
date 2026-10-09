from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..models.roblox_api_avatar_models_outfit_update_model_v3_outfit_type import (
    RobloxApiAvatarModelsOutfitUpdateModelV3OutfitType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_api_avatar_models_asset_wear_model import RobloxApiAvatarModelsAssetWearModel
    from ..models.roblox_api_avatar_models_body_colors_3_model import RobloxApiAvatarModelsBodyColors3Model
    from ..models.roblox_web_responses_avatar_scale_model import RobloxWebResponsesAvatarScaleModel


T = TypeVar("T", bound="RobloxApiAvatarModelsOutfitUpdateModelV3")


@_attrs_define
class RobloxApiAvatarModelsOutfitUpdateModelV3:
    """A model containing details needed to update or create an outfit.

    Attributes:
        name (str | Unset): The outfit name.
        body_color_3_s (RobloxApiAvatarModelsBodyColors3Model | Unset): A model containing RGB hex colors for each body
            part.
        assets (list[RobloxApiAvatarModelsAssetWearModel] | Unset): Array of assets.
        scale (RobloxWebResponsesAvatarScaleModel | Unset):
        player_avatar_type (str | Unset): The avatar scale.
        outfit_type (RobloxApiAvatarModelsOutfitUpdateModelV3OutfitType | Unset): The type of outfit.
    """

    name: str | Unset = UNSET
    body_color_3_s: RobloxApiAvatarModelsBodyColors3Model | Unset = UNSET
    assets: list[RobloxApiAvatarModelsAssetWearModel] | Unset = UNSET
    scale: RobloxWebResponsesAvatarScaleModel | Unset = UNSET
    player_avatar_type: str | Unset = UNSET
    outfit_type: RobloxApiAvatarModelsOutfitUpdateModelV3OutfitType | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        body_color_3_s: dict[str, Any] | Unset = UNSET
        if not isinstance(self.body_color_3_s, Unset):
            body_color_3_s = self.body_color_3_s.to_dict()

        assets: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.assets, Unset):
            assets = []
            for assets_item_data in self.assets:
                assets_item = assets_item_data.to_dict()
                assets.append(assets_item)

        scale: dict[str, Any] | Unset = UNSET
        if not isinstance(self.scale, Unset):
            scale = self.scale.to_dict()

        player_avatar_type = self.player_avatar_type

        outfit_type: int | Unset = UNSET
        if not isinstance(self.outfit_type, Unset):
            outfit_type = self.outfit_type.value

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if body_color_3_s is not UNSET:
            field_dict["bodyColor3s"] = body_color_3_s
        if assets is not UNSET:
            field_dict["assets"] = assets
        if scale is not UNSET:
            field_dict["scale"] = scale
        if player_avatar_type is not UNSET:
            field_dict["playerAvatarType"] = player_avatar_type
        if outfit_type is not UNSET:
            field_dict["outfitType"] = outfit_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_api_avatar_models_asset_wear_model import RobloxApiAvatarModelsAssetWearModel
        from ..models.roblox_api_avatar_models_body_colors_3_model import RobloxApiAvatarModelsBodyColors3Model
        from ..models.roblox_web_responses_avatar_scale_model import RobloxWebResponsesAvatarScaleModel

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        name = d.pop("name", UNSET)

        _body_color_3_s = d.pop("bodyColor3s", UNSET)
        body_color_3_s: RobloxApiAvatarModelsBodyColors3Model | Unset
        if isinstance(_body_color_3_s, Unset):
            body_color_3_s = UNSET
        else:
            body_color_3_s = RobloxApiAvatarModelsBodyColors3Model.from_dict(_body_color_3_s)

        _assets = d.pop("assets", UNSET)
        assets: list[RobloxApiAvatarModelsAssetWearModel] | Unset = UNSET
        if _assets is not UNSET:
            assets = []
            for assets_item_data in _assets:
                assets_item = RobloxApiAvatarModelsAssetWearModel.from_dict(assets_item_data)

                assets.append(assets_item)

        _scale = d.pop("scale", UNSET)
        scale: RobloxWebResponsesAvatarScaleModel | Unset
        if isinstance(_scale, Unset):
            scale = UNSET
        else:
            scale = RobloxWebResponsesAvatarScaleModel.from_dict(_scale)

        player_avatar_type = d.pop("playerAvatarType", UNSET)

        _outfit_type = d.pop("outfitType", UNSET)
        outfit_type: RobloxApiAvatarModelsOutfitUpdateModelV3OutfitType | Unset
        if isinstance(_outfit_type, Unset):
            outfit_type = UNSET
        else:
            outfit_type = RobloxApiAvatarModelsOutfitUpdateModelV3OutfitType(_outfit_type)

        roblox_api_avatar_models_outfit_update_model_v3 = cls(
            name=name,
            body_color_3_s=body_color_3_s,
            assets=assets,
            scale=scale,
            player_avatar_type=player_avatar_type,
            outfit_type=outfit_type,
        )

        return roblox_api_avatar_models_outfit_update_model_v3
