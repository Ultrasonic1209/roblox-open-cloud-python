from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_asset_delivery_api_asset_metadata import RobloxAssetDeliveryApiAssetMetadata
    from ..models.roblox_web_assets_asset_content_representation_specifier import (
        RobloxWebAssetsAssetContentRepresentationSpecifier,
    )
    from ..models.roblox_web_assets_i_asset_item_error import RobloxWebAssetsIAssetItemError


T = TypeVar("T", bound="RobloxWebAssetsAssetResponseItemV1")


@_attrs_define
class RobloxWebAssetsAssetResponseItemV1:
    """
    Attributes:
        location (str | Unset):
        errors (list[RobloxWebAssetsIAssetItemError] | Unset):
        request_id (str | Unset):
        is_archived (bool | Unset): Whether the asset has been archived.
        asset_type_id (int | Unset): Asset Type.
        content_representation_specifier (RobloxWebAssetsAssetContentRepresentationSpecifier | Unset):
        asset_metadatas (list[RobloxAssetDeliveryApiAssetMetadata] | Unset):
        is_recordable (bool | Unset): Whether the asset is recordable in screen recordings.
    """

    location: str | Unset = UNSET
    errors: list[RobloxWebAssetsIAssetItemError] | Unset = UNSET
    request_id: str | Unset = UNSET
    is_archived: bool | Unset = UNSET
    asset_type_id: int | Unset = UNSET
    content_representation_specifier: RobloxWebAssetsAssetContentRepresentationSpecifier | Unset = UNSET
    asset_metadatas: list[RobloxAssetDeliveryApiAssetMetadata] | Unset = UNSET
    is_recordable: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        location = self.location

        errors: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.errors, Unset):
            errors = []
            for errors_item_data in self.errors:
                errors_item = errors_item_data.to_dict()
                errors.append(errors_item)

        request_id = self.request_id

        is_archived = self.is_archived

        asset_type_id = self.asset_type_id

        content_representation_specifier: dict[str, Any] | Unset = UNSET
        if not isinstance(self.content_representation_specifier, Unset):
            content_representation_specifier = self.content_representation_specifier.to_dict()

        asset_metadatas: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.asset_metadatas, Unset):
            asset_metadatas = []
            for asset_metadatas_item_data in self.asset_metadatas:
                asset_metadatas_item = asset_metadatas_item_data.to_dict()
                asset_metadatas.append(asset_metadatas_item)

        is_recordable = self.is_recordable

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if location is not UNSET:
            field_dict["location"] = location
        if errors is not UNSET:
            field_dict["errors"] = errors
        if request_id is not UNSET:
            field_dict["requestId"] = request_id
        if is_archived is not UNSET:
            field_dict["isArchived"] = is_archived
        if asset_type_id is not UNSET:
            field_dict["assetTypeId"] = asset_type_id
        if content_representation_specifier is not UNSET:
            field_dict["contentRepresentationSpecifier"] = content_representation_specifier
        if asset_metadatas is not UNSET:
            field_dict["assetMetadatas"] = asset_metadatas
        if is_recordable is not UNSET:
            field_dict["isRecordable"] = is_recordable

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_asset_delivery_api_asset_metadata import RobloxAssetDeliveryApiAssetMetadata
        from ..models.roblox_web_assets_asset_content_representation_specifier import (
            RobloxWebAssetsAssetContentRepresentationSpecifier,
        )
        from ..models.roblox_web_assets_i_asset_item_error import RobloxWebAssetsIAssetItemError

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        location = d.pop("location", UNSET)

        _errors = d.pop("errors", UNSET)
        errors: list[RobloxWebAssetsIAssetItemError] | Unset = UNSET
        if _errors is not UNSET:
            errors = []
            for errors_item_data in _errors:
                errors_item = RobloxWebAssetsIAssetItemError.from_dict(errors_item_data)

                errors.append(errors_item)

        request_id = d.pop("requestId", UNSET)

        is_archived = d.pop("isArchived", UNSET)

        asset_type_id = d.pop("assetTypeId", UNSET)

        _content_representation_specifier = d.pop("contentRepresentationSpecifier", UNSET)
        content_representation_specifier: RobloxWebAssetsAssetContentRepresentationSpecifier | Unset
        if isinstance(_content_representation_specifier, Unset):
            content_representation_specifier = UNSET
        else:
            content_representation_specifier = RobloxWebAssetsAssetContentRepresentationSpecifier.from_dict(
                _content_representation_specifier
            )

        _asset_metadatas = d.pop("assetMetadatas", UNSET)
        asset_metadatas: list[RobloxAssetDeliveryApiAssetMetadata] | Unset = UNSET
        if _asset_metadatas is not UNSET:
            asset_metadatas = []
            for asset_metadatas_item_data in _asset_metadatas:
                asset_metadatas_item = RobloxAssetDeliveryApiAssetMetadata.from_dict(asset_metadatas_item_data)

                asset_metadatas.append(asset_metadatas_item)

        is_recordable = d.pop("isRecordable", UNSET)

        roblox_web_assets_asset_response_item_v1 = cls(
            location=location,
            errors=errors,
            request_id=request_id,
            is_archived=is_archived,
            asset_type_id=asset_type_id,
            content_representation_specifier=content_representation_specifier,
            asset_metadatas=asset_metadatas,
            is_recordable=is_recordable,
        )

        return roblox_web_assets_asset_response_item_v1
