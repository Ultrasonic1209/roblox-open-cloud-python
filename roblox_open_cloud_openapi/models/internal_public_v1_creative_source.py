from enum import Enum


class InternalPublicV1CreativeSource(str, Enum):
    IN_HOUSE_GEN_AI = "IN_HOUSE_GEN_AI"
    UPLOAD = "UPLOAD"

    def __str__(self) -> str:
        return str(self.value)
