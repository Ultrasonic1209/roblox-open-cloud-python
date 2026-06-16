from enum import Enum


class GetV1BundlesThumbnailsFormat(str, Enum):
    PNG = "Png"
    WEBP = "Webp"

    def __str__(self) -> str:
        return str(self.value)
