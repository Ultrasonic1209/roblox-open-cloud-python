from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="TransactionUsedTypesResponse")


@_attrs_define
class TransactionUsedTypesResponse:
    """
    Attributes:
        has_purchase (bool | Unset):
        has_sale (bool | Unset):
        has_affiliate_payout (bool | Unset):
        has_affiliate_sale (bool | Unset):
        has_group_payout (bool | Unset):
        has_currency_purchase (bool | Unset):
        has_trade_robux (bool | Unset):
        has_premium_stipend (bool | Unset):
        has_engagement_payout (bool | Unset):
        has_group_engagement_payout (bool | Unset):
        has_ad_spend (bool | Unset):
        has_dev_ex (bool | Unset):
        has_pending_robux (bool | Unset):
        has_individual_to_group (bool | Unset):
        has_cs_adjustment (bool | Unset):
        has_ads_revshare_payout (bool | Unset):
        has_group_ads_revshare_payout (bool | Unset):
        has_subscriptions_revshare_payout (bool | Unset):
        has_group_subscriptions_revshare_payout (bool | Unset):
        has_publishing_advance_rebates (bool | Unset):
        has_licensing_payment (bool | Unset):
        has_transfer (bool | Unset):
        has_roblox_select_transfer (bool | Unset):
        has_private_server_engagement_payout (bool | Unset):
    """

    has_purchase: bool | Unset = UNSET
    has_sale: bool | Unset = UNSET
    has_affiliate_payout: bool | Unset = UNSET
    has_affiliate_sale: bool | Unset = UNSET
    has_group_payout: bool | Unset = UNSET
    has_currency_purchase: bool | Unset = UNSET
    has_trade_robux: bool | Unset = UNSET
    has_premium_stipend: bool | Unset = UNSET
    has_engagement_payout: bool | Unset = UNSET
    has_group_engagement_payout: bool | Unset = UNSET
    has_ad_spend: bool | Unset = UNSET
    has_dev_ex: bool | Unset = UNSET
    has_pending_robux: bool | Unset = UNSET
    has_individual_to_group: bool | Unset = UNSET
    has_cs_adjustment: bool | Unset = UNSET
    has_ads_revshare_payout: bool | Unset = UNSET
    has_group_ads_revshare_payout: bool | Unset = UNSET
    has_subscriptions_revshare_payout: bool | Unset = UNSET
    has_group_subscriptions_revshare_payout: bool | Unset = UNSET
    has_publishing_advance_rebates: bool | Unset = UNSET
    has_licensing_payment: bool | Unset = UNSET
    has_transfer: bool | Unset = UNSET
    has_roblox_select_transfer: bool | Unset = UNSET
    has_private_server_engagement_payout: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        has_purchase = self.has_purchase

        has_sale = self.has_sale

        has_affiliate_payout = self.has_affiliate_payout

        has_affiliate_sale = self.has_affiliate_sale

        has_group_payout = self.has_group_payout

        has_currency_purchase = self.has_currency_purchase

        has_trade_robux = self.has_trade_robux

        has_premium_stipend = self.has_premium_stipend

        has_engagement_payout = self.has_engagement_payout

        has_group_engagement_payout = self.has_group_engagement_payout

        has_ad_spend = self.has_ad_spend

        has_dev_ex = self.has_dev_ex

        has_pending_robux = self.has_pending_robux

        has_individual_to_group = self.has_individual_to_group

        has_cs_adjustment = self.has_cs_adjustment

        has_ads_revshare_payout = self.has_ads_revshare_payout

        has_group_ads_revshare_payout = self.has_group_ads_revshare_payout

        has_subscriptions_revshare_payout = self.has_subscriptions_revshare_payout

        has_group_subscriptions_revshare_payout = self.has_group_subscriptions_revshare_payout

        has_publishing_advance_rebates = self.has_publishing_advance_rebates

        has_licensing_payment = self.has_licensing_payment

        has_transfer = self.has_transfer

        has_roblox_select_transfer = self.has_roblox_select_transfer

        has_private_server_engagement_payout = self.has_private_server_engagement_payout

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if has_purchase is not UNSET:
            field_dict["HasPurchase"] = has_purchase
        if has_sale is not UNSET:
            field_dict["HasSale"] = has_sale
        if has_affiliate_payout is not UNSET:
            field_dict["HasAffiliatePayout"] = has_affiliate_payout
        if has_affiliate_sale is not UNSET:
            field_dict["HasAffiliateSale"] = has_affiliate_sale
        if has_group_payout is not UNSET:
            field_dict["HasGroupPayout"] = has_group_payout
        if has_currency_purchase is not UNSET:
            field_dict["HasCurrencyPurchase"] = has_currency_purchase
        if has_trade_robux is not UNSET:
            field_dict["HasTradeRobux"] = has_trade_robux
        if has_premium_stipend is not UNSET:
            field_dict["HasPremiumStipend"] = has_premium_stipend
        if has_engagement_payout is not UNSET:
            field_dict["HasEngagementPayout"] = has_engagement_payout
        if has_group_engagement_payout is not UNSET:
            field_dict["HasGroupEngagementPayout"] = has_group_engagement_payout
        if has_ad_spend is not UNSET:
            field_dict["HasAdSpend"] = has_ad_spend
        if has_dev_ex is not UNSET:
            field_dict["HasDevEx"] = has_dev_ex
        if has_pending_robux is not UNSET:
            field_dict["HasPendingRobux"] = has_pending_robux
        if has_individual_to_group is not UNSET:
            field_dict["HasIndividualToGroup"] = has_individual_to_group
        if has_cs_adjustment is not UNSET:
            field_dict["HasCSAdjustment"] = has_cs_adjustment
        if has_ads_revshare_payout is not UNSET:
            field_dict["HasAdsRevsharePayout"] = has_ads_revshare_payout
        if has_group_ads_revshare_payout is not UNSET:
            field_dict["HasGroupAdsRevsharePayout"] = has_group_ads_revshare_payout
        if has_subscriptions_revshare_payout is not UNSET:
            field_dict["HasSubscriptionsRevsharePayout"] = has_subscriptions_revshare_payout
        if has_group_subscriptions_revshare_payout is not UNSET:
            field_dict["HasGroupSubscriptionsRevsharePayout"] = has_group_subscriptions_revshare_payout
        if has_publishing_advance_rebates is not UNSET:
            field_dict["HasPublishingAdvanceRebates"] = has_publishing_advance_rebates
        if has_licensing_payment is not UNSET:
            field_dict["HasLicensingPayment"] = has_licensing_payment
        if has_transfer is not UNSET:
            field_dict["HasTransfer"] = has_transfer
        if has_roblox_select_transfer is not UNSET:
            field_dict["HasRobloxSelectTransfer"] = has_roblox_select_transfer
        if has_private_server_engagement_payout is not UNSET:
            field_dict["HasPrivateServerEngagementPayout"] = has_private_server_engagement_payout

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        has_purchase = d.pop("HasPurchase", UNSET)

        has_sale = d.pop("HasSale", UNSET)

        has_affiliate_payout = d.pop("HasAffiliatePayout", UNSET)

        has_affiliate_sale = d.pop("HasAffiliateSale", UNSET)

        has_group_payout = d.pop("HasGroupPayout", UNSET)

        has_currency_purchase = d.pop("HasCurrencyPurchase", UNSET)

        has_trade_robux = d.pop("HasTradeRobux", UNSET)

        has_premium_stipend = d.pop("HasPremiumStipend", UNSET)

        has_engagement_payout = d.pop("HasEngagementPayout", UNSET)

        has_group_engagement_payout = d.pop("HasGroupEngagementPayout", UNSET)

        has_ad_spend = d.pop("HasAdSpend", UNSET)

        has_dev_ex = d.pop("HasDevEx", UNSET)

        has_pending_robux = d.pop("HasPendingRobux", UNSET)

        has_individual_to_group = d.pop("HasIndividualToGroup", UNSET)

        has_cs_adjustment = d.pop("HasCSAdjustment", UNSET)

        has_ads_revshare_payout = d.pop("HasAdsRevsharePayout", UNSET)

        has_group_ads_revshare_payout = d.pop("HasGroupAdsRevsharePayout", UNSET)

        has_subscriptions_revshare_payout = d.pop("HasSubscriptionsRevsharePayout", UNSET)

        has_group_subscriptions_revshare_payout = d.pop("HasGroupSubscriptionsRevsharePayout", UNSET)

        has_publishing_advance_rebates = d.pop("HasPublishingAdvanceRebates", UNSET)

        has_licensing_payment = d.pop("HasLicensingPayment", UNSET)

        has_transfer = d.pop("HasTransfer", UNSET)

        has_roblox_select_transfer = d.pop("HasRobloxSelectTransfer", UNSET)

        has_private_server_engagement_payout = d.pop("HasPrivateServerEngagementPayout", UNSET)

        transaction_used_types_response = cls(
            has_purchase=has_purchase,
            has_sale=has_sale,
            has_affiliate_payout=has_affiliate_payout,
            has_affiliate_sale=has_affiliate_sale,
            has_group_payout=has_group_payout,
            has_currency_purchase=has_currency_purchase,
            has_trade_robux=has_trade_robux,
            has_premium_stipend=has_premium_stipend,
            has_engagement_payout=has_engagement_payout,
            has_group_engagement_payout=has_group_engagement_payout,
            has_ad_spend=has_ad_spend,
            has_dev_ex=has_dev_ex,
            has_pending_robux=has_pending_robux,
            has_individual_to_group=has_individual_to_group,
            has_cs_adjustment=has_cs_adjustment,
            has_ads_revshare_payout=has_ads_revshare_payout,
            has_group_ads_revshare_payout=has_group_ads_revshare_payout,
            has_subscriptions_revshare_payout=has_subscriptions_revshare_payout,
            has_group_subscriptions_revshare_payout=has_group_subscriptions_revshare_payout,
            has_publishing_advance_rebates=has_publishing_advance_rebates,
            has_licensing_payment=has_licensing_payment,
            has_transfer=has_transfer,
            has_roblox_select_transfer=has_roblox_select_transfer,
            has_private_server_engagement_payout=has_private_server_engagement_payout,
        )

        return transaction_used_types_response
