from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_api_avatar_models_asset_meta_model_v1 import RobloxApiAvatarModelsAssetMetaModelV1


T = TypeVar("T", bound="RobloxApiAvatarModelsAssetWearModel")


@_attrs_define
class RobloxApiAvatarModelsAssetWearModel:
    """A model which contains
    - an asset id
    - AssetMetaModel

        Attributes:
            id (int | Unset): An asset id
            meta (RobloxApiAvatarModelsAssetMetaModelV1 | Unset): Exhaustive model denoting all possible metadata fields of
                an asset
    """

    id: int | Unset = UNSET
    meta: RobloxApiAvatarModelsAssetMetaModelV1 | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        meta: dict[str, Any] | Unset = UNSET
        if not isinstance(self.meta, Unset):
            meta = self.meta.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if meta is not UNSET:
            field_dict["meta"] = meta

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_api_avatar_models_asset_meta_model_v1 import RobloxApiAvatarModelsAssetMetaModelV1

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        id = d.pop("id", UNSET)

        _meta = d.pop("meta", UNSET)
        meta: RobloxApiAvatarModelsAssetMetaModelV1 | Unset
        if isinstance(_meta, Unset):
            meta = UNSET
        else:
            meta = RobloxApiAvatarModelsAssetMetaModelV1.from_dict(_meta)

        roblox_api_avatar_models_asset_wear_model = cls(
            id=id,
            meta=meta,
        )

        return roblox_api_avatar_models_asset_wear_model
