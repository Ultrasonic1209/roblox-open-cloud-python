from enum import Enum


class PrivateServerInviteResponseType(str, Enum):
    CANINVITE = "CanInvite"
    INVALID = "Invalid"
    UNABLETOADDANYUSER = "UnableToAddAnyUser"
    UNABLETOADDNONFRIENDS = "UnableToAddNonFriends"
    UNABLETOADDSPECIFICUSER = "UnableToAddSpecificUser"

    def __str__(self) -> str:
        return str(self.value)
