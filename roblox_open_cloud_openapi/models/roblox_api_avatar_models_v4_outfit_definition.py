from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_api_avatar_models_v4_outfit_configurations import RobloxApiAvatarModelsV4OutfitConfigurations
    from ..models.roblox_api_avatar_models_v4_outfit_model_v4 import RobloxApiAvatarModelsV4OutfitModelV4


T = TypeVar("T", bound="RobloxApiAvatarModelsV4OutfitDefinition")


@_attrs_define
class RobloxApiAvatarModelsV4OutfitDefinition:
    """Details about an outfit.

    Attributes:
        moderation_status (str | Unset): The moderation status of the outfit, not applicable when outfit is created
            outside experience
        bundle_id (int | Unset): The bundle ID, currently only returned for in-experience created outfits.
        outfit_model (RobloxApiAvatarModelsV4OutfitModelV4 | Unset): A model containing core outfit details.
        outfit_configurations (RobloxApiAvatarModelsV4OutfitConfigurations | Unset): Background configuration for an
            outfit.
    """

    moderation_status: str | Unset = UNSET
    bundle_id: int | Unset = UNSET
    outfit_model: RobloxApiAvatarModelsV4OutfitModelV4 | Unset = UNSET
    outfit_configurations: RobloxApiAvatarModelsV4OutfitConfigurations | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        moderation_status = self.moderation_status

        bundle_id = self.bundle_id

        outfit_model: dict[str, Any] | Unset = UNSET
        if not isinstance(self.outfit_model, Unset):
            outfit_model = self.outfit_model.to_dict()

        outfit_configurations: dict[str, Any] | Unset = UNSET
        if not isinstance(self.outfit_configurations, Unset):
            outfit_configurations = self.outfit_configurations.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if moderation_status is not UNSET:
            field_dict["moderationStatus"] = moderation_status
        if bundle_id is not UNSET:
            field_dict["bundleId"] = bundle_id
        if outfit_model is not UNSET:
            field_dict["outfitModel"] = outfit_model
        if outfit_configurations is not UNSET:
            field_dict["outfitConfigurations"] = outfit_configurations

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_api_avatar_models_v4_outfit_configurations import (
            RobloxApiAvatarModelsV4OutfitConfigurations,
        )
        from ..models.roblox_api_avatar_models_v4_outfit_model_v4 import RobloxApiAvatarModelsV4OutfitModelV4

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        moderation_status = d.pop("moderationStatus", UNSET)

        bundle_id = d.pop("bundleId", UNSET)

        _outfit_model = d.pop("outfitModel", UNSET)
        outfit_model: RobloxApiAvatarModelsV4OutfitModelV4 | Unset
        if isinstance(_outfit_model, Unset):
            outfit_model = UNSET
        else:
            outfit_model = RobloxApiAvatarModelsV4OutfitModelV4.from_dict(_outfit_model)

        _outfit_configurations = d.pop("outfitConfigurations", UNSET)
        outfit_configurations: RobloxApiAvatarModelsV4OutfitConfigurations | Unset
        if isinstance(_outfit_configurations, Unset):
            outfit_configurations = UNSET
        else:
            outfit_configurations = RobloxApiAvatarModelsV4OutfitConfigurations.from_dict(_outfit_configurations)

        roblox_api_avatar_models_v4_outfit_definition = cls(
            moderation_status=moderation_status,
            bundle_id=bundle_id,
            outfit_model=outfit_model,
            outfit_configurations=outfit_configurations,
        )

        return roblox_api_avatar_models_v4_outfit_definition
