from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..models.roblox_api_avatar_models_avatar_model_v2_player_avatar_type import (
    RobloxApiAvatarModelsAvatarModelV2PlayerAvatarType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_api_avatar_models_asset_model_v2 import RobloxApiAvatarModelsAssetModelV2
    from ..models.roblox_api_avatar_models_body_colors_model import RobloxApiAvatarModelsBodyColorsModel
    from ..models.roblox_api_avatar_models_emote_response_model import RobloxApiAvatarModelsEmoteResponseModel
    from ..models.roblox_web_responses_avatar_scale_model import RobloxWebResponsesAvatarScaleModel


T = TypeVar("T", bound="RobloxApiAvatarModelsAvatarModelV2")


@_attrs_define
class RobloxApiAvatarModelsAvatarModelV2:
    """A model containing details about an avatar

    Attributes:
        scales (RobloxWebResponsesAvatarScaleModel | Unset):
        player_avatar_type (RobloxApiAvatarModelsAvatarModelV2PlayerAvatarType | Unset): The avatar type
        body_colors (RobloxApiAvatarModelsBodyColorsModel | Unset): A model container BrickColor ids for each body part.
        assets (list[RobloxApiAvatarModelsAssetModelV2] | Unset): The assets worn on the character
        default_shirt_applied (bool | Unset): Whether default clothing has been applied to this avatar.
        default_pants_applied (bool | Unset): Whether default clothing has been applied to this avatar.
        emotes (list[RobloxApiAvatarModelsEmoteResponseModel] | Unset): The emotes on the character
    """

    scales: RobloxWebResponsesAvatarScaleModel | Unset = UNSET
    player_avatar_type: RobloxApiAvatarModelsAvatarModelV2PlayerAvatarType | Unset = UNSET
    body_colors: RobloxApiAvatarModelsBodyColorsModel | Unset = UNSET
    assets: list[RobloxApiAvatarModelsAssetModelV2] | Unset = UNSET
    default_shirt_applied: bool | Unset = UNSET
    default_pants_applied: bool | Unset = UNSET
    emotes: list[RobloxApiAvatarModelsEmoteResponseModel] | Unset = UNSET

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

        default_shirt_applied = self.default_shirt_applied

        default_pants_applied = self.default_pants_applied

        emotes: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.emotes, Unset):
            emotes = []
            for emotes_item_data in self.emotes:
                emotes_item = emotes_item_data.to_dict()
                emotes.append(emotes_item)

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
        if default_shirt_applied is not UNSET:
            field_dict["defaultShirtApplied"] = default_shirt_applied
        if default_pants_applied is not UNSET:
            field_dict["defaultPantsApplied"] = default_pants_applied
        if emotes is not UNSET:
            field_dict["emotes"] = emotes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_api_avatar_models_asset_model_v2 import RobloxApiAvatarModelsAssetModelV2
        from ..models.roblox_api_avatar_models_body_colors_model import RobloxApiAvatarModelsBodyColorsModel
        from ..models.roblox_api_avatar_models_emote_response_model import RobloxApiAvatarModelsEmoteResponseModel
        from ..models.roblox_web_responses_avatar_scale_model import RobloxWebResponsesAvatarScaleModel

        d = dict(src_dict)
        _scales = d.pop("scales", UNSET)
        scales: RobloxWebResponsesAvatarScaleModel | Unset
        if isinstance(_scales, Unset):
            scales = UNSET
        else:
            scales = RobloxWebResponsesAvatarScaleModel.from_dict(_scales)

        _player_avatar_type = d.pop("playerAvatarType", UNSET)
        player_avatar_type: RobloxApiAvatarModelsAvatarModelV2PlayerAvatarType | Unset
        if isinstance(_player_avatar_type, Unset):
            player_avatar_type = UNSET
        else:
            player_avatar_type = RobloxApiAvatarModelsAvatarModelV2PlayerAvatarType(_player_avatar_type)

        _body_colors = d.pop("bodyColors", UNSET)
        body_colors: RobloxApiAvatarModelsBodyColorsModel | Unset
        if isinstance(_body_colors, Unset):
            body_colors = UNSET
        else:
            body_colors = RobloxApiAvatarModelsBodyColorsModel.from_dict(_body_colors)

        _assets = d.pop("assets", UNSET)
        assets: list[RobloxApiAvatarModelsAssetModelV2] | Unset = UNSET
        if _assets is not UNSET:
            assets = []
            for assets_item_data in _assets:
                assets_item = RobloxApiAvatarModelsAssetModelV2.from_dict(assets_item_data)

                assets.append(assets_item)

        default_shirt_applied = d.pop("defaultShirtApplied", UNSET)

        default_pants_applied = d.pop("defaultPantsApplied", UNSET)

        _emotes = d.pop("emotes", UNSET)
        emotes: list[RobloxApiAvatarModelsEmoteResponseModel] | Unset = UNSET
        if _emotes is not UNSET:
            emotes = []
            for emotes_item_data in _emotes:
                emotes_item = RobloxApiAvatarModelsEmoteResponseModel.from_dict(emotes_item_data)

                emotes.append(emotes_item)

        roblox_api_avatar_models_avatar_model_v2 = cls(
            scales=scales,
            player_avatar_type=player_avatar_type,
            body_colors=body_colors,
            assets=assets,
            default_shirt_applied=default_shirt_applied,
            default_pants_applied=default_pants_applied,
            emotes=emotes,
        )

        return roblox_api_avatar_models_avatar_model_v2
