from enum import StrEnum


class RobloxGameInternationalizationApiGetNameDescriptionHistoryV2RequestContentType(StrEnum):
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
