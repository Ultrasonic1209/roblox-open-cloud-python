from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.inventory_item_collectible_details_instance_state import InventoryItemCollectibleDetailsInstanceState
from ..types import UNSET, Unset

T = TypeVar("T", bound="InventoryItemCollectibleDetails")


@_attrs_define
class InventoryItemCollectibleDetails:
    """Specific fields that are applicable to a collectible.

    Attributes:
        item_id (str | Unset): A unique ID of a Roblox item that is a collectible.
        instance_id (str | Unset): A unique ID of an individual copy of a collectible with ownership tied
            to a group or user.
        instance_state (InventoryItemCollectibleDetailsInstanceState | Unset): The instance state of this specific
            Collectible Item Instance which
            affects whether it can be resold or traded.
        serial_number (int | None | Unset): If the asset is a Limited, a user-visible number that shows this item is
            the nth replica of the asset. Otherwise, this attribute will be omitted.
    """

    item_id: str | Unset = UNSET
    instance_id: str | Unset = UNSET
    instance_state: InventoryItemCollectibleDetailsInstanceState | Unset = UNSET
    serial_number: int | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        item_id = self.item_id

        instance_id = self.instance_id

        instance_state: str | Unset = UNSET
        if not isinstance(self.instance_state, Unset):
            instance_state = self.instance_state.value

        serial_number: int | None | Unset
        if isinstance(self.serial_number, Unset):
            serial_number = UNSET
        else:
            serial_number = self.serial_number

        field_dict: dict[str, Any] = {}

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

        def _parse_serial_number(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        serial_number = _parse_serial_number(d.pop("serialNumber", UNSET))

        inventory_item_collectible_details = cls(
            item_id=item_id,
            instance_id=instance_id,
            instance_state=instance_state,
            serial_number=serial_number,
        )

        return inventory_item_collectible_details
