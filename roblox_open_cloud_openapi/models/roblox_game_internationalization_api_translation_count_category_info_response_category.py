from enum import Enum


class RobloxGameInternationalizationApiTranslationCountCategoryInfoResponseCategory(str, Enum):
    INGAMECONTENT = "InGameContent"

    def __str__(self) -> str:
        return str(self.value)
