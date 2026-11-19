from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..models.roblox_economy_api_models_purchasable_detail_response_reason import (
    RobloxEconomyApiModelsPurchasableDetailResponseReason,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_economy_api_premium_pricing_model import RobloxEconomyApiPremiumPricingModel


T = TypeVar("T", bound="RobloxEconomyApiModelsPurchasableDetailResponse")


@_attrs_define
class RobloxEconomyApiModelsPurchasableDetailResponse:
    """Purchasable detail request model.

    Attributes:
        purchasable (bool | Unset): Defines if the product is purchasable.
        reason (RobloxEconomyApiModelsPurchasableDetailResponseReason | Unset): Defines the reason for failure.
        product_id (int | Unset): Reflects the requested product id for reference.
        status_code (int | Unset):
        title (str | Unset):
        error_msg (str | Unset):
        show_div_id (str | Unset):
        shortfall_price (int | Unset):
        balance_after_sale (int | Unset):
        expected_price (int | Unset):
        currency (int | Unset):
        price (int | Unset):
        asset_id (int | Unset):
        asset_name (str | Unset):
        asset_type (str | Unset):
        asset_type_display_name (str | Unset):
        asset_is_wearable (bool | Unset):
        seller_name (str | Unset):
        transaction_verb (str | Unset):
        is_multi_private_sale (bool | Unset):
        premium_pricing (RobloxEconomyApiPremiumPricingModel | Unset): Defines the Premium pricing for a product
    """

    purchasable: bool | Unset = UNSET
    reason: RobloxEconomyApiModelsPurchasableDetailResponseReason | Unset = UNSET
    product_id: int | Unset = UNSET
    status_code: int | Unset = UNSET
    title: str | Unset = UNSET
    error_msg: str | Unset = UNSET
    show_div_id: str | Unset = UNSET
    shortfall_price: int | Unset = UNSET
    balance_after_sale: int | Unset = UNSET
    expected_price: int | Unset = UNSET
    currency: int | Unset = UNSET
    price: int | Unset = UNSET
    asset_id: int | Unset = UNSET
    asset_name: str | Unset = UNSET
    asset_type: str | Unset = UNSET
    asset_type_display_name: str | Unset = UNSET
    asset_is_wearable: bool | Unset = UNSET
    seller_name: str | Unset = UNSET
    transaction_verb: str | Unset = UNSET
    is_multi_private_sale: bool | Unset = UNSET
    premium_pricing: RobloxEconomyApiPremiumPricingModel | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        purchasable = self.purchasable

        reason: int | Unset = UNSET
        if not isinstance(self.reason, Unset):
            reason = self.reason.value

        product_id = self.product_id

        status_code = self.status_code

        title = self.title

        error_msg = self.error_msg

        show_div_id = self.show_div_id

        shortfall_price = self.shortfall_price

        balance_after_sale = self.balance_after_sale

        expected_price = self.expected_price

        currency = self.currency

        price = self.price

        asset_id = self.asset_id

        asset_name = self.asset_name

        asset_type = self.asset_type

        asset_type_display_name = self.asset_type_display_name

        asset_is_wearable = self.asset_is_wearable

        seller_name = self.seller_name

        transaction_verb = self.transaction_verb

        is_multi_private_sale = self.is_multi_private_sale

        premium_pricing: dict[str, Any] | Unset = UNSET
        if not isinstance(self.premium_pricing, Unset):
            premium_pricing = self.premium_pricing.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if purchasable is not UNSET:
            field_dict["purchasable"] = purchasable
        if reason is not UNSET:
            field_dict["reason"] = reason
        if product_id is not UNSET:
            field_dict["productId"] = product_id
        if status_code is not UNSET:
            field_dict["statusCode"] = status_code
        if title is not UNSET:
            field_dict["title"] = title
        if error_msg is not UNSET:
            field_dict["errorMsg"] = error_msg
        if show_div_id is not UNSET:
            field_dict["showDivId"] = show_div_id
        if shortfall_price is not UNSET:
            field_dict["shortfallPrice"] = shortfall_price
        if balance_after_sale is not UNSET:
            field_dict["balanceAfterSale"] = balance_after_sale
        if expected_price is not UNSET:
            field_dict["expectedPrice"] = expected_price
        if currency is not UNSET:
            field_dict["currency"] = currency
        if price is not UNSET:
            field_dict["price"] = price
        if asset_id is not UNSET:
            field_dict["assetId"] = asset_id
        if asset_name is not UNSET:
            field_dict["assetName"] = asset_name
        if asset_type is not UNSET:
            field_dict["assetType"] = asset_type
        if asset_type_display_name is not UNSET:
            field_dict["assetTypeDisplayName"] = asset_type_display_name
        if asset_is_wearable is not UNSET:
            field_dict["assetIsWearable"] = asset_is_wearable
        if seller_name is not UNSET:
            field_dict["sellerName"] = seller_name
        if transaction_verb is not UNSET:
            field_dict["transactionVerb"] = transaction_verb
        if is_multi_private_sale is not UNSET:
            field_dict["isMultiPrivateSale"] = is_multi_private_sale
        if premium_pricing is not UNSET:
            field_dict["premiumPricing"] = premium_pricing

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_economy_api_premium_pricing_model import RobloxEconomyApiPremiumPricingModel  # noqa: PLC0415

        d = dict(src_dict)
        purchasable = d.pop("purchasable", UNSET)

        _reason = d.pop("reason", UNSET)
        reason: RobloxEconomyApiModelsPurchasableDetailResponseReason | Unset
        if isinstance(_reason, Unset):
            reason = UNSET
        else:
            reason = RobloxEconomyApiModelsPurchasableDetailResponseReason(_reason)

        product_id = d.pop("productId", UNSET)

        status_code = d.pop("statusCode", UNSET)

        title = d.pop("title", UNSET)

        error_msg = d.pop("errorMsg", UNSET)

        show_div_id = d.pop("showDivId", UNSET)

        shortfall_price = d.pop("shortfallPrice", UNSET)

        balance_after_sale = d.pop("balanceAfterSale", UNSET)

        expected_price = d.pop("expectedPrice", UNSET)

        currency = d.pop("currency", UNSET)

        price = d.pop("price", UNSET)

        asset_id = d.pop("assetId", UNSET)

        asset_name = d.pop("assetName", UNSET)

        asset_type = d.pop("assetType", UNSET)

        asset_type_display_name = d.pop("assetTypeDisplayName", UNSET)

        asset_is_wearable = d.pop("assetIsWearable", UNSET)

        seller_name = d.pop("sellerName", UNSET)

        transaction_verb = d.pop("transactionVerb", UNSET)

        is_multi_private_sale = d.pop("isMultiPrivateSale", UNSET)

        _premium_pricing = d.pop("premiumPricing", UNSET)
        premium_pricing: RobloxEconomyApiPremiumPricingModel | Unset
        if isinstance(_premium_pricing, Unset):
            premium_pricing = UNSET
        else:
            premium_pricing = RobloxEconomyApiPremiumPricingModel.from_dict(_premium_pricing)

        roblox_economy_api_models_purchasable_detail_response = cls(
            purchasable=purchasable,
            reason=reason,
            product_id=product_id,
            status_code=status_code,
            title=title,
            error_msg=error_msg,
            show_div_id=show_div_id,
            shortfall_price=shortfall_price,
            balance_after_sale=balance_after_sale,
            expected_price=expected_price,
            currency=currency,
            price=price,
            asset_id=asset_id,
            asset_name=asset_name,
            asset_type=asset_type,
            asset_type_display_name=asset_type_display_name,
            asset_is_wearable=asset_is_wearable,
            seller_name=seller_name,
            transaction_verb=transaction_verb,
            is_multi_private_sale=is_multi_private_sale,
            premium_pricing=premium_pricing,
        )

        return roblox_economy_api_models_purchasable_detail_response
