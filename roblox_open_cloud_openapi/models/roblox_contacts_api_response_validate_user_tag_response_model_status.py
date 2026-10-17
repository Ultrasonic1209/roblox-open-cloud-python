from enum import StrEnum


class RobloxContactsApiResponseValidateUserTagResponseModelStatus(StrEnum):
    MODERATED = "Moderated"
    SUCCESS = "Success"
    TOOLONG = "TooLong"

    def __str__(self) -> str:
        return str(self.value)
