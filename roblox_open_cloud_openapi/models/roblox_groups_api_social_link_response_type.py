from enum import StrEnum


class RobloxGroupsApiSocialLinkResponseType(StrEnum):
    AMAZON = "Amazon"
    DISCORD = "Discord"
    FACEBOOK = "Facebook"
    GOOGLEPLUS = "GooglePlus"
    GUILDED = "Guilded"
    ROBLOXGROUP = "RobloxGroup"
    TWITCH = "Twitch"
    TWITTER = "Twitter"
    YOUTUBE = "YouTube"

    def __str__(self) -> str:
        return str(self.value)
