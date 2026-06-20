from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_api_avatar_models_outfit_model import RobloxApiAvatarModelsOutfitModel


T = TypeVar("T", bound="RobloxApiAvatarModelsAvatarFilteredPageResponseRobloxApiAvatarModelsOutfitModel")


@_attrs_define
class RobloxApiAvatarModelsAvatarFilteredPageResponseRobloxApiAvatarModelsOutfitModel:
    """Filtered page response

    Attributes:
        filtered_count (int | Unset): Number of !:TPagedObject filtered.
        data (list[RobloxApiAvatarModelsOutfitModel] | Unset):
        total (int | Unset):
    """

    filtered_count: int | Unset = UNSET
    data: list[RobloxApiAvatarModelsOutfitModel] | Unset = UNSET
    total: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        filtered_count = self.filtered_count

        data: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.data, Unset):
            data = []
            for data_item_data in self.data:
                data_item = data_item_data.to_dict()
                data.append(data_item)

        total = self.total

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if filtered_count is not UNSET:
            field_dict["filteredCount"] = filtered_count
        if data is not UNSET:
            field_dict["data"] = data
        if total is not UNSET:
            field_dict["total"] = total

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_api_avatar_models_outfit_model import RobloxApiAvatarModelsOutfitModel

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        filtered_count = d.pop("filteredCount", UNSET)

        _data = d.pop("data", UNSET)
        data: list[RobloxApiAvatarModelsOutfitModel] | Unset = UNSET
        if _data is not UNSET:
            data = []
            for data_item_data in _data:
                data_item = RobloxApiAvatarModelsOutfitModel.from_dict(data_item_data)

                data.append(data_item)

        total = d.pop("total", UNSET)

        roblox_api_avatar_models_avatar_filtered_page_response_roblox_api_avatar_models_outfit_model = cls(
            filtered_count=filtered_count,
            data=data,
            total=total,
        )

        return roblox_api_avatar_models_avatar_filtered_page_response_roblox_api_avatar_models_outfit_model
