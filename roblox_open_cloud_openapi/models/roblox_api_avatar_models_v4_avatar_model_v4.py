from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..models.roblox_api_avatar_models_v4_avatar_model_v4_player_avatar_type import (
    RobloxApiAvatarModelsV4AvatarModelV4PlayerAvatarType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_api_avatar_models_asset_model_v2 import RobloxApiAvatarModelsAssetModelV2
    from ..models.roblox_api_avatar_models_body_colors_model_v4 import RobloxApiAvatarModelsBodyColorsModelV4
    from ..models.roblox_web_responses_avatar_scale_model import RobloxWebResponsesAvatarScaleModel


T = TypeVar("T", bound="RobloxApiAvatarModelsV4AvatarModelV4")


@_attrs_define
class RobloxApiAvatarModelsV4AvatarModelV4:
    """A model containing details about an avatar.

    Attributes:
        scales (RobloxWebResponsesAvatarScaleModel | Unset):
        player_avatar_type (RobloxApiAvatarModelsV4AvatarModelV4PlayerAvatarType | Unset): The avatar type.
        body_colors (RobloxApiAvatarModelsBodyColorsModelV4 | Unset): A model containing RGB hex colors for each body
            part.
        assets (list[RobloxApiAvatarModelsAssetModelV2] | Unset): The assets worn on the character.
    """

    scales: RobloxWebResponsesAvatarScaleModel | Unset = UNSET
    player_avatar_type: RobloxApiAvatarModelsV4AvatarModelV4PlayerAvatarType | Unset = UNSET
    body_colors: RobloxApiAvatarModelsBodyColorsModelV4 | Unset = UNSET
    assets: list[RobloxApiAvatarModelsAssetModelV2] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        scales: dict[str, Any] | Unset = UNSET
        if not isinstance(self.scales, Unset):
            scales = self.scales.to_dict()

        player_avatar_type: int | Unset = UNSET
        if not isinstance(self.player_avatar_type, Unset):
            player_avatar_type = self.player_avatar_type.value

        body_colors: dict[str, Any] | Unset = UNSET
        if not isinstance(self.body_colors, Unset):
            body_colors = self.body_colors.to_dict()

        assets: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.assets, Unset):
            assets = []
            for assets_item_data in self.assets:
                assets_item = assets_item_data.to_dict()
                assets.append(assets_item)

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if scales is not UNSET:
            field_dict["scales"] = scales
        if player_avatar_type is not UNSET:
            field_dict["playerAvatarType"] = player_avatar_type
        if body_colors is not UNSET:
            field_dict["bodyColors"] = body_colors
        if assets is not UNSET:
            field_dict["assets"] = assets

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_api_avatar_models_asset_model_v2 import RobloxApiAvatarModelsAssetModelV2
        from ..models.roblox_api_avatar_models_body_colors_model_v4 import RobloxApiAvatarModelsBodyColorsModelV4
        from ..models.roblox_web_responses_avatar_scale_model import RobloxWebResponsesAvatarScaleModel

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        _scales = d.pop("scales", UNSET)
        scales: RobloxWebResponsesAvatarScaleModel | Unset
        if isinstance(_scales, Unset):
            scales = UNSET
        else:
            scales = RobloxWebResponsesAvatarScaleModel.from_dict(_scales)

        _player_avatar_type = d.pop("playerAvatarType", UNSET)
        player_avatar_type: RobloxApiAvatarModelsV4AvatarModelV4PlayerAvatarType | Unset
        if isinstance(_player_avatar_type, Unset):
            player_avatar_type = UNSET
        else:
            player_avatar_type = RobloxApiAvatarModelsV4AvatarModelV4PlayerAvatarType(_player_avatar_type)

        _body_colors = d.pop("bodyColors", UNSET)
        body_colors: RobloxApiAvatarModelsBodyColorsModelV4 | Unset
        if isinstance(_body_colors, Unset):
            body_colors = UNSET
        else:
            body_colors = RobloxApiAvatarModelsBodyColorsModelV4.from_dict(_body_colors)

        _assets = d.pop("assets", UNSET)
        assets: list[RobloxApiAvatarModelsAssetModelV2] | Unset = UNSET
        if _assets is not UNSET:
            assets = []
            for assets_item_data in _assets:
                assets_item = RobloxApiAvatarModelsAssetModelV2.from_dict(assets_item_data)

                assets.append(assets_item)

        roblox_api_avatar_models_v4_avatar_model_v4 = cls(
            scales=scales,
            player_avatar_type=player_avatar_type,
            body_colors=body_colors,
            assets=assets,
        )

        return roblox_api_avatar_models_v4_avatar_model_v4
