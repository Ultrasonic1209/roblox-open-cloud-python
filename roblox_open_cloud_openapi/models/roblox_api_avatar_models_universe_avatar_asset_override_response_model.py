from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxApiAvatarModelsUniverseAvatarAssetOverrideResponseModel")


@_attrs_define
class RobloxApiAvatarModelsUniverseAvatarAssetOverrideResponseModel:
    """
    Attributes:
        asset_id (int | Unset):
        asset_type_id (int | Unset):
        is_player_choice (bool | Unset):
    """

    asset_id: int | Unset = UNSET
    asset_type_id: int | Unset = UNSET
    is_player_choice: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        asset_id = self.asset_id

        asset_type_id = self.asset_type_id

        is_player_choice = self.is_player_choice

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if asset_id is not UNSET:
            field_dict["assetID"] = asset_id
        if asset_type_id is not UNSET:
            field_dict["assetTypeID"] = asset_type_id
        if is_player_choice is not UNSET:
            field_dict["isPlayerChoice"] = is_player_choice

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        asset_id = d.pop("assetID", UNSET)

        asset_type_id = d.pop("assetTypeID", UNSET)

        is_player_choice = d.pop("isPlayerChoice", UNSET)

        roblox_api_avatar_models_universe_avatar_asset_override_response_model = cls(
            asset_id=asset_id,
            asset_type_id=asset_type_id,
            is_player_choice=is_player_choice,
        )

        return roblox_api_avatar_models_universe_avatar_asset_override_response_model
