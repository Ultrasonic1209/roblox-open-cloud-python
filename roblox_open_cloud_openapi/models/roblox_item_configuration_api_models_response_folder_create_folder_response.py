from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxItemConfigurationApiModelsResponseFolderCreateFolderResponse")


@_attrs_define
class RobloxItemConfigurationApiModelsResponseFolderCreateFolderResponse:
    """Response model for creating a folder.

    Attributes:
        folder_id (str | Unset): The ID of the created folder.
    """

    folder_id: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        folder_id = self.folder_id

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if folder_id is not UNSET:
            field_dict["folderId"] = folder_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        folder_id = d.pop("folderId", UNSET)

        roblox_item_configuration_api_models_response_folder_create_folder_response = cls(
            folder_id=folder_id,
        )

        return roblox_item_configuration_api_models_response_folder_create_folder_response
