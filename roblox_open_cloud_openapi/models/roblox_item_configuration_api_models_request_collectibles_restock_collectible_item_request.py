from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxItemConfigurationApiModelsRequestCollectiblesRestockCollectibleItemRequest")


@_attrs_define
class RobloxItemConfigurationApiModelsRequestCollectiblesRestockCollectibleItemRequest:
    """Request model for restocking a collectible item.

    Attributes:
        new_total_quantity (int | Unset): The new total quantity for the item after restocking.
        agreed_restocking_fee (int | Unset): The restocking fee the user agreed to pay.
    """

    new_total_quantity: int | Unset = UNSET
    agreed_restocking_fee: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        new_total_quantity = self.new_total_quantity

        agreed_restocking_fee = self.agreed_restocking_fee

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if new_total_quantity is not UNSET:
            field_dict["newTotalQuantity"] = new_total_quantity
        if agreed_restocking_fee is not UNSET:
            field_dict["agreedRestockingFee"] = agreed_restocking_fee

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        new_total_quantity = d.pop("newTotalQuantity", UNSET)

        agreed_restocking_fee = d.pop("agreedRestockingFee", UNSET)

        roblox_item_configuration_api_models_request_collectibles_restock_collectible_item_request = cls(
            new_total_quantity=new_total_quantity,
            agreed_restocking_fee=agreed_restocking_fee,
        )

        return roblox_item_configuration_api_models_request_collectibles_restock_collectible_item_request
