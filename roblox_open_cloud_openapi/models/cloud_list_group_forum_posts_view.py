from enum import StrEnum


class CloudListGroupForumPostsView(StrEnum):
    FULL = "FULL"
    FULL_WITH_FIRST_COMMENT = "FULL_WITH_FIRST_COMMENT"
    VIEW_UNSPECIFIED = "VIEW_UNSPECIFIED"

    def __str__(self) -> str:
        return str(self.value)
