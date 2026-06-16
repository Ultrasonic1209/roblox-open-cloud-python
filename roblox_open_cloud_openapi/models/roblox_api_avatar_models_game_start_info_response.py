from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_api_avatar_models_universe_avatar_asset_override_response_model import (
        RobloxApiAvatarModelsUniverseAvatarAssetOverrideResponseModel,
    )
    from ..models.roblox_web_responses_avatar_scale_model import RobloxWebResponsesAvatarScaleModel


T = TypeVar("T", bound="RobloxApiAvatarModelsGameStartInfoResponse")


@_attrs_define
class RobloxApiAvatarModelsGameStartInfoResponse:
    """The game start info

    Attributes:
        game_avatar_type (str | Unset): Avatar Type
        allow_custom_animations (str | Unset): Custom animation enabled
        universe_avatar_collision_type (str | Unset): collision type for the univers
        universe_avatar_body_type (str | Unset): Body type for the univers
        joint_positioning_type (str | Unset): Joing positioning type
        message (str | Unset): Mesasge
        universe_avatar_min_scales (RobloxWebResponsesAvatarScaleModel | Unset):
        universe_avatar_max_scales (RobloxWebResponsesAvatarScaleModel | Unset):
        universe_avatar_asset_overrides (list[RobloxApiAvatarModelsUniverseAvatarAssetOverrideResponseModel] | Unset):
            asset overrides for the univers
        moderation_status (str | Unset): Moderation status
    """

    game_avatar_type: str | Unset = UNSET
    allow_custom_animations: str | Unset = UNSET
    universe_avatar_collision_type: str | Unset = UNSET
    universe_avatar_body_type: str | Unset = UNSET
    joint_positioning_type: str | Unset = UNSET
    message: str | Unset = UNSET
    universe_avatar_min_scales: RobloxWebResponsesAvatarScaleModel | Unset = UNSET
    universe_avatar_max_scales: RobloxWebResponsesAvatarScaleModel | Unset = UNSET
    universe_avatar_asset_overrides: list[RobloxApiAvatarModelsUniverseAvatarAssetOverrideResponseModel] | Unset = UNSET
    moderation_status: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        game_avatar_type = self.game_avatar_type

        allow_custom_animations = self.allow_custom_animations

        universe_avatar_collision_type = self.universe_avatar_collision_type

        universe_avatar_body_type = self.universe_avatar_body_type

        joint_positioning_type = self.joint_positioning_type

        message = self.message

        universe_avatar_min_scales: dict[str, Any] | Unset = UNSET
        if not isinstance(self.universe_avatar_min_scales, Unset):
            universe_avatar_min_scales = self.universe_avatar_min_scales.to_dict()

        universe_avatar_max_scales: dict[str, Any] | Unset = UNSET
        if not isinstance(self.universe_avatar_max_scales, Unset):
            universe_avatar_max_scales = self.universe_avatar_max_scales.to_dict()

        universe_avatar_asset_overrides: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.universe_avatar_asset_overrides, Unset):
            universe_avatar_asset_overrides = []
            for universe_avatar_asset_overrides_item_data in self.universe_avatar_asset_overrides:
                universe_avatar_asset_overrides_item = universe_avatar_asset_overrides_item_data.to_dict()
                universe_avatar_asset_overrides.append(universe_avatar_asset_overrides_item)

        moderation_status = self.moderation_status

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if game_avatar_type is not UNSET:
            field_dict["gameAvatarType"] = game_avatar_type
        if allow_custom_animations is not UNSET:
            field_dict["allowCustomAnimations"] = allow_custom_animations
        if universe_avatar_collision_type is not UNSET:
            field_dict["universeAvatarCollisionType"] = universe_avatar_collision_type
        if universe_avatar_body_type is not UNSET:
            field_dict["universeAvatarBodyType"] = universe_avatar_body_type
        if joint_positioning_type is not UNSET:
            field_dict["jointPositioningType"] = joint_positioning_type
        if message is not UNSET:
            field_dict["message"] = message
        if universe_avatar_min_scales is not UNSET:
            field_dict["universeAvatarMinScales"] = universe_avatar_min_scales
        if universe_avatar_max_scales is not UNSET:
            field_dict["universeAvatarMaxScales"] = universe_avatar_max_scales
        if universe_avatar_asset_overrides is not UNSET:
            field_dict["universeAvatarAssetOverrides"] = universe_avatar_asset_overrides
        if moderation_status is not UNSET:
            field_dict["moderationStatus"] = moderation_status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_api_avatar_models_universe_avatar_asset_override_response_model import (
            RobloxApiAvatarModelsUniverseAvatarAssetOverrideResponseModel,
        )
        from ..models.roblox_web_responses_avatar_scale_model import RobloxWebResponsesAvatarScaleModel

        d = dict(src_dict)
        game_avatar_type = d.pop("gameAvatarType", UNSET)

        allow_custom_animations = d.pop("allowCustomAnimations", UNSET)

        universe_avatar_collision_type = d.pop("universeAvatarCollisionType", UNSET)

        universe_avatar_body_type = d.pop("universeAvatarBodyType", UNSET)

        joint_positioning_type = d.pop("jointPositioningType", UNSET)

        message = d.pop("message", UNSET)

        _universe_avatar_min_scales = d.pop("universeAvatarMinScales", UNSET)
        universe_avatar_min_scales: RobloxWebResponsesAvatarScaleModel | Unset
        if isinstance(_universe_avatar_min_scales, Unset):
            universe_avatar_min_scales = UNSET
        else:
            universe_avatar_min_scales = RobloxWebResponsesAvatarScaleModel.from_dict(_universe_avatar_min_scales)

        _universe_avatar_max_scales = d.pop("universeAvatarMaxScales", UNSET)
        universe_avatar_max_scales: RobloxWebResponsesAvatarScaleModel | Unset
        if isinstance(_universe_avatar_max_scales, Unset):
            universe_avatar_max_scales = UNSET
        else:
            universe_avatar_max_scales = RobloxWebResponsesAvatarScaleModel.from_dict(_universe_avatar_max_scales)

        _universe_avatar_asset_overrides = d.pop("universeAvatarAssetOverrides", UNSET)
        universe_avatar_asset_overrides: list[RobloxApiAvatarModelsUniverseAvatarAssetOverrideResponseModel] | Unset = (
            UNSET
        )
        if _universe_avatar_asset_overrides is not UNSET:
            universe_avatar_asset_overrides = []
            for universe_avatar_asset_overrides_item_data in _universe_avatar_asset_overrides:
                universe_avatar_asset_overrides_item = (
                    RobloxApiAvatarModelsUniverseAvatarAssetOverrideResponseModel.from_dict(
                        universe_avatar_asset_overrides_item_data
                    )
                )

                universe_avatar_asset_overrides.append(universe_avatar_asset_overrides_item)

        moderation_status = d.pop("moderationStatus", UNSET)

        roblox_api_avatar_models_game_start_info_response = cls(
            game_avatar_type=game_avatar_type,
            allow_custom_animations=allow_custom_animations,
            universe_avatar_collision_type=universe_avatar_collision_type,
            universe_avatar_body_type=universe_avatar_body_type,
            joint_positioning_type=joint_positioning_type,
            message=message,
            universe_avatar_min_scales=universe_avatar_min_scales,
            universe_avatar_max_scales=universe_avatar_max_scales,
            universe_avatar_asset_overrides=universe_avatar_asset_overrides,
            moderation_status=moderation_status,
        )

        return roblox_api_avatar_models_game_start_info_response
