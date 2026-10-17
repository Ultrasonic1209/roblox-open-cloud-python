from enum import StrEnum


class GamePassesPricingFeature(StrEnum):
    INVALID = "Invalid"
    PRICEOPTIMIZATION = "PriceOptimization"
    REGIONALPRICING = "RegionalPricing"
    USERFIXEDPRICE = "UserFixedPrice"

    def __str__(self) -> str:
        return str(self.value)
