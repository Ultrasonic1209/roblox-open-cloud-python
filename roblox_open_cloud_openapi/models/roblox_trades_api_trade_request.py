from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_trades_api_trade_offer_request import RobloxTradesApiTradeOfferRequest


T = TypeVar("T", bound="RobloxTradesApiTradeRequest")


@_attrs_define
class RobloxTradesApiTradeRequest:
    """
    Attributes:
        offers (list[RobloxTradesApiTradeOfferRequest] | Unset):
    """

    offers: list[RobloxTradesApiTradeOfferRequest] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        offers: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.offers, Unset):
            offers = []
            for offers_item_data in self.offers:
                offers_item = offers_item_data.to_dict()
                offers.append(offers_item)

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if offers is not UNSET:
            field_dict["offers"] = offers

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_trades_api_trade_offer_request import RobloxTradesApiTradeOfferRequest

        d = dict(src_dict)
        _offers = d.pop("offers", UNSET)
        offers: list[RobloxTradesApiTradeOfferRequest] | Unset = UNSET
        if _offers is not UNSET:
            offers = []
            for offers_item_data in _offers:
                offers_item = RobloxTradesApiTradeOfferRequest.from_dict(offers_item_data)

                offers.append(offers_item)

        roblox_trades_api_trade_request = cls(
            offers=offers,
        )

        return roblox_trades_api_trade_request
