from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..models.roblox_2_assetdelivery_v3_asset_request_item_data_model_mode import (
    Roblox2AssetdeliveryV3AssetRequestItemDataModelMode,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_2_assetdelivery_v3_asset_identifier import Roblox2AssetdeliveryV3AssetIdentifier
    from ..models.roblox_2_assetdelivery_v3_insert_context import Roblox2AssetdeliveryV3InsertContext
    from ..models.roblox_2_assetdelivery_v3_options import Roblox2AssetdeliveryV3Options
    from ..models.roblox_2_assetdelivery_v3_representation_request import Roblox2AssetdeliveryV3RepresentationRequest
    from ..models.roblox_2_assetdelivery_v3_version_strategy import Roblox2AssetdeliveryV3VersionStrategy


T = TypeVar("T", bound="Roblox2AssetdeliveryV3AssetRequestItem")


@_attrs_define
class Roblox2AssetdeliveryV3AssetRequestItem:
    """
    Attributes:
        request_id (str):
        asset (Roblox2AssetdeliveryV3AssetIdentifier):
        version (Roblox2AssetdeliveryV3VersionStrategy):
        asset_type (str | Unset):
        representation (Roblox2AssetdeliveryV3RepresentationRequest | Unset):
        skip_signing_scripts (bool | Unset):
        permission_context (str | Unset):
        options (Roblox2AssetdeliveryV3Options | Unset):
        insert_context (Roblox2AssetdeliveryV3InsertContext | Unset):
        asset_resolution_mode (str | Unset):
        data_model_mode (Roblox2AssetdeliveryV3AssetRequestItemDataModelMode | Unset):
        usage_context (str | Unset):
        access_context (Any | Unset):
        thumbnail_moderation_access_key (str | Unset):
        place_id (int | Unset):
        module_place_id (int | Unset):
        xcachesplit (int | Unset):
    """

    request_id: str
    asset: Roblox2AssetdeliveryV3AssetIdentifier
    version: Roblox2AssetdeliveryV3VersionStrategy
    asset_type: str | Unset = UNSET
    representation: Roblox2AssetdeliveryV3RepresentationRequest | Unset = UNSET
    skip_signing_scripts: bool | Unset = UNSET
    permission_context: str | Unset = UNSET
    options: Roblox2AssetdeliveryV3Options | Unset = UNSET
    insert_context: Roblox2AssetdeliveryV3InsertContext | Unset = UNSET
    asset_resolution_mode: str | Unset = UNSET
    data_model_mode: Roblox2AssetdeliveryV3AssetRequestItemDataModelMode | Unset = UNSET
    usage_context: str | Unset = UNSET
    access_context: Any | Unset = UNSET
    thumbnail_moderation_access_key: str | Unset = UNSET
    place_id: int | Unset = UNSET
    module_place_id: int | Unset = UNSET
    xcachesplit: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        request_id = self.request_id

        asset = self.asset.to_dict()

        version = self.version.to_dict()

        asset_type = self.asset_type

        representation: dict[str, Any] | Unset = UNSET
        if not isinstance(self.representation, Unset):
            representation = self.representation.to_dict()

        skip_signing_scripts = self.skip_signing_scripts

        permission_context = self.permission_context

        options: dict[str, Any] | Unset = UNSET
        if not isinstance(self.options, Unset):
            options = self.options.to_dict()

        insert_context: dict[str, Any] | Unset = UNSET
        if not isinstance(self.insert_context, Unset):
            insert_context = self.insert_context.to_dict()

        asset_resolution_mode = self.asset_resolution_mode

        data_model_mode: int | Unset = UNSET
        if not isinstance(self.data_model_mode, Unset):
            data_model_mode = self.data_model_mode.value

        usage_context = self.usage_context

        access_context = self.access_context

        thumbnail_moderation_access_key = self.thumbnail_moderation_access_key

        place_id = self.place_id

        module_place_id = self.module_place_id

        xcachesplit = self.xcachesplit

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "requestId": request_id,
                "asset": asset,
                "version": version,
            }
        )
        if asset_type is not UNSET:
            field_dict["assetType"] = asset_type
        if representation is not UNSET:
            field_dict["representation"] = representation
        if skip_signing_scripts is not UNSET:
            field_dict["skipSigningScripts"] = skip_signing_scripts
        if permission_context is not UNSET:
            field_dict["permissionContext"] = permission_context
        if options is not UNSET:
            field_dict["options"] = options
        if insert_context is not UNSET:
            field_dict["insertContext"] = insert_context
        if asset_resolution_mode is not UNSET:
            field_dict["assetResolutionMode"] = asset_resolution_mode
        if data_model_mode is not UNSET:
            field_dict["dataModelMode"] = data_model_mode
        if usage_context is not UNSET:
            field_dict["usageContext"] = usage_context
        if access_context is not UNSET:
            field_dict["accessContext"] = access_context
        if thumbnail_moderation_access_key is not UNSET:
            field_dict["thumbnailModerationAccessKey"] = thumbnail_moderation_access_key
        if place_id is not UNSET:
            field_dict["placeId"] = place_id
        if module_place_id is not UNSET:
            field_dict["modulePlaceId"] = module_place_id
        if xcachesplit is not UNSET:
            field_dict["xcachesplit"] = xcachesplit

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_2_assetdelivery_v3_asset_identifier import Roblox2AssetdeliveryV3AssetIdentifier  # noqa: PLC0415
        from ..models.roblox_2_assetdelivery_v3_insert_context import Roblox2AssetdeliveryV3InsertContext  # noqa: PLC0415
        from ..models.roblox_2_assetdelivery_v3_options import Roblox2AssetdeliveryV3Options  # noqa: PLC0415
        from ..models.roblox_2_assetdelivery_v3_representation_request import (
            Roblox2AssetdeliveryV3RepresentationRequest,  # noqa: PLC0415
        )
        from ..models.roblox_2_assetdelivery_v3_version_strategy import Roblox2AssetdeliveryV3VersionStrategy  # noqa: PLC0415

        d = dict(src_dict)
        request_id = d.pop("requestId")

        asset = Roblox2AssetdeliveryV3AssetIdentifier.from_dict(d.pop("asset"))

        version = Roblox2AssetdeliveryV3VersionStrategy.from_dict(d.pop("version"))

        asset_type = d.pop("assetType", UNSET)

        _representation = d.pop("representation", UNSET)
        representation: Roblox2AssetdeliveryV3RepresentationRequest | Unset
        if isinstance(_representation, Unset):
            representation = UNSET
        else:
            representation = Roblox2AssetdeliveryV3RepresentationRequest.from_dict(_representation)

        skip_signing_scripts = d.pop("skipSigningScripts", UNSET)

        permission_context = d.pop("permissionContext", UNSET)

        _options = d.pop("options", UNSET)
        options: Roblox2AssetdeliveryV3Options | Unset
        if isinstance(_options, Unset):
            options = UNSET
        else:
            options = Roblox2AssetdeliveryV3Options.from_dict(_options)

        _insert_context = d.pop("insertContext", UNSET)
        insert_context: Roblox2AssetdeliveryV3InsertContext | Unset
        if isinstance(_insert_context, Unset):
            insert_context = UNSET
        else:
            insert_context = Roblox2AssetdeliveryV3InsertContext.from_dict(_insert_context)

        asset_resolution_mode = d.pop("assetResolutionMode", UNSET)

        _data_model_mode = d.pop("dataModelMode", UNSET)
        data_model_mode: Roblox2AssetdeliveryV3AssetRequestItemDataModelMode | Unset
        if isinstance(_data_model_mode, Unset):
            data_model_mode = UNSET
        else:
            data_model_mode = Roblox2AssetdeliveryV3AssetRequestItemDataModelMode(_data_model_mode)

        usage_context = d.pop("usageContext", UNSET)

        access_context = d.pop("accessContext", UNSET)

        thumbnail_moderation_access_key = d.pop("thumbnailModerationAccessKey", UNSET)

        place_id = d.pop("placeId", UNSET)

        module_place_id = d.pop("modulePlaceId", UNSET)

        xcachesplit = d.pop("xcachesplit", UNSET)

        roblox_2_assetdelivery_v3_asset_request_item = cls(
            request_id=request_id,
            asset=asset,
            version=version,
            asset_type=asset_type,
            representation=representation,
            skip_signing_scripts=skip_signing_scripts,
            permission_context=permission_context,
            options=options,
            insert_context=insert_context,
            asset_resolution_mode=asset_resolution_mode,
            data_model_mode=data_model_mode,
            usage_context=usage_context,
            access_context=access_context,
            thumbnail_moderation_access_key=thumbnail_moderation_access_key,
            place_id=place_id,
            module_place_id=module_place_id,
            xcachesplit=xcachesplit,
        )

        return roblox_2_assetdelivery_v3_asset_request_item
