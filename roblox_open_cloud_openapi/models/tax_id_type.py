from enum import Enum


class TaxIdType(str, Enum):
    CANADIANBUSINESSNUMBER = "CanadianBusinessNumber"
    CANADIANGSTHSTNUMBER = "CanadianGstHstNumber"
    EUROPEANVATNUMBER = "EuropeanVatNumber"
    INVALID = "Invalid"
    MEXICANRFCNUMBER = "MexicanRfcNumber"
    UNITEDKINGDOMVATNUMBER = "UnitedKingdomVatNumber"
    UNITEDSTATESEIN = "UnitedStatesEin"

    def __str__(self) -> str:
        return str(self.value)
