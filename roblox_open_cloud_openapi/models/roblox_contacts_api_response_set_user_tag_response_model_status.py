from enum import StrEnum


class RobloxContactsApiResponseSetUserTagResponseModelStatus(StrEnum):
    MODERATED = "Moderated"
    SUCCESS = "Success"

    def __str__(self) -> str:
        return str(self.value)
