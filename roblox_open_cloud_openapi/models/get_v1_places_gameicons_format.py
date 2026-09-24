from enum import Enum


class GetV1PlacesGameiconsFormat(str, Enum):
    ICNS = "Icns"
    ICO = "Ico"
    JPEG = "Jpeg"
    PNG = "Png"
    WEBP = "Webp"

    def __str__(self) -> str:
        return str(self.value)
