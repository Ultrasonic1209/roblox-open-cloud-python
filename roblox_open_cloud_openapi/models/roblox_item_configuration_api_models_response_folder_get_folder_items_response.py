from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_item_configuration_api_models_folder_folder_item_details import (
        RobloxItemConfigurationApiModelsFolderFolderItemDetails,
    )


T = TypeVar("T", bound="RobloxItemConfigurationApiModelsResponseFolderGetFolderItemsResponse")


@_attrs_define
class RobloxItemConfigurationApiModelsResponseFolderGetFolderItemsResponse:
    """Response model for getting folder items.

    Attributes:
        items (list[RobloxItemConfigurationApiModelsFolderFolderItemDetails] | Unset): The list of items in the folder.
        next_cursor (str | Unset):
        prev_cursor (str | Unset):
    """

    items: list[RobloxItemConfigurationApiModelsFolderFolderItemDetails] | Unset = UNSET
    next_cursor: str | Unset = UNSET
    prev_cursor: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        items: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.items, Unset):
            items = []
            for items_item_data in self.items:
                items_item = items_item_data.to_dict()
                items.append(items_item)

        next_cursor = self.next_cursor

        prev_cursor = self.prev_cursor

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if items is not UNSET:
            field_dict["items"] = items
        if next_cursor is not UNSET:
            field_dict["nextCursor"] = next_cursor
        if prev_cursor is not UNSET:
            field_dict["prevCursor"] = prev_cursor

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_item_configuration_api_models_folder_folder_item_details import (
            RobloxItemConfigurationApiModelsFolderFolderItemDetails,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _items = d.pop("items", UNSET)
        items: list[RobloxItemConfigurationApiModelsFolderFolderItemDetails] | Unset = UNSET
        if _items is not UNSET:
            items = []
            for items_item_data in _items:
                items_item = RobloxItemConfigurationApiModelsFolderFolderItemDetails.from_dict(items_item_data)

                items.append(items_item)

        next_cursor = d.pop("nextCursor", UNSET)

        prev_cursor = d.pop("prevCursor", UNSET)

        roblox_item_configuration_api_models_response_folder_get_folder_items_response = cls(
            items=items,
            next_cursor=next_cursor,
            prev_cursor=prev_cursor,
        )

        return roblox_item_configuration_api_models_response_folder_get_folder_items_response
