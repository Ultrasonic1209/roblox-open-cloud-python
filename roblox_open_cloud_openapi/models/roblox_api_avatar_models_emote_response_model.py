from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxApiAvatarModelsEmoteResponseModel")


@_attrs_define
class RobloxApiAvatarModelsEmoteResponseModel:
    """Response object representing a user's emote

    Attributes:
        asset_id (int | Unset): The asset id of the emote.
        asset_name (str | Unset): The name of the emote.
        position (int | Unset): The position the emote is equipped to.
    """

    asset_id: int | Unset = UNSET
    asset_name: str | Unset = UNSET
    position: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        asset_id = self.asset_id

        asset_name = self.asset_name

        position = self.position

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if asset_id is not UNSET:
            field_dict["assetId"] = asset_id
        if asset_name is not UNSET:
            field_dict["assetName"] = asset_name
        if position is not UNSET:
            field_dict["position"] = position

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        asset_id = d.pop("assetId", UNSET)

        asset_name = d.pop("assetName", UNSET)

        position = d.pop("position", UNSET)

        roblox_api_avatar_models_emote_response_model = cls(
            asset_id=asset_id,
            asset_name=asset_name,
            position=position,
        )

        return roblox_api_avatar_models_emote_response_model
