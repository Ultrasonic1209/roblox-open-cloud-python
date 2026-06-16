from enum import Enum


class RobloxGroupsApiGroupFeatureResponseFeature(str, Enum):
    CONTENTUPLOAD = "ContentUpload"
    FORUMREAD = "ForumRead"
    FORUMWRITE = "ForumWrite"
    GAMEOWNERSHIPTRANSFER = "GameOwnershipTransfer"
    GROUPOWNERSHIPTRANSFER = "GroupOwnershipTransfer"
    PAYOUTS = "Payouts"

    def __str__(self) -> str:
        return str(self.value)
