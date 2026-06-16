from enum import Enum


class ModelInstanceType(str, Enum):
    ANIMATION = "Animation"
    AUDIO = "Audio"
    DECAL = "Decal"
    MESH_PART = "MeshPart"
    SCRIPT = "Script"
    TOOL = "Tool"

    def __str__(self) -> str:
        return str(self.value)
