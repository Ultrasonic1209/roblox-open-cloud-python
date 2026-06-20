from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_trades_api_models_v2_trade_offer_request import RobloxTradesApiModelsV2TradeOfferRequest


T = TypeVar("T", bound="RobloxTradesApiModelsV2TradeRequest")


@_attrs_define
class RobloxTradesApiModelsV2TradeRequest:
    """Represents a trade request. The calling user must be either participant A or B in the trade.

    Attributes:
        sender_offer (RobloxTradesApiModelsV2TradeOfferRequest | Unset): Represents a trade offer.
        recipient_offer (RobloxTradesApiModelsV2TradeOfferRequest | Unset): Represents a trade offer.
    """

    sender_offer: RobloxTradesApiModelsV2TradeOfferRequest | Unset = UNSET
    recipient_offer: RobloxTradesApiModelsV2TradeOfferRequest | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        sender_offer: dict[str, Any] | Unset = UNSET
        if not isinstance(self.sender_offer, Unset):
            sender_offer = self.sender_offer.to_dict()

        recipient_offer: dict[str, Any] | Unset = UNSET
        if not isinstance(self.recipient_offer, Unset):
            recipient_offer = self.recipient_offer.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if sender_offer is not UNSET:
            field_dict["senderOffer"] = sender_offer
        if recipient_offer is not UNSET:
            field_dict["recipientOffer"] = recipient_offer

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_trades_api_models_v2_trade_offer_request import RobloxTradesApiModelsV2TradeOfferRequest

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        _sender_offer = d.pop("senderOffer", UNSET)
        sender_offer: RobloxTradesApiModelsV2TradeOfferRequest | Unset
        if isinstance(_sender_offer, Unset):
            sender_offer = UNSET
        else:
            sender_offer = RobloxTradesApiModelsV2TradeOfferRequest.from_dict(_sender_offer)

        _recipient_offer = d.pop("recipientOffer", UNSET)
        recipient_offer: RobloxTradesApiModelsV2TradeOfferRequest | Unset
        if isinstance(_recipient_offer, Unset):
            recipient_offer = UNSET
        else:
            recipient_offer = RobloxTradesApiModelsV2TradeOfferRequest.from_dict(_recipient_offer)

        roblox_trades_api_models_v2_trade_request = cls(
            sender_offer=sender_offer,
            recipient_offer=recipient_offer,
        )

        return roblox_trades_api_models_v2_trade_request
