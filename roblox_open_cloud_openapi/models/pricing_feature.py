from enum import StrEnum


class PricingFeature(StrEnum):
    INVALID = "Invalid"
    PRICEOPTIMIZATION = "PriceOptimization"
    REGIONALPRICING = "RegionalPricing"
    USERFIXEDPRICE = "UserFixedPrice"

    def __str__(self) -> str:
        return str(self.value)
