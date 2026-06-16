from enum import Enum


class RobloxApiNotificationsModelsNotificationStreamEntriesModelNotificationSourceType(str, Enum):
    CHATNEWMESSAGE = "ChatNewMessage"
    CONVERSATIONUNIVERSECHANGED = "ConversationUniverseChanged"
    DEVELOPERMETRICSAVAILABLE = "DeveloperMetricsAvailable"
    EXPERIENCEINVITATION = "ExperienceInvitation"
    FRIENDREQUESTACCEPTED = "FriendRequestAccepted"
    FRIENDREQUESTRECEIVED = "FriendRequestReceived"
    GAMEUPDATE = "GameUpdate"
    GROUPJOINREQUESTACCEPTED = "GroupJoinRequestAccepted"
    PARTYINVITERECEIVED = "PartyInviteReceived"
    PARTYMEMBERJOINED = "PartyMemberJoined"
    PRIVATEMESSAGERECEIVED = "PrivateMessageReceived"
    SENDR = "Sendr"
    TEAMCREATEINVITE = "TeamCreateInvite"
    TEST = "Test"
    USERADDEDTOPRIVATESERVERWHITELIST = "UserAddedToPrivateServerWhiteList"

    def __str__(self) -> str:
        return str(self.value)
