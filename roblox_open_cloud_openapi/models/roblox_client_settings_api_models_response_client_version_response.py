from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxClientSettingsApiModelsResponseClientVersionResponse")


@_attrs_define
class RobloxClientSettingsApiModelsResponseClientVersionResponse:
    """
    Attributes:
        version (str | Unset):
        client_version_upload (str | Unset):
        bootstrapper_version (str | Unset):
        next_client_version_upload (str | Unset):
        next_client_version (str | Unset):
    """

    version: str | Unset = UNSET
    client_version_upload: str | Unset = UNSET
    bootstrapper_version: str | Unset = UNSET
    next_client_version_upload: str | Unset = UNSET
    next_client_version: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        version = self.version

        client_version_upload = self.client_version_upload

        bootstrapper_version = self.bootstrapper_version

        next_client_version_upload = self.next_client_version_upload

        next_client_version = self.next_client_version

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if version is not UNSET:
            field_dict["version"] = version
        if client_version_upload is not UNSET:
            field_dict["clientVersionUpload"] = client_version_upload
        if bootstrapper_version is not UNSET:
            field_dict["bootstrapperVersion"] = bootstrapper_version
        if next_client_version_upload is not UNSET:
            field_dict["nextClientVersionUpload"] = next_client_version_upload
        if next_client_version is not UNSET:
            field_dict["nextClientVersion"] = next_client_version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        version = d.pop("version", UNSET)

        client_version_upload = d.pop("clientVersionUpload", UNSET)

        bootstrapper_version = d.pop("bootstrapperVersion", UNSET)

        next_client_version_upload = d.pop("nextClientVersionUpload", UNSET)

        next_client_version = d.pop("nextClientVersion", UNSET)

        roblox_client_settings_api_models_response_client_version_response = cls(
            version=version,
            client_version_upload=client_version_upload,
            bootstrapper_version=bootstrapper_version,
            next_client_version_upload=next_client_version_upload,
            next_client_version=next_client_version,
        )

        return roblox_client_settings_api_models_response_client_version_response
