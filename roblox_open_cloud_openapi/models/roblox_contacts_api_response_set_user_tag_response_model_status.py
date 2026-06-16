from enum import Enum


class RobloxContactsApiResponseSetUserTagResponseModelStatus(str, Enum):
    MODERATED = "Moderated"
    SUCCESS = "Success"

    def __str__(self) -> str:
        return str(self.value)
