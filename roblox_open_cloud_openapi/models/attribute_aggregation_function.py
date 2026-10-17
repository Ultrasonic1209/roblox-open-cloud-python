from enum import StrEnum


class AttributeAggregationFunction(StrEnum):
    AVERAGE = "Average"
    INVALID = "Invalid"
    MEDIAN = "Median"
    SUM = "Sum"

    def __str__(self) -> str:
        return str(self.value)
