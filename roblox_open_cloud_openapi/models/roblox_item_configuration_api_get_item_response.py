from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_item_configuration_api_marketplace_item import RobloxItemConfigurationApiMarketplaceItem


T = TypeVar("T", bound="RobloxItemConfigurationApiGetItemResponse")


@_attrs_define
class RobloxItemConfigurationApiGetItemResponse:
    """Defines the response model for the GET v1/marketplace-items/get-item.

    Attributes:
        item (RobloxItemConfigurationApiMarketplaceItem | Unset):
    """

    item: RobloxItemConfigurationApiMarketplaceItem | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        item: dict[str, Any] | Unset = UNSET
        if not isinstance(self.item, Unset):
            item = self.item.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if item is not UNSET:
            field_dict["item"] = item

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_item_configuration_api_marketplace_item import RobloxItemConfigurationApiMarketplaceItem  # noqa: PLC0415

        d = dict(src_dict)
        _item = d.pop("item", UNSET)
        item: RobloxItemConfigurationApiMarketplaceItem | Unset
        if isinstance(_item, Unset):
            item = UNSET
        else:
            item = RobloxItemConfigurationApiMarketplaceItem.from_dict(_item)

        roblox_item_configuration_api_get_item_response = cls(
            item=item,
        )

        return roblox_item_configuration_api_get_item_response
