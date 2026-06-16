from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.roblox_api_avatar_models_avatar_rules_model_player_avatar_types_item import (
    RobloxApiAvatarModelsAvatarRulesModelPlayerAvatarTypesItem,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_api_avatar_models_asset_type_rules_model import RobloxApiAvatarModelsAssetTypeRulesModel
    from ..models.roblox_api_avatar_models_avatar_rules_model_accessory_refinement_lower_bounds import (
        RobloxApiAvatarModelsAvatarRulesModelAccessoryRefinementLowerBounds,
    )
    from ..models.roblox_api_avatar_models_avatar_rules_model_accessory_refinement_upper_bounds import (
        RobloxApiAvatarModelsAvatarRulesModelAccessoryRefinementUpperBounds,
    )
    from ..models.roblox_api_avatar_models_avatar_rules_model_scales import RobloxApiAvatarModelsAvatarRulesModelScales
    from ..models.roblox_api_avatar_models_body_color_model import RobloxApiAvatarModelsBodyColorModel
    from ..models.roblox_api_avatar_models_default_clothing_assets import RobloxApiAvatarModelsDefaultClothingAssets


T = TypeVar("T", bound="RobloxApiAvatarModelsAvatarRulesModel")


@_attrs_define
class RobloxApiAvatarModelsAvatarRulesModel:
    """A model containing details about avatar-related business rules

    Attributes:
        player_avatar_types (list[RobloxApiAvatarModelsAvatarRulesModelPlayerAvatarTypesItem] | Unset): The avatar type
        scales (RobloxApiAvatarModelsAvatarRulesModelScales | Unset): The scales
        wearable_asset_types (list[RobloxApiAvatarModelsAssetTypeRulesModel] | Unset): The assets worn on the character
        accessory_refinement_types (list[int] | Unset): The list of asset type ids for Accessory Refinement.
        accessory_refinement_lower_bounds (RobloxApiAvatarModelsAvatarRulesModelAccessoryRefinementLowerBounds | Unset):
            The lower bounds for accessory refinement settings.
        accessory_refinement_upper_bounds (RobloxApiAvatarModelsAvatarRulesModelAccessoryRefinementUpperBounds | Unset):
            The lower bounds for accessory refinement settings.
        body_colors_palette (list[RobloxApiAvatarModelsBodyColorModel] | Unset): The full set of usable body colors
        basic_body_colors_palette (list[RobloxApiAvatarModelsBodyColorModel] | Unset): The basic set of body colors
        minimum_delta_e_body_color_difference (float | Unset): The minimum Delta-E difference in body colors
            for default clothing not to be applied
        proportions_and_body_type_enabled_for_user (bool | Unset): Whether proportion and bodyType scales are allowed to
            be set by the authenticated user
        default_clothing_asset_lists (RobloxApiAvatarModelsDefaultClothingAssets | Unset): A model containing details
            about avatar-related business rules
        bundles_enabled_for_user (bool | Unset): Whether or not bundles are enabled for the specific user
        emotes_enabled_for_user (bool | Unset): Whether or not emotes are enabled
    """

    player_avatar_types: list[RobloxApiAvatarModelsAvatarRulesModelPlayerAvatarTypesItem] | Unset = UNSET
    scales: RobloxApiAvatarModelsAvatarRulesModelScales | Unset = UNSET
    wearable_asset_types: list[RobloxApiAvatarModelsAssetTypeRulesModel] | Unset = UNSET
    accessory_refinement_types: list[int] | Unset = UNSET
    accessory_refinement_lower_bounds: RobloxApiAvatarModelsAvatarRulesModelAccessoryRefinementLowerBounds | Unset = (
        UNSET
    )
    accessory_refinement_upper_bounds: RobloxApiAvatarModelsAvatarRulesModelAccessoryRefinementUpperBounds | Unset = (
        UNSET
    )
    body_colors_palette: list[RobloxApiAvatarModelsBodyColorModel] | Unset = UNSET
    basic_body_colors_palette: list[RobloxApiAvatarModelsBodyColorModel] | Unset = UNSET
    minimum_delta_e_body_color_difference: float | Unset = UNSET
    proportions_and_body_type_enabled_for_user: bool | Unset = UNSET
    default_clothing_asset_lists: RobloxApiAvatarModelsDefaultClothingAssets | Unset = UNSET
    bundles_enabled_for_user: bool | Unset = UNSET
    emotes_enabled_for_user: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        player_avatar_types: list[int] | Unset = UNSET
        if not isinstance(self.player_avatar_types, Unset):
            player_avatar_types = []
            for player_avatar_types_item_data in self.player_avatar_types:
                player_avatar_types_item = player_avatar_types_item_data.value
                player_avatar_types.append(player_avatar_types_item)

        scales: dict[str, Any] | Unset = UNSET
        if not isinstance(self.scales, Unset):
            scales = self.scales.to_dict()

        wearable_asset_types: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.wearable_asset_types, Unset):
            wearable_asset_types = []
            for wearable_asset_types_item_data in self.wearable_asset_types:
                wearable_asset_types_item = wearable_asset_types_item_data.to_dict()
                wearable_asset_types.append(wearable_asset_types_item)

        accessory_refinement_types: list[int] | Unset = UNSET
        if not isinstance(self.accessory_refinement_types, Unset):
            accessory_refinement_types = self.accessory_refinement_types

        accessory_refinement_lower_bounds: dict[str, Any] | Unset = UNSET
        if not isinstance(self.accessory_refinement_lower_bounds, Unset):
            accessory_refinement_lower_bounds = self.accessory_refinement_lower_bounds.to_dict()

        accessory_refinement_upper_bounds: dict[str, Any] | Unset = UNSET
        if not isinstance(self.accessory_refinement_upper_bounds, Unset):
            accessory_refinement_upper_bounds = self.accessory_refinement_upper_bounds.to_dict()

        body_colors_palette: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.body_colors_palette, Unset):
            body_colors_palette = []
            for body_colors_palette_item_data in self.body_colors_palette:
                body_colors_palette_item = body_colors_palette_item_data.to_dict()
                body_colors_palette.append(body_colors_palette_item)

        basic_body_colors_palette: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.basic_body_colors_palette, Unset):
            basic_body_colors_palette = []
            for basic_body_colors_palette_item_data in self.basic_body_colors_palette:
                basic_body_colors_palette_item = basic_body_colors_palette_item_data.to_dict()
                basic_body_colors_palette.append(basic_body_colors_palette_item)

        minimum_delta_e_body_color_difference = self.minimum_delta_e_body_color_difference

        proportions_and_body_type_enabled_for_user = self.proportions_and_body_type_enabled_for_user

        default_clothing_asset_lists: dict[str, Any] | Unset = UNSET
        if not isinstance(self.default_clothing_asset_lists, Unset):
            default_clothing_asset_lists = self.default_clothing_asset_lists.to_dict()

        bundles_enabled_for_user = self.bundles_enabled_for_user

        emotes_enabled_for_user = self.emotes_enabled_for_user

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if player_avatar_types is not UNSET:
            field_dict["playerAvatarTypes"] = player_avatar_types
        if scales is not UNSET:
            field_dict["scales"] = scales
        if wearable_asset_types is not UNSET:
            field_dict["wearableAssetTypes"] = wearable_asset_types
        if accessory_refinement_types is not UNSET:
            field_dict["accessoryRefinementTypes"] = accessory_refinement_types
        if accessory_refinement_lower_bounds is not UNSET:
            field_dict["accessoryRefinementLowerBounds"] = accessory_refinement_lower_bounds
        if accessory_refinement_upper_bounds is not UNSET:
            field_dict["accessoryRefinementUpperBounds"] = accessory_refinement_upper_bounds
        if body_colors_palette is not UNSET:
            field_dict["bodyColorsPalette"] = body_colors_palette
        if basic_body_colors_palette is not UNSET:
            field_dict["basicBodyColorsPalette"] = basic_body_colors_palette
        if minimum_delta_e_body_color_difference is not UNSET:
            field_dict["minimumDeltaEBodyColorDifference"] = minimum_delta_e_body_color_difference
        if proportions_and_body_type_enabled_for_user is not UNSET:
            field_dict["proportionsAndBodyTypeEnabledForUser"] = proportions_and_body_type_enabled_for_user
        if default_clothing_asset_lists is not UNSET:
            field_dict["defaultClothingAssetLists"] = default_clothing_asset_lists
        if bundles_enabled_for_user is not UNSET:
            field_dict["bundlesEnabledForUser"] = bundles_enabled_for_user
        if emotes_enabled_for_user is not UNSET:
            field_dict["emotesEnabledForUser"] = emotes_enabled_for_user

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_api_avatar_models_asset_type_rules_model import RobloxApiAvatarModelsAssetTypeRulesModel
        from ..models.roblox_api_avatar_models_avatar_rules_model_accessory_refinement_lower_bounds import (
            RobloxApiAvatarModelsAvatarRulesModelAccessoryRefinementLowerBounds,
        )
        from ..models.roblox_api_avatar_models_avatar_rules_model_accessory_refinement_upper_bounds import (
            RobloxApiAvatarModelsAvatarRulesModelAccessoryRefinementUpperBounds,
        )
        from ..models.roblox_api_avatar_models_avatar_rules_model_scales import (
            RobloxApiAvatarModelsAvatarRulesModelScales,
        )
        from ..models.roblox_api_avatar_models_body_color_model import RobloxApiAvatarModelsBodyColorModel
        from ..models.roblox_api_avatar_models_default_clothing_assets import RobloxApiAvatarModelsDefaultClothingAssets

        d = dict(src_dict)
        _player_avatar_types = d.pop("playerAvatarTypes", UNSET)
        player_avatar_types: list[RobloxApiAvatarModelsAvatarRulesModelPlayerAvatarTypesItem] | Unset = UNSET
        if _player_avatar_types is not UNSET:
            player_avatar_types = []
            for player_avatar_types_item_data in _player_avatar_types:
                player_avatar_types_item = RobloxApiAvatarModelsAvatarRulesModelPlayerAvatarTypesItem(
                    player_avatar_types_item_data
                )

                player_avatar_types.append(player_avatar_types_item)

        _scales = d.pop("scales", UNSET)
        scales: RobloxApiAvatarModelsAvatarRulesModelScales | Unset
        if isinstance(_scales, Unset):
            scales = UNSET
        else:
            scales = RobloxApiAvatarModelsAvatarRulesModelScales.from_dict(_scales)

        _wearable_asset_types = d.pop("wearableAssetTypes", UNSET)
        wearable_asset_types: list[RobloxApiAvatarModelsAssetTypeRulesModel] | Unset = UNSET
        if _wearable_asset_types is not UNSET:
            wearable_asset_types = []
            for wearable_asset_types_item_data in _wearable_asset_types:
                wearable_asset_types_item = RobloxApiAvatarModelsAssetTypeRulesModel.from_dict(
                    wearable_asset_types_item_data
                )

                wearable_asset_types.append(wearable_asset_types_item)

        accessory_refinement_types = cast(list[int], d.pop("accessoryRefinementTypes", UNSET))

        _accessory_refinement_lower_bounds = d.pop("accessoryRefinementLowerBounds", UNSET)
        accessory_refinement_lower_bounds: RobloxApiAvatarModelsAvatarRulesModelAccessoryRefinementLowerBounds | Unset
        if isinstance(_accessory_refinement_lower_bounds, Unset):
            accessory_refinement_lower_bounds = UNSET
        else:
            accessory_refinement_lower_bounds = (
                RobloxApiAvatarModelsAvatarRulesModelAccessoryRefinementLowerBounds.from_dict(
                    _accessory_refinement_lower_bounds
                )
            )

        _accessory_refinement_upper_bounds = d.pop("accessoryRefinementUpperBounds", UNSET)
        accessory_refinement_upper_bounds: RobloxApiAvatarModelsAvatarRulesModelAccessoryRefinementUpperBounds | Unset
        if isinstance(_accessory_refinement_upper_bounds, Unset):
            accessory_refinement_upper_bounds = UNSET
        else:
            accessory_refinement_upper_bounds = (
                RobloxApiAvatarModelsAvatarRulesModelAccessoryRefinementUpperBounds.from_dict(
                    _accessory_refinement_upper_bounds
                )
            )

        _body_colors_palette = d.pop("bodyColorsPalette", UNSET)
        body_colors_palette: list[RobloxApiAvatarModelsBodyColorModel] | Unset = UNSET
        if _body_colors_palette is not UNSET:
            body_colors_palette = []
            for body_colors_palette_item_data in _body_colors_palette:
                body_colors_palette_item = RobloxApiAvatarModelsBodyColorModel.from_dict(body_colors_palette_item_data)

                body_colors_palette.append(body_colors_palette_item)

        _basic_body_colors_palette = d.pop("basicBodyColorsPalette", UNSET)
        basic_body_colors_palette: list[RobloxApiAvatarModelsBodyColorModel] | Unset = UNSET
        if _basic_body_colors_palette is not UNSET:
            basic_body_colors_palette = []
            for basic_body_colors_palette_item_data in _basic_body_colors_palette:
                basic_body_colors_palette_item = RobloxApiAvatarModelsBodyColorModel.from_dict(
                    basic_body_colors_palette_item_data
                )

                basic_body_colors_palette.append(basic_body_colors_palette_item)

        minimum_delta_e_body_color_difference = d.pop("minimumDeltaEBodyColorDifference", UNSET)

        proportions_and_body_type_enabled_for_user = d.pop("proportionsAndBodyTypeEnabledForUser", UNSET)

        _default_clothing_asset_lists = d.pop("defaultClothingAssetLists", UNSET)
        default_clothing_asset_lists: RobloxApiAvatarModelsDefaultClothingAssets | Unset
        if isinstance(_default_clothing_asset_lists, Unset):
            default_clothing_asset_lists = UNSET
        else:
            default_clothing_asset_lists = RobloxApiAvatarModelsDefaultClothingAssets.from_dict(
                _default_clothing_asset_lists
            )

        bundles_enabled_for_user = d.pop("bundlesEnabledForUser", UNSET)

        emotes_enabled_for_user = d.pop("emotesEnabledForUser", UNSET)

        roblox_api_avatar_models_avatar_rules_model = cls(
            player_avatar_types=player_avatar_types,
            scales=scales,
            wearable_asset_types=wearable_asset_types,
            accessory_refinement_types=accessory_refinement_types,
            accessory_refinement_lower_bounds=accessory_refinement_lower_bounds,
            accessory_refinement_upper_bounds=accessory_refinement_upper_bounds,
            body_colors_palette=body_colors_palette,
            basic_body_colors_palette=basic_body_colors_palette,
            minimum_delta_e_body_color_difference=minimum_delta_e_body_color_difference,
            proportions_and_body_type_enabled_for_user=proportions_and_body_type_enabled_for_user,
            default_clothing_asset_lists=default_clothing_asset_lists,
            bundles_enabled_for_user=bundles_enabled_for_user,
            emotes_enabled_for_user=emotes_enabled_for_user,
        )

        return roblox_api_avatar_models_avatar_rules_model
