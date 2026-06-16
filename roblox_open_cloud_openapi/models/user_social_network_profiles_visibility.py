from enum import Enum


class UserSocialNetworkProfilesVisibility(str, Enum):
    EVERYONE = "EVERYONE"
    FRIENDS = "FRIENDS"
    FRIENDS_AND_FOLLOWING = "FRIENDS_AND_FOLLOWING"
    FRIENDS_FOLLOWING_AND_FOLLOWERS = "FRIENDS_FOLLOWING_AND_FOLLOWERS"
    NO_ONE = "NO_ONE"
    SOCIAL_NETWORK_VISIBILITY_UNSPECIFIED = "SOCIAL_NETWORK_VISIBILITY_UNSPECIFIED"

    def __str__(self) -> str:
        return str(self.value)
