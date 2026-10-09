from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_api_avatar_models_v4_avatar_background_request_model import (
        RobloxApiAvatarModelsV4AvatarBackgroundRequestModel,
    )


T = TypeVar("T", bound="RobloxApiAvatarModelsV4UpdateOutfitConfig")


@_attrs_define
class RobloxApiAvatarModelsV4UpdateOutfitConfig:
    """A model containing outfit config fields to update.

    Attributes:
        background_request_model (RobloxApiAvatarModelsV4AvatarBackgroundRequestModel | Unset): A model which contains
            the asset id of the background. This can be
            extended to have more attributes in the future.
    """

    background_request_model: RobloxApiAvatarModelsV4AvatarBackgroundRequestModel | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        background_request_model: dict[str, Any] | Unset = UNSET
        if not isinstance(self.background_request_model, Unset):
            background_request_model = self.background_request_model.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if background_request_model is not UNSET:
            field_dict["backgroundRequestModel"] = background_request_model

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_api_avatar_models_v4_avatar_background_request_model import (
            RobloxApiAvatarModelsV4AvatarBackgroundRequestModel,
        )

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        _background_request_model = d.pop("backgroundRequestModel", UNSET)
        background_request_model: RobloxApiAvatarModelsV4AvatarBackgroundRequestModel | Unset
        if isinstance(_background_request_model, Unset):
            background_request_model = UNSET
        else:
            background_request_model = RobloxApiAvatarModelsV4AvatarBackgroundRequestModel.from_dict(
                _background_request_model
            )

        roblox_api_avatar_models_v4_update_outfit_config = cls(
            background_request_model=background_request_model,
        )

        return roblox_api_avatar_models_v4_update_outfit_config
