from enum import StrEnum


class TargetingDimensionsRegionsItem(StrEnum):
    AFRICA = "AFRICA"
    ALL = "ALL"
    ANZ = "ANZ"
    EASTERN_EUROPE = "EASTERN_EUROPE"
    EAST_ASIA = "EAST_ASIA"
    LATIN_AMERICA = "LATIN_AMERICA"
    MIDDLE_EAST = "MIDDLE_EAST"
    ROW = "ROW"
    SOUTHEAST_ASIA = "SOUTHEAST_ASIA"
    UAC = "UAC"
    WESTERN_EUROPE = "WESTERN_EUROPE"

    def __str__(self) -> str:
        return str(self.value)
