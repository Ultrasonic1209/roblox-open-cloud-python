from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxApiAvatarModelsInvalidProfileFrameResponse")


@_attrs_define
class RobloxApiAvatarModelsInvalidProfileFrameResponse:
    """Validation error for a profile frame that could not be applied.

    Attributes:
        frame_asset_id (int | Unset): The asset id of the profile frame.
        error (str | Unset): The error associated with the profile frame.
    """

    frame_asset_id: int | Unset = UNSET
    error: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        frame_asset_id = self.frame_asset_id

        error = self.error

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if frame_asset_id is not UNSET:
            field_dict["FrameAssetId"] = frame_asset_id
        if error is not UNSET:
            field_dict["Error"] = error

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        frame_asset_id = d.pop("FrameAssetId", UNSET)

        error = d.pop("Error", UNSET)

        roblox_api_avatar_models_invalid_profile_frame_response = cls(
            frame_asset_id=frame_asset_id,
            error=error,
        )

        return roblox_api_avatar_models_invalid_profile_frame_response
