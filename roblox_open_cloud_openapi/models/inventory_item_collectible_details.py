from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.inventory_item_collectible_details_instance_state import InventoryItemCollectibleDetailsInstanceState
from ..types import UNSET, Unset

T = TypeVar("T", bound="InventoryItemCollectibleDetails")


@_attrs_define
class InventoryItemCollectibleDetails:
    """Specific fields that are applicable to a collectible.

    Attributes:
        item_id (str | Unset): A unique ID of a Roblox item that is a collectible. Example:
            521cca19-75bb-4e05-a0af-633b1532c24d.
        instance_id (str | Unset): A unique ID of an individual copy of a collectible with ownership tied
            to a group or user. Example: a8a27d38-ee51-4cf4-8b0a-485d0dfd8607.
        instance_state (InventoryItemCollectibleDetailsInstanceState | Unset): The instance state of this specific
            Collectible Item Instance which
            affects whether it can be resold or traded.

            Possible values:

              | Value | Description |
              | --- | --- |
              | COLLECTIBLE_ITEM_INSTANCE_STATE_UNSPECIFIED | Default CollectibleItemInstanceState |
              | AVAILABLE | Collectible item is available for all actions |
              | HOLD | Collectible item is on hold (can't be resold or traded) | Example:
            COLLECTIBLE_ITEM_INSTANCE_STATE_UNSPECIFIED.
        serial_number (int | Unset): If the asset is a Limited, a user-visible number that shows this item is
            the nth replica of the asset. Otherwise, this attribute will be omitted. Example: 160.
    """

    item_id: str | Unset = UNSET
    instance_id: str | Unset = UNSET
    instance_state: InventoryItemCollectibleDetailsInstanceState | Unset = UNSET
    serial_number: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        item_id = self.item_id

        instance_id = self.instance_id

        instance_state: str | Unset = UNSET
        if not isinstance(self.instance_state, Unset):
            instance_state = self.instance_state.value

        serial_number = self.serial_number

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if item_id is not UNSET:
            field_dict["itemId"] = item_id
        if instance_id is not UNSET:
            field_dict["instanceId"] = instance_id
        if instance_state is not UNSET:
            field_dict["instanceState"] = instance_state
        if serial_number is not UNSET:
            field_dict["serialNumber"] = serial_number

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        item_id = d.pop("itemId", UNSET)

        instance_id = d.pop("instanceId", UNSET)

        _instance_state = d.pop("instanceState", UNSET)
        instance_state: InventoryItemCollectibleDetailsInstanceState | Unset
        if isinstance(_instance_state, Unset):
            instance_state = UNSET
        else:
            instance_state = InventoryItemCollectibleDetailsInstanceState(_instance_state)

        serial_number = d.pop("serialNumber", UNSET)

        inventory_item_collectible_details = cls(
            item_id=item_id,
            instance_id=instance_id,
            instance_state=instance_state,
            serial_number=serial_number,
        )

        inventory_item_collectible_details.additional_properties = d
        return inventory_item_collectible_details

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
