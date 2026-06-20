from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..models.roblox_trades_api_models_v2_trade_details_response_status import (
    RobloxTradesApiModelsV2TradeDetailsResponseStatus,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_trades_api_models_v2_trade_offer import RobloxTradesApiModelsV2TradeOffer


T = TypeVar("T", bound="RobloxTradesApiModelsV2TradeDetailsResponse")


@_attrs_define
class RobloxTradesApiModelsV2TradeDetailsResponse:
    """The response for the TradeDetailsV2 endpoint.

    Attributes:
        trade_id (int | Unset): The ID of the trade.
        status (RobloxTradesApiModelsV2TradeDetailsResponseStatus | Unset): The status of the trade. ['Unknown' = 1,
            'Open' = 2, 'Pending' = 3, 'Completed' = 4, 'Expired' = 5, 'Declined' = 6, 'RejectedDueToError' = 7, 'Countered'
            = 8, 'Processing' = 9, 'InterventionRequired' = 10, 'TwoStepVerificationRequired' = 11]
        participant_a_offer (RobloxTradesApiModelsV2TradeOffer | Unset): Represents a trade offer.
        participant_b_offer (RobloxTradesApiModelsV2TradeOffer | Unset): Represents a trade offer.
    """

    trade_id: int | Unset = UNSET
    status: RobloxTradesApiModelsV2TradeDetailsResponseStatus | Unset = UNSET
    participant_a_offer: RobloxTradesApiModelsV2TradeOffer | Unset = UNSET
    participant_b_offer: RobloxTradesApiModelsV2TradeOffer | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        trade_id = self.trade_id

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        participant_a_offer: dict[str, Any] | Unset = UNSET
        if not isinstance(self.participant_a_offer, Unset):
            participant_a_offer = self.participant_a_offer.to_dict()

        participant_b_offer: dict[str, Any] | Unset = UNSET
        if not isinstance(self.participant_b_offer, Unset):
            participant_b_offer = self.participant_b_offer.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if trade_id is not UNSET:
            field_dict["tradeId"] = trade_id
        if status is not UNSET:
            field_dict["status"] = status
        if participant_a_offer is not UNSET:
            field_dict["participantAOffer"] = participant_a_offer
        if participant_b_offer is not UNSET:
            field_dict["participantBOffer"] = participant_b_offer

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_trades_api_models_v2_trade_offer import RobloxTradesApiModelsV2TradeOffer

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        trade_id = d.pop("tradeId", UNSET)

        _status = d.pop("status", UNSET)
        status: RobloxTradesApiModelsV2TradeDetailsResponseStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = RobloxTradesApiModelsV2TradeDetailsResponseStatus(_status)

        _participant_a_offer = d.pop("participantAOffer", UNSET)
        participant_a_offer: RobloxTradesApiModelsV2TradeOffer | Unset
        if isinstance(_participant_a_offer, Unset):
            participant_a_offer = UNSET
        else:
            participant_a_offer = RobloxTradesApiModelsV2TradeOffer.from_dict(_participant_a_offer)

        _participant_b_offer = d.pop("participantBOffer", UNSET)
        participant_b_offer: RobloxTradesApiModelsV2TradeOffer | Unset
        if isinstance(_participant_b_offer, Unset):
            participant_b_offer = UNSET
        else:
            participant_b_offer = RobloxTradesApiModelsV2TradeOffer.from_dict(_participant_b_offer)

        roblox_trades_api_models_v2_trade_details_response = cls(
            trade_id=trade_id,
            status=status,
            participant_a_offer=participant_a_offer,
            participant_b_offer=participant_b_offer,
        )

        return roblox_trades_api_models_v2_trade_details_response
