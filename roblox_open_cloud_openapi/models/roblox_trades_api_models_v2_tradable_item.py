from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_trades_api_models_v2_item_target import RobloxTradesApiModelsV2ItemTarget
    from ..models.roblox_trades_api_models_v2_tradable_item_instance import RobloxTradesApiModelsV2TradableItemInstance


T = TypeVar("T", bound="RobloxTradesApiModelsV2TradableItem")


@_attrs_define
class RobloxTradesApiModelsV2TradableItem:
    """A tradable item.

    Attributes:
        collectible_item_id (str | Unset): The collectible item id.
        item_target (RobloxTradesApiModelsV2ItemTarget | Unset): The underlying of a tradable item.
        item_name (str | Unset): The name of the item.
        original_price (int | Unset): The original price of the item.
        recent_average_price (int | Unset): The recent average price of the item.
        asset_stock (int | Unset): Total quantity of the item.
        instances (list[RobloxTradesApiModelsV2TradableItemInstance] | Unset):
    """

    collectible_item_id: str | Unset = UNSET
    item_target: RobloxTradesApiModelsV2ItemTarget | Unset = UNSET
    item_name: str | Unset = UNSET
    original_price: int | Unset = UNSET
    recent_average_price: int | Unset = UNSET
    asset_stock: int | Unset = UNSET
    instances: list[RobloxTradesApiModelsV2TradableItemInstance] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        collectible_item_id = self.collectible_item_id

        item_target: dict[str, Any] | Unset = UNSET
        if not isinstance(self.item_target, Unset):
            item_target = self.item_target.to_dict()

        item_name = self.item_name

        original_price = self.original_price

        recent_average_price = self.recent_average_price

        asset_stock = self.asset_stock

        instances: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.instances, Unset):
            instances = []
            for instances_item_data in self.instances:
                instances_item = instances_item_data.to_dict()
                instances.append(instances_item)

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if collectible_item_id is not UNSET:
            field_dict["collectibleItemId"] = collectible_item_id
        if item_target is not UNSET:
            field_dict["itemTarget"] = item_target
        if item_name is not UNSET:
            field_dict["itemName"] = item_name
        if original_price is not UNSET:
            field_dict["originalPrice"] = original_price
        if recent_average_price is not UNSET:
            field_dict["recentAveragePrice"] = recent_average_price
        if asset_stock is not UNSET:
            field_dict["assetStock"] = asset_stock
        if instances is not UNSET:
            field_dict["instances"] = instances

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_trades_api_models_v2_item_target import RobloxTradesApiModelsV2ItemTarget
        from ..models.roblox_trades_api_models_v2_tradable_item_instance import (
            RobloxTradesApiModelsV2TradableItemInstance,
        )

        d = dict(src_dict)
        collectible_item_id = d.pop("collectibleItemId", UNSET)

        _item_target = d.pop("itemTarget", UNSET)
        item_target: RobloxTradesApiModelsV2ItemTarget | Unset
        if isinstance(_item_target, Unset):
            item_target = UNSET
        else:
            item_target = RobloxTradesApiModelsV2ItemTarget.from_dict(_item_target)

        item_name = d.pop("itemName", UNSET)

        original_price = d.pop("originalPrice", UNSET)

        recent_average_price = d.pop("recentAveragePrice", UNSET)

        asset_stock = d.pop("assetStock", UNSET)

        _instances = d.pop("instances", UNSET)
        instances: list[RobloxTradesApiModelsV2TradableItemInstance] | Unset = UNSET
        if _instances is not UNSET:
            instances = []
            for instances_item_data in _instances:
                instances_item = RobloxTradesApiModelsV2TradableItemInstance.from_dict(instances_item_data)

                instances.append(instances_item)

        roblox_trades_api_models_v2_tradable_item = cls(
            collectible_item_id=collectible_item_id,
            item_target=item_target,
            item_name=item_name,
            original_price=original_price,
            recent_average_price=recent_average_price,
            asset_stock=asset_stock,
            instances=instances,
        )

        return roblox_trades_api_models_v2_tradable_item
