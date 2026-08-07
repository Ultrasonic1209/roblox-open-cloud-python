from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..models.roblox_api_avatar_models_v4_outfit_model_v4_outfit_type import (
    RobloxApiAvatarModelsV4OutfitModelV4OutfitType,
)
from ..models.roblox_api_avatar_models_v4_outfit_model_v4_player_avatar_type import (
    RobloxApiAvatarModelsV4OutfitModelV4PlayerAvatarType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_api_avatar_models_asset_model_v2 import RobloxApiAvatarModelsAssetModelV2
    from ..models.roblox_api_avatar_models_body_colors_model_v4 import RobloxApiAvatarModelsBodyColorsModelV4
    from ..models.roblox_web_responses_avatar_scale_model import RobloxWebResponsesAvatarScaleModel


T = TypeVar("T", bound="RobloxApiAvatarModelsV4OutfitModelV4")


@_attrs_define
class RobloxApiAvatarModelsV4OutfitModelV4:
    """A model containing core outfit details.

    Attributes:
        universe_id (int | Unset): The universe id of the outfit, null when outfit is not created in-experience
        inventory_type (str | Unset): The inventory type of the outfit.
        id (str | Unset): The outfit id.
        name (str | Unset): The outfit name.
        is_editable (bool | Unset): Whether the outfit can be modified by the user.
        outfit_type (RobloxApiAvatarModelsV4OutfitModelV4OutfitType | Unset): The type of the outfit.
        assets (list[RobloxApiAvatarModelsAssetModelV2] | Unset): The assets on the outfit.
        body_colors (RobloxApiAvatarModelsBodyColorsModelV4 | Unset): A model containing RGB hex colors for each body
            part.
        scale (RobloxWebResponsesAvatarScaleModel | Unset):
        player_avatar_type (RobloxApiAvatarModelsV4OutfitModelV4PlayerAvatarType | Unset): The player avatar type.
    """

    universe_id: int | Unset = UNSET
    inventory_type: str | Unset = UNSET
    id: str | Unset = UNSET
    name: str | Unset = UNSET
    is_editable: bool | Unset = UNSET
    outfit_type: RobloxApiAvatarModelsV4OutfitModelV4OutfitType | Unset = UNSET
    assets: list[RobloxApiAvatarModelsAssetModelV2] | Unset = UNSET
    body_colors: RobloxApiAvatarModelsBodyColorsModelV4 | Unset = UNSET
    scale: RobloxWebResponsesAvatarScaleModel | Unset = UNSET
    player_avatar_type: RobloxApiAvatarModelsV4OutfitModelV4PlayerAvatarType | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        universe_id = self.universe_id

        inventory_type = self.inventory_type

        id = self.id

        name = self.name

        is_editable = self.is_editable

        outfit_type: int | Unset = UNSET
        if not isinstance(self.outfit_type, Unset):
            outfit_type = self.outfit_type.value

        assets: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.assets, Unset):
            assets = []
            for assets_item_data in self.assets:
                assets_item = assets_item_data.to_dict()
                assets.append(assets_item)

        body_colors: dict[str, Any] | Unset = UNSET
        if not isinstance(self.body_colors, Unset):
            body_colors = self.body_colors.to_dict()

        scale: dict[str, Any] | Unset = UNSET
        if not isinstance(self.scale, Unset):
            scale = self.scale.to_dict()

        player_avatar_type: int | Unset = UNSET
        if not isinstance(self.player_avatar_type, Unset):
            player_avatar_type = self.player_avatar_type.value

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if universe_id is not UNSET:
            field_dict["universeId"] = universe_id
        if inventory_type is not UNSET:
            field_dict["inventoryType"] = inventory_type
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if is_editable is not UNSET:
            field_dict["isEditable"] = is_editable
        if outfit_type is not UNSET:
            field_dict["outfitType"] = outfit_type
        if assets is not UNSET:
            field_dict["assets"] = assets
        if body_colors is not UNSET:
            field_dict["bodyColors"] = body_colors
        if scale is not UNSET:
            field_dict["scale"] = scale
        if player_avatar_type is not UNSET:
            field_dict["playerAvatarType"] = player_avatar_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_api_avatar_models_asset_model_v2 import RobloxApiAvatarModelsAssetModelV2
        from ..models.roblox_api_avatar_models_body_colors_model_v4 import RobloxApiAvatarModelsBodyColorsModelV4
        from ..models.roblox_web_responses_avatar_scale_model import RobloxWebResponsesAvatarScaleModel

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        universe_id = d.pop("universeId", UNSET)

        inventory_type = d.pop("inventoryType", UNSET)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        is_editable = d.pop("isEditable", UNSET)

        _outfit_type = d.pop("outfitType", UNSET)
        outfit_type: RobloxApiAvatarModelsV4OutfitModelV4OutfitType | Unset
        if isinstance(_outfit_type, Unset):
            outfit_type = UNSET
        else:
            outfit_type = RobloxApiAvatarModelsV4OutfitModelV4OutfitType(_outfit_type)

        _assets = d.pop("assets", UNSET)
        assets: list[RobloxApiAvatarModelsAssetModelV2] | Unset = UNSET
        if _assets is not UNSET:
            assets = []
            for assets_item_data in _assets:
                assets_item = RobloxApiAvatarModelsAssetModelV2.from_dict(assets_item_data)

                assets.append(assets_item)

        _body_colors = d.pop("bodyColors", UNSET)
        body_colors: RobloxApiAvatarModelsBodyColorsModelV4 | Unset
        if isinstance(_body_colors, Unset):
            body_colors = UNSET
        else:
            body_colors = RobloxApiAvatarModelsBodyColorsModelV4.from_dict(_body_colors)

        _scale = d.pop("scale", UNSET)
        scale: RobloxWebResponsesAvatarScaleModel | Unset
        if isinstance(_scale, Unset):
            scale = UNSET
        else:
            scale = RobloxWebResponsesAvatarScaleModel.from_dict(_scale)

        _player_avatar_type = d.pop("playerAvatarType", UNSET)
        player_avatar_type: RobloxApiAvatarModelsV4OutfitModelV4PlayerAvatarType | Unset
        if isinstance(_player_avatar_type, Unset):
            player_avatar_type = UNSET
        else:
            player_avatar_type = RobloxApiAvatarModelsV4OutfitModelV4PlayerAvatarType(_player_avatar_type)

        roblox_api_avatar_models_v4_outfit_model_v4 = cls(
            universe_id=universe_id,
            inventory_type=inventory_type,
            id=id,
            name=name,
            is_editable=is_editable,
            outfit_type=outfit_type,
            assets=assets,
            body_colors=body_colors,
            scale=scale,
            player_avatar_type=player_avatar_type,
        )

        return roblox_api_avatar_models_v4_outfit_model_v4
