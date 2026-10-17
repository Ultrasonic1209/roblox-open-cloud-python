from enum import StrEnum


class CloudGenerateUserThumbnailShape(StrEnum):
    ROUND = "ROUND"
    SHAPE_UNSPECIFIED = "SHAPE_UNSPECIFIED"
    SQUARE = "SQUARE"

    def __str__(self) -> str:
        return str(self.value)
