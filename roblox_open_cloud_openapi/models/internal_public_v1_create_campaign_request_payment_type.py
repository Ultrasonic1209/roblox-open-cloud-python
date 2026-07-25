from enum import Enum


class InternalPublicV1CreateCampaignRequestPaymentType(str, Enum):
    ADS_CREDIT = "ADS_CREDIT"
    CREDIT_CARD = "CREDIT_CARD"
    INVOICE = "INVOICE"

    def __str__(self) -> str:
        return str(self.value)
