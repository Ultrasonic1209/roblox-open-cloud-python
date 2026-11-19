from enum import StrEnum


class AdCreditConversionTierBreakdownTier(StrEnum):
    O18_ELIGIBLE_ROBUX = "O18_ELIGIBLE_ROBUX"
    STANDARD_ROBUX = "STANDARD_ROBUX"

    def __str__(self) -> str:
        return str(self.value)
