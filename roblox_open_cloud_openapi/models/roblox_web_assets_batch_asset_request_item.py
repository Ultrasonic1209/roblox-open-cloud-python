from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxWebAssetsBatchAssetRequestItem")


@_attrs_define
class RobloxWebAssetsBatchAssetRequestItem:
    """
    Attributes:
        asset_name (str | Unset):
        asset_type (str | Unset):
        client_insert (bool | Unset):
        place_id (int | Unset):
        request_id (str | Unset):
        script_insert (bool | Unset):
        server_place_id (int | Unset):
        universe_id (int | Unset):
        accept (str | Unset):
        encoding (str | Unset):
        hash_ (str | Unset):
        user_asset_id (int | Unset):
        asset_id (int | Unset):
        version (int | Unset):
        asset_version_id (int | Unset):
        module_place_id (int | Unset):
        asset_format (str | Unset):
        roblox_asset_format (str | Unset):
        asset_resolution_mode (str | Unset):
        access_context (str | Unset):
        usage_context (int | Unset):
        content_representation_priority_list (str | Unset):
        do_not_fallback_to_baseline_representation (bool | Unset):
    """

    asset_name: str | Unset = UNSET
    asset_type: str | Unset = UNSET
    client_insert: bool | Unset = UNSET
    place_id: int | Unset = UNSET
    request_id: str | Unset = UNSET
    script_insert: bool | Unset = UNSET
    server_place_id: int | Unset = UNSET
    universe_id: int | Unset = UNSET
    accept: str | Unset = UNSET
    encoding: str | Unset = UNSET
    hash_: str | Unset = UNSET
    user_asset_id: int | Unset = UNSET
    asset_id: int | Unset = UNSET
    version: int | Unset = UNSET
    asset_version_id: int | Unset = UNSET
    module_place_id: int | Unset = UNSET
    asset_format: str | Unset = UNSET
    roblox_asset_format: str | Unset = UNSET
    asset_resolution_mode: str | Unset = UNSET
    access_context: str | Unset = UNSET
    usage_context: int | Unset = UNSET
    content_representation_priority_list: str | Unset = UNSET
    do_not_fallback_to_baseline_representation: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        asset_name = self.asset_name

        asset_type = self.asset_type

        client_insert = self.client_insert

        place_id = self.place_id

        request_id = self.request_id

        script_insert = self.script_insert

        server_place_id = self.server_place_id

        universe_id = self.universe_id

        accept = self.accept

        encoding = self.encoding

        hash_ = self.hash_

        user_asset_id = self.user_asset_id

        asset_id = self.asset_id

        version = self.version

        asset_version_id = self.asset_version_id

        module_place_id = self.module_place_id

        asset_format = self.asset_format

        roblox_asset_format = self.roblox_asset_format

        asset_resolution_mode = self.asset_resolution_mode

        access_context = self.access_context

        usage_context = self.usage_context

        content_representation_priority_list = self.content_representation_priority_list

        do_not_fallback_to_baseline_representation = self.do_not_fallback_to_baseline_representation

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if asset_name is not UNSET:
            field_dict["assetName"] = asset_name
        if asset_type is not UNSET:
            field_dict["assetType"] = asset_type
        if client_insert is not UNSET:
            field_dict["clientInsert"] = client_insert
        if place_id is not UNSET:
            field_dict["placeId"] = place_id
        if request_id is not UNSET:
            field_dict["requestId"] = request_id
        if script_insert is not UNSET:
            field_dict["scriptInsert"] = script_insert
        if server_place_id is not UNSET:
            field_dict["serverPlaceId"] = server_place_id
        if universe_id is not UNSET:
            field_dict["universeId"] = universe_id
        if accept is not UNSET:
            field_dict["accept"] = accept
        if encoding is not UNSET:
            field_dict["encoding"] = encoding
        if hash_ is not UNSET:
            field_dict["hash"] = hash_
        if user_asset_id is not UNSET:
            field_dict["userAssetId"] = user_asset_id
        if asset_id is not UNSET:
            field_dict["assetId"] = asset_id
        if version is not UNSET:
            field_dict["version"] = version
        if asset_version_id is not UNSET:
            field_dict["assetVersionId"] = asset_version_id
        if module_place_id is not UNSET:
            field_dict["modulePlaceId"] = module_place_id
        if asset_format is not UNSET:
            field_dict["assetFormat"] = asset_format
        if roblox_asset_format is not UNSET:
            field_dict["roblox-assetFormat"] = roblox_asset_format
        if asset_resolution_mode is not UNSET:
            field_dict["assetResolutionMode"] = asset_resolution_mode
        if access_context is not UNSET:
            field_dict["accessContext"] = access_context
        if usage_context is not UNSET:
            field_dict["usageContext"] = usage_context
        if content_representation_priority_list is not UNSET:
            field_dict["contentRepresentationPriorityList"] = content_representation_priority_list
        if do_not_fallback_to_baseline_representation is not UNSET:
            field_dict["doNotFallbackToBaselineRepresentation"] = do_not_fallback_to_baseline_representation

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        asset_name = d.pop("assetName", UNSET)

        asset_type = d.pop("assetType", UNSET)

        client_insert = d.pop("clientInsert", UNSET)

        place_id = d.pop("placeId", UNSET)

        request_id = d.pop("requestId", UNSET)

        script_insert = d.pop("scriptInsert", UNSET)

        server_place_id = d.pop("serverPlaceId", UNSET)

        universe_id = d.pop("universeId", UNSET)

        accept = d.pop("accept", UNSET)

        encoding = d.pop("encoding", UNSET)

        hash_ = d.pop("hash", UNSET)

        user_asset_id = d.pop("userAssetId", UNSET)

        asset_id = d.pop("assetId", UNSET)

        version = d.pop("version", UNSET)

        asset_version_id = d.pop("assetVersionId", UNSET)

        module_place_id = d.pop("modulePlaceId", UNSET)

        asset_format = d.pop("assetFormat", UNSET)

        roblox_asset_format = d.pop("roblox-assetFormat", UNSET)

        asset_resolution_mode = d.pop("assetResolutionMode", UNSET)

        access_context = d.pop("accessContext", UNSET)

        usage_context = d.pop("usageContext", UNSET)

        content_representation_priority_list = d.pop("contentRepresentationPriorityList", UNSET)

        do_not_fallback_to_baseline_representation = d.pop("doNotFallbackToBaselineRepresentation", UNSET)

        roblox_web_assets_batch_asset_request_item = cls(
            asset_name=asset_name,
            asset_type=asset_type,
            client_insert=client_insert,
            place_id=place_id,
            request_id=request_id,
            script_insert=script_insert,
            server_place_id=server_place_id,
            universe_id=universe_id,
            accept=accept,
            encoding=encoding,
            hash_=hash_,
            user_asset_id=user_asset_id,
            asset_id=asset_id,
            version=version,
            asset_version_id=asset_version_id,
            module_place_id=module_place_id,
            asset_format=asset_format,
            roblox_asset_format=roblox_asset_format,
            asset_resolution_mode=asset_resolution_mode,
            access_context=access_context,
            usage_context=usage_context,
            content_representation_priority_list=content_representation_priority_list,
            do_not_fallback_to_baseline_representation=do_not_fallback_to_baseline_representation,
        )

        return roblox_web_assets_batch_asset_request_item
