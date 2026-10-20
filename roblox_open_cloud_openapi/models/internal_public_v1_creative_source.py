from enum import StrEnum


class InternalPublicV1CreativeSource(StrEnum):
    IN_HOUSE_GEN_AI = "IN_HOUSE_GEN_AI"
    UPLOAD = "UPLOAD"

    def __str__(self) -> str:
        return str(self.value)
