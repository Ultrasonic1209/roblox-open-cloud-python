from enum import StrEnum


class MatchmakingScoringConfigurationTemplate(StrEnum):
    NOTAPPLICABLE = "NotApplicable"
    USEDEFAULT = "UseDefault"

    def __str__(self) -> str:
        return str(self.value)
