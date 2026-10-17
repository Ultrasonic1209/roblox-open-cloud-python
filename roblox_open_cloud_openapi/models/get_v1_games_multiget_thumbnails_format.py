from enum import StrEnum


class GetV1GamesMultigetThumbnailsFormat(StrEnum):
    JPEG = "Jpeg"
    PNG = "Png"
    WEBP = "Webp"

    def __str__(self) -> str:
        return str(self.value)
