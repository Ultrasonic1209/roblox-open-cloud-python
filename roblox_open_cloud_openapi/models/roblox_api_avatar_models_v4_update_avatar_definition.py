from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_api_avatar_models_v4_update_avatar_config import RobloxApiAvatarModelsV4UpdateAvatarConfig
    from ..models.roblox_api_avatar_models_v4_update_avatar_model_v4 import RobloxApiAvatarModelsV4UpdateAvatarModelV4


T = TypeVar("T", bound="RobloxApiAvatarModelsV4UpdateAvatarDefinition")


@_attrs_define
class RobloxApiAvatarModelsV4UpdateAvatarDefinition:
    """A model containing details about an avatar update.

    Attributes:
        update_avatar_model (RobloxApiAvatarModelsV4UpdateAvatarModelV4 | Unset): A model containing avatar model fields
            to update.
        update_avatar_config (RobloxApiAvatarModelsV4UpdateAvatarConfig | Unset): A model containing avatar config
            fields to update.
    """

    update_avatar_model: RobloxApiAvatarModelsV4UpdateAvatarModelV4 | Unset = UNSET
    update_avatar_config: RobloxApiAvatarModelsV4UpdateAvatarConfig | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        update_avatar_model: dict[str, Any] | Unset = UNSET
        if not isinstance(self.update_avatar_model, Unset):
            update_avatar_model = self.update_avatar_model.to_dict()

        update_avatar_config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.update_avatar_config, Unset):
            update_avatar_config = self.update_avatar_config.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if update_avatar_model is not UNSET:
            field_dict["updateAvatarModel"] = update_avatar_model
        if update_avatar_config is not UNSET:
            field_dict["updateAvatarConfig"] = update_avatar_config

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_api_avatar_models_v4_update_avatar_config import RobloxApiAvatarModelsV4UpdateAvatarConfig
        from ..models.roblox_api_avatar_models_v4_update_avatar_model_v4 import (
            RobloxApiAvatarModelsV4UpdateAvatarModelV4,
        )

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        _update_avatar_model = d.pop("updateAvatarModel", UNSET)
        update_avatar_model: RobloxApiAvatarModelsV4UpdateAvatarModelV4 | Unset
        if isinstance(_update_avatar_model, Unset):
            update_avatar_model = UNSET
        else:
            update_avatar_model = RobloxApiAvatarModelsV4UpdateAvatarModelV4.from_dict(_update_avatar_model)

        _update_avatar_config = d.pop("updateAvatarConfig", UNSET)
        update_avatar_config: RobloxApiAvatarModelsV4UpdateAvatarConfig | Unset
        if isinstance(_update_avatar_config, Unset):
            update_avatar_config = UNSET
        else:
            update_avatar_config = RobloxApiAvatarModelsV4UpdateAvatarConfig.from_dict(_update_avatar_config)

        roblox_api_avatar_models_v4_update_avatar_definition = cls(
            update_avatar_model=update_avatar_model,
            update_avatar_config=update_avatar_config,
        )

        return roblox_api_avatar_models_v4_update_avatar_definition
