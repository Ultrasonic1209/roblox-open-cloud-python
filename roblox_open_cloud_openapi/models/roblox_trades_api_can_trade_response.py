from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.roblox_trades_api_can_trade_response_status import RobloxTradesApiCanTradeResponseStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxTradesApiCanTradeResponse")


@_attrs_define
class RobloxTradesApiCanTradeResponse:
    """
    Attributes:
        can_trade (bool | Unset): Returns true if you can trade with the given user.
        status (RobloxTradesApiCanTradeResponseStatus | Unset): If you can't trade with a user, status explains why you
            can't trade with them. ['Unknown' = 0, 'CanTrade' = 1, 'CannotTradeWithSelf' = 2, 'SenderCannotTrade' = 3,
            'ReceiverCannotTrade' = 4, 'SenderPrivacyTooStrict' = 5, 'UsersCannotTrade' = 6, 'TradeAccepterNeedsFriction' =
            7]
    """

    can_trade: bool | Unset = UNSET
    status: RobloxTradesApiCanTradeResponseStatus | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        can_trade = self.can_trade

        status: int | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if can_trade is not UNSET:
            field_dict["canTrade"] = can_trade
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        can_trade = d.pop("canTrade", UNSET)

        _status = d.pop("status", UNSET)
        status: RobloxTradesApiCanTradeResponseStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = RobloxTradesApiCanTradeResponseStatus(_status)

        roblox_trades_api_can_trade_response = cls(
            can_trade=can_trade,
            status=status,
        )

        return roblox_trades_api_can_trade_response
