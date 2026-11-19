from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.roblox_item_configuration_api_models_folder_folder_item_item_type import (
    RobloxItemConfigurationApiModelsFolderFolderItemItemType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxItemConfigurationApiModelsFolderFolderItem")


@_attrs_define
class RobloxItemConfigurationApiModelsFolderFolderItem:
    """Represents an identifier for an item in a folder.

    Attributes:
        id (str | Unset): The unique identifier for the item.
        item_type (RobloxItemConfigurationApiModelsFolderFolderItemItemType | Unset): The type of the item to be added
            to the folder. ['Unknown' = 0, 'Asset' = 1, 'Bundle' = 2, 'IECToken' = 3, 'Folder' = 4]
    """

    id: str | Unset = UNSET
    item_type: RobloxItemConfigurationApiModelsFolderFolderItemItemType | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        item_type: str | Unset = UNSET
        if not isinstance(self.item_type, Unset):
            item_type = self.item_type.value

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if item_type is not UNSET:
            field_dict["itemType"] = item_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        _item_type = d.pop("itemType", UNSET)
        item_type: RobloxItemConfigurationApiModelsFolderFolderItemItemType | Unset
        if isinstance(_item_type, Unset):
            item_type = UNSET
        else:
            item_type = RobloxItemConfigurationApiModelsFolderFolderItemItemType(_item_type)

        roblox_item_configuration_api_models_folder_folder_item = cls(
            id=id,
            item_type=item_type,
        )

        return roblox_item_configuration_api_models_folder_folder_item
