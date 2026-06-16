from enum import IntEnum


class LinkType(IntEnum):
    INVALID = 0
    FACEBOOK = 1
    TWITTER = 2
    YOUTUBE = 3
    TWITCH = 4
    DISCORD = 5
    GITHUB = 6
    GUILDED = 7
    ROBLOX = 8
    DEVFORUM = 9
    TRY_IN_EXPERIENCE = 10

    def __str__(self) -> str:
        return str(self.value)
