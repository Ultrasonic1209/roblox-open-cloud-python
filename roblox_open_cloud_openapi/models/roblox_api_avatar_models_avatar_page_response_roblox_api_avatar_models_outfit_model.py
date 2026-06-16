from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_api_avatar_models_outfit_model import RobloxApiAvatarModelsOutfitModel


T = TypeVar("T", bound="RobloxApiAvatarModelsAvatarPageResponseRobloxApiAvatarModelsOutfitModel")


@_attrs_define
class RobloxApiAvatarModelsAvatarPageResponseRobloxApiAvatarModelsOutfitModel:
    """Avatar page response.

    Attributes:
        data (list[RobloxApiAvatarModelsOutfitModel] | Unset): The data
        pagination_token (str | Unset): A non empty string indicates that there is more data available than this
            response contains. An empty string indicates the last page.
    """

    data: list[RobloxApiAvatarModelsOutfitModel] | Unset = UNSET
    pagination_token: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        data: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.data, Unset):
            data = []
            for data_item_data in self.data:
                data_item = data_item_data.to_dict()
                data.append(data_item)

        pagination_token = self.pagination_token

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if data is not UNSET:
            field_dict["data"] = data
        if pagination_token is not UNSET:
            field_dict["paginationToken"] = pagination_token

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_api_avatar_models_outfit_model import RobloxApiAvatarModelsOutfitModel

        d = dict(src_dict)
        _data = d.pop("data", UNSET)
        data: list[RobloxApiAvatarModelsOutfitModel] | Unset = UNSET
        if _data is not UNSET:
            data = []
            for data_item_data in _data:
                data_item = RobloxApiAvatarModelsOutfitModel.from_dict(data_item_data)

                data.append(data_item)

        pagination_token = d.pop("paginationToken", UNSET)

        roblox_api_avatar_models_avatar_page_response_roblox_api_avatar_models_outfit_model = cls(
            data=data,
            pagination_token=pagination_token,
        )

        return roblox_api_avatar_models_avatar_page_response_roblox_api_avatar_models_outfit_model
