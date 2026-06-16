from enum import Enum


class RobloxContactsApiResponseValidateUserTagResponseModelStatus(str, Enum):
    MODERATED = "Moderated"
    SUCCESS = "Success"
    TOOLONG = "TooLong"

    def __str__(self) -> str:
        return str(self.value)
