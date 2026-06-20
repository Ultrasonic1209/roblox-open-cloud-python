from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_trades_api_models_v2_tradable_item_instance import RobloxTradesApiModelsV2TradableItemInstance
    from ..models.roblox_web_responses_users_skinny_user_response import RobloxWebResponsesUsersSkinnyUserResponse


T = TypeVar("T", bound="RobloxTradesApiModelsV2TradeOffer")


@_attrs_define
class RobloxTradesApiModelsV2TradeOffer:
    """Represents a trade offer.

    Attributes:
        user (RobloxWebResponsesUsersSkinnyUserResponse | Unset):
        robux (int | Unset): The amount of Robux in the trade offer.
        items (list[RobloxTradesApiModelsV2TradableItemInstance] | Unset): The items in the trade offer.
    """

    user: RobloxWebResponsesUsersSkinnyUserResponse | Unset = UNSET
    robux: int | Unset = UNSET
    items: list[RobloxTradesApiModelsV2TradableItemInstance] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        user: dict[str, Any] | Unset = UNSET
        if not isinstance(self.user, Unset):
            user = self.user.to_dict()

        robux = self.robux

        items: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.items, Unset):
            items = []
            for items_item_data in self.items:
                items_item = items_item_data.to_dict()
                items.append(items_item)

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if user is not UNSET:
            field_dict["user"] = user
        if robux is not UNSET:
            field_dict["robux"] = robux
        if items is not UNSET:
            field_dict["items"] = items

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_trades_api_models_v2_tradable_item_instance import (
            RobloxTradesApiModelsV2TradableItemInstance,
        )
        from ..models.roblox_web_responses_users_skinny_user_response import RobloxWebResponsesUsersSkinnyUserResponse

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        _user = d.pop("user", UNSET)
        user: RobloxWebResponsesUsersSkinnyUserResponse | Unset
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = RobloxWebResponsesUsersSkinnyUserResponse.from_dict(_user)

        robux = d.pop("robux", UNSET)

        _items = d.pop("items", UNSET)
        items: list[RobloxTradesApiModelsV2TradableItemInstance] | Unset = UNSET
        if _items is not UNSET:
            items = []
            for items_item_data in _items:
                items_item = RobloxTradesApiModelsV2TradableItemInstance.from_dict(items_item_data)

                items.append(items_item)

        roblox_trades_api_models_v2_trade_offer = cls(
            user=user,
            robux=robux,
            items=items,
        )

        return roblox_trades_api_models_v2_trade_offer
