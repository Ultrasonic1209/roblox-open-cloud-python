from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.roblox_trades_api_models_v2_can_trade_response_trade_eligibility import (
    RobloxTradesApiModelsV2CanTradeResponseTradeEligibility,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxTradesApiModelsV2CanTradeResponse")


@_attrs_define
class RobloxTradesApiModelsV2CanTradeResponse:
    """The response for the CanTrade endpoint.

    Attributes:
        user_id (int | Unset): The ID of the user.
        can_trade (bool | Unset): Whether the user can trade or not.
        trade_eligibility (RobloxTradesApiModelsV2CanTradeResponseTradeEligibility | Unset): The trade eligibility
            status of the user. ['Unknown' = 0, 'Eligible' = 1, 'IneligibleTradeSystemDisabled' = 2,
            'IneligibleCannotTradeWithRoblox' = 3, 'IneligibleUserNotFound' = 4, 'IneligibleMissingPremiumMembership' = 5,
            'IneligibleLegalOrRegulatoryRestrictions' = 6]
    """

    user_id: int | Unset = UNSET
    can_trade: bool | Unset = UNSET
    trade_eligibility: RobloxTradesApiModelsV2CanTradeResponseTradeEligibility | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        user_id = self.user_id

        can_trade = self.can_trade

        trade_eligibility: str | Unset = UNSET
        if not isinstance(self.trade_eligibility, Unset):
            trade_eligibility = self.trade_eligibility.value

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if user_id is not UNSET:
            field_dict["userId"] = user_id
        if can_trade is not UNSET:
            field_dict["canTrade"] = can_trade
        if trade_eligibility is not UNSET:
            field_dict["tradeEligibility"] = trade_eligibility

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        user_id = d.pop("userId", UNSET)

        can_trade = d.pop("canTrade", UNSET)

        _trade_eligibility = d.pop("tradeEligibility", UNSET)
        trade_eligibility: RobloxTradesApiModelsV2CanTradeResponseTradeEligibility | Unset
        if isinstance(_trade_eligibility, Unset):
            trade_eligibility = UNSET
        else:
            trade_eligibility = RobloxTradesApiModelsV2CanTradeResponseTradeEligibility(_trade_eligibility)

        roblox_trades_api_models_v2_can_trade_response = cls(
            user_id=user_id,
            can_trade=can_trade,
            trade_eligibility=trade_eligibility,
        )

        return roblox_trades_api_models_v2_can_trade_response
