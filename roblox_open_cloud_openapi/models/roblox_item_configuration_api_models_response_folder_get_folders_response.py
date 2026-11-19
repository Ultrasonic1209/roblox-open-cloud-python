from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_item_configuration_api_models_folder_folder import RobloxItemConfigurationApiModelsFolderFolder


T = TypeVar("T", bound="RobloxItemConfigurationApiModelsResponseFolderGetFoldersResponse")


@_attrs_define
class RobloxItemConfigurationApiModelsResponseFolderGetFoldersResponse:
    """Response model for getting folders.

    Attributes:
        folders (list[RobloxItemConfigurationApiModelsFolderFolder] | Unset): The list of folders for the authenticated
            user.
    """

    folders: list[RobloxItemConfigurationApiModelsFolderFolder] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        folders: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.folders, Unset):
            folders = []
            for folders_item_data in self.folders:
                folders_item = folders_item_data.to_dict()
                folders.append(folders_item)

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if folders is not UNSET:
            field_dict["folders"] = folders

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_item_configuration_api_models_folder_folder import (
            RobloxItemConfigurationApiModelsFolderFolder,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _folders = d.pop("folders", UNSET)
        folders: list[RobloxItemConfigurationApiModelsFolderFolder] | Unset = UNSET
        if _folders is not UNSET:
            folders = []
            for folders_item_data in _folders:
                folders_item = RobloxItemConfigurationApiModelsFolderFolder.from_dict(folders_item_data)

                folders.append(folders_item)

        roblox_item_configuration_api_models_response_folder_get_folders_response = cls(
            folders=folders,
        )

        return roblox_item_configuration_api_models_response_folder_get_folders_response
