from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxInventoryApiModelsCanViewInventoryResponse")


@_attrs_define
class RobloxInventoryApiModelsCanViewInventoryResponse:
    """
    Attributes:
        can_view (bool | Unset): Boolean describing if the user's inventory can be viewed
    """

    can_view: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        can_view = self.can_view

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if can_view is not UNSET:
            field_dict["canView"] = can_view

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        can_view = d.pop("canView", UNSET)

        roblox_inventory_api_models_can_view_inventory_response = cls(
            can_view=can_view,
        )

        return roblox_inventory_api_models_can_view_inventory_response
