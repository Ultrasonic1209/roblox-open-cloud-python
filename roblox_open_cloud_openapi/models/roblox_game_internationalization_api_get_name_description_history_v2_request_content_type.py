from enum import Enum


class RobloxGameInternationalizationApiGetNameDescriptionHistoryV2RequestContentType(str, Enum):
    BADGEDISPLAYDESCRIPTION = "BadgeDisplayDescription"
    BADGEDISPLAYNAME = "BadgeDisplayName"
    DEVELOPERPRODUCTDISPLAYDESCRIPTION = "DeveloperProductDisplayDescription"
    DEVELOPERPRODUCTDISPLAYNAME = "DeveloperProductDisplayName"
    GAMEPASSDISPLAYDESCRIPTION = "GamePassDisplayDescription"
    GAMEPASSDISPLAYNAME = "GamePassDisplayName"
    UNIVERSEDISPLAYDESCRIPTIONS = "UniverseDisplayDescriptions"
    UNIVERSEDISPLAYNAMES = "UniverseDisplayNames"

    def __str__(self) -> str:
        return str(self.value)
