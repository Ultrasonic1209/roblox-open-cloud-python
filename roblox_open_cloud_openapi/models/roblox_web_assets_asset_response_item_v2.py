from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_web_assets_asset_content_representation_specifier import (
        RobloxWebAssetsAssetContentRepresentationSpecifier,
    )
    from ..models.roblox_web_assets_asset_format_location import RobloxWebAssetsAssetFormatLocation
    from ..models.roblox_web_assets_i_asset_item_error import RobloxWebAssetsIAssetItemError


T = TypeVar("T", bound="RobloxWebAssetsAssetResponseItemV2")


@_attrs_define
class RobloxWebAssetsAssetResponseItemV2:
    """
    Attributes:
        locations (list[RobloxWebAssetsAssetFormatLocation] | Unset):
        errors (list[RobloxWebAssetsIAssetItemError] | Unset):
        request_id (str | Unset):
        is_archived (bool | Unset): Whether the asset has been archived.
        asset_type_id (int | Unset): Asset Type.
        content_representation_specifier (RobloxWebAssetsAssetContentRepresentationSpecifier | Unset):
        is_recordable (bool | Unset): Whether the asset is recordable in screen recordings.
    """

    locations: list[RobloxWebAssetsAssetFormatLocation] | Unset = UNSET
    errors: list[RobloxWebAssetsIAssetItemError] | Unset = UNSET
    request_id: str | Unset = UNSET
    is_archived: bool | Unset = UNSET
    asset_type_id: int | Unset = UNSET
    content_representation_specifier: RobloxWebAssetsAssetContentRepresentationSpecifier | Unset = UNSET
    is_recordable: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        locations: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.locations, Unset):
            locations = []
            for locations_item_data in self.locations:
                locations_item = locations_item_data.to_dict()
                locations.append(locations_item)

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

        is_recordable = self.is_recordable

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if locations is not UNSET:
            field_dict["locations"] = locations
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
        if is_recordable is not UNSET:
            field_dict["isRecordable"] = is_recordable

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_web_assets_asset_content_representation_specifier import (
            RobloxWebAssetsAssetContentRepresentationSpecifier,
        )
        from ..models.roblox_web_assets_asset_format_location import RobloxWebAssetsAssetFormatLocation
        from ..models.roblox_web_assets_i_asset_item_error import RobloxWebAssetsIAssetItemError

        d = dict(src_dict)
        _locations = d.pop("locations", UNSET)
        locations: list[RobloxWebAssetsAssetFormatLocation] | Unset = UNSET
        if _locations is not UNSET:
            locations = []
            for locations_item_data in _locations:
                locations_item = RobloxWebAssetsAssetFormatLocation.from_dict(locations_item_data)

                locations.append(locations_item)

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

        is_recordable = d.pop("isRecordable", UNSET)

        roblox_web_assets_asset_response_item_v2 = cls(
            locations=locations,
            errors=errors,
            request_id=request_id,
            is_archived=is_archived,
            asset_type_id=asset_type_id,
            content_representation_specifier=content_representation_specifier,
            is_recordable=is_recordable,
        )

        return roblox_web_assets_asset_response_item_v2
