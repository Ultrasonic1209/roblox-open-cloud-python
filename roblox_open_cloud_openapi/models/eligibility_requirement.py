from enum import StrEnum


class EligibilityRequirement(StrEnum):
    ACCOUNTCOUNTRY = "AccountCountry"
    AGE = "Age"
    EMAILVERIFIED = "EmailVerified"
    IDVERIFIED = "IdVerified"
    INVALID = "Invalid"
    MODERATIONSTATUS = "ModerationStatus"
    PREMIUM = "Premium"
    USERAGREEMENT = "UserAgreement"

    def __str__(self) -> str:
        return str(self.value)
