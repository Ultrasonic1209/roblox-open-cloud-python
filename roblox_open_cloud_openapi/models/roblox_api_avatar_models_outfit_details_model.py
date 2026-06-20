from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_api_avatar_models_asset_model_v2 import RobloxApiAvatarModelsAssetModelV2
    from ..models.roblox_api_avatar_models_body_colors_model import RobloxApiAvatarModelsBodyColorsModel
    from ..models.roblox_web_responses_avatar_scale_model import RobloxWebResponsesAvatarScaleModel


T = TypeVar("T", bound="RobloxApiAvatarModelsOutfitDetailsModel")


@_attrs_define
class RobloxApiAvatarModelsOutfitDetailsModel:
    """A model containing details about a user outfit

    Attributes:
        id (int | Unset): The id
        universe_id (int | Unset): The universe id of the outfit, null when outfit is not created in-experience
        name (str | Unset): The name
        assets (list[RobloxApiAvatarModelsAssetModelV2] | Unset): A list of assetIds
        body_colors (RobloxApiAvatarModelsBodyColorsModel | Unset): A model container BrickColor ids for each body part.
        scale (RobloxWebResponsesAvatarScaleModel | Unset):
        player_avatar_type (str | Unset): The player avatar type - this can be R6 or R15.
        outfit_type (str | Unset): The outfit type of the outfit
        is_editable (bool | Unset): Whether the outfit can be edited by the user
        moderation_status (str | Unset): The moderation status of the outfit, not applicable when outfit is created
            outside experience
    """

    id: int | Unset = UNSET
    universe_id: int | Unset = UNSET
    name: str | Unset = UNSET
    assets: list[RobloxApiAvatarModelsAssetModelV2] | Unset = UNSET
    body_colors: RobloxApiAvatarModelsBodyColorsModel | Unset = UNSET
    scale: RobloxWebResponsesAvatarScaleModel | Unset = UNSET
    player_avatar_type: str | Unset = UNSET
    outfit_type: str | Unset = UNSET
    is_editable: bool | Unset = UNSET
    moderation_status: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        universe_id = self.universe_id

        name = self.name

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

        player_avatar_type = self.player_avatar_type

        outfit_type = self.outfit_type

        is_editable = self.is_editable

        moderation_status = self.moderation_status

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if universe_id is not UNSET:
            field_dict["universeId"] = universe_id
        if name is not UNSET:
            field_dict["name"] = name
        if assets is not UNSET:
            field_dict["assets"] = assets
        if body_colors is not UNSET:
            field_dict["bodyColors"] = body_colors
        if scale is not UNSET:
            field_dict["scale"] = scale
        if player_avatar_type is not UNSET:
            field_dict["playerAvatarType"] = player_avatar_type
        if outfit_type is not UNSET:
            field_dict["outfitType"] = outfit_type
        if is_editable is not UNSET:
            field_dict["isEditable"] = is_editable
        if moderation_status is not UNSET:
            field_dict["moderationStatus"] = moderation_status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_api_avatar_models_asset_model_v2 import RobloxApiAvatarModelsAssetModelV2
        from ..models.roblox_api_avatar_models_body_colors_model import RobloxApiAvatarModelsBodyColorsModel
        from ..models.roblox_web_responses_avatar_scale_model import RobloxWebResponsesAvatarScaleModel

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        id = d.pop("id", UNSET)

        universe_id = d.pop("universeId", UNSET)

        name = d.pop("name", UNSET)

        _assets = d.pop("assets", UNSET)
        assets: list[RobloxApiAvatarModelsAssetModelV2] | Unset = UNSET
        if _assets is not UNSET:
            assets = []
            for assets_item_data in _assets:
                assets_item = RobloxApiAvatarModelsAssetModelV2.from_dict(assets_item_data)

                assets.append(assets_item)

        _body_colors = d.pop("bodyColors", UNSET)
        body_colors: RobloxApiAvatarModelsBodyColorsModel | Unset
        if isinstance(_body_colors, Unset):
            body_colors = UNSET
        else:
            body_colors = RobloxApiAvatarModelsBodyColorsModel.from_dict(_body_colors)

        _scale = d.pop("scale", UNSET)
        scale: RobloxWebResponsesAvatarScaleModel | Unset
        if isinstance(_scale, Unset):
            scale = UNSET
        else:
            scale = RobloxWebResponsesAvatarScaleModel.from_dict(_scale)

        player_avatar_type = d.pop("playerAvatarType", UNSET)

        outfit_type = d.pop("outfitType", UNSET)

        is_editable = d.pop("isEditable", UNSET)

        moderation_status = d.pop("moderationStatus", UNSET)

        roblox_api_avatar_models_outfit_details_model = cls(
            id=id,
            universe_id=universe_id,
            name=name,
            assets=assets,
            body_colors=body_colors,
            scale=scale,
            player_avatar_type=player_avatar_type,
            outfit_type=outfit_type,
            is_editable=is_editable,
            moderation_status=moderation_status,
        )

        return roblox_api_avatar_models_outfit_details_model
