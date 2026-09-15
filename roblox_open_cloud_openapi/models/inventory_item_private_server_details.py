from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="InventoryItemPrivateServerDetails")


@_attrs_define
class InventoryItemPrivateServerDetails:
    """Specific fields that are applicable to a private server.

    Attributes:
        private_server_id (str | Unset): A unique ID that identifies a private server.
    """

    private_server_id: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        private_server_id = self.private_server_id

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if private_server_id is not UNSET:
            field_dict["privateServerId"] = private_server_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        private_server_id = d.pop("privateServerId", UNSET)

        inventory_item_private_server_details = cls(
            private_server_id=private_server_id,
        )

        return inventory_item_private_server_details
