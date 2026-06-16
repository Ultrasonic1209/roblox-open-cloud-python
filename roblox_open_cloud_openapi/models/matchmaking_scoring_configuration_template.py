from enum import Enum


class MatchmakingScoringConfigurationTemplate(str, Enum):
    NOTAPPLICABLE = "NotApplicable"
    USEDEFAULT = "UseDefault"

    def __str__(self) -> str:
        return str(self.value)
