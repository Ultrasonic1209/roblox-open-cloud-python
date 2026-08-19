from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_api_avatar_models_v4_update_outfit_config import RobloxApiAvatarModelsV4UpdateOutfitConfig
    from ..models.roblox_api_avatar_models_v4_update_outfit_model_v4 import RobloxApiAvatarModelsV4UpdateOutfitModelV4


T = TypeVar("T", bound="RobloxApiAvatarModelsV4UpdateOutfitDefinition")


@_attrs_define
class RobloxApiAvatarModelsV4UpdateOutfitDefinition:
    """A model containing outfit fields to create or update.

    Attributes:
        update_outfit_model (RobloxApiAvatarModelsV4UpdateOutfitModelV4 | Unset): A model containing core outfit fields
            to update.
        update_outfit_config (RobloxApiAvatarModelsV4UpdateOutfitConfig | Unset): A model containing outfit config
            fields to update.
    """

    update_outfit_model: RobloxApiAvatarModelsV4UpdateOutfitModelV4 | Unset = UNSET
    update_outfit_config: RobloxApiAvatarModelsV4UpdateOutfitConfig | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        update_outfit_model: dict[str, Any] | Unset = UNSET
        if not isinstance(self.update_outfit_model, Unset):
            update_outfit_model = self.update_outfit_model.to_dict()

        update_outfit_config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.update_outfit_config, Unset):
            update_outfit_config = self.update_outfit_config.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if update_outfit_model is not UNSET:
            field_dict["updateOutfitModel"] = update_outfit_model
        if update_outfit_config is not UNSET:
            field_dict["updateOutfitConfig"] = update_outfit_config

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_api_avatar_models_v4_update_outfit_config import RobloxApiAvatarModelsV4UpdateOutfitConfig
        from ..models.roblox_api_avatar_models_v4_update_outfit_model_v4 import (
            RobloxApiAvatarModelsV4UpdateOutfitModelV4,
        )

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        _update_outfit_model = d.pop("updateOutfitModel", UNSET)
        update_outfit_model: RobloxApiAvatarModelsV4UpdateOutfitModelV4 | Unset
        if isinstance(_update_outfit_model, Unset):
            update_outfit_model = UNSET
        else:
            update_outfit_model = RobloxApiAvatarModelsV4UpdateOutfitModelV4.from_dict(_update_outfit_model)

        _update_outfit_config = d.pop("updateOutfitConfig", UNSET)
        update_outfit_config: RobloxApiAvatarModelsV4UpdateOutfitConfig | Unset
        if isinstance(_update_outfit_config, Unset):
            update_outfit_config = UNSET
        else:
            update_outfit_config = RobloxApiAvatarModelsV4UpdateOutfitConfig.from_dict(_update_outfit_config)

        roblox_api_avatar_models_v4_update_outfit_definition = cls(
            update_outfit_model=update_outfit_model,
            update_outfit_config=update_outfit_config,
        )

        return roblox_api_avatar_models_v4_update_outfit_definition
