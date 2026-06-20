from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_trades_api_models_v2_tradable_item import RobloxTradesApiModelsV2TradableItem


T = TypeVar("T", bound="RobloxTradesApiModelsV2GetUserTradableItemsResponse")


@_attrs_define
class RobloxTradesApiModelsV2GetUserTradableItemsResponse:
    """The response for the GetUserTradableItems endpoint.

    Attributes:
        user_id (int | Unset): The ID of the user.
        items (list[RobloxTradesApiModelsV2TradableItem] | Unset): The items that the user can trade.
        next_page_cursor (str | Unset): The cursor for the next page of items.
    """

    user_id: int | Unset = UNSET
    items: list[RobloxTradesApiModelsV2TradableItem] | Unset = UNSET
    next_page_cursor: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        user_id = self.user_id

        items: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.items, Unset):
            items = []
            for items_item_data in self.items:
                items_item = items_item_data.to_dict()
                items.append(items_item)

        next_page_cursor = self.next_page_cursor

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if user_id is not UNSET:
            field_dict["userId"] = user_id
        if items is not UNSET:
            field_dict["items"] = items
        if next_page_cursor is not UNSET:
            field_dict["nextPageCursor"] = next_page_cursor

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_trades_api_models_v2_tradable_item import RobloxTradesApiModelsV2TradableItem

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        user_id = d.pop("userId", UNSET)

        _items = d.pop("items", UNSET)
        items: list[RobloxTradesApiModelsV2TradableItem] | Unset = UNSET
        if _items is not UNSET:
            items = []
            for items_item_data in _items:
                items_item = RobloxTradesApiModelsV2TradableItem.from_dict(items_item_data)

                items.append(items_item)

        next_page_cursor = d.pop("nextPageCursor", UNSET)

        roblox_trades_api_models_v2_get_user_tradable_items_response = cls(
            user_id=user_id,
            items=items,
            next_page_cursor=next_page_cursor,
        )

        return roblox_trades_api_models_v2_get_user_tradable_items_response
