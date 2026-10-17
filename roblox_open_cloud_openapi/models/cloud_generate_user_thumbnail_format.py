from enum import StrEnum


class CloudGenerateUserThumbnailFormat(StrEnum):
    FORMAT_UNSPECIFIED = "FORMAT_UNSPECIFIED"
    JPEG = "JPEG"
    PNG = "PNG"

    def __str__(self) -> str:
        return str(self.value)
