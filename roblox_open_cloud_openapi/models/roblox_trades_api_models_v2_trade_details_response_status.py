from enum import StrEnum


class RobloxTradesApiModelsV2TradeDetailsResponseStatus(StrEnum):
    COMPLETED = "Completed"
    COUNTERED = "Countered"
    DECLINED = "Declined"
    EXPIRED = "Expired"
    INTERVENTIONREQUIRED = "InterventionRequired"
    OPEN = "Open"
    PENDING = "Pending"
    PROCESSING = "Processing"
    REJECTEDDUETOERROR = "RejectedDueToError"
    TWOSTEPVERIFICATIONREQUIRED = "TwoStepVerificationRequired"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
