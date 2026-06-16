from enum import Enum


class TransactionType(str, Enum):
    ADIMPRESSIONPAYOUT = "AdImpressionPayout"
    ADSPEND = "AdSpend"
    ADSREVSHAREPAYOUT = "AdsRevsharePayout"
    AFFILIATEPAYOUT = "AffiliatePayout"
    AFFILIATESALE = "AffiliateSale"
    CSADJUSTMENT = "CSAdjustment"
    CURRENCYPURCHASE = "CurrencyPurchase"
    CURRENCYTRANSFER = "CurrencyTransfer"
    DEVEX = "DevEx"
    ENGAGEMENTPAYOUT = "EngagementPayout"
    GROUPADSREVSHAREPAYOUT = "GroupAdsRevsharePayout"
    GROUPENGAGEMENTPAYOUT = "GroupEngagementPayout"
    GROUPPAYOUT = "GroupPayout"
    GROUPSUBSCRIPTIONSREVSHARECLAWBACK = "GroupSubscriptionsRevshareClawback"
    GROUPSUBSCRIPTIONSREVSHAREPAYOUT = "GroupSubscriptionsRevsharePayout"
    INDIVIDUALTOGROUP = "IndividualToGroup"
    LICENSINGPAYMENT = "LicensingPayment"
    LICENSINGPAYMENTCLAWBACK = "LicensingPaymentClawback"
    PENDINGROBUX = "PendingRobux"
    PREMIUMSTIPEND = "PremiumStipend"
    PUBLISHINGADVANCEREBATES = "PublishingAdvanceRebates"
    PURCHASE = "Purchase"
    ROBLOXSELECTTRANSFER = "RobloxSelectTransfer"
    SALE = "Sale"
    SUBSCRIPTIONSREVSHARECLAWBACK = "SubscriptionsRevshareClawback"
    SUBSCRIPTIONSREVSHAREPAYOUT = "SubscriptionsRevsharePayout"
    SUMMARY = "Summary"
    TRADEROBUX = "TradeRobux"
    UNDEFINED = "Undefined"

    def __str__(self) -> str:
        return str(self.value)
