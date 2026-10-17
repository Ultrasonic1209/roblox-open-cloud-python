from enum import StrEnum


class GetV1MessagesMessageTab(StrEnum):
    ARCHIVE = "Archive"
    INBOX = "Inbox"
    SENT = "Sent"

    def __str__(self) -> str:
        return str(self.value)
