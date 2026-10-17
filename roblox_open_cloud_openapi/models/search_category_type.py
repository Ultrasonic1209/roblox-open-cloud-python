from enum import StrEnum


class SearchCategoryType(StrEnum):
    AUDIO = "Audio"
    DECAL = "Decal"
    FONT_FAMILY = "FontFamily"
    MESH_PART = "MeshPart"
    MODEL = "Model"
    PLACE = "Place"
    PLUGIN = "Plugin"
    VIDEO = "Video"

    def __str__(self) -> str:
        return str(self.value)
