from enum import Enum


class AttributeAggregationFunction(str, Enum):
    AVERAGE = "Average"
    INVALID = "Invalid"
    MEDIAN = "Median"
    SUM = "Sum"

    def __str__(self) -> str:
        return str(self.value)
