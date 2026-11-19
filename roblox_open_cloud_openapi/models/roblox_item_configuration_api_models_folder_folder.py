from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxItemConfigurationApiModelsFolderFolder")


@_attrs_define
class RobloxItemConfigurationApiModelsFolderFolder:
    """Information about a folder.

    Attributes:
        folder_id (str | Unset): The unique identifier for the folder.
        name (str | Unset): The name of the folder.
        parent_folder_id (str | Unset): The ID of the parent folder. Null for root folders.
    """

    folder_id: str | Unset = UNSET
    name: str | Unset = UNSET
    parent_folder_id: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        folder_id = self.folder_id

        name = self.name

        parent_folder_id = self.parent_folder_id

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if folder_id is not UNSET:
            field_dict["folderId"] = folder_id
        if name is not UNSET:
            field_dict["name"] = name
        if parent_folder_id is not UNSET:
            field_dict["parentFolderId"] = parent_folder_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        folder_id = d.pop("folderId", UNSET)

        name = d.pop("name", UNSET)

        parent_folder_id = d.pop("parentFolderId", UNSET)

        roblox_item_configuration_api_models_folder_folder = cls(
            folder_id=folder_id,
            name=name,
            parent_folder_id=parent_folder_id,
        )

        return roblox_item_configuration_api_models_folder_folder
