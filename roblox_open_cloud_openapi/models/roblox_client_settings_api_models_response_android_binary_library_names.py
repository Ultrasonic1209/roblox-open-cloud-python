from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxClientSettingsApiModelsResponseAndroidBinaryLibraryNames")


@_attrs_define
class RobloxClientSettingsApiModelsResponseAndroidBinaryLibraryNames:
    """Contains the names of the libraries in an Android Binary Module.

    Attributes:
        engine (str | Unset): Name of the engine library.
    """

    engine: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        engine = self.engine

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if engine is not UNSET:
            field_dict["engine"] = engine

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        engine = d.pop("engine", UNSET)

        roblox_client_settings_api_models_response_android_binary_library_names = cls(
            engine=engine,
        )

        return roblox_client_settings_api_models_response_android_binary_library_names
