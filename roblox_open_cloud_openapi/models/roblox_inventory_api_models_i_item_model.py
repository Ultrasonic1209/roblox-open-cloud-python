from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.roblox_inventory_api_models_i_item_model_type import RobloxInventoryApiModelsIItemModelType
from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxInventoryApiModelsIItemModel")


@_attrs_define
class RobloxInventoryApiModelsIItemModel:
    """Model representing an inventory item

    Attributes:
        id (int | Unset): The ID of the item
        name (str | Unset): The name of the item
        type_ (RobloxInventoryApiModelsIItemModelType | Unset): The type of the item ['Asset' = 0, 'GamePass' = 1,
            'Badge' = 2, 'Bundle' = 3, 'Avatar' = 4]
        instance_id (int | Unset): The instance id of the item if applicable
    """

    id: int | Unset = UNSET
    name: str | Unset = UNSET
    type_: RobloxInventoryApiModelsIItemModelType | Unset = UNSET
    instance_id: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        type_: int | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        instance_id = self.instance_id

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if type_ is not UNSET:
            field_dict["type"] = type_
        if instance_id is not UNSET:
            field_dict["instanceId"] = instance_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: RobloxInventoryApiModelsIItemModelType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = RobloxInventoryApiModelsIItemModelType(_type_)

        instance_id = d.pop("instanceId", UNSET)

        roblox_inventory_api_models_i_item_model = cls(
            id=id,
            name=name,
            type_=type_,
            instance_id=instance_id,
        )

        return roblox_inventory_api_models_i_item_model
