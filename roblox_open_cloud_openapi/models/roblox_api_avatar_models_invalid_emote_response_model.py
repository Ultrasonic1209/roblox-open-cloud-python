from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxApiAvatarModelsInvalidEmoteResponseModel")


@_attrs_define
class RobloxApiAvatarModelsInvalidEmoteResponseModel:
    """Response object representing an invalid emote

    Attributes:
        asset_id (int | Unset): The asset id of the emote
        position (int | Unset): The position the emote is equipped to
        error (str | Unset): The error occured while trying to equip this emote
    """

    asset_id: int | Unset = UNSET
    position: int | Unset = UNSET
    error: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        asset_id = self.asset_id

        position = self.position

        error = self.error

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if asset_id is not UNSET:
            field_dict["assetId"] = asset_id
        if position is not UNSET:
            field_dict["position"] = position
        if error is not UNSET:
            field_dict["error"] = error

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        asset_id = d.pop("assetId", UNSET)

        position = d.pop("position", UNSET)

        error = d.pop("error", UNSET)

        roblox_api_avatar_models_invalid_emote_response_model = cls(
            asset_id=asset_id,
            position=position,
            error=error,
        )

        return roblox_api_avatar_models_invalid_emote_response_model
