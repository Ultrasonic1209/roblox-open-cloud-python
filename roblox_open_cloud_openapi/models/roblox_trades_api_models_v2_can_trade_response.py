from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..models.roblox_trades_api_models_v2_can_trade_response_trade_eligibility import (
    RobloxTradesApiModelsV2CanTradeResponseTradeEligibility,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_trades_api_models_v2_currency_transfer_eligibility_response import (
        RobloxTradesApiModelsV2CurrencyTransferEligibilityResponse,
    )
    from ..models.roblox_trades_api_models_v2_free_trades_allowance_response import (
        RobloxTradesApiModelsV2FreeTradesAllowanceResponse,
    )


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
            'IneligibleLegalOrRegulatoryRestrictions' = 6, 'IneligibleFreeTradesLimitReached' = 7]
        free_trades_allowance (RobloxTradesApiModelsV2FreeTradesAllowanceResponse | Unset):
        currency_transfer_eligibility (RobloxTradesApiModelsV2CurrencyTransferEligibilityResponse | Unset):
    """

    user_id: int | Unset = UNSET
    can_trade: bool | Unset = UNSET
    trade_eligibility: RobloxTradesApiModelsV2CanTradeResponseTradeEligibility | Unset = UNSET
    free_trades_allowance: RobloxTradesApiModelsV2FreeTradesAllowanceResponse | Unset = UNSET
    currency_transfer_eligibility: RobloxTradesApiModelsV2CurrencyTransferEligibilityResponse | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        user_id = self.user_id

        can_trade = self.can_trade

        trade_eligibility: str | Unset = UNSET
        if not isinstance(self.trade_eligibility, Unset):
            trade_eligibility = self.trade_eligibility.value

        free_trades_allowance: dict[str, Any] | Unset = UNSET
        if not isinstance(self.free_trades_allowance, Unset):
            free_trades_allowance = self.free_trades_allowance.to_dict()

        currency_transfer_eligibility: dict[str, Any] | Unset = UNSET
        if not isinstance(self.currency_transfer_eligibility, Unset):
            currency_transfer_eligibility = self.currency_transfer_eligibility.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if user_id is not UNSET:
            field_dict["userId"] = user_id
        if can_trade is not UNSET:
            field_dict["canTrade"] = can_trade
        if trade_eligibility is not UNSET:
            field_dict["tradeEligibility"] = trade_eligibility
        if free_trades_allowance is not UNSET:
            field_dict["freeTradesAllowance"] = free_trades_allowance
        if currency_transfer_eligibility is not UNSET:
            field_dict["currencyTransferEligibility"] = currency_transfer_eligibility

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_trades_api_models_v2_currency_transfer_eligibility_response import (
            RobloxTradesApiModelsV2CurrencyTransferEligibilityResponse,
        )
        from ..models.roblox_trades_api_models_v2_free_trades_allowance_response import (
            RobloxTradesApiModelsV2FreeTradesAllowanceResponse,
        )

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        user_id = d.pop("userId", UNSET)

        can_trade = d.pop("canTrade", UNSET)

        _trade_eligibility = d.pop("tradeEligibility", UNSET)
        trade_eligibility: RobloxTradesApiModelsV2CanTradeResponseTradeEligibility | Unset
        if isinstance(_trade_eligibility, Unset):
            trade_eligibility = UNSET
        else:
            trade_eligibility = RobloxTradesApiModelsV2CanTradeResponseTradeEligibility(_trade_eligibility)

        _free_trades_allowance = d.pop("freeTradesAllowance", UNSET)
        free_trades_allowance: RobloxTradesApiModelsV2FreeTradesAllowanceResponse | Unset
        if isinstance(_free_trades_allowance, Unset):
            free_trades_allowance = UNSET
        else:
            free_trades_allowance = RobloxTradesApiModelsV2FreeTradesAllowanceResponse.from_dict(_free_trades_allowance)

        _currency_transfer_eligibility = d.pop("currencyTransferEligibility", UNSET)
        currency_transfer_eligibility: RobloxTradesApiModelsV2CurrencyTransferEligibilityResponse | Unset
        if isinstance(_currency_transfer_eligibility, Unset):
            currency_transfer_eligibility = UNSET
        else:
            currency_transfer_eligibility = RobloxTradesApiModelsV2CurrencyTransferEligibilityResponse.from_dict(
                _currency_transfer_eligibility
            )

        roblox_trades_api_models_v2_can_trade_response = cls(
            user_id=user_id,
            can_trade=can_trade,
            trade_eligibility=trade_eligibility,
            free_trades_allowance=free_trades_allowance,
            currency_transfer_eligibility=currency_transfer_eligibility,
        )

        return roblox_trades_api_models_v2_can_trade_response
