from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxApiAvatarModelsV4AvatarProfileFrameRequestModel")


@_attrs_define
class RobloxApiAvatarModelsV4AvatarProfileFrameRequestModel:
    """A model which contains the asset id of the profile frame.

    Attributes:
        id (int | Unset): An asset id. Use 0 to clear the equipped frame.
    """

    id: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        id = d.pop("id", UNSET)

        roblox_api_avatar_models_v4_avatar_profile_frame_request_model = cls(
            id=id,
        )

        return roblox_api_avatar_models_v4_avatar_profile_frame_request_model
