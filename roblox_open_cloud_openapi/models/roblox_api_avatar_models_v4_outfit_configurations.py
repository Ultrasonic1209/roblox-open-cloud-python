from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_api_avatar_models_v4_avatar_background_model import (
        RobloxApiAvatarModelsV4AvatarBackgroundModel,
    )


T = TypeVar("T", bound="RobloxApiAvatarModelsV4OutfitConfigurations")


@_attrs_define
class RobloxApiAvatarModelsV4OutfitConfigurations:
    """Background configuration for an outfit.

    Attributes:
        background (RobloxApiAvatarModelsV4AvatarBackgroundModel | Unset): A model containing avatar background data.
    """

    background: RobloxApiAvatarModelsV4AvatarBackgroundModel | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        background: dict[str, Any] | Unset = UNSET
        if not isinstance(self.background, Unset):
            background = self.background.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if background is not UNSET:
            field_dict["background"] = background

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_api_avatar_models_v4_avatar_background_model import (
            RobloxApiAvatarModelsV4AvatarBackgroundModel,
        )

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        _background = d.pop("background", UNSET)
        background: RobloxApiAvatarModelsV4AvatarBackgroundModel | Unset
        if isinstance(_background, Unset):
            background = UNSET
        else:
            background = RobloxApiAvatarModelsV4AvatarBackgroundModel.from_dict(_background)

        roblox_api_avatar_models_v4_outfit_configurations = cls(
            background=background,
        )

        return roblox_api_avatar_models_v4_outfit_configurations
