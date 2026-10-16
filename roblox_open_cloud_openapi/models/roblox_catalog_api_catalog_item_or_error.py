from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..models.roblox_catalog_api_catalog_item_or_error_item_type import RobloxCatalogApiCatalogItemOrErrorItemType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_catalog_api_catalog_search_detailed_complete_response_item import (
        RobloxCatalogApiCatalogSearchDetailedCompleteResponseItem,
    )


T = TypeVar("T", bound="RobloxCatalogApiCatalogItemOrError")


@_attrs_define
class RobloxCatalogApiCatalogItemOrError:
    """A union type representing either a successfully hydrated item or an error.
    Exactly one of Roblox.Catalog.Api.CatalogItemOrError.Item or Roblox.Catalog.Api.CatalogItemOrError.HttpStatusCode
    will be non-null.

        Attributes:
            id (int | Unset):
            item_type (RobloxCatalogApiCatalogItemOrErrorItemType | Unset):  ['Asset' = 1, 'Bundle' = 2]
            item (RobloxCatalogApiCatalogSearchDetailedCompleteResponseItem | Unset): The detailed model for catalog items,
                complete with economy and ownership info.
                This response model is bound in the game-engine here:
                https://create.roblox.com/docs/reference/engine/classes/AvatarEditorService#GetItemDetails.
            http_status_code (int | Unset):
    """

    id: int | Unset = UNSET
    item_type: RobloxCatalogApiCatalogItemOrErrorItemType | Unset = UNSET
    item: RobloxCatalogApiCatalogSearchDetailedCompleteResponseItem | Unset = UNSET
    http_status_code: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        item_type: int | Unset = UNSET
        if not isinstance(self.item_type, Unset):
            item_type = self.item_type.value

        item: dict[str, Any] | Unset = UNSET
        if not isinstance(self.item, Unset):
            item = self.item.to_dict()

        http_status_code = self.http_status_code

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if item_type is not UNSET:
            field_dict["itemType"] = item_type
        if item is not UNSET:
            field_dict["item"] = item
        if http_status_code is not UNSET:
            field_dict["httpStatusCode"] = http_status_code

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_catalog_api_catalog_search_detailed_complete_response_item import (
            RobloxCatalogApiCatalogSearchDetailedCompleteResponseItem,
        )

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        id = d.pop("id", UNSET)

        _item_type = d.pop("itemType", UNSET)
        item_type: RobloxCatalogApiCatalogItemOrErrorItemType | Unset
        if isinstance(_item_type, Unset):
            item_type = UNSET
        else:
            item_type = RobloxCatalogApiCatalogItemOrErrorItemType(_item_type)

        _item = d.pop("item", UNSET)
        item: RobloxCatalogApiCatalogSearchDetailedCompleteResponseItem | Unset
        if isinstance(_item, Unset):
            item = UNSET
        else:
            item = RobloxCatalogApiCatalogSearchDetailedCompleteResponseItem.from_dict(_item)

        http_status_code = d.pop("httpStatusCode", UNSET)

        roblox_catalog_api_catalog_item_or_error = cls(
            id=id,
            item_type=item_type,
            item=item,
            http_status_code=http_status_code,
        )

        return roblox_catalog_api_catalog_item_or_error
