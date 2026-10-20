from enum import StrEnum


class TaxIdType(StrEnum):
    CANADIANBUSINESSNUMBER = "CanadianBusinessNumber"
    CANADIANGSTHSTNUMBER = "CanadianGstHstNumber"
    EUROPEANVATNUMBER = "EuropeanVatNumber"
    INVALID = "Invalid"
    MEXICANRFCNUMBER = "MexicanRfcNumber"
    UNITEDKINGDOMVATNUMBER = "UnitedKingdomVatNumber"
    UNITEDSTATESEIN = "UnitedStatesEin"

    def __str__(self) -> str:
        return str(self.value)
