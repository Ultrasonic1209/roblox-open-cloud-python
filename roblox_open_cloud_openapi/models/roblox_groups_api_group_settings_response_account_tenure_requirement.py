from enum import StrEnum


class RobloxGroupsApiGroupSettingsResponseAccountTenureRequirement(StrEnum):
    NONE = "None"
    ONEDAY = "OneDay"
    ONEMONTH = "OneMonth"
    ONEWEEK = "OneWeek"
    THREEDAYS = "ThreeDays"
    THREEMONTHS = "ThreeMonths"

    def __str__(self) -> str:
        return str(self.value)
