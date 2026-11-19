from enum import StrEnum


class RobloxItemConfigurationApiModelsRequestBundleCreateBundleContextRequestBundleType(StrEnum):
    AVATARANIMATIONS = "AvatarAnimations"
    BODY = "Body"
    DYNAMICHEAD = "DynamicHead"
    SHOES = "Shoes"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
