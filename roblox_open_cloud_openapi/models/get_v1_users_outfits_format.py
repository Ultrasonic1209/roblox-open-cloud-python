from enum import Enum


class GetV1UsersOutfitsFormat(str, Enum):
    PNG = "Png"
    WEBP = "Webp"

    def __str__(self) -> str:
        return str(self.value)
