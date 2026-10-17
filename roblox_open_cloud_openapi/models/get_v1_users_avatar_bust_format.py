from enum import StrEnum


class GetV1UsersAvatarBustFormat(StrEnum):
    PNG = "Png"
    WEBP = "Webp"

    def __str__(self) -> str:
        return str(self.value)
