from enum import StrEnum


class RobloxOpencloudScopeconfigurationV2RiskLevel(StrEnum):
    RISK_LEVEL_HIGH = "RISK_LEVEL_HIGH"
    RISK_LEVEL_INVALID = "RISK_LEVEL_INVALID"
    RISK_LEVEL_LOW = "RISK_LEVEL_LOW"
    RISK_LEVEL_MODERATE = "RISK_LEVEL_MODERATE"

    def __str__(self) -> str:
        return str(self.value)
