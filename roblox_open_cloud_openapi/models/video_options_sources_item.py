from enum import StrEnum


class VideoOptionsSourcesItem(StrEnum):
    IMAGE_ONLY = "IMAGE_ONLY"
    PREVIEW_VIDEO = "PREVIEW_VIDEO"

    def __str__(self) -> str:
        return str(self.value)
