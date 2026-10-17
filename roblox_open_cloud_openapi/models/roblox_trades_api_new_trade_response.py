from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxTradesApiNewTradeResponse")


@_attrs_define
class RobloxTradesApiNewTradeResponse:
    """
    Attributes:
        id (int | Unset): The trade id.
    """

    id: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        roblox_trades_api_new_trade_response = cls(
            id=id,
        )

        return roblox_trades_api_new_trade_response
