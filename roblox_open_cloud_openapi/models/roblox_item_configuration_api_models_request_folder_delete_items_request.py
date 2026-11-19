from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_item_configuration_api_models_folder_folder_item import (
        RobloxItemConfigurationApiModelsFolderFolderItem,
    )


T = TypeVar("T", bound="RobloxItemConfigurationApiModelsRequestFolderDeleteItemsRequest")


@_attrs_define
class RobloxItemConfigurationApiModelsRequestFolderDeleteItemsRequest:
    """Request model for removing one or more items from a folder via the bulk DELETE endpoint.

    Attributes:
        items (list[RobloxItemConfigurationApiModelsFolderFolderItem] | Unset): The items to remove from the folder.
    """

    items: list[RobloxItemConfigurationApiModelsFolderFolderItem] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        items: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.items, Unset):
            items = []
            for items_item_data in self.items:
                items_item = items_item_data.to_dict()
                items.append(items_item)

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if items is not UNSET:
            field_dict["items"] = items

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_item_configuration_api_models_folder_folder_item import (
            RobloxItemConfigurationApiModelsFolderFolderItem,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _items = d.pop("items", UNSET)
        items: list[RobloxItemConfigurationApiModelsFolderFolderItem] | Unset = UNSET
        if _items is not UNSET:
            items = []
            for items_item_data in _items:
                items_item = RobloxItemConfigurationApiModelsFolderFolderItem.from_dict(items_item_data)

                items.append(items_item)

        roblox_item_configuration_api_models_request_folder_delete_items_request = cls(
            items=items,
        )

        return roblox_item_configuration_api_models_request_folder_delete_items_request
