from enum import StrEnum


class RobloxGroupsApiGroupFeatureResponseFeature(StrEnum):
    CONTENTUPLOAD = "ContentUpload"
    FORUMREAD = "ForumRead"
    FORUMWRITE = "ForumWrite"
    GAMEOWNERSHIPTRANSFER = "GameOwnershipTransfer"
    GROUPOWNERSHIPTRANSFER = "GroupOwnershipTransfer"
    PAYOUTS = "Payouts"

    def __str__(self) -> str:
        return str(self.value)
