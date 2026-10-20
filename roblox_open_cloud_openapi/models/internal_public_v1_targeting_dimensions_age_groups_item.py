from enum import StrEnum


class InternalPublicV1TargetingDimensionsAgeGroupsItem(StrEnum):
    AGE_13_17 = "AGE_13_17"
    AGE_18_24 = "AGE_18_24"
    AGE_25_PLUS = "AGE_25_PLUS"

    def __str__(self) -> str:
        return str(self.value)
