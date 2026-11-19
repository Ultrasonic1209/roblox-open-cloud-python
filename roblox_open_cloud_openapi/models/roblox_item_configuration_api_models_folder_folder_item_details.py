from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_item_configuration_api_marketplace_item import RobloxItemConfigurationApiMarketplaceItem
    from ..models.roblox_item_configuration_api_models_folder_folder import RobloxItemConfigurationApiModelsFolderFolder


T = TypeVar("T", bound="RobloxItemConfigurationApiModelsFolderFolderItemDetails")


@_attrs_define
class RobloxItemConfigurationApiModelsFolderFolderItemDetails:
    """Represents an item in a folder that can be either a MarketplaceItem or a Folder.

    Attributes:
        id (str | Unset): The unique identifier for the item.
        marketplace_item (RobloxItemConfigurationApiMarketplaceItem | Unset):
        folder (RobloxItemConfigurationApiModelsFolderFolder | Unset): Information about a folder.
    """

    id: str | Unset = UNSET
    marketplace_item: RobloxItemConfigurationApiMarketplaceItem | Unset = UNSET
    folder: RobloxItemConfigurationApiModelsFolderFolder | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        marketplace_item: dict[str, Any] | Unset = UNSET
        if not isinstance(self.marketplace_item, Unset):
            marketplace_item = self.marketplace_item.to_dict()

        folder: dict[str, Any] | Unset = UNSET
        if not isinstance(self.folder, Unset):
            folder = self.folder.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if marketplace_item is not UNSET:
            field_dict["marketplaceItem"] = marketplace_item
        if folder is not UNSET:
            field_dict["folder"] = folder

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_item_configuration_api_marketplace_item import RobloxItemConfigurationApiMarketplaceItem  # noqa: PLC0415
        from ..models.roblox_item_configuration_api_models_folder_folder import (
            RobloxItemConfigurationApiModelsFolderFolder,  # noqa: PLC0415
        )

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        _marketplace_item = d.pop("marketplaceItem", UNSET)
        marketplace_item: RobloxItemConfigurationApiMarketplaceItem | Unset
        if isinstance(_marketplace_item, Unset):
            marketplace_item = UNSET
        else:
            marketplace_item = RobloxItemConfigurationApiMarketplaceItem.from_dict(_marketplace_item)

        _folder = d.pop("folder", UNSET)
        folder: RobloxItemConfigurationApiModelsFolderFolder | Unset
        if isinstance(_folder, Unset):
            folder = UNSET
        else:
            folder = RobloxItemConfigurationApiModelsFolderFolder.from_dict(_folder)

        roblox_item_configuration_api_models_folder_folder_item_details = cls(
            id=id,
            marketplace_item=marketplace_item,
            folder=folder,
        )

        return roblox_item_configuration_api_models_folder_folder_item_details
