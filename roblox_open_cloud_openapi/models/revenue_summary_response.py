from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RevenueSummaryResponse")


@_attrs_define
class RevenueSummaryResponse:
    """
    Attributes:
        recurring_robux_stipend (int | Unset):
        item_sale_robux (int | Unset):
        purchased_robux (int | Unset):
        trade_system_robux (int | Unset):
        pending_robux (int | Unset):
        group_payout_robux (int | Unset):
        individual_to_group_robux (int | Unset):
        premium_payouts (int | Unset):
        group_premium_payouts (int | Unset):
        adjustment_robux (int | Unset):
        immersive_ad_payouts (int | Unset):
        subscription_payouts (int | Unset):
        subscription_clawbacks (int | Unset):
        is_show_immersive_ad_payout_summary_on_zero_enabled (bool | Unset):
        commission_robux (int | Unset):
        publishing_advance_rebates (int | Unset):
        group_affiliate_payout_robux (int | Unset):
    """

    recurring_robux_stipend: int | Unset = UNSET
    item_sale_robux: int | Unset = UNSET
    purchased_robux: int | Unset = UNSET
    trade_system_robux: int | Unset = UNSET
    pending_robux: int | Unset = UNSET
    group_payout_robux: int | Unset = UNSET
    individual_to_group_robux: int | Unset = UNSET
    premium_payouts: int | Unset = UNSET
    group_premium_payouts: int | Unset = UNSET
    adjustment_robux: int | Unset = UNSET
    immersive_ad_payouts: int | Unset = UNSET
    subscription_payouts: int | Unset = UNSET
    subscription_clawbacks: int | Unset = UNSET
    is_show_immersive_ad_payout_summary_on_zero_enabled: bool | Unset = UNSET
    commission_robux: int | Unset = UNSET
    publishing_advance_rebates: int | Unset = UNSET
    group_affiliate_payout_robux: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        recurring_robux_stipend = self.recurring_robux_stipend

        item_sale_robux = self.item_sale_robux

        purchased_robux = self.purchased_robux

        trade_system_robux = self.trade_system_robux

        pending_robux = self.pending_robux

        group_payout_robux = self.group_payout_robux

        individual_to_group_robux = self.individual_to_group_robux

        premium_payouts = self.premium_payouts

        group_premium_payouts = self.group_premium_payouts

        adjustment_robux = self.adjustment_robux

        immersive_ad_payouts = self.immersive_ad_payouts

        subscription_payouts = self.subscription_payouts

        subscription_clawbacks = self.subscription_clawbacks

        is_show_immersive_ad_payout_summary_on_zero_enabled = self.is_show_immersive_ad_payout_summary_on_zero_enabled

        commission_robux = self.commission_robux

        publishing_advance_rebates = self.publishing_advance_rebates

        group_affiliate_payout_robux = self.group_affiliate_payout_robux

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if recurring_robux_stipend is not UNSET:
            field_dict["recurringRobuxStipend"] = recurring_robux_stipend
        if item_sale_robux is not UNSET:
            field_dict["itemSaleRobux"] = item_sale_robux
        if purchased_robux is not UNSET:
            field_dict["purchasedRobux"] = purchased_robux
        if trade_system_robux is not UNSET:
            field_dict["tradeSystemRobux"] = trade_system_robux
        if pending_robux is not UNSET:
            field_dict["pendingRobux"] = pending_robux
        if group_payout_robux is not UNSET:
            field_dict["groupPayoutRobux"] = group_payout_robux
        if individual_to_group_robux is not UNSET:
            field_dict["individualToGroupRobux"] = individual_to_group_robux
        if premium_payouts is not UNSET:
            field_dict["premiumPayouts"] = premium_payouts
        if group_premium_payouts is not UNSET:
            field_dict["groupPremiumPayouts"] = group_premium_payouts
        if adjustment_robux is not UNSET:
            field_dict["adjustmentRobux"] = adjustment_robux
        if immersive_ad_payouts is not UNSET:
            field_dict["immersiveAdPayouts"] = immersive_ad_payouts
        if subscription_payouts is not UNSET:
            field_dict["subscriptionPayouts"] = subscription_payouts
        if subscription_clawbacks is not UNSET:
            field_dict["subscriptionClawbacks"] = subscription_clawbacks
        if is_show_immersive_ad_payout_summary_on_zero_enabled is not UNSET:
            field_dict["isShowImmersiveAdPayoutSummaryOnZeroEnabled"] = (
                is_show_immersive_ad_payout_summary_on_zero_enabled
            )
        if commission_robux is not UNSET:
            field_dict["commissionRobux"] = commission_robux
        if publishing_advance_rebates is not UNSET:
            field_dict["publishingAdvanceRebates"] = publishing_advance_rebates
        if group_affiliate_payout_robux is not UNSET:
            field_dict["groupAffiliatePayoutRobux"] = group_affiliate_payout_robux

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        recurring_robux_stipend = d.pop("recurringRobuxStipend", UNSET)

        item_sale_robux = d.pop("itemSaleRobux", UNSET)

        purchased_robux = d.pop("purchasedRobux", UNSET)

        trade_system_robux = d.pop("tradeSystemRobux", UNSET)

        pending_robux = d.pop("pendingRobux", UNSET)

        group_payout_robux = d.pop("groupPayoutRobux", UNSET)

        individual_to_group_robux = d.pop("individualToGroupRobux", UNSET)

        premium_payouts = d.pop("premiumPayouts", UNSET)

        group_premium_payouts = d.pop("groupPremiumPayouts", UNSET)

        adjustment_robux = d.pop("adjustmentRobux", UNSET)

        immersive_ad_payouts = d.pop("immersiveAdPayouts", UNSET)

        subscription_payouts = d.pop("subscriptionPayouts", UNSET)

        subscription_clawbacks = d.pop("subscriptionClawbacks", UNSET)

        is_show_immersive_ad_payout_summary_on_zero_enabled = d.pop(
            "isShowImmersiveAdPayoutSummaryOnZeroEnabled", UNSET
        )

        commission_robux = d.pop("commissionRobux", UNSET)

        publishing_advance_rebates = d.pop("publishingAdvanceRebates", UNSET)

        group_affiliate_payout_robux = d.pop("groupAffiliatePayoutRobux", UNSET)

        revenue_summary_response = cls(
            recurring_robux_stipend=recurring_robux_stipend,
            item_sale_robux=item_sale_robux,
            purchased_robux=purchased_robux,
            trade_system_robux=trade_system_robux,
            pending_robux=pending_robux,
            group_payout_robux=group_payout_robux,
            individual_to_group_robux=individual_to_group_robux,
            premium_payouts=premium_payouts,
            group_premium_payouts=group_premium_payouts,
            adjustment_robux=adjustment_robux,
            immersive_ad_payouts=immersive_ad_payouts,
            subscription_payouts=subscription_payouts,
            subscription_clawbacks=subscription_clawbacks,
            is_show_immersive_ad_payout_summary_on_zero_enabled=is_show_immersive_ad_payout_summary_on_zero_enabled,
            commission_robux=commission_robux,
            publishing_advance_rebates=publishing_advance_rebates,
            group_affiliate_payout_robux=group_affiliate_payout_robux,
        )

        return revenue_summary_response
