from enum import Enum


class CloudGenerateUserThumbnailFormat(str, Enum):
    FORMAT_UNSPECIFIED = "FORMAT_UNSPECIFIED"
    JPEG = "JPEG"
    PNG = "PNG"

    def __str__(self) -> str:
        return str(self.value)
