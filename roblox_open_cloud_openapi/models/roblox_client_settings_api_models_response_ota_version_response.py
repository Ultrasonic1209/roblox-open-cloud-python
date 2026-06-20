from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_client_settings_api_models_response_ota_version_response_assets_manifest import (
        RobloxClientSettingsApiModelsResponseOtaVersionResponseAssetsManifest,
    )


T = TypeVar("T", bound="RobloxClientSettingsApiModelsResponseOtaVersionResponse")


@_attrs_define
class RobloxClientSettingsApiModelsResponseOtaVersionResponse:
    """Response for endpoints returning ota information.

    Attributes:
        name (str | Unset): Ota library/plugin name
        version (str | Unset): Version number of asset
        download_url (str | Unset): URL to download the ota asset
        is_standalone (bool | Unset): Refers to whether the plugin is core to Studio functions, and is used to determine
            when it is loaded.
        asset_id (str | Unset): The asset ID of the LuaApp OTA.
        asset_version (str | Unset): The asset version of the LuaApp OTA.
        max_app_version (str | Unset): The maximum application version compatible with the LuaApp OTA.
        tryout_name (str | Unset): The name of the tryout for the LuaApp OTA.
        local_asset_uri (str | Unset): The local asset URI for the LuaApp OTA.
        is_forced_update (bool | Unset): Indicates whether the LuaApp OTA is a forced update.
        app_storage_reset_id (str | Unset): The application storage reset ID for the LuaApp OTA.
        is_development_config (bool | Unset): Indicates whether the LuaApp OTA is a development configuration.
        assets_manifest (RobloxClientSettingsApiModelsResponseOtaVersionResponseAssetsManifest | Unset): Inlined assets
            manifest for the LuaApp OTA.
        version_v2 (int | Unset): VersionV2 of the OTA asset.
    """

    name: str | Unset = UNSET
    version: str | Unset = UNSET
    download_url: str | Unset = UNSET
    is_standalone: bool | Unset = UNSET
    asset_id: str | Unset = UNSET
    asset_version: str | Unset = UNSET
    max_app_version: str | Unset = UNSET
    tryout_name: str | Unset = UNSET
    local_asset_uri: str | Unset = UNSET
    is_forced_update: bool | Unset = UNSET
    app_storage_reset_id: str | Unset = UNSET
    is_development_config: bool | Unset = UNSET
    assets_manifest: RobloxClientSettingsApiModelsResponseOtaVersionResponseAssetsManifest | Unset = UNSET
    version_v2: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        version = self.version

        download_url = self.download_url

        is_standalone = self.is_standalone

        asset_id = self.asset_id

        asset_version = self.asset_version

        max_app_version = self.max_app_version

        tryout_name = self.tryout_name

        local_asset_uri = self.local_asset_uri

        is_forced_update = self.is_forced_update

        app_storage_reset_id = self.app_storage_reset_id

        is_development_config = self.is_development_config

        assets_manifest: dict[str, Any] | Unset = UNSET
        if not isinstance(self.assets_manifest, Unset):
            assets_manifest = self.assets_manifest.to_dict()

        version_v2 = self.version_v2

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if version is not UNSET:
            field_dict["version"] = version
        if download_url is not UNSET:
            field_dict["downloadUrl"] = download_url
        if is_standalone is not UNSET:
            field_dict["isStandalone"] = is_standalone
        if asset_id is not UNSET:
            field_dict["assetId"] = asset_id
        if asset_version is not UNSET:
            field_dict["assetVersion"] = asset_version
        if max_app_version is not UNSET:
            field_dict["maxAppVersion"] = max_app_version
        if tryout_name is not UNSET:
            field_dict["tryoutName"] = tryout_name
        if local_asset_uri is not UNSET:
            field_dict["localAssetURI"] = local_asset_uri
        if is_forced_update is not UNSET:
            field_dict["isForcedUpdate"] = is_forced_update
        if app_storage_reset_id is not UNSET:
            field_dict["appStorageResetId"] = app_storage_reset_id
        if is_development_config is not UNSET:
            field_dict["isDevelopmentConfig"] = is_development_config
        if assets_manifest is not UNSET:
            field_dict["assetsManifest"] = assets_manifest
        if version_v2 is not UNSET:
            field_dict["versionV2"] = version_v2

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_client_settings_api_models_response_ota_version_response_assets_manifest import (
            RobloxClientSettingsApiModelsResponseOtaVersionResponseAssetsManifest,
        )

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        name = d.pop("name", UNSET)

        version = d.pop("version", UNSET)

        download_url = d.pop("downloadUrl", UNSET)

        is_standalone = d.pop("isStandalone", UNSET)

        asset_id = d.pop("assetId", UNSET)

        asset_version = d.pop("assetVersion", UNSET)

        max_app_version = d.pop("maxAppVersion", UNSET)

        tryout_name = d.pop("tryoutName", UNSET)

        local_asset_uri = d.pop("localAssetURI", UNSET)

        is_forced_update = d.pop("isForcedUpdate", UNSET)

        app_storage_reset_id = d.pop("appStorageResetId", UNSET)

        is_development_config = d.pop("isDevelopmentConfig", UNSET)

        _assets_manifest = d.pop("assetsManifest", UNSET)
        assets_manifest: RobloxClientSettingsApiModelsResponseOtaVersionResponseAssetsManifest | Unset
        if isinstance(_assets_manifest, Unset):
            assets_manifest = UNSET
        else:
            assets_manifest = RobloxClientSettingsApiModelsResponseOtaVersionResponseAssetsManifest.from_dict(
                _assets_manifest
            )

        version_v2 = d.pop("versionV2", UNSET)

        roblox_client_settings_api_models_response_ota_version_response = cls(
            name=name,
            version=version,
            download_url=download_url,
            is_standalone=is_standalone,
            asset_id=asset_id,
            asset_version=asset_version,
            max_app_version=max_app_version,
            tryout_name=tryout_name,
            local_asset_uri=local_asset_uri,
            is_forced_update=is_forced_update,
            app_storage_reset_id=app_storage_reset_id,
            is_development_config=is_development_config,
            assets_manifest=assets_manifest,
            version_v2=version_v2,
        )

        return roblox_client_settings_api_models_response_ota_version_response
