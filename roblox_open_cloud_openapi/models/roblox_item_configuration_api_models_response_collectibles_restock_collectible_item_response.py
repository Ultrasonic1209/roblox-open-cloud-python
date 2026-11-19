from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxItemConfigurationApiModelsResponseCollectiblesRestockCollectibleItemResponse")


@_attrs_define
class RobloxItemConfigurationApiModelsResponseCollectiblesRestockCollectibleItemResponse:
    """Response model for restocking a collectible item.

    Attributes:
        new_total_quantity (int | Unset): The new total quantity after restock.
    """

    new_total_quantity: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        new_total_quantity = self.new_total_quantity

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if new_total_quantity is not UNSET:
            field_dict["newTotalQuantity"] = new_total_quantity

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        new_total_quantity = d.pop("newTotalQuantity", UNSET)

        roblox_item_configuration_api_models_response_collectibles_restock_collectible_item_response = cls(
            new_total_quantity=new_total_quantity,
        )

        return roblox_item_configuration_api_models_response_collectibles_restock_collectible_item_response
