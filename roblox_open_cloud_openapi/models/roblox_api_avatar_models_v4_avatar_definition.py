from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_api_avatar_models_v4_avatar_configurations import RobloxApiAvatarModelsV4AvatarConfigurations
    from ..models.roblox_api_avatar_models_v4_avatar_model_v4 import RobloxApiAvatarModelsV4AvatarModelV4


T = TypeVar("T", bound="RobloxApiAvatarModelsV4AvatarDefinition")


@_attrs_define
class RobloxApiAvatarModelsV4AvatarDefinition:
    """Details about an avatar.

    Attributes:
        avatar_model (RobloxApiAvatarModelsV4AvatarModelV4 | Unset): A model containing details about an avatar.
        avatar_configurations (RobloxApiAvatarModelsV4AvatarConfigurations | Unset): Avatar config details.
    """

    avatar_model: RobloxApiAvatarModelsV4AvatarModelV4 | Unset = UNSET
    avatar_configurations: RobloxApiAvatarModelsV4AvatarConfigurations | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        avatar_model: dict[str, Any] | Unset = UNSET
        if not isinstance(self.avatar_model, Unset):
            avatar_model = self.avatar_model.to_dict()

        avatar_configurations: dict[str, Any] | Unset = UNSET
        if not isinstance(self.avatar_configurations, Unset):
            avatar_configurations = self.avatar_configurations.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if avatar_model is not UNSET:
            field_dict["avatarModel"] = avatar_model
        if avatar_configurations is not UNSET:
            field_dict["avatarConfigurations"] = avatar_configurations

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_api_avatar_models_v4_avatar_configurations import (
            RobloxApiAvatarModelsV4AvatarConfigurations,
        )
        from ..models.roblox_api_avatar_models_v4_avatar_model_v4 import RobloxApiAvatarModelsV4AvatarModelV4

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        _avatar_model = d.pop("avatarModel", UNSET)
        avatar_model: RobloxApiAvatarModelsV4AvatarModelV4 | Unset
        if isinstance(_avatar_model, Unset):
            avatar_model = UNSET
        else:
            avatar_model = RobloxApiAvatarModelsV4AvatarModelV4.from_dict(_avatar_model)

        _avatar_configurations = d.pop("avatarConfigurations", UNSET)
        avatar_configurations: RobloxApiAvatarModelsV4AvatarConfigurations | Unset
        if isinstance(_avatar_configurations, Unset):
            avatar_configurations = UNSET
        else:
            avatar_configurations = RobloxApiAvatarModelsV4AvatarConfigurations.from_dict(_avatar_configurations)

        roblox_api_avatar_models_v4_avatar_definition = cls(
            avatar_model=avatar_model,
            avatar_configurations=avatar_configurations,
        )

        return roblox_api_avatar_models_v4_avatar_definition
