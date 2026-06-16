from enum import Enum


class GetV1GamesUniverseIdThumbnailsFormat(str, Enum):
    JPEG = "Jpeg"
    PNG = "Png"
    WEBP = "Webp"

    def __str__(self) -> str:
        return str(self.value)
