from enum import StrEnum


class ObjectiveOptionAudienceTypesItem(StrEnum):
    ALL_PLAYERS = "ALL_PLAYERS"
    NEW_USERS = "NEW_USERS"
    REACTIVATION = "REACTIVATION"
    RETENTION = "RETENTION"

    def __str__(self) -> str:
        return str(self.value)
