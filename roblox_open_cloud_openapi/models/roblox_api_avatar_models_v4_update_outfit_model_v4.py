from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..models.roblox_api_avatar_models_v4_update_outfit_model_v4_outfit_type import (
    RobloxApiAvatarModelsV4UpdateOutfitModelV4OutfitType,
)
from ..models.roblox_api_avatar_models_v4_update_outfit_model_v4_player_avatar_type import (
    RobloxApiAvatarModelsV4UpdateOutfitModelV4PlayerAvatarType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_api_avatar_models_asset_wear_model import RobloxApiAvatarModelsAssetWearModel
    from ..models.roblox_api_avatar_models_body_colors_model_v4 import RobloxApiAvatarModelsBodyColorsModelV4
    from ..models.roblox_web_responses_avatar_scale_model import RobloxWebResponsesAvatarScaleModel


T = TypeVar("T", bound="RobloxApiAvatarModelsV4UpdateOutfitModelV4")


@_attrs_define
class RobloxApiAvatarModelsV4UpdateOutfitModelV4:
    """A model containing core outfit fields to update.

    Attributes:
        name (str | Unset): The outfit name.
        body_colors (RobloxApiAvatarModelsBodyColorsModelV4 | Unset): A model containing RGB hex colors for each body
            part.
        assets (list[RobloxApiAvatarModelsAssetWearModel] | Unset): The assets on the outfit.
        scale (RobloxWebResponsesAvatarScaleModel | Unset):
        player_avatar_type (RobloxApiAvatarModelsV4UpdateOutfitModelV4PlayerAvatarType | Unset): The player avatar type.
        outfit_type (RobloxApiAvatarModelsV4UpdateOutfitModelV4OutfitType | Unset): The type of outfit (for example
            Avatar or Makeup). Defaults to Avatar when omitted.
    """

    name: str | Unset = UNSET
    body_colors: RobloxApiAvatarModelsBodyColorsModelV4 | Unset = UNSET
    assets: list[RobloxApiAvatarModelsAssetWearModel] | Unset = UNSET
    scale: RobloxWebResponsesAvatarScaleModel | Unset = UNSET
    player_avatar_type: RobloxApiAvatarModelsV4UpdateOutfitModelV4PlayerAvatarType | Unset = UNSET
    outfit_type: RobloxApiAvatarModelsV4UpdateOutfitModelV4OutfitType | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        body_colors: dict[str, Any] | Unset = UNSET
        if not isinstance(self.body_colors, Unset):
            body_colors = self.body_colors.to_dict()

        assets: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.assets, Unset):
            assets = []
            for assets_item_data in self.assets:
                assets_item = assets_item_data.to_dict()
                assets.append(assets_item)

        scale: dict[str, Any] | Unset = UNSET
        if not isinstance(self.scale, Unset):
            scale = self.scale.to_dict()

        player_avatar_type: int | Unset = UNSET
        if not isinstance(self.player_avatar_type, Unset):
            player_avatar_type = self.player_avatar_type.value

        outfit_type: int | Unset = UNSET
        if not isinstance(self.outfit_type, Unset):
            outfit_type = self.outfit_type.value

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if body_colors is not UNSET:
            field_dict["bodyColors"] = body_colors
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
        from ..models.roblox_api_avatar_models_body_colors_model_v4 import RobloxApiAvatarModelsBodyColorsModelV4
        from ..models.roblox_web_responses_avatar_scale_model import RobloxWebResponsesAvatarScaleModel

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        name = d.pop("name", UNSET)

        _body_colors = d.pop("bodyColors", UNSET)
        body_colors: RobloxApiAvatarModelsBodyColorsModelV4 | Unset
        if isinstance(_body_colors, Unset):
            body_colors = UNSET
        else:
            body_colors = RobloxApiAvatarModelsBodyColorsModelV4.from_dict(_body_colors)

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

        _player_avatar_type = d.pop("playerAvatarType", UNSET)
        player_avatar_type: RobloxApiAvatarModelsV4UpdateOutfitModelV4PlayerAvatarType | Unset
        if isinstance(_player_avatar_type, Unset):
            player_avatar_type = UNSET
        else:
            player_avatar_type = RobloxApiAvatarModelsV4UpdateOutfitModelV4PlayerAvatarType(_player_avatar_type)

        _outfit_type = d.pop("outfitType", UNSET)
        outfit_type: RobloxApiAvatarModelsV4UpdateOutfitModelV4OutfitType | Unset
        if isinstance(_outfit_type, Unset):
            outfit_type = UNSET
        else:
            outfit_type = RobloxApiAvatarModelsV4UpdateOutfitModelV4OutfitType(_outfit_type)

        roblox_api_avatar_models_v4_update_outfit_model_v4 = cls(
            name=name,
            body_colors=body_colors,
            assets=assets,
            scale=scale,
            player_avatar_type=player_avatar_type,
            outfit_type=outfit_type,
        )

        return roblox_api_avatar_models_v4_update_outfit_model_v4
