from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_api_avatar_models_asset_wear_model import RobloxApiAvatarModelsAssetWearModel


T = TypeVar("T", bound="RobloxApiAvatarModelsWearRequestModel")


@_attrs_define
class RobloxApiAvatarModelsWearRequestModel:
    """A model that contains a list of AssetWear models

    Attributes:
        assets (list[RobloxApiAvatarModelsAssetWearModel] | Unset): The asset ids
    """

    assets: list[RobloxApiAvatarModelsAssetWearModel] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        assets: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.assets, Unset):
            assets = []
            for assets_item_data in self.assets:
                assets_item = assets_item_data.to_dict()
                assets.append(assets_item)

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if assets is not UNSET:
            field_dict["assets"] = assets

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_api_avatar_models_asset_wear_model import RobloxApiAvatarModelsAssetWearModel

        d = dict(src_dict)
        _assets = d.pop("assets", UNSET)
        assets: list[RobloxApiAvatarModelsAssetWearModel] | Unset = UNSET
        if _assets is not UNSET:
            assets = []
            for assets_item_data in _assets:
                assets_item = RobloxApiAvatarModelsAssetWearModel.from_dict(assets_item_data)

                assets.append(assets_item)

        roblox_api_avatar_models_wear_request_model = cls(
            assets=assets,
        )

        return roblox_api_avatar_models_wear_request_model
