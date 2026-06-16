from enum import Enum


class GetV1MessagesMessageTab(str, Enum):
    ARCHIVE = "Archive"
    INBOX = "Inbox"
    SENT = "Sent"

    def __str__(self) -> str:
        return str(self.value)
