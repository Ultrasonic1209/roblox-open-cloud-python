from enum import StrEnum


class SubjectType(StrEnum):
    ALL = "All"
    COMMUNICATIONPLATFORMMESSAGE = "CommunicationPlatformMessage"
    GROUP = "Group"
    GROUPROLESET = "GroupRoleset"
    INVALID = "Invalid"
    IPPLATFORM = "IpPlatform"
    UNIVERSE = "Universe"
    USER = "User"

    def __str__(self) -> str:
        return str(self.value)
