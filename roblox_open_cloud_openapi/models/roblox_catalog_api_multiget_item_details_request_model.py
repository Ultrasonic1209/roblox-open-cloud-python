from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_catalog_api_multiget_item_details_request_item import (
        RobloxCatalogApiMultigetItemDetailsRequestItem,
    )


T = TypeVar("T", bound="RobloxCatalogApiMultigetItemDetailsRequestModel")


@_attrs_define
class RobloxCatalogApiMultigetItemDetailsRequestModel:
    """
    Attributes:
        items (list[RobloxCatalogApiMultigetItemDetailsRequestItem] | Unset): The items to retrieve details for. Each
            endpoint has an item count limit per request.
    """

    items: list[RobloxCatalogApiMultigetItemDetailsRequestItem] | Unset = UNSET

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
        from ..models.roblox_catalog_api_multiget_item_details_request_item import (
            RobloxCatalogApiMultigetItemDetailsRequestItem,
        )

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        _items = d.pop("items", UNSET)
        items: list[RobloxCatalogApiMultigetItemDetailsRequestItem] | Unset = UNSET
        if _items is not UNSET:
            items = []
            for items_item_data in _items:
                items_item = RobloxCatalogApiMultigetItemDetailsRequestItem.from_dict(items_item_data)

                items.append(items_item)

        roblox_catalog_api_multiget_item_details_request_model = cls(
            items=items,
        )

        return roblox_catalog_api_multiget_item_details_request_model
