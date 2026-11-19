from enum import StrEnum


class RobloxItemConfigurationApiModelsRequestBundleCreateBundleRequestBundleType(StrEnum):
    AVATARANIMATIONS = "AvatarAnimations"
    BODY = "Body"
    DYNAMICHEAD = "DynamicHead"
    SHOES = "Shoes"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
