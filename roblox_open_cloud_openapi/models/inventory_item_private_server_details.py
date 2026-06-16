from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="InventoryItemPrivateServerDetails")


@_attrs_define
class InventoryItemPrivateServerDetails:
    """Specific fields that are applicable to a private server.

    Attributes:
        private_server_id (str | Unset): A unique ID that identifies a private server. Example: 175156.
    """

    private_server_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        private_server_id = self.private_server_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if private_server_id is not UNSET:
            field_dict["privateServerId"] = private_server_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        private_server_id = d.pop("privateServerId", UNSET)

        inventory_item_private_server_details = cls(
            private_server_id=private_server_id,
        )

        inventory_item_private_server_details.additional_properties = d
        return inventory_item_private_server_details

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
