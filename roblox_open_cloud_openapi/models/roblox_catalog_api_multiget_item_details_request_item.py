from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.roblox_catalog_api_multiget_item_details_request_item_item_type import (
    RobloxCatalogApiMultigetItemDetailsRequestItemItemType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxCatalogApiMultigetItemDetailsRequestItem")


@_attrs_define
class RobloxCatalogApiMultigetItemDetailsRequestItem:
    """
    Attributes:
        item_type (RobloxCatalogApiMultigetItemDetailsRequestItemItemType | Unset):  ['Asset' = 1, 'Bundle' = 2]
        id (int | Unset):
    """

    item_type: RobloxCatalogApiMultigetItemDetailsRequestItemItemType | Unset = UNSET
    id: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        item_type: int | Unset = UNSET
        if not isinstance(self.item_type, Unset):
            item_type = self.item_type.value

        id = self.id

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if item_type is not UNSET:
            field_dict["itemType"] = item_type
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        _item_type = d.pop("itemType", UNSET)
        item_type: RobloxCatalogApiMultigetItemDetailsRequestItemItemType | Unset
        if isinstance(_item_type, Unset):
            item_type = UNSET
        else:
            item_type = RobloxCatalogApiMultigetItemDetailsRequestItemItemType(_item_type)

        id = d.pop("id", UNSET)

        roblox_catalog_api_multiget_item_details_request_item = cls(
            item_type=item_type,
            id=id,
        )

        return roblox_catalog_api_multiget_item_details_request_item
