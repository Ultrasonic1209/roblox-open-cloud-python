from enum import Enum


class EventCategory(str, Enum):
    ACTIVITY = "activity"
    CHALLENGE = "challenge"
    CONTENTUPDATE = "contentUpdate"
    EARLYACCESS = "earlyAccess"
    EXPANSION = "expansion"
    FESTIVAL = "festival"
    ITEMDROP = "itemDrop"
    LOCATIONUPDATE = "locationUpdate"
    MORELEVELS = "moreLevels"
    NEWCONTENT = "newContent"
    NEWFEATURE = "newFeature"
    NEWLOCATION = "newLocation"
    NEWMAP = "newMap"
    NEWSEASON = "newSeason"
    QUEST = "quest"
    SYSTEMUPDATE = "systemUpdate"

    def __str__(self) -> str:
        return str(self.value)
