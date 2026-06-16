from enum import Enum


class PricingFeature(str, Enum):
    INVALID = "Invalid"
    PRICEOPTIMIZATION = "PriceOptimization"
    REGIONALPRICING = "RegionalPricing"
    USERFIXEDPRICE = "UserFixedPrice"

    def __str__(self) -> str:
        return str(self.value)
