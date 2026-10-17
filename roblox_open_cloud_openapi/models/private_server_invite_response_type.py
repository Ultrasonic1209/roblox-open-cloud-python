from enum import StrEnum


class PrivateServerInviteResponseType(StrEnum):
    CANINVITE = "CanInvite"
    INVALID = "Invalid"
    UNABLETOADDANYUSER = "UnableToAddAnyUser"
    UNABLETOADDNONFRIENDS = "UnableToAddNonFriends"
    UNABLETOADDSPECIFICUSER = "UnableToAddSpecificUser"

    def __str__(self) -> str:
        return str(self.value)
