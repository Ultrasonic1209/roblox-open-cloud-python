from enum import Enum


class GetV1BadgesIconsFormat(str, Enum):
    PNG = "Png"
    WEBP = "Webp"

    def __str__(self) -> str:
        return str(self.value)
