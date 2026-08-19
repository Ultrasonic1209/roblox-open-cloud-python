from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxApiAvatarModelsInvalidBackgroundResponse")


@_attrs_define
class RobloxApiAvatarModelsInvalidBackgroundResponse:
    """
    Attributes:
        background_asset_id (int | Unset): The asset id of the emote
        error (str | Unset): The error associated with the background.
    """

    background_asset_id: int | Unset = UNSET
    error: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        background_asset_id = self.background_asset_id

        error = self.error

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if background_asset_id is not UNSET:
            field_dict["BackgroundAssetId"] = background_asset_id
        if error is not UNSET:
            field_dict["Error"] = error

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        background_asset_id = d.pop("BackgroundAssetId", UNSET)

        error = d.pop("Error", UNSET)

        roblox_api_avatar_models_invalid_background_response = cls(
            background_asset_id=background_asset_id,
            error=error,
        )

        return roblox_api_avatar_models_invalid_background_response
