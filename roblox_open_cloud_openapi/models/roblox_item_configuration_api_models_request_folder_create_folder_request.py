from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxItemConfigurationApiModelsRequestFolderCreateFolderRequest")


@_attrs_define
class RobloxItemConfigurationApiModelsRequestFolderCreateFolderRequest:
    """Request model for creating a new folder.

    Attributes:
        name (str | Unset): The name of the folder to create.
        parent_folder_id (str | Unset): The ID of the parent folder. Null for root folders.
        group_id (int | Unset): The group id that the folder will to belong to.
    """

    name: str | Unset = UNSET
    parent_folder_id: str | Unset = UNSET
    group_id: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        parent_folder_id = self.parent_folder_id

        group_id = self.group_id

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if parent_folder_id is not UNSET:
            field_dict["parentFolderId"] = parent_folder_id
        if group_id is not UNSET:
            field_dict["groupId"] = group_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        parent_folder_id = d.pop("parentFolderId", UNSET)

        group_id = d.pop("groupId", UNSET)

        roblox_item_configuration_api_models_request_folder_create_folder_request = cls(
            name=name,
            parent_folder_id=parent_folder_id,
            group_id=group_id,
        )

        return roblox_item_configuration_api_models_request_folder_create_folder_request
