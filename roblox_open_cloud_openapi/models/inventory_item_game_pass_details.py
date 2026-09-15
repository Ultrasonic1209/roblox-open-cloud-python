from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="InventoryItemGamePassDetails")


@_attrs_define
class InventoryItemGamePassDetails:
    """Specific fields that are applicable to a game pass.

    Attributes:
        game_pass_id (str | Unset): A unique ID that identifies a game pass.
    """

    game_pass_id: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        game_pass_id = self.game_pass_id

        field_dict: dict[str, Any] = {}

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

        return inventory_item_game_pass_details
