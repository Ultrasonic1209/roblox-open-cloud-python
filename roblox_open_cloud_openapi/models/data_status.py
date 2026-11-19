from enum import StrEnum


class DataStatus(StrEnum):
    INSUFFICIENTSAMPLESIZE = "InsufficientSampleSize"
    NOTSTATISTICALLYSIGNIFICANT = "NotStatisticallySignificant"
    PROJECTED = "Projected"
    VALID = "Valid"

    def __str__(self) -> str:
        return str(self.value)
