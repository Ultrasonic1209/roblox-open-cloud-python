from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.roblox_api_avatar_models_player_avatar_type_model_player_avatar_type import (
    RobloxApiAvatarModelsPlayerAvatarTypeModelPlayerAvatarType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxApiAvatarModelsPlayerAvatarTypeModel")


@_attrs_define
class RobloxApiAvatarModelsPlayerAvatarTypeModel:
    """A model that contains a playerAvatarType

    Attributes:
        player_avatar_type (RobloxApiAvatarModelsPlayerAvatarTypeModelPlayerAvatarType | Unset): The playerAvatarType
    """

    player_avatar_type: RobloxApiAvatarModelsPlayerAvatarTypeModelPlayerAvatarType | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        player_avatar_type: int | Unset = UNSET
        if not isinstance(self.player_avatar_type, Unset):
            player_avatar_type = self.player_avatar_type.value

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if player_avatar_type is not UNSET:
            field_dict["playerAvatarType"] = player_avatar_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        _player_avatar_type = d.pop("playerAvatarType", UNSET)
        player_avatar_type: RobloxApiAvatarModelsPlayerAvatarTypeModelPlayerAvatarType | Unset
        if isinstance(_player_avatar_type, Unset):
            player_avatar_type = UNSET
        else:
            player_avatar_type = RobloxApiAvatarModelsPlayerAvatarTypeModelPlayerAvatarType(_player_avatar_type)

        roblox_api_avatar_models_player_avatar_type_model = cls(
            player_avatar_type=player_avatar_type,
        )

        return roblox_api_avatar_models_player_avatar_type_model
