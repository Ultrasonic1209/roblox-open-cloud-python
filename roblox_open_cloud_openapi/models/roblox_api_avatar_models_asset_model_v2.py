from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_api_avatar_models_asset_meta_model_v1 import RobloxApiAvatarModelsAssetMetaModelV1
    from ..models.roblox_api_avatar_models_asset_type_model import RobloxApiAvatarModelsAssetTypeModel


T = TypeVar("T", bound="RobloxApiAvatarModelsAssetModelV2")


@_attrs_define
class RobloxApiAvatarModelsAssetModelV2:
    """A model containing details about an asset
    - V2: adds CurrentVersionId, AssetMetaModel

        Attributes:
            id (int | Unset): The id
            name (str | Unset): The name
            asset_type (RobloxApiAvatarModelsAssetTypeModel | Unset): A model containing details about an asset type
            current_version_id (int | Unset): Id of the current version of asset
            meta (RobloxApiAvatarModelsAssetMetaModelV1 | Unset): Exhaustive model denoting all possible metadata fields of
                an asset
            availability_status (str | Unset): Asset availability status.
            expiration_time (datetime.datetime | Unset): For rental assets only. (Future) ownership expiration time of the
                asset.
            supports_head_shapes (bool | Unset): If the "Id" is swappable, applicable for DH assets.
    """

    id: int | Unset = UNSET
    name: str | Unset = UNSET
    asset_type: RobloxApiAvatarModelsAssetTypeModel | Unset = UNSET
    current_version_id: int | Unset = UNSET
    meta: RobloxApiAvatarModelsAssetMetaModelV1 | Unset = UNSET
    availability_status: str | Unset = UNSET
    expiration_time: datetime.datetime | Unset = UNSET
    supports_head_shapes: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        asset_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.asset_type, Unset):
            asset_type = self.asset_type.to_dict()

        current_version_id = self.current_version_id

        meta: dict[str, Any] | Unset = UNSET
        if not isinstance(self.meta, Unset):
            meta = self.meta.to_dict()

        availability_status = self.availability_status

        expiration_time: str | Unset = UNSET
        if not isinstance(self.expiration_time, Unset):
            expiration_time = self.expiration_time.isoformat()

        supports_head_shapes = self.supports_head_shapes

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if asset_type is not UNSET:
            field_dict["assetType"] = asset_type
        if current_version_id is not UNSET:
            field_dict["currentVersionId"] = current_version_id
        if meta is not UNSET:
            field_dict["meta"] = meta
        if availability_status is not UNSET:
            field_dict["availabilityStatus"] = availability_status
        if expiration_time is not UNSET:
            field_dict["expirationTime"] = expiration_time
        if supports_head_shapes is not UNSET:
            field_dict["supportsHeadShapes"] = supports_head_shapes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_api_avatar_models_asset_meta_model_v1 import RobloxApiAvatarModelsAssetMetaModelV1
        from ..models.roblox_api_avatar_models_asset_type_model import RobloxApiAvatarModelsAssetTypeModel

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        _asset_type = d.pop("assetType", UNSET)
        asset_type: RobloxApiAvatarModelsAssetTypeModel | Unset
        if isinstance(_asset_type, Unset):
            asset_type = UNSET
        else:
            asset_type = RobloxApiAvatarModelsAssetTypeModel.from_dict(_asset_type)

        current_version_id = d.pop("currentVersionId", UNSET)

        _meta = d.pop("meta", UNSET)
        meta: RobloxApiAvatarModelsAssetMetaModelV1 | Unset
        if isinstance(_meta, Unset):
            meta = UNSET
        else:
            meta = RobloxApiAvatarModelsAssetMetaModelV1.from_dict(_meta)

        availability_status = d.pop("availabilityStatus", UNSET)

        _expiration_time = d.pop("expirationTime", UNSET)
        expiration_time: datetime.datetime | Unset
        if isinstance(_expiration_time, Unset):
            expiration_time = UNSET
        else:
            expiration_time = datetime.datetime.fromisoformat(_expiration_time)

        supports_head_shapes = d.pop("supportsHeadShapes", UNSET)

        roblox_api_avatar_models_asset_model_v2 = cls(
            id=id,
            name=name,
            asset_type=asset_type,
            current_version_id=current_version_id,
            meta=meta,
            availability_status=availability_status,
            expiration_time=expiration_time,
            supports_head_shapes=supports_head_shapes,
        )

        return roblox_api_avatar_models_asset_model_v2
