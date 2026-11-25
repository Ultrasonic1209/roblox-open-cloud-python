from enum import StrEnum


class RobloxGroupsApiModelsResponseUserModelBuildersClubMembershipType(StrEnum):
    BC = "BC"
    NONE = "None"
    OBC = "OBC"
    ROBLOXPREMIUM = "RobloxPremium"
    TBC = "TBC"

    def __str__(self) -> str:
        return str(self.value)
