from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..models.roblox_api_avatar_models_update_avatar_request_model_update_mask_item import (
    RobloxApiAvatarModelsUpdateAvatarRequestModelUpdateMaskItem,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_api_avatar_models_update_avatar_data_model import RobloxApiAvatarModelsUpdateAvatarDataModel


T = TypeVar("T", bound="RobloxApiAvatarModelsUpdateAvatarRequestModel")


@_attrs_define
class RobloxApiAvatarModelsUpdateAvatarRequestModel:
    """A model containing details about an avatar update request.

    Attributes:
        update_mask (list[RobloxApiAvatarModelsUpdateAvatarRequestModelUpdateMaskItem] | Unset): Update mask specifying
            which avatar fields to update (can include multiple).
            Acceptable values:
            - UpdateAvatarType: updates avatar.type (R6/R15)
            - UpdateScales: updates avatar.scale
            - UpdateBodyColors: updates avatar.body_color_set
            - UpdateAssets: updates avatar.avatar_assets
        data (RobloxApiAvatarModelsUpdateAvatarDataModel | Unset): A model containing details about an avatar.
    """

    update_mask: list[RobloxApiAvatarModelsUpdateAvatarRequestModelUpdateMaskItem] | Unset = UNSET
    data: RobloxApiAvatarModelsUpdateAvatarDataModel | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        update_mask: list[int] | Unset = UNSET
        if not isinstance(self.update_mask, Unset):
            update_mask = []
            for update_mask_item_data in self.update_mask:
                update_mask_item = update_mask_item_data.value
                update_mask.append(update_mask_item)

        data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if update_mask is not UNSET:
            field_dict["updateMask"] = update_mask
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_api_avatar_models_update_avatar_data_model import (
            RobloxApiAvatarModelsUpdateAvatarDataModel,
        )

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        _update_mask = d.pop("updateMask", UNSET)
        update_mask: list[RobloxApiAvatarModelsUpdateAvatarRequestModelUpdateMaskItem] | Unset = UNSET
        if _update_mask is not UNSET:
            update_mask = []
            for update_mask_item_data in _update_mask:
                update_mask_item = RobloxApiAvatarModelsUpdateAvatarRequestModelUpdateMaskItem(update_mask_item_data)

                update_mask.append(update_mask_item)

        _data = d.pop("data", UNSET)
        data: RobloxApiAvatarModelsUpdateAvatarDataModel | Unset
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = RobloxApiAvatarModelsUpdateAvatarDataModel.from_dict(_data)

        roblox_api_avatar_models_update_avatar_request_model = cls(
            update_mask=update_mask,
            data=data,
        )

        return roblox_api_avatar_models_update_avatar_request_model
