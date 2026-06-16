from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_trades_api_models_v2_item_target import RobloxTradesApiModelsV2ItemTarget


T = TypeVar("T", bound="RobloxTradesApiModelsV2TradableItemInstance")


@_attrs_define
class RobloxTradesApiModelsV2TradableItemInstance:
    """A tradable item instance.

    Attributes:
        collectible_item_instance_id (str | Unset): The collectible item instance id.
        item_target (RobloxTradesApiModelsV2ItemTarget | Unset): The underlying of a tradable item.
        item_name (str | Unset): The name of the item.
        serial_number (int | Unset): The serial number of the item if it is LimitedUnique.
        original_price (int | Unset): The original price of the item.
        recent_average_price (int | Unset): The recent average price of the item.
        asset_stock (int | Unset): Total quantity of the item.
        is_on_hold (bool | Unset): Whether the item is on hold.
    """

    collectible_item_instance_id: str | Unset = UNSET
    item_target: RobloxTradesApiModelsV2ItemTarget | Unset = UNSET
    item_name: str | Unset = UNSET
    serial_number: int | Unset = UNSET
    original_price: int | Unset = UNSET
    recent_average_price: int | Unset = UNSET
    asset_stock: int | Unset = UNSET
    is_on_hold: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        collectible_item_instance_id = self.collectible_item_instance_id

        item_target: dict[str, Any] | Unset = UNSET
        if not isinstance(self.item_target, Unset):
            item_target = self.item_target.to_dict()

        item_name = self.item_name

        serial_number = self.serial_number

        original_price = self.original_price

        recent_average_price = self.recent_average_price

        asset_stock = self.asset_stock

        is_on_hold = self.is_on_hold

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if collectible_item_instance_id is not UNSET:
            field_dict["collectibleItemInstanceId"] = collectible_item_instance_id
        if item_target is not UNSET:
            field_dict["itemTarget"] = item_target
        if item_name is not UNSET:
            field_dict["itemName"] = item_name
        if serial_number is not UNSET:
            field_dict["serialNumber"] = serial_number
        if original_price is not UNSET:
            field_dict["originalPrice"] = original_price
        if recent_average_price is not UNSET:
            field_dict["recentAveragePrice"] = recent_average_price
        if asset_stock is not UNSET:
            field_dict["assetStock"] = asset_stock
        if is_on_hold is not UNSET:
            field_dict["isOnHold"] = is_on_hold

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_trades_api_models_v2_item_target import RobloxTradesApiModelsV2ItemTarget

        d = dict(src_dict)
        collectible_item_instance_id = d.pop("collectibleItemInstanceId", UNSET)

        _item_target = d.pop("itemTarget", UNSET)
        item_target: RobloxTradesApiModelsV2ItemTarget | Unset
        if isinstance(_item_target, Unset):
            item_target = UNSET
        else:
            item_target = RobloxTradesApiModelsV2ItemTarget.from_dict(_item_target)

        item_name = d.pop("itemName", UNSET)

        serial_number = d.pop("serialNumber", UNSET)

        original_price = d.pop("originalPrice", UNSET)

        recent_average_price = d.pop("recentAveragePrice", UNSET)

        asset_stock = d.pop("assetStock", UNSET)

        is_on_hold = d.pop("isOnHold", UNSET)

        roblox_trades_api_models_v2_tradable_item_instance = cls(
            collectible_item_instance_id=collectible_item_instance_id,
            item_target=item_target,
            item_name=item_name,
            serial_number=serial_number,
            original_price=original_price,
            recent_average_price=recent_average_price,
            asset_stock=asset_stock,
            is_on_hold=is_on_hold,
        )

        return roblox_trades_api_models_v2_tradable_item_instance
