from enum import StrEnum


class GetV1UsersOutfitsFormat(StrEnum):
    PNG = "Png"
    WEBP = "Webp"

    def __str__(self) -> str:
        return str(self.value)
