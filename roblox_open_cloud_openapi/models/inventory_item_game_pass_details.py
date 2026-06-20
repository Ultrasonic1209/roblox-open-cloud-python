from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="InventoryItemGamePassDetails")


@_attrs_define
class InventoryItemGamePassDetails:
    """Specific fields that are applicable to a game pass.

    Attributes:
        game_pass_id (str | Unset): A unique ID that identifies a game pass. Example: 83167572.
    """

    game_pass_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        game_pass_id = self.game_pass_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if game_pass_id is not UNSET:
            field_dict["gamePassId"] = game_pass_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        game_pass_id = d.pop("gamePassId", UNSET)

        inventory_item_game_pass_details = cls(
            game_pass_id=game_pass_id,
        )

        inventory_item_game_pass_details.additional_properties = d
        return inventory_item_game_pass_details

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
