from enum import StrEnum


class GetV1GamesIconsFormat(StrEnum):
    ICNS = "Icns"
    ICO = "Ico"
    JPEG = "Jpeg"
    PNG = "Png"
    WEBP = "Webp"

    def __str__(self) -> str:
        return str(self.value)
