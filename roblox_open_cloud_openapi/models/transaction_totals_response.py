from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="TransactionTotalsResponse")


@_attrs_define
class TransactionTotalsResponse:
    """
    Attributes:
        sales_total (int | Unset):
        purchases_total (int | Unset):
        affiliate_sales_total (int | Unset):
        group_payouts_total (int | Unset):
        currency_purchases_total (int | Unset):
        premium_stipends_total (int | Unset):
        trade_system_earnings_total (int | Unset):
        trade_system_costs_total (int | Unset):
        premium_payouts_total (int | Unset):
        group_premium_payouts_total (int | Unset):
        ad_spend_total (int | Unset):
        developer_exchange_total (int | Unset):
        pending_robux_total (int | Unset):
        incoming_robux_total (int | Unset):
        outgoing_robux_total (int | Unset):
        individual_to_group_total (int | Unset):
        cs_adjustment_total (int | Unset):
        ads_revshare_payouts_total (int | Unset):
        group_ads_revshare_payouts_total (int | Unset):
        subscriptions_revshare_total (int | Unset):
        group_subscriptions_revshare_total (int | Unset):
        subscriptions_revshare_outgoing_total (int | Unset):
        group_subscriptions_revshare_outgoing_total (int | Unset):
        publishing_advance_rebates_total (int | Unset):
        affiliate_payout_total (int | Unset):
        licensing_payment_total (int | Unset):
        licensing_payment_clawback_outgoing_total (int | Unset):
        incoming_robux_transfer_total (int | Unset):
        outgoing_robux_transfer_total (int | Unset):
        roblox_select_incoming_total (int | Unset):
        roblox_select_outgoing_total (int | Unset):
    """

    sales_total: int | Unset = UNSET
    purchases_total: int | Unset = UNSET
    affiliate_sales_total: int | Unset = UNSET
    group_payouts_total: int | Unset = UNSET
    currency_purchases_total: int | Unset = UNSET
    premium_stipends_total: int | Unset = UNSET
    trade_system_earnings_total: int | Unset = UNSET
    trade_system_costs_total: int | Unset = UNSET
    premium_payouts_total: int | Unset = UNSET
    group_premium_payouts_total: int | Unset = UNSET
    ad_spend_total: int | Unset = UNSET
    developer_exchange_total: int | Unset = UNSET
    pending_robux_total: int | Unset = UNSET
    incoming_robux_total: int | Unset = UNSET
    outgoing_robux_total: int | Unset = UNSET
    individual_to_group_total: int | Unset = UNSET
    cs_adjustment_total: int | Unset = UNSET
    ads_revshare_payouts_total: int | Unset = UNSET
    group_ads_revshare_payouts_total: int | Unset = UNSET
    subscriptions_revshare_total: int | Unset = UNSET
    group_subscriptions_revshare_total: int | Unset = UNSET
    subscriptions_revshare_outgoing_total: int | Unset = UNSET
    group_subscriptions_revshare_outgoing_total: int | Unset = UNSET
    publishing_advance_rebates_total: int | Unset = UNSET
    affiliate_payout_total: int | Unset = UNSET
    licensing_payment_total: int | Unset = UNSET
    licensing_payment_clawback_outgoing_total: int | Unset = UNSET
    incoming_robux_transfer_total: int | Unset = UNSET
    outgoing_robux_transfer_total: int | Unset = UNSET
    roblox_select_incoming_total: int | Unset = UNSET
    roblox_select_outgoing_total: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        sales_total = self.sales_total

        purchases_total = self.purchases_total

        affiliate_sales_total = self.affiliate_sales_total

        group_payouts_total = self.group_payouts_total

        currency_purchases_total = self.currency_purchases_total

        premium_stipends_total = self.premium_stipends_total

        trade_system_earnings_total = self.trade_system_earnings_total

        trade_system_costs_total = self.trade_system_costs_total

        premium_payouts_total = self.premium_payouts_total

        group_premium_payouts_total = self.group_premium_payouts_total

        ad_spend_total = self.ad_spend_total

        developer_exchange_total = self.developer_exchange_total

        pending_robux_total = self.pending_robux_total

        incoming_robux_total = self.incoming_robux_total

        outgoing_robux_total = self.outgoing_robux_total

        individual_to_group_total = self.individual_to_group_total

        cs_adjustment_total = self.cs_adjustment_total

        ads_revshare_payouts_total = self.ads_revshare_payouts_total

        group_ads_revshare_payouts_total = self.group_ads_revshare_payouts_total

        subscriptions_revshare_total = self.subscriptions_revshare_total

        group_subscriptions_revshare_total = self.group_subscriptions_revshare_total

        subscriptions_revshare_outgoing_total = self.subscriptions_revshare_outgoing_total

        group_subscriptions_revshare_outgoing_total = self.group_subscriptions_revshare_outgoing_total

        publishing_advance_rebates_total = self.publishing_advance_rebates_total

        affiliate_payout_total = self.affiliate_payout_total

        licensing_payment_total = self.licensing_payment_total

        licensing_payment_clawback_outgoing_total = self.licensing_payment_clawback_outgoing_total

        incoming_robux_transfer_total = self.incoming_robux_transfer_total

        outgoing_robux_transfer_total = self.outgoing_robux_transfer_total

        roblox_select_incoming_total = self.roblox_select_incoming_total

        roblox_select_outgoing_total = self.roblox_select_outgoing_total

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if sales_total is not UNSET:
            field_dict["salesTotal"] = sales_total
        if purchases_total is not UNSET:
            field_dict["purchasesTotal"] = purchases_total
        if affiliate_sales_total is not UNSET:
            field_dict["affiliateSalesTotal"] = affiliate_sales_total
        if group_payouts_total is not UNSET:
            field_dict["groupPayoutsTotal"] = group_payouts_total
        if currency_purchases_total is not UNSET:
            field_dict["currencyPurchasesTotal"] = currency_purchases_total
        if premium_stipends_total is not UNSET:
            field_dict["premiumStipendsTotal"] = premium_stipends_total
        if trade_system_earnings_total is not UNSET:
            field_dict["tradeSystemEarningsTotal"] = trade_system_earnings_total
        if trade_system_costs_total is not UNSET:
            field_dict["tradeSystemCostsTotal"] = trade_system_costs_total
        if premium_payouts_total is not UNSET:
            field_dict["premiumPayoutsTotal"] = premium_payouts_total
        if group_premium_payouts_total is not UNSET:
            field_dict["groupPremiumPayoutsTotal"] = group_premium_payouts_total
        if ad_spend_total is not UNSET:
            field_dict["adSpendTotal"] = ad_spend_total
        if developer_exchange_total is not UNSET:
            field_dict["developerExchangeTotal"] = developer_exchange_total
        if pending_robux_total is not UNSET:
            field_dict["pendingRobuxTotal"] = pending_robux_total
        if incoming_robux_total is not UNSET:
            field_dict["incomingRobuxTotal"] = incoming_robux_total
        if outgoing_robux_total is not UNSET:
            field_dict["outgoingRobuxTotal"] = outgoing_robux_total
        if individual_to_group_total is not UNSET:
            field_dict["individualToGroupTotal"] = individual_to_group_total
        if cs_adjustment_total is not UNSET:
            field_dict["csAdjustmentTotal"] = cs_adjustment_total
        if ads_revshare_payouts_total is not UNSET:
            field_dict["adsRevsharePayoutsTotal"] = ads_revshare_payouts_total
        if group_ads_revshare_payouts_total is not UNSET:
            field_dict["groupAdsRevsharePayoutsTotal"] = group_ads_revshare_payouts_total
        if subscriptions_revshare_total is not UNSET:
            field_dict["subscriptionsRevshareTotal"] = subscriptions_revshare_total
        if group_subscriptions_revshare_total is not UNSET:
            field_dict["groupSubscriptionsRevshareTotal"] = group_subscriptions_revshare_total
        if subscriptions_revshare_outgoing_total is not UNSET:
            field_dict["subscriptionsRevshareOutgoingTotal"] = subscriptions_revshare_outgoing_total
        if group_subscriptions_revshare_outgoing_total is not UNSET:
            field_dict["groupSubscriptionsRevshareOutgoingTotal"] = group_subscriptions_revshare_outgoing_total
        if publishing_advance_rebates_total is not UNSET:
            field_dict["publishingAdvanceRebatesTotal"] = publishing_advance_rebates_total
        if affiliate_payout_total is not UNSET:
            field_dict["affiliatePayoutTotal"] = affiliate_payout_total
        if licensing_payment_total is not UNSET:
            field_dict["licensingPaymentTotal"] = licensing_payment_total
        if licensing_payment_clawback_outgoing_total is not UNSET:
            field_dict["licensingPaymentClawbackOutgoingTotal"] = licensing_payment_clawback_outgoing_total
        if incoming_robux_transfer_total is not UNSET:
            field_dict["incomingRobuxTransferTotal"] = incoming_robux_transfer_total
        if outgoing_robux_transfer_total is not UNSET:
            field_dict["outgoingRobuxTransferTotal"] = outgoing_robux_transfer_total
        if roblox_select_incoming_total is not UNSET:
            field_dict["robloxSelectIncomingTotal"] = roblox_select_incoming_total
        if roblox_select_outgoing_total is not UNSET:
            field_dict["robloxSelectOutgoingTotal"] = roblox_select_outgoing_total

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        sales_total = d.pop("salesTotal", UNSET)

        purchases_total = d.pop("purchasesTotal", UNSET)

        affiliate_sales_total = d.pop("affiliateSalesTotal", UNSET)

        group_payouts_total = d.pop("groupPayoutsTotal", UNSET)

        currency_purchases_total = d.pop("currencyPurchasesTotal", UNSET)

        premium_stipends_total = d.pop("premiumStipendsTotal", UNSET)

        trade_system_earnings_total = d.pop("tradeSystemEarningsTotal", UNSET)

        trade_system_costs_total = d.pop("tradeSystemCostsTotal", UNSET)

        premium_payouts_total = d.pop("premiumPayoutsTotal", UNSET)

        group_premium_payouts_total = d.pop("groupPremiumPayoutsTotal", UNSET)

        ad_spend_total = d.pop("adSpendTotal", UNSET)

        developer_exchange_total = d.pop("developerExchangeTotal", UNSET)

        pending_robux_total = d.pop("pendingRobuxTotal", UNSET)

        incoming_robux_total = d.pop("incomingRobuxTotal", UNSET)

        outgoing_robux_total = d.pop("outgoingRobuxTotal", UNSET)

        individual_to_group_total = d.pop("individualToGroupTotal", UNSET)

        cs_adjustment_total = d.pop("csAdjustmentTotal", UNSET)

        ads_revshare_payouts_total = d.pop("adsRevsharePayoutsTotal", UNSET)

        group_ads_revshare_payouts_total = d.pop("groupAdsRevsharePayoutsTotal", UNSET)

        subscriptions_revshare_total = d.pop("subscriptionsRevshareTotal", UNSET)

        group_subscriptions_revshare_total = d.pop("groupSubscriptionsRevshareTotal", UNSET)

        subscriptions_revshare_outgoing_total = d.pop("subscriptionsRevshareOutgoingTotal", UNSET)

        group_subscriptions_revshare_outgoing_total = d.pop("groupSubscriptionsRevshareOutgoingTotal", UNSET)

        publishing_advance_rebates_total = d.pop("publishingAdvanceRebatesTotal", UNSET)

        affiliate_payout_total = d.pop("affiliatePayoutTotal", UNSET)

        licensing_payment_total = d.pop("licensingPaymentTotal", UNSET)

        licensing_payment_clawback_outgoing_total = d.pop("licensingPaymentClawbackOutgoingTotal", UNSET)

        incoming_robux_transfer_total = d.pop("incomingRobuxTransferTotal", UNSET)

        outgoing_robux_transfer_total = d.pop("outgoingRobuxTransferTotal", UNSET)

        roblox_select_incoming_total = d.pop("robloxSelectIncomingTotal", UNSET)

        roblox_select_outgoing_total = d.pop("robloxSelectOutgoingTotal", UNSET)

        transaction_totals_response = cls(
            sales_total=sales_total,
            purchases_total=purchases_total,
            affiliate_sales_total=affiliate_sales_total,
            group_payouts_total=group_payouts_total,
            currency_purchases_total=currency_purchases_total,
            premium_stipends_total=premium_stipends_total,
            trade_system_earnings_total=trade_system_earnings_total,
            trade_system_costs_total=trade_system_costs_total,
            premium_payouts_total=premium_payouts_total,
            group_premium_payouts_total=group_premium_payouts_total,
            ad_spend_total=ad_spend_total,
            developer_exchange_total=developer_exchange_total,
            pending_robux_total=pending_robux_total,
            incoming_robux_total=incoming_robux_total,
            outgoing_robux_total=outgoing_robux_total,
            individual_to_group_total=individual_to_group_total,
            cs_adjustment_total=cs_adjustment_total,
            ads_revshare_payouts_total=ads_revshare_payouts_total,
            group_ads_revshare_payouts_total=group_ads_revshare_payouts_total,
            subscriptions_revshare_total=subscriptions_revshare_total,
            group_subscriptions_revshare_total=group_subscriptions_revshare_total,
            subscriptions_revshare_outgoing_total=subscriptions_revshare_outgoing_total,
            group_subscriptions_revshare_outgoing_total=group_subscriptions_revshare_outgoing_total,
            publishing_advance_rebates_total=publishing_advance_rebates_total,
            affiliate_payout_total=affiliate_payout_total,
            licensing_payment_total=licensing_payment_total,
            licensing_payment_clawback_outgoing_total=licensing_payment_clawback_outgoing_total,
            incoming_robux_transfer_total=incoming_robux_transfer_total,
            outgoing_robux_transfer_total=outgoing_robux_transfer_total,
            roblox_select_incoming_total=roblox_select_incoming_total,
            roblox_select_outgoing_total=roblox_select_outgoing_total,
        )

        return transaction_totals_response
