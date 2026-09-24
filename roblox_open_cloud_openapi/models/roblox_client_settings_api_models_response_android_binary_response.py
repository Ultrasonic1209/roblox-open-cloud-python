from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_client_settings_api_models_response_android_binary_library_names import (
        RobloxClientSettingsApiModelsResponseAndroidBinaryLibraryNames,
    )


T = TypeVar("T", bound="RobloxClientSettingsApiModelsResponseAndroidBinaryResponse")


@_attrs_define
class RobloxClientSettingsApiModelsResponseAndroidBinaryResponse:
    """Contains information about an Android Binary Module for a given channel.
    including its module name, the names of its libraries, and whether the channel supports Android binaries.

        Attributes:
            library_names (RobloxClientSettingsApiModelsResponseAndroidBinaryLibraryNames): Contains the names of the
                libraries in an Android Binary Module.
            module_name (str | Unset): The name of the Android Binary Module.
            supports_android_binaries (bool | Unset): True if the channel supports android binaries. False otherwise.
    """

    library_names: RobloxClientSettingsApiModelsResponseAndroidBinaryLibraryNames
    module_name: str | Unset = UNSET
    supports_android_binaries: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        library_names = self.library_names.to_dict()

        module_name = self.module_name

        supports_android_binaries = self.supports_android_binaries

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "libraryNames": library_names,
            }
        )
        if module_name is not UNSET:
            field_dict["moduleName"] = module_name
        if supports_android_binaries is not UNSET:
            field_dict["supportsAndroidBinaries"] = supports_android_binaries

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_client_settings_api_models_response_android_binary_library_names import (
            RobloxClientSettingsApiModelsResponseAndroidBinaryLibraryNames,
        )

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        library_names = RobloxClientSettingsApiModelsResponseAndroidBinaryLibraryNames.from_dict(d.pop("libraryNames"))

        module_name = d.pop("moduleName", UNSET)

        supports_android_binaries = d.pop("supportsAndroidBinaries", UNSET)

        roblox_client_settings_api_models_response_android_binary_response = cls(
            library_names=library_names,
            module_name=module_name,
            supports_android_binaries=supports_android_binaries,
        )

        return roblox_client_settings_api_models_response_android_binary_response
