from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_games_api_models_response_purchase_data import RobloxGamesApiModelsResponsePurchaseData


T = TypeVar("T", bound="RobloxGamesApiModelsResponseGameProductResponse")


@_attrs_define
class RobloxGamesApiModelsResponseGameProductResponse:
    """Response model for getting the game product information

    Attributes:
        universe_id (int | Unset): The game universe id
        is_for_sale (bool | Unset): The game purchasability
        product_id (int | Unset): The game product id
        price (int | Unset): The game price
        seller_id (int | Unset): The game seller id
            User ID for users, Agent ID for groups
        fiat_purchase_data (RobloxGamesApiModelsResponsePurchaseData | Unset):
    """

    universe_id: int | Unset = UNSET
    is_for_sale: bool | Unset = UNSET
    product_id: int | Unset = UNSET
    price: int | Unset = UNSET
    seller_id: int | Unset = UNSET
    fiat_purchase_data: RobloxGamesApiModelsResponsePurchaseData | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        universe_id = self.universe_id

        is_for_sale = self.is_for_sale

        product_id = self.product_id

        price = self.price

        seller_id = self.seller_id

        fiat_purchase_data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.fiat_purchase_data, Unset):
            fiat_purchase_data = self.fiat_purchase_data.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if universe_id is not UNSET:
            field_dict["universeId"] = universe_id
        if is_for_sale is not UNSET:
            field_dict["isForSale"] = is_for_sale
        if product_id is not UNSET:
            field_dict["productId"] = product_id
        if price is not UNSET:
            field_dict["price"] = price
        if seller_id is not UNSET:
            field_dict["sellerId"] = seller_id
        if fiat_purchase_data is not UNSET:
            field_dict["fiatPurchaseData"] = fiat_purchase_data

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_games_api_models_response_purchase_data import RobloxGamesApiModelsResponsePurchaseData

        d = dict(src_dict)
        universe_id = d.pop("universeId", UNSET)

        is_for_sale = d.pop("isForSale", UNSET)

        product_id = d.pop("productId", UNSET)

        price = d.pop("price", UNSET)

        seller_id = d.pop("sellerId", UNSET)

        _fiat_purchase_data = d.pop("fiatPurchaseData", UNSET)
        fiat_purchase_data: RobloxGamesApiModelsResponsePurchaseData | Unset
        if isinstance(_fiat_purchase_data, Unset):
            fiat_purchase_data = UNSET
        else:
            fiat_purchase_data = RobloxGamesApiModelsResponsePurchaseData.from_dict(_fiat_purchase_data)

        roblox_games_api_models_response_game_product_response = cls(
            universe_id=universe_id,
            is_for_sale=is_for_sale,
            product_id=product_id,
            price=price,
            seller_id=seller_id,
            fiat_purchase_data=fiat_purchase_data,
        )

        return roblox_games_api_models_response_game_product_response
